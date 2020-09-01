import jsonHandler
import requests
import bs4
import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify

class UpdateHandler():
	def __init__(self):
		self.jsonPath="../json/websites.json"
		self.configPath="../config/config.json"
		self.isCSStudent=jsonHandler.readJson(self.configPath)['configInfo']['isCSStudent']

	def getLatestAnnouncement(self,url,htmlClass):
		"""
			This method searches the html code and finds the most recent 
			announcement of the university and then returns it.
		"""
		try:
			# We are trying to do a get request.
			respone=requests.get(url)
		except ConnectionError:
			pass
			# do samething here.

		if respone.status_code==200:
			# We get the latest announcement
			siteSoup=bs4.BeautifulSoup(respone.text,"html.parser")
			announcementList=siteSoup.find(class_=htmlClass)
			announcements=announcementList.find_all('a')
			latestAnnouncement=announcements[0].contents[0]
		else:
			# if there is no announcement, probably due to failure we return zero.
			return 0

		return latestAnnouncement

	def getMostRecent(self):
		"""
			This method checks if there is a new announcement, if it exists 
			then updates the json file with the new announcement and displays 
			a message saying there is a new announcement.
		"""
		webSites=jsonHandler.readJson(self.jsonPath)
		# We read the necessary information to proceed with the process
		if self.isCSStudent:
			# If the unipi student is an IT student then check the cs.unipi page.
			page="ITMainPage"
			mainPageUrl=webSites['websites']['ITMainPage']['url']
			announcementLoc=webSites['websites']['ITMainPage']['announcementLocation']
			previousAnnouncement=webSites['websites']['ITMainPage']['latestAnnouncement']
		else:
			# If the unipi student is not an IT student then check the main page.
			page="UNIPIMainPage"
			mainPageUrl=webSites['websites']['UNIPIMainPage']['url']
			announcementLoc=webSites['websites']['UNIPIMainPage']['announcementLocation']
			previousAnnouncement=webSites['websites']['UNIPIMainPage']['latestAnnouncement']
		# get's the new a announcement
		newAnnouncement=self.getLatestAnnouncement(mainPageUrl,announcementLoc)
		if newAnnouncement!=previousAnnouncement and newAnnouncement:
			# We check if there is an announcement and save it if exists.
			webSites['websites'][page]['latestAnnouncement']=newAnnouncement
			jsonHandler.writeJson(self.jsonPath,webSites)
			self.showNotify(newAnnouncement)
		else:
			pass

	def showNotify(self,title):
		"""
			This method displays the new announcement
		"""
		Notify.init("University News")
		newNotification=Notify.Notification.new("There is an announcement from the University of Piraeus.",title,"/home/rounnus/Pictures/anime_notifier/icon.png")
		newNotification.show()
