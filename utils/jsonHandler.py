import json


def readJson(jsonPath):
	"""
		This function simply reads a json file and returns 
		a dictionary that contains the data we want.
	"""
	try:
		# Trying to read the json.
		jsonFile=open(jsonPath,encoding="utf-8")
		content=json.load(jsonFile)
	except:
		raise Exception("Unable to read the json!!")
	finally:
		jsonFile.close()
	# return the content
	return content

def writeJson(jsonPath,newData):
	"""
		This function simply writes a json file.
	"""
	try:
		# Trying to write the json.
		jsonFile=open(jsonPath,"w",encoding="utf-8")
		json.dump(newData,jsonFile,indent=4)
	except:
		raise Exception("Unable to write the json!!")
	finally:
		jsonFile.close()