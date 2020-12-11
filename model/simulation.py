from model.particle import Particle
# from model.particleState import ParticleState
# from model.statistics import Statistics
import random


class Simulation:
    def __init__(self, countParticles):
        print("Simulation Created")
        self.stepCounter = 0
        self.radius = 3
        self.particleList = {}
        for i in range(0, countParticles):
            rndmX = random.randint(0, 200)
            rndmY = random.randint(0, 200)
            self.particleList[i] = Particle(rndmX, rndmY)
        self.particleList[random.randint(0, len(self.particleList) - 1)].state = "infected"

    def performStep(self):
        self.stepCounter += 1
        print("Simulation step {} processed.".format(self.stepCounter))
        for i in range(0, len(self.particleList)):
            self.particleList[i].move()
        self.detectCollisions()

    def detectCollisions(self):
        for i in range(0, len(self.particleList)):
            for j in range(0, len(self.particleList)):
                if(abs(self.particleList[i].x -self.particleList[j].x) <= self.radius and abs(self.particleList[i].y - self.particleList[j].y) <= self.radius and self.particleList[i].state == "healthy" and self.particleList[j].state == "infected"): #and self.particleList[j].state == "infected"
                    infectionRate = 12 #Percent
                    rndm = random.randint(1, 100)
                    print(rndm)
                    if(rndm <= infectionRate):
                        self.particleList[i].state = "infected"

    def setRadius(self, radius):
        self.radius = radius

    def getData(self):
        return self.stepCounter

    def getParticles(self):
        return self.particleList