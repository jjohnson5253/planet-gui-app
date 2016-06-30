from PyQt4 import QtGui, QtCore
from planets import SolarSystem


###################################ORBIT DIALOG#####################################
class orbitDialog(QtGui.QDialog):
	def __init__(self):
		#inherit QtDialog class properties
		QtGui.QDialog.__init__(self)

		self.setWindowTitle("Orbits")

		self.resize(400,500)

		#main layout for orbit dialog (Horizontal)
		#dialog has parent already so just add layout
		#with setLayout(layout) function
		self.mainLayout = QtGui.QHBoxLayout()
		self.setLayout(self.mainLayout)

		#left side layout
		self.leftLayout = QtGui.QVBoxLayout()
		self.mainLayout.addLayout(self.leftLayout)

		#right side layout
		self.rightLayout = QtGui.QVBoxLayout()
		self.mainLayout.addLayout(self.rightLayout)

#####	#is there a better way to enter a lot of text???
		#instruction label
		self.instrLabel = QtGui.QLabel("Enter a day to see how many times\n each planet has orbitted the sun")
		self.leftLayout.addWidget(self.instrLabel)

		#textField
		self.textField = QtGui.QLineEdit()
		self.leftLayout.addWidget(self.textField)

		#go button
		self.goButton = QtGui.QPushButton("Go")
		self.leftLayout.addWidget(self.goButton)
		self.goButton.clicked.connect(self.goButtonClicked)

		#Text label
		self.textLabel = QtGui.QLabel("Some text for now")
		self.rightLayout.addWidget(self.textLabel)

		#get a solarsystem object
		self.mySolar = SolarSystem()

	#for some reason this also runs when u press enter
	def goButtonClicked(self):
		#collect the text from the textField
		inputText = int(self.textField.text())

		#clear the text from the field
		self.textField.setText("")

		#call orbitTime function (defined in SolarSystem class) with input
		self.mySolar.orbitTime(inputText)

		#add orbit times to textLabel
		self.textLabel.setText("Mercury has orbited the sun " + str(self.mySolar.mercuryOrbit) + " times\n\n"
			+ "Venus has orbited the sun " + str(self.mySolar.venusOrbit) + " times\n\n"
			+ "Earth has orbited the sun " + str(self.mySolar.earthOrbit) + " times\n\n"
			+ "Mars has orbited the sun " + str(self.mySolar.marsOrbit) + " times\n\n"
			+ "Jupiter has orbited the sun " + str(self.mySolar.jupiterOrbit) + " times\n\n"
			+ "Saturn has orbited the sun " + str(self.mySolar.saturnOrbit) + " times\n\n"
			+ "Uranus has orbited the sun " + str(self.mySolar.uranusOrbit) + " times\n\n"
			+ "Neptune has orbited the sun " + str(self.mySolar.neptuneOrbit) + " times\n\n"
			+ "pluto has orbited the sun " + str(self.mySolar.plutoOrbit) + " times\n\n")


##############################END ORBIT DIALOG######################################


