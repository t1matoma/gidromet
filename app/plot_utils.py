import matplotlib.pyplot as plt
from io import BytesIO


def plot_to_png(data, lats, lons, title):
    plt.figure(figsize=(8,6))
    contour = plt.contourf(lons, lats, data, cmap='viridis')
    plt.colorbar(contour)
    plt.title(title)
    plt.xlabel("Долгота")
    plt.ylabel("Широта")

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    return buf.read()