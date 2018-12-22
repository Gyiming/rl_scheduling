from __future__ import with_statement
import os
import configparser
import random
import numpy as np 

def governer():
	i =0
	cpu_id = 0
	policy = ["conservative","ondemand","powersave","performance"]
	if (i==0):
		execute_command = 'sudo cpufrep-set -c' + str(cpu_id) + '-g' + policy[i]
		os.system(execute_command)
		#print "sudo cpufrep-set -c %d -g %s", cpu_id, policy[i]
	if (i==1):
		execute_command = 'sudo cpufrep-set -c' + str(cpu_id) + '-g' + policy[i]
		os.system(execute_command)
		#print "sudo cpufrep-set -c %d -g %s", cpu_id, policy[i]
	if (i==2):
		execute_command = 'sudo cpufrep-set -c' + str(cpu_id) + '-g' + policy[i]
		os.system(execute_command)
		#print "sudo cpufrep-set -c %d -g %s", cpu_id, policy[i]
	if (i==3):
		execute_command = 'sudo cpufrep-set -c' + str(cpu_id) + '-g' + policy[i]
		os.system(execute_command)
		#print "sudo cpufrep-set -c %d -g %s", cpu_id, policy[i]

def run_benchmark():
	execute_command = 'parsecmgmt -a run -p all'
	os.system(execute_command)

def power_measure_tx2():
	

if __name__ == '__main__':
	main()




