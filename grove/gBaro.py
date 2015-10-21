import time, sys, signal, atexit
import pyupm_bmpx8x as upmBmpx8x

# Load Barometer module on i2c
myBarometer = upmBmpx8x.BMPX8X(0, upmBmpx8x.ADDR);


## Exit handlers ##
# This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
    raise SystemExit

# This function lets you run code on exit, including functions from myBarometer
def exitHandler():
    print "Exiting"
    sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)


# Print the pressure, altitude, sea level, and
# temperature values every 0.1 seconds
while(1):
    outputStr = ("pressure value = {0}"
    ", altitude value = {1}"
    ", sealevel value = {2}"
    ", temperature = {3}".format(
    myBarometer.getPressure(),
    myBarometer.getTemperature(),
    myBarometer.getAltitude(),
    myBarometer.getSealevelPressure()))

    print outputStr
    time.sleep(.1)
