
class Planet(object):
	def __init__(self,name,distance=149600000,orbitalPeriod=1.0):
		self.name = name
		self.distanceToSun = distance
		self.orbitalPeriod = orbitalPeriod

	def getDistanceToSun(self):
		return(self.distanceToSun)

	def getName(self):
		return(self.name)

	def getOrbitalPeriod(self):
		return(self.orbitalPeriod)

	def setDistanceToSun(self, distance):
		self.distanceToSun = distance

	def setName(self, name):
		self.name = name

	def setOrbitalPeriod(self, orbitalPeriod):
		self.orbitalPeriod = orbitalPeriod

#class Earth as a child of Planet
class Earth(Planet):
	#runs automatically when this class is instantiated
	def __init__(self):
		#inherit all the characteristics of Planet Class with specific values
		Planet.__init__(self, "Earth", 149600000, 1.0) #run Planets __init__ to initialize Earth
		self.color = "blue"

class Mercury(Planet):
	def __init__(self):
		Planet.__init__(self, "Mercury", 57909175, 87.97)
		self.mass = 0.33011 #x10^24 kg
		self.density = 5427 #kg/m^3
	def getMass(self):
		return(self.mass)
	def getDensity(self):
		return(self.density)


class Venus(Planet):
	def __init__(self):
		Planet.__init__(self, "Venus", 108208930, 224.7)
		self.mass = 4.87 #x10^24 kg
		self.density = 5243 #kg/m^3
	def getMass(self):
		return(self.mass)
	def getDensity(self):
		return(self.density)

class Mars(Planet):
	def __init__(self):
		Planet.__init__(self, "Mars", 227936640, 686.98)
		self.mass = 0.642 #x10^24 kg
		self.density = 3933 #kg/m^3
	def getMass(self):
		return(self.mass)
	def getDensity(self):
		return(self.density)

class Jupiter(Planet):
	def __init__(self):
		Planet.__init__(self, "Jupiter", 778412020, 11.86)
		self.diameter = 142984 #km
		self.gravity = 23.1 #m/s^2
	def getDiameter(self):
		return(self.diameter)
	def getGravity(self):
		return(self.gravity)

class Saturn(Planet):
	def __init__(self):
		Planet.__init__(self, "Saturn", 1426725400, 29.46)
		self.diameter = 120536 #km
		self.gravity = 9.0 #m/s^2
	def getDiameter(self):
		return(self.diameter)
	def getGravity(self):
		return(self.gravity)

class Uranus(Planet):
	def __init__(self):
		Planet.__init__(self, "Uranus", 2870972200, 30685)
		self.diameter = 51118 #km
		self.gravity = 8.7 #m/s^2
	def getDiameter(self):
		return(self.diameter)
	def getGravity(self):
		return(self.gravity)

class Neptune(Planet):
	def __init__(self):
		Planet.__init__(self, "Neptune", 4498252900, 60190)
		self.diameter = 49528 #km
		self.gravity = 11.0 #m/s^2
	def getDiameter(self):
		return(self.diameter)
	def getGravity(self):
		return(self.gravity)

class Pluto(Planet):
	def __init__(self):
		Planet.__init__(self, "Pluto", 5906376200, 247.92)
		self.diameter = 2370 #km
		self.gravity = 0.7 #m/s^2
	def getDiameter(self):
		return(self.diameter)
	def getGravity(self):
		return(self.gravity)


class SolarSystem():
	def __init__(self):
		self.Mercury = Mercury()
		self.Venus = Venus()
		self.Earth = Earth()
		self.Mars = Mars()
		self.Jupiter = Jupiter()
		self.Saturn = Saturn()
		self.Uranus = Uranus()
		self.Neptune = Neptune()
		self.Pluto = Pluto()

	def orbitTime(self,days):

		#days = 1825 #5 years

		years = days / 365

		self.mercuryOrbit = years / self.Mercury.orbitalPeriod
		self.venusOrbit = years / self.Venus.orbitalPeriod
		self.earthOrbit = years / self.Earth.orbitalPeriod
		self.marsOrbit = years / self.Mars.orbitalPeriod
		self.jupiterOrbit = years / self.Jupiter.orbitalPeriod
		self.saturnOrbit = years / self.Saturn.orbitalPeriod
		self.uranusOrbit = years / self.Uranus.orbitalPeriod
		self.neptuneOrbit = years / self.Neptune.orbitalPeriod
		self.plutoOrbit = years / self.Pluto.orbitalPeriod


#		print('Mercury', mercuryOrbit)
#		print('Venus', venusOrbit)
#		print('Earth', earthOrbit)
#		print('Mars', marsOrbit)
#		print('Jupiter', jupiterOrbit)
#		print('Saturn', saturnOrbit)
#		print('Uranus', uranusOrbit)
#		print('Neptune', neptuneOrbit)
#		print('Pluto', plutoOrbit)





	#This prints all the names, distances, and orbital periods of each planet+pluto
	def seeInfo(self):

		print(self.Mercury.name)
		print(self.Mercury.distanceToSun)
		print(self.Mercury.orbitalPeriod)

		print(self.Venus.name)
		print(self.Venus.distanceToSun)
		print(self.Venus.orbitalPeriod)

		print(self.Earth.name)# + " " + Earth.getDistanceToSun + " " + Earth.getOrbitalPeriod)
		print(self.Earth.distanceToSun)
		print(self.Earth.orbitalPeriod)

		print(self.Mars.name)
		print(self.Mars.distanceToSun)
		print(self.Mars.orbitalPeriod)

		print(self.Jupiter.name)
		print(self.Jupiter.distanceToSun)
		print(self.Jupiter.orbitalPeriod)

		print(self.Saturn.name)
		print(self.Saturn.distanceToSun)
		print(self.Saturn.orbitalPeriod)

		print(self.Uranus.name)
		print(self.Uranus.distanceToSun)
		print(self.Uranus.orbitalPeriod)

		print(self.Neptune.name)
		print(self.Neptune.distanceToSun)
		print(self.Neptune.orbitalPeriod)

		print(self.Pluto.name)
		print(self.Pluto.distanceToSun)
		print(self.Pluto.orbitalPeriod)


####UNCOMMENT TO SEE INFO AND ORBIT TIMES##############

#Solar = SolarSystem()

#Solar.seeInfo()

#print()

#Solar.orbitTime(365)











