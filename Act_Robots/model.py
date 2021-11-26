from mesa.time import SimultaneousActivation
from mesa.space import Grid
from mesa import Model
from mesa.datacollection import DataCollector
from agent import Robot, ObstacleAgent, Box
import time

#Numero celdas sucias
class RobotModel(Model):
    def __init__(self, n_sliders, alto, ancho, nCajas, tiempo):

        #totalCeldas = ancho*alto
        #nSucias = ((totalCeldas) * porcentaje)/100
        #nLimpias = int(totalCeldas - nSucias)

        global start_time
        start_time = time.time_ns() 
        start_time = start_time + (tiempo*1000000000)
        
        self.num_boxes = nCajas
        self.num_agents = n_sliders
        self.grid = Grid(ancho, alto, torus=False)
        self.schedule = SimultaneousActivation(self)

        self.alto =alto
        self.ancho = ancho

        
        self.time = tiempo

        # self.cleanCells = (alto*ancho)-porcentaje(alto*ancho)

        global movimientosCount 
        movimientosCount = 0

        self.datacollector = DataCollector(
            {
                "Movimientos": lambda m: self.count_moves(m),
                "Clean Tiles (in percentage)": lambda m: self.count_type(m),
            }
        )

        numObs = (self.ancho * 2) + (self.alto * 2 - 4)

        listaPosLimite = [(col, ren) for col in [0, ancho-1]
                          for ren in range(alto)]

        for col in range(1, ancho):
            for ren in [0, alto-1]:
                listaPosLimite.append((col, ren))

        for i in range(numObs):
            a = ObstacleAgent(i+1000, self)
            self.schedule.add(a)
            self.grid.place_agent(a, listaPosLimite[i])
        
        for i in range(self.num_boxes):
            while True:
                x= self.random.randint(1,ancho-2)
                y= self.random.randint(1,alto-2)
                if self.grid.is_cell_empty((x, y)):
                    new_dirt = Box((x, y), self)
                    self.grid.place_agent(new_dirt, (x, y))
                    self.schedule.add(new_dirt)
                    break
                
        for i in range(self.num_agents):
            a = Robot(i+2000, self)
            self.schedule.add(a)

            while True:
                x= self.random.randint(1,ancho-2)
                y= self.random.randint(1,alto-2)
                if self.grid.is_cell_empty((x, y)):
                    self.grid.place_agent(a, (x, y))
                    break
        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

        #if self.count_type(self, 'Dirty') == 0:
        #    self.running = False
        current_time = time.time_ns()
        print(current_time - start_time)
        if current_time >= start_time:
            self.running = False
        
    @staticmethod
    def count_type(model):
        count  = 0
        for agent in model.schedule.agents:
            if isinstance(agent, Box):
                count+1
        return (count)

    @staticmethod
    def count_moves(model):
        count = 0
        for agent in model.schedule.agents:
            if isinstance(agent, Robot):
                    count += agent.value
        return count