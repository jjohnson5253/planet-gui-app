from PyQt4 import QtGui, QtCore
from planets import SolarSystem

###############################MAIN WIDGET################################

class MainWidget(QtGui.QWidget):

	def __init__(self):
		#make this a widget
		QtGui.QWidget.__init__(self)

		#main layout will be a Horizontal Box layout
		self.mainLayout = QtGui.QHBoxLayout(self)

		#button layout is within main layout on left-hand side
		self.buttonWidget = buttonWidget()
		#self.myButtonLayout = buttonLayout()
		self.mainLayout.addWidget(self.buttonWidget)

		self.testButton = QtGui.QPushButton("testing")
		#self.buttonLayout.addWidget(self.testButton)

		#adds a cool stretch layout
		self.mainLayout.addStretch(0)

		#info layout is within main layout on right-hand side
		self.infoWidget = infoWidget()
		self.mainLayout.addWidget(self.infoWidget)

		self.mainLayout.addStretch(0)

		#connect button clicks from button widget to printPlanetInfo method
		self.buttonWidget.mercuryButton.clicked.connect(self.printPlanetInfo)
		self.buttonWidget.venusButton.clicked.connect(self.printPlanetInfo)
		self.buttonWidget.earthButton.clicked.connect(self.printPlanetInfo)
		self.buttonWidget.marsButton.clicked.connect(self.printPlanetInfo)
		self.buttonWidget.jupiterButton.clicked.connect(self.printPlanetInfo)
		self.buttonWidget.saturnButton.clicked.connect(self.printPlanetInfo)
		self.buttonWidget.uranusButton.clicked.connect(self.printPlanetInfo)
		self.buttonWidget.neptuneButton.clicked.connect(self.printPlanetInfo)
		self.buttonWidget.plutoButton.clicked.connect(self.printPlanetInfo)

#####is there a way to access mySolar objects by sender.text()? i.e. mySolar.[sender.text()].getDistanceToSun()
	def printPlanetInfo(self):
		#find out which button sent the signal
		sender = self.sender()
		name = sender.text()

		#instantiate solar system
		mySolar = SolarSystem()

		#if/else statements capturing which button was clicked
		if(name == "Mercury"):
			#get distance/orbit from mySolar object and call functions from infoWidget to set text
			distance = mySolar.Mercury.getDistanceToSun()
			orbit = mySolar.Mercury.getOrbitalPeriod()
			newDistanceLabelText = "Mercury is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/mercury.jpeg").scaled(400,400))

		elif(name == "Venus"):
			distance = mySolar.Venus.getDistanceToSun()
			orbit = mySolar.Venus.getOrbitalPeriod()
			newDistanceLabelText = "Venus is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/venus.jpeg").scaled(400,400))

		elif(name == "Earth"):
			distance = mySolar.Earth.getDistanceToSun()
			orbit = mySolar.Earth.getOrbitalPeriod()
			newDistanceLabelText = "Earth is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/earth.jpg").scaled(400,400))

		elif(name == "Mars"):
			distance = mySolar.Mars.getDistanceToSun()
			orbit = mySolar.Mars.getOrbitalPeriod()
			newDistanceLabelText = "Mars is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/mars.jpeg").scaled(400,400))

		elif(name == "Jupiter"):
			distance = mySolar.Jupiter.getDistanceToSun()
			orbit = mySolar.Jupiter.getOrbitalPeriod()
			newDistanceLabelText = "Jupiter is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/jupiter.jpeg").scaled(400,400))

		elif(name == "Saturn"):
			distance = mySolar.Saturn.getDistanceToSun()
			orbit = mySolar.Saturn.getOrbitalPeriod()
			newDistanceLabelText = "Saturn is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/saturn.jpeg").scaled(400,400))

		elif(name == "Uranus"):
			distance = mySolar.Uranus.getDistanceToSun()
			orbit = mySolar.Uranus.getOrbitalPeriod()
			newDistanceLabelText = "Uranus is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/uranus.jpeg").scaled(400,400))

		elif(name == "Neptune"):
			distance = mySolar.Neptune.getDistanceToSun()
			orbit = mySolar.Neptune.getOrbitalPeriod()
			newDistanceLabelText = "Neptune is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/neptune.jpeg").scaled(400,400))

		elif(name == "Pluto"):
			distance = mySolar.Pluto.getDistanceToSun()
			orbit = mySolar.Pluto.getOrbitalPeriod()
			newDistanceLabelText = "Pluto is " + str(distance) + " km from the sun"
			newOrbitLabelText = "It takes " + str(orbit) + " years to orbit the sun"
			self.infoWidget.setDistanceLabelText(newDistanceLabelText)
			self.infoWidget.setOrbitLabelText(newOrbitLabelText)
			self.infoWidget.imageLabel.setPixmap(QtGui.QPixmap("img/pluto.jpeg").scaled(400,400))

		else:
			print("No buttons found")


