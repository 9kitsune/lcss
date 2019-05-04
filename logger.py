from sense_hat import SenseHat 
from datetime import datetime
from time import sleep
from csv import writer

sense = SenseHat()
winks = 30  #rest 30 seconds before sampling

def get_acc():
	acc = sense.get_accelerometer_raw()
	return acc

def get_sense_data():
	sense_data = []
	x,y,z = [sense.get_accelerometer_raw()[key] for key in ['x','y','z']]
	sense_data.append(x)
	sense_data.append(y)
	sense_data.append(z)
	yaw,pitch,roll = [sense.get_orientation()[key] for key in ['yaw','pitch','roll']]
    sense_data.append(pitch)
	sense_data.append(roll)
	sense_data.append(yaw)
	sense_data.append(datetime.now())
	return sense_data

with open('baseline.csv', 'w') as f:
    data_writer = writer(f)
    data_writer.writerow(['x','y','z','pitch','roll','yaw', 'datetime'])
    while True:
        data = get_sense_data()
        data_writer.writerow(data)
        sleep(winks)
