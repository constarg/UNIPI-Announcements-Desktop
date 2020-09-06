import time
import sys
import setproctitle
sys.path.insert(1,"utils/")
import UpdateHandler

if __name__=="__main__":
	# here we running the application.
	setproctitle.setproctitle("Announcements")
	update=UpdateHandler.UpdateHandler()
	update.showNotify("Started.")
	while True:
		# We check every hour if there are new notifications
		update.getMostRecent()
		time.sleep(3600) # wait for an hour.
