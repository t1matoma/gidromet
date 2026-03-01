import pygrib

grbs = pygrib.open("temperature.grib")

times = set()

for grb in grbs:
    times.add(grb.validDate)

for t in sorted(times):
    print(t)