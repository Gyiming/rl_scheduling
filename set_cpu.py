from __future__ import with_statement
from multiprocessing import Process
import multiprocessing
import os
import configparser
import random
import numpy as np 
import time
import math
import psutil
from random import randint
import cpuinfo

def agent():
    return 0

def governer(i):
	#cpu_id = 0
	policy = ["conservative","ondemand","powersave","performance"]
	if (i==0):
		execute_command = 'sudo cpufrep-set -c' + ' -r' + ' -g' + ' ' + policy[i]
		#os.system(execute_command)
		print execute_command
	if (i==1):
		execute_command = 'sudo cpufrep-set -c' + ' -r' + ' -g' + ' ' + policy[i]
		#os.system(execute_command)
		print execute_command
	if (i==2):
		execute_command = 'sudo cpufrep-set -c' + ' -r' + ' -g' + ' ' + policy[i]
		#os.system(execute_command)
		print execute_command
	if (i==3):
		execute_command = 'sudo cpufrep-set -c' + ' -r' + ' -g' + ' ' + policy[i]
		#os.system(execute_command)
		print execute_command

def run_benchmark(i):
	execute_command = ['parsecmgmt -a run -p blackscholes -i smilarge' ,
					   'parsecmgmt -a run -p dedup -i smilarge' ,
					   'parsecmgmt -a run -p facesim -i smilarge' ,
					   'parsecmgmt -a run -p fluidanimate -i smilarge' , 
					   'parsecmgmt -a run -p freqmine -i smilarge' ,
					   'parsecmgmt -a run -p streamcluster -i smilarge' ,]
	#os.system(execute_command)
	print execute_command(i)

def power_measure_tx2():
	f = open("/sys/devices/316000.i2c/i2c-0/0-0041/iio_device/in_power1_input","r")
	cpu_power = f.read()
	return cpu_power

def agent(util,freq):
	return 1

def main():
	start_p1 = time.time()
	start_p2 = time.time()
	start_p3 = time.time()
	start_simulation = time.time()
	gover_update_freq = 0.5
	run_bench_freq = 1
	colleco_power_freq = 5
	feedback_freq = []
	feedback_util = []
	power_measurement = []
	while (time.time() - start_simulation < 15):
		p1 = multiprocessing.Process(target=run_benchmark)
		p2 = multiprocessing.Process(target=governer)
		p3 = multiprocessing.Process(target=power_measure_tx2)
		accumulate_p1 = time.time() - start_p1
		accumulate_p2 = time.time() - start_p2
		accumulate_p3 = time.time() - start_p3
		if accumulate_p1 > run_bench_freq:
			app = randint(0,6)
			p1.start(app)
			start_p1 = time.time()
		if accumulate_p2 > gover_update_freq:
			util = psutil.cpu_percent()
			info = cpuinfo.get_cpu_info()
			freq = info['hz_actual_raw'][0]
			choice = agent(util,freq)
			feedback_util.append(util)
			feedback_freq.append(freq)
			p2.start(choice)
			#print math.floor((time.time() - start_p2))
			start_p2 = time.time()
		if accumulate_p3 > 5:
			p = p3.start()
			#print math.floor((time.time() - start_p3))
			power_measurement.append(p)
            start_p3 = time.time()
    print(feedback_freq)
    print(feedback_util)
    print(power_measurement)


if __name__ == '__main__':
	main()




