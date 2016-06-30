#!/usr/bin/env python3

#Jake Johnson 2016

from PyQt4 import QtGui, QtCore

from widgets import MainWidget, buttonWidget, infoWidget
from dialogs import orbitDialog
import sys



class App(QtGui.QApplication):
	def __init__(self):
		#initialize this class as a QApplication
		QtGui.QApplication.__init__(self, sys.argv)

		#set application name
		self.setApplicationName("Planets")

		#instantiate the main window
		self.mainWindow = MainWindow()

		#display the window
		self.mainWindow.show()


class MainWindow(QtGui.QMainWindow):
	'''This is the main GUI window.  This is what contains all the QWidgets seen in the app'''
	def __init__(self):
		#initialize this class as a QMainWindow
		QtGui.QMainWindow.__init__(self)

		#set window title
		self.setWindowTitle("Planets")

		#set window size
		self.resize(470,380)

		#create menu bar
		self.menuBar = self.menuBar()

		#create and add drop down menu to menu bar
		self.menu1 = QtGui.QMenu("Menu1")
		self.menuBar.addMenu(self.menu1)

		#create and add action to drop down menu1
		self.dummyAction = QtGui.QAction("test",self)
		self.menu1.addAction(self.dummyAction)

		#create/add orbitDialog option to main menu bar
		self.orbitAction = QtGui.QAction("Orbits",self)
		self.menuBar.addAction(self.orbitAction)

		#add triggered response to orbitAction
		self.orbitAction.triggered.connect(self.openOrbitWindow)

		#instantiate main widget into this main window (class is described below)
		self.mainWidget = MainWidget()

		#set this windows central widget to the main widget
		self.setCentralWidget(self.mainWidget)

	def openOrbitWindow(self):
		self.orbitDialog = orbitDialog()
		self.orbitDialog.exec_()


#main application loop
def main():
	app = App()

	#start the application loop
	sys.exit(app.exec_())

if(__name__ == "__main__"):
	main()