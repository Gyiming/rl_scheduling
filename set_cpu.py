from __future__ import with_statement
from multiprocessing import Process
import multiprocessing
import os
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
		execute_command = 'sudo cpufreq-set' + ' -r' + ' -g' + ' ' + policy[i]
		os.system(execute_command)
		#print execute_command
	if (i==1):
		execute_command = 'sudo cpufreq-set' + ' -r' + ' -g' + ' ' + policy[i]
		os.system(execute_command)
		#print execute_command
	if (i==2):
		execute_command = 'sudo cpufreq-set' + ' -r' + ' -g' + ' ' + policy[i]
		os.system(execute_command)
		#print execute_command
	if (i==3):
		execute_command = 'sudo cpufreq-set' + ' -r' + ' -g' + ' ' + policy[i]
		os.system(execute_command)
		#print execute_command

def run_benchmark(i):
	execute_command = ['parsecmgmt -a run -p blackscholes' ,
					   'parsecmgmt -a run -p dedup' ,
					   'parsecmgmt -a run -p facesim' ,
					   'parsecmgmt -a run -p fluidanimate' , 
					   'parsecmgmt -a run -p freqmine' ,
					   'parsecmgmt -a run -p streamcluster' ,]
	os.system(execute_command[i])
	#print execute_command(i)

def power_measure_tx2(send_end):
	f = open("/sys/devices/3160000.i2c/i2c-0/0-0041/iio_device/in_power1_input","r")
	cpu_power = f.read()
	send_end.send(cpu_power)

def agent(util,freq):
	return 1

def main():
	start_p1 = time.time()
	start_p2 = time.time()
	start_p3 = time.time()
	start_simulation = time.time()
	gover_update_freq = 0.5
	run_bench_freq = 2
	collect_power_freq = 4
	feedback_freq = []
	feedback_util = []
	times = 0
        power_measurement = []
	while (time.time() - start_simulation < 15):
		accumulate_p1 = time.time() - start_p1
		accumulate_p2 = time.time() - start_p2
		accumulate_p3 = time.time() - start_p3
		if accumulate_p1 > run_bench_freq:
			app = randint(0,5)
			p1 = multiprocessing.Process(target=run_benchmark,args=(app,))
			p1.start()
			start_p1 = time.time()
		if accumulate_p2 > gover_update_freq:
			util = psutil.cpu_percent()
			info = cpuinfo.get_cpu_info()
			freq = info['hz_actual_raw'][0]
			choice = agent(util,freq)
			feedback_util.append(util)
			feedback_freq.append(freq)
			p2 = multiprocessing.Process(target=governer,args=(choice,))
			p2.start()
			#print math.floor((time.time() - start_p2))
			start_p2 = time.time()
		if accumulate_p3 > collect_power_freq:
			manager = multiprocessing.Manager()
			recv_end, send_end = multiprocessing.Pipe(False)
			p3 = multiprocessing.Process(target=power_measure_tx2,args=(send_end,))
			p3.start()
			#print math.floor((time.time() - start_p3))
			power_measurement.append(recv_end)
                        start_p3 = time.time()
        print(feedback_freq)
        print(feedback_util)
	power_number = [x.recv() for x in power_measurement]
        print(power_number)


if __name__ == '__main__':
	main()




