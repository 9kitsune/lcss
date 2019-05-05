### file history ###
# created by 9kitsune
# created on 05/05/2019
# version 1.0
####################

### sensor libraries ###
from lsm303d import LSM303D
from bh1745 import BH1745
from VL53L1X import VL53L1X 

### general libraries ###
from datetime import datetime
from time import sleep
from csv import writer

### Sensors declaration ###
lsm = LSM303D(0x1d)
bh = BH1745()
tof = VL53L1X(i2c_bus=1, i2c_address=0x29)

### Sensor calibration ###
bh.setup()
bh.set_leds(1)
tof.open()
tof.start_ranging(3)

### monitoring ### 
sample_rate = 0.1  #rest 0.1 seconds before taking a sample
duration_hr = 2 # in [3] hours period
duration = duration_hr*60*60 # in [duration_hr*60*60] seconds period
#duration = 10 # in [10] seconds period ### TESTING ONLY ####
count = duration/sample_rate # number of samples in the time period
counter = 1

### csv paramters ###
now = datetime.now()
timenow = now.time()
datenow = now.date()
fn = str(datenow) + str(timenow) + '.csv'

### main program ###
def get_sense_data():
	sense_data = []
	xyz = lsm.accelerometer()
	x,y,z = [xyz[key] for key in [0,1,2]]
	sense_data.append(x)
	sense_data.append(y)
	sense_data.append(z)
	rgbc = bh.get_rgbc_raw()
	r,g,b,c = [rgbc[key] for key in [0,1,2,3]]
	sense_data.append(r)
	sense_data.append(g)
	sense_data.append(b)
	sense_data.append(c)
	d = tof.get_distance()	#in mm
	sense_data.append(d)
	sense_data.append(datetime.now())
	return sense_data

with open(fn, 'w') as f:
	data_writer = writer(f)
	data_writer.writerow(['x','y','z','r','g','b','c','d','datetime'])
	while counter < count:
		data = get_sense_data()
		data_writer.writerow(data)
		sleep(sample_rate)
		counter += 1
bh.set_leds(0)		# stop luminance sensor
tof.stop_ranging() 	# stops tof sensor
print('complete')