##################################END MAIN WIDGET###################################

class buttonWidget(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)

		self.mainLayout = QtGui.QHBoxLayout(self)

		self.buttonFrame = QtGui.QFrame()
		self.buttonFrame.setFrameShape(2)

		self.layout = QtGui.QVBoxLayout(self.buttonFrame)

		self.mercuryButton = QtGui.QPushButton("Mercury")
		self.layout.addWidget(self.mercuryButton)

		self.venusButton = QtGui.QPushButton("Venus")
		self.layout.addWidget(self.venusButton)

		self.earthButton = QtGui.QPushButton("Earth")
		self.layout.addWidget(self.earthButton)

		self.marsButton = QtGui.QPushButton("Mars")
		self.layout.addWidget(self.marsButton)

		self.jupiterButton = QtGui.QPushButton("Jupiter")
		self.layout.addWidget(self.jupiterButton)

		self.saturnButton = QtGui.QPushButton("Saturn")
		self.layout.addWidget(self.saturnButton)

		self.uranusButton = QtGui.QPushButton("Uranus")
		self.layout.addWidget(self.uranusButton)

		self.neptuneButton = QtGui.QPushButton("Neptune")
		self.layout.addWidget(self.neptuneButton)

		self.plutoButton = QtGui.QPushButton("Pluto")
		self.layout.addWidget(self.plutoButton)

		self.mainLayout.addWidget(self.buttonFrame)


class infoWidget(QtGui.QWidget):
	def __init__(self):	
		QtGui.QWidget.__init__(self)

		self.layout = QtGui.QVBoxLayout(self)

		self.layout.addStretch(0)

		#one way to make an image:
		#self.image = QtGui.QImage("img/mercury.jpg")
		#self.imageLabel = QtGui.QLabel()
		#self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.image))
		#self.layout.addWidget(self.imageLabel)

		#better way to make an image
		self.pixmap = QtGui.QPixmap("img/solarSystem.jpeg").scaled(400,400)
		self.imageLabel = QtGui.QLabel()
		self.imageLabel.setPixmap(self.pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignHCenter)
		self.layout.addWidget(self.imageLabel)

		#make distance label
		self.distanceLabel = QtGui.QLabel("Distance from sun")
		self.distanceLabel.setAlignment(QtCore.Qt.AlignHCenter)
		#self.distanceLabel.setMargin(50)
		self.layout.addWidget(self.distanceLabel)

		#make orbit label
		self.orbitLabel = QtGui.QLabel("Orbital Period")
		self.orbitLabel.setAlignment(QtCore.Qt.AlignCenter)
		#self.orbitLabel.setMargin(50)
		self.layout.addWidget(self.orbitLabel)

		self.layout.addStretch(0)

	#These methods set the labels to the inputed text
	def setDistanceLabelText(self,text):
		self.distanceLabel.setText(text)

	def setOrbitLabelText(self,text):
		self.orbitLabel.setText(text)
