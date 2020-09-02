import jsonHandler
import gi
gi.require_version('Gtk','3.0')
gi.require_version("Notify", "0.7")
from gi.repository import Gtk
from gi.repository import Notify

class UIBuilder():
	def __init__(self,filePath):
		"""
			Here we define the basic features that each 
			window environment will have.
		"""
		self.filePath=filePath
		self.builder=Gtk.Builder()
		self.builder.add_from_file(self.filePath)
		self.window=self.builder.get_object("mainWindow")

	def destroy(self,widget):
		Gtk.main_quit()

class Settings(UIBuilder):
	def __init__(self):
		"""
			Here we define the features for the window 
			environment that manages the user settings.
		"""
		super().__init__("../GUI/glade/settings.glade") # We create the basic features
		self.configPath="../config/config.json"
		# Below we define which items we will use
		self.submit=self.builder.get_object("submitButton")
		self.cancel=self.builder.get_object("cancelButton")
		self.startOnSwitch=self.builder.get_object("starton-switch")
		self.csStudentSwitch=self.builder.get_object("CS-switch")
		self.nonCSStudentSwitch=self.builder.get_object("NonCS-switch")
		self.startOnSwitch.set_active(jsonHandler.readJson(self.configPath)['configInfo']['startONPowerButtonON'])
		self.csStudentSwitch.set_active(jsonHandler.readJson(self.configPath)['configInfo']['csButtonON'])
		self.nonCSStudentSwitch.set_active(jsonHandler.readJson(self.configPath)['configInfo']['nonCSButtonON'])
		# Below we define what will be the functions of each object in the window.
		self.window.connect("destroy",self.destroy)
		self.cancel.connect("clicked",self.destroy)
		self.startOnSwitch.connect("button-press-event",self.startOnPower)
		self.csStudentSwitch.connect("button-press-event",self.sigleSwitchON)
		self.csStudentSwitch.connect("key-press-event",self.sigleSwitchON)
		self.nonCSStudentSwitch.connect("button-press-event",self.sigleSwitchON)
		self.nonCSStudentSwitch.connect("key-press-event",self.sigleSwitchON)
		self.submit.connect("clicked",self.onSubmit)

	def onSubmit(self,widget):
		"""
			This method refers to the button that stores 
			user information in the json file.
		"""
		configUpdate=jsonHandler.readJson(self.configPath)
		# We put the settings chosen by the user in the file.
		configUpdate['configInfo']['startONPowerButtonON']=self.startOnSwitch.get_active()
		configUpdate['configInfo']['csButtonON']=self.csStudentSwitch.get_active()
		configUpdate['configInfo']['nonCSButtonON']=self.nonCSStudentSwitch.get_active()
		# In this condition we define the appropriate settings so that the other 
		# program understands what type of student we are referring to.
		if self.csStudentSwitch.get_active():
			configUpdate['configInfo']['isCSStudent']=True
		else:
			configUpdate['configInfo']['isCSStudent']=False
		jsonHandler.writeJson(self.configPath,configUpdate)

	def sigleSwitchON(self,widget,logs):
		"""
			This method ensures that only one of the student's 
			two buttons will be active at a time.
		"""
		if widget.get_name()=="CS-switch" and widget.get_active:
			self.nonCSStudentSwitch.set_active(False)
		else:
			self.csStudentSwitch.set_active(False)

	def startOnPower(self,widget,logs):
		"""
			This method performs the appropriate procedures so that the 
			program starts automatically when the system is activated.
		"""
		pass


Settings()
Gtk.main()