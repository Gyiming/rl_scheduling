from __future__ import with_statement
from multiprocessing import Process
import multiprocessing
import os
import configparser
import random
import numpy as np 
import time
import math

def agent():
    return 0

def governer():
	i =0
	cpu_id = 0
	policy = ["conservative","ondemand","powersave","performance"]
	if (i==0):
		execute_command = 'sudo cpufrep-set -c' + str(cpu_id) + '-g' + policy[i]
		#os.system(execute_command)
		print execute_command
	if (i==1):
		execute_command = 'sudo cpufrep-set -c' + str(cpu_id) + '-g' + policy[i]
		#os.system(execute_command)
		print execute_command
	if (i==2):
		execute_command = 'sudo cpufrep-set -c' + str(cpu_id) + '-g' + policy[i]
		#os.system(execute_command)
		print execute_command
	if (i==3):
		execute_command = 'sudo cpufrep-set -c' + str(cpu_id) + '-g' + policy[i]
		#os.system(execute_command)
		print execute_command

def run_benchmark(i):
	execute_command = ['parsecmgmt -a run -p blackscholes -i smilarge' ,
					   'parsecmgmt -a run -p bodytrack -i smilarge' ,
					   'parsecmgmt -a run -p canneal -i smilarge' ,
					   'parsecmgmt -a run -p dedup -i smilarge' ,
					   'parsecmgmt -a run -p facesim -i smilarge' ,
					   'parsecmgmt -a run -p ferret -i smilarge' ,
					   'parsecmgmt -a run -p fluidanimate -i smilarge' , 
					   'parsecmgmt -a run -p freqmine -i smilarge' ,
					   'parsecmgmt -a run -p raytrace -i smilarge' ,
					   'parsecmgmt -a run -p streamcluster -i smilarge' ,
					   'parsecmgmt -a run -p swaptions -i smilarge' ,
					   'parsecmgmt -a run -p vips -i smilarge' ,
					   'parsecmgmt -a run -p x264 -i smilarge' ,]
	#os.system(execute_command)
	print execute_command(i)

def power_measure_tx2():
	#f = open("/sys/devices/316000.i2c/i2c-0/0-0041/iio_device/in_power1_input","r")
	#cpu_power = f.read()
	print('150mw')

def main():
	start_p1 = time.time()
	start_p2 = time.time()
	start_p3 = time.time()
	while True:
		p1 = multiprocessing.Process(target=run_benchmark)
		p2 = multiprocessing.Process(target=governer)
		p3 = multiprocessing.Process(target=power_measure_tx2)
		accumulate_p1 = time.time() - start_p1
		accumulate_p2 = time.time() - start_p2
		accumulate_p3 = time.time() - start_p3
		if accumulate_p1 > 5:
			p1.start(5)
			start_p1 = time.time()
		if accumulate_p2 > 3:
			p2.start()
			#print math.floor((time.time() - start_p2))
			start_p2 = time.time()
		if accumulate_p3 > 10:
			p3.start()
			#print math.floor((time.time() - start_p3))
                        start_p3 = time.time()


if __name__ == '__main__':
	main()




