#!/usr/bin/env python
# coding: utf-8

class Config:
	APP_NAME = 'itplex'
	ADMIN_NAME = 'administrator'

class AppConfig(Config):
	APP_NAME = 'itplex'
	ADMIN_NAME = 'administrator'
	MOUNT_PATH = "/ixTemp"

class clusterConfig(Config):
	DEBUG = True

	NODE_COUNT = 2
	NODE_CHECK_TIME = 3

class HA_Config(Config):
	HA_List= ["A","B","C","D","E","F","G","H","A","B"]
