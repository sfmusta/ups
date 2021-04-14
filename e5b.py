import subprocess

cmd="upsc e5b"
output=""
string_measurements=["battery.charge", "battery.charge.low", "battery.runtime", "battery.type", "device.mfr", "device.model", "device.serial", "device.type", "driver.name", "driver.parameter.pollfreq", "driver.parameter.pollinterval", "driver.parameter.port", "driver.parameter.serial", "driver.parameter.synchronous", "driver.version", "driver.version.data", "driver.version.internal", "input.frequency", "input.transfer.high", "input.transfer.low", "input.voltage", "input.voltage.nominal", "outlet.1.status", "output.current", "output.frequency", "output.frequency.nominal", "output.voltage", "output.voltage.nominal", "ups.beeper.status", "ups.delay.shutdown", "ups.delay.start", "ups.load", "ups.load.high", "ups.mfr", "ups.model", "ups.power", "ups.power.nominal", "ups.productid", "ups.realpower", "ups.serial", "ups.status", "ups.temperature", "ups.test.result", "ups.timer.shutdown", "ups.timer.start", "ups.vendorid", ]

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

for line in p.stdout.readlines(): #read and store result in log file
    line = line.decode("utf-8").rstrip()
    key = line[:line.find(":")]
    value = line[line.find(":")+2:]

    if key in string_measurements:
        try:
            value = str(float(value))
        except:
            value = '"' + value + '"'
        measurement = key + "=" + value
        if output != "":
            measurement = "," + measurement
        output += measurement

output = "ups,ups.name=e5b " + output.rstrip()
print(output, end='')
