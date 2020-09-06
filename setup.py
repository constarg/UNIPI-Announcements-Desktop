import os
import sys
sys.path.insert(1,"utils/")
import jsonHandler

def systemInstalls():
	os.system("sh 'makeLuncher.sh'")
	os.system("sh 'shellScripts/install.sh'")

def configureIcon():
	"""
		In this function we inform the json file
		about the locations of icon.
	"""
	defaultPath=(os.popen("pwd").read()).replace("\n","")
	iconPath=defaultPath+"/icon/icon.png" # icon path
	updateConfig=jsonHandler.readJson("config/config.json")	# read the json.
	updateConfig['configInfo']['paths']['notificationIcon']=iconPath
	jsonHandler.writeJson("config/config.json",updateConfig) # update json.


if __name__=="__main__":
	systemInstalls()
	configureIcon()