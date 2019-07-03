### file history ###
# created by 9kitsune
# created on 05/05/2019
# version 1.0
####################

### sensor libraries ###
from lsm303d import LSM303D

### general libraries ###
from datetime import datetime
from time import sleep
from csv import writer

### Sensors declaration ###
lsm = LSM303D(0x1d)

### monitoring ### 
sample_rate = 0.2  #rest 0.1 seconds before taking a sample
duration_hr = 1 # in [3] hours period
duration = duration_hr*60*60 # in [duration_hr*60*60] seconds period
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
	sense_data.append(datetime.now())
	return sense_data

with open(fn, 'w') as f:
	data_writer = writer(f)
	data_writer.writerow(['x','y','z','datetime'])
	while counter < count:
		data = get_sense_data()
		data_writer.writerow(data)
		sleep(sample_rate)
		counter += 1
		if counter > count:
			break
