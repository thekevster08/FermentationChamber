import OutputTools 
from ConfigParser import SafeConfigParser

class Discrete:
	config = SafeConfigParser()

	def __init__(self):
		self.config.read('config.ini')
		self.sp = int(self.config.get('controller', 'setpoint'))
		self.activeDeadband = int(self.config.get('controller', 'activeDeadband'))
		self.inactiveDeadband = int(self.config.get('controller', 'inactiveDeadband'))
		self.highActive = self.sp + self.activeDeadband
		self.lowActive = self.sp - self.activeDeadband
		self.highInactive = self.sp + self.inactiveDeadband
		self.lowInactive = self.sp - self.inactiveDeadband

	def update(self, pv):
		self.config.read('config.ini')
		self.sp = int(self.config.get('controller', 'setpoint'))
		self.activeDeadband = int(self.config.get('controller', 'activeDeadband'))
		self.inactiveDeadband = int(self.config.get('controller', 'inactiveDeadband'))
		self.highActive = self.sp + self.activeDeadband
		self.lowActive = self.sp - self.activeDeadband
		self.highInactive = self.sp + self.inactiveDeadband
		self.lowInactive = self.sp - self.inactiveDeadband

		if pv > self.highActive:
			OutputTools.coldOn()
			OutputTools.heatOff()

		elif pv < self.lowActive:
			OutputTools.coldOff()
			OutputTools.heatOn()

		elif pv < self.lowInactive: 
			OutputTools.coldOff()
			OutputTools.heatOff()
			
		elif pv > self.highInactive:
			OutputTools.coldOff()
			OutputTools.heatOff()