import pyupm_grove

celsius = pyupm_grove.GroveTemp(3).value()
fahrenheit = celsius * 9.0/5.0 + 32.0

print(celsius, fahrenheit)
    

