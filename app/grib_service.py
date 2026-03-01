from datetime import datetime
import numpy as np

from fastapi import HTTPException
import pygrib

from app.settings import LAT_MIN, LAT_MAX, LON_MIN, LON_MAX


def load_grib_data(file_path: str, time_str: str):
    try:
        target_time = datetime.fromisoformat(time_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Некорректный формат времени, используйте ISO")

    try:
        grbs = pygrib.open(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка чтения файла GRIB: {e}")

    grb_msg = None
    for grb in grbs:
        if grb.validDate.strftime("%Y-%m-%dT%H:%M") == target_time.strftime("%Y-%m-%dT%H:%M"):
            grb_msg = grb
            break

    if grb_msg is None:
        raise HTTPException(status_code=404, detail="Данные для указанного времени не найдены")

    data, lats, lons = grb_msg.data()
    lons = np.where(lons > 180, lons - 360, lons)

    region_mask = (
        (lats >= LAT_MIN) & (lats <= LAT_MAX) &
        (lons >= LON_MIN) & (lons <= LON_MAX)
    )
    indices = np.where(region_mask)
    if len(indices[0]) == 0:
        raise HTTPException(status_code=404, detail="Регион не найден")

    i_min, i_max = indices[0].min(), indices[0].max()
    j_min, j_max = indices[1].min(), indices[1].max()

    data_region = data[i_min:i_max+1, j_min:j_max+1]
    lats_region = lats[i_min:i_max+1, j_min:j_max+1]
    lons_region = lons[i_min:i_max+1, j_min:j_max+1]

    return data_region, lats_region, lons_region