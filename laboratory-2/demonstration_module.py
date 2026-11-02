from conversion import bothways_conversion, feet_to_meters, meters_to_feet



feet_to_meters = feet_to_meters(100)
meters_to_feet = meters_to_feet(100)

dBm_to_watt = bothways_conversion(10,10)
watt_to_dBm = bothways_conversion(10,10)

print(f"100 feet into meters are: {feet_to_meters}")
print(f"100 meters into feet are: {meters_to_feet}")

print(f"10 dBm into watt: {dBm_to_watt}")
print(f"10 watt into dBm: {watt_to_dBm}")