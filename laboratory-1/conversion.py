import math

def feet_to_meters(feet):
    return feet * 0.3048

feet_to_meters(100)

def meters_to_feet(meters):
    return meters * 3.28084

meters_to_feet(100)

def bothways_conversion(dBm, watt):
    option = input("Enter the parameter you want to convert from: 1. dbM -> watt \n 2. watt -> dBm")

    if option == '1':
        return (math.pow(10,(dBm/10)))/1000
    elif option == '2':
        return 10 * math.log10(watt*1000)