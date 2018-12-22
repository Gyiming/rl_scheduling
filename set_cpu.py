from __future__ import with_statement
from multiprocessing import Process
import os
import configparser
import random
import numpy as np 
import timeit

def agent():


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

def run_benchmark():
	execute_command = 'parsecmgmt -a run -p all'
	os.system(execute_command)

def power_measure_tx2():
	f = open("/sys/devices/316000.i2c/i2c-0/0-0041/iio_device/in_power1_input","r")
	cpu_power = f.read()

def main():
	start = timeit.timeit()
	while True:
		p1 = multiprocessing.Process(target=run_benchmark)
		p2 = multiprocessing.Process(target=governer)
		p3 = multiprocessing.Process(target=power_measure_tx2)
		p1.start()
		if (timeit.timeit() - start) % 100 == 0:
			p2.start()

		if (timeit.timeit() - start) % 10000 == 0:
			p3.start()


if __name__ == '__main__':
	main()




