#!/usr/bin/env python
# coding: utf-8

import os, sys
import config, gc
import time, commands
import timeit

class mount_Checker():
	def __init__(self, mnt_point):
		self.mntCheck = ""
		self.check_cmd = 'grep -c "' + mnt_point + '" /proc/mounts'

	def _check(self):
		try:
			self.mntCheck = commands.getstatusoutput(self.check_cmd)
			if int(self.mntCheck[1]) == 1:
				return True
			else:
				return False
		except:
			return False
			pass

	def __del__(self):
		del(self.mntCheck)
		gc.collect()


class main:
    def __init__(self):
	start = timeit.default_timer()
        #print(config.clusterConfig.NODE_COUNT)
        #_a = config.HA_Config.HA_List
        #b = list(set(_a))
        #print(b)
        #print(b[0])

	#_b = config.AppConfig.APP_NAME
	#print(_b)
	#config.AppConfig.APP_NAME = "ClusterPlex 1.1.0"
	#_c = config.AppConfig.APP_NAME
	#print(_c)
	_b = config.AppConfig.MOUNT_PATH
	while True:
		try:
			_a = mount_Checker(_b)
			_c = _a._check()
			end = timeit.default_timer()
			run_time = end - start 
			m, s = divmod(run_time, 60)
			h, m = divmod(m, 60)
			print "%d:%02d:%02d" % (h, m, s)
			print(_c)
			gc.collect()
			
			if bool(_c) == True:
				_d = commands.getstatusoutput("service itplex_res_agent stop")
				print(_d)
				exit()	
			time.sleep(3)			
		except KeyboardInterrupt as e: # Ctrl-C
			exit()
if __name__ == '__main__':
    a = main()
