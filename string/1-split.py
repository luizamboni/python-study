

date = "2010-08-17 12:09:36"

[ date, time ] = date.split(" ")

[ year, month, day ] = date.split("-")
[ hour, minutes, seconds ] = time.split(":")

print year, month, day, hour, minutes