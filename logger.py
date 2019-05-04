from lsm303d import LSM303D
from datetime import datetime
from time import sleep
from csv import writer

lsm = LSM303D(0x1d)
sample_rate = 0.1  #rest 0.1 seconds before taking a sample
duration = 10 # in 10 seconds period
count = duration/sample_rate # number of samples in the time period
counter = 1

def get_acc():
	acc = sense.get_accelerometer_raw()
	return acc
# xyz = lsm.accelerometer()


def get_sense_data():
	sense_data = []
	xyz = lsm.accelerometer()
	x,y,z = [xyz[key] for key in [0,1,2]]
	sense_data.append(x)
	sense_data.append(y)
	sense_data.append(z)
	sense_data.append(datetime.now())
	return sense_data

with open('baseline.csv', 'w') as f:
	data_writer = writer(f)
	data_writer.writerow(['x','y','z','datetime'])
	while counter < count:
		data = get_sense_data()
		data_writer.writerow(data)
		sleep(sample_rate)
		counter += 1
		if counter > count:
			break
