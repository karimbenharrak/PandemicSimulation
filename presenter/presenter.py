from PyQt5 import QtCore

from view.view import View
from model.simulation import Simulation

FPS = 60

class Presenter(QtCore.QObject):
    def __init__(self):
        super(Presenter, self).__init__()
        # create main window
        self.ui = View()
        self.simulation = None
        self.isSimulationRunning = False

        # create timer that will call the mainLoop every 1000/FPS milliseconds
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainLoop)
        self.timer.start(int(1000 / FPS))
        self.framecounter = 0

        self._connectUIElements()

    def mainLoop(self):
        if self.isSimulationRunning:
            self.simulation.performStep()
            self.ui.updateParticles(self.simulation.getParticles())
            # self.ui.updateData(self.simulation.getData())

    def startSimulation(self, countParticles):
        self.isSimulationRunning = True
        print("Hello World from Presenter")
        self.simulation = Simulation(countParticles)
        self.ui.startSimulation()

    def pauseSimulation(self):
        self.isSimulationRunning = False
        print("Hello World from Presenter")
        self.ui.pauseSimulation()

    def resetSimulation(self):
        self.isSimulationRunning = False
        self.simulation = None
        print("Hello World from Presenter")
        self.ui.resetSimulation()

    def speedSimulation(self, value):
        self.timer.disconnect()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainLoop)
        self.timer.start(int(1000 / value))

    def changeRadius(self, radius):
        if(self.simulation != None):
            self.simulation.setRadius(radius)

    def _connectUIElements(self) -> None:
        # elements of the main window
        self.ui.startSimulationSignal.connect(self.startSimulation)
        self.ui.pauseSimulationSignal.connect(self.pauseSimulation)
        self.ui.resetSimulationSignal.connect(self.resetSimulation)
        self.ui.speedSimulationSignal.connect(self.speedSimulation)
        self.ui.radiusChangedSignal.connect(self.changeRadius)