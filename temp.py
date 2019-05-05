from bme680 import BME680

### general libraries ###
from datetime import datetime
from time import sleep
from csv import writer

try:
    bme = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    bme = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

### monitoring ### 
sample_rate = 0.1  #rest 0.1 seconds before taking a sample
duration = 10 # in 10 seconds period
count = duration/sample_rate # number of samples in the time period
counter = 1