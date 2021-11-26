from mesa import Agent
import numpy as np

class ObstacleAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    def step(self):
        pass

class Box(Agent):
    def __init__(self, pos, model):
        super().__init__(pos,model)
        self.pos = pos
        self.carried = False

class StackOfBoxes2(Agent):
    def __init__(self, pos, model):
        super().__init__(pos,model)
        self.pos = pos
        self.boxes =[]

class StackOfBoxes3(Agent):
    def __init__(self, pos, model):
        super().__init__(pos,model)
        self.pos = pos
        self.boxes =[]

class StackOfBoxes4(Agent):
    def __init__(self, pos, model):
        super().__init__(pos,model)
        self.pos = pos
        self.boxes =[]

class StackOfBoxes5(Agent):
    def __init__(self, pos, model):
        super().__init__(pos,model)
        self.pos = pos
        self.boxes =[]
        
class Robot(Agent):
    
    def __init__(self, unique_id, model):

        super().__init__(unique_id, model)
        self.carrying = False
        self.value = 0
        self.box = None

    # def look(self):
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos,moore=False,include_center=False)
        self.direccion = self.random.randrange(0,len(possible_steps))

        disponible = []

        for pos in possible_steps:
            var = True
            for agent in self.model.grid.get_cell_list_contents(pos):
                # if (isinstance(agent, ObstacleAgent) or isinstance(agent,Robot) or isinstance(agent,Box) or isinstance(agent,StackOfBoxes)):
                if (isinstance(agent, ObstacleAgent) or isinstance(agent,Robot) or isinstance(agent,Box) or isinstance(agent,StackOfBoxes2)
                or isinstance(agent,StackOfBoxes3) or isinstance(agent,StackOfBoxes4) or isinstance(agent,StackOfBoxes5)):
                    var = False
                    
            disponible.append(var)
        
        if disponible[self.direccion]:
            self.model.grid.move_agent(self, possible_steps[self.direccion])
            self.value += 1

    def grabBox(self):
        neighbors = self.model.grid.get_neighbors(self.pos,moore=True,include_center=False)
        for n in neighbors:
            if isinstance(n,Box) and self.carrying==False:
                self.box= n
                self.model.grid.remove_agent(n)
                #self.model.grid.move_agent(self,{10,0})
                self.carrying=True
        if self.carrying==False:
            self.move()

    def stackBox(self):
        neighbors = self.model.grid.get_neighbors(self.pos,moore=True,include_center=False)
        for n in neighbors:

            if isinstance(n,StackOfBoxes4) and self.carrying==True and len(n.boxes)==4:
                new_stack = StackOfBoxes5(n.pos,n.pos)
                new_stack.boxes= n.boxes
                new_stack.boxes.append(self.box)
                self.carrying=False
                self.box= None
                
                pos = n.pos
                self.model.grid.remove_agent(n)
                self.model.grid.place_agent(new_stack,pos)
            elif isinstance(n,StackOfBoxes3) and self.carrying==True and len(n.boxes)==3:
                new_stack = StackOfBoxes4(n.pos,n.pos)
                new_stack.boxes= n.boxes
                new_stack.boxes.append(self.box)
                self.carrying=False
                self.box= None
                
                pos = n.pos
                self.model.grid.remove_agent(n)
                self.model.grid.place_agent(new_stack,pos)
            elif isinstance(n,StackOfBoxes2) and self.carrying==True and len(n.boxes)==2:
                new_stack = StackOfBoxes3(n.pos,n.pos)
                new_stack.boxes= n.boxes
                new_stack.boxes.append(self.box)
                self.carrying=False
                self.box= None
                
                pos = n.pos
                self.model.grid.remove_agent(n)
                self.model.grid.place_agent(new_stack,pos)
            elif (self.carrying==True and isinstance(n,Box)):
                    new_stack = StackOfBoxes2(n.pos,n.pos)
                    new_stack.boxes.append(n)
                    new_stack.boxes.append(self.box)

                    pos = n.pos
                    self.model.grid.remove_agent(n)
                    
                    self.model.grid.place_agent(new_stack,pos)
                    
                    self.carrying=False
                    self.box= None     
        if self.carrying==True:
            self.move()

    # def stackBox(self):
    #     neighbors = self.model.grid.get_neighbors(self.pos,moore=True,include_center=False)
    #     for n in neighbors:
    #         if isinstance(n,StackOfBoxes) and self.carrying==True:
    #             if len(n.boxes)<5:
    #                     n.boxes.append(self.box)
    #                     self.carrying=False
    #                     self.box= Box
    #         elif (self.carrying==True and isinstance(n,Box)):
    #                 new_stack = StackOfBoxes(n.pos,n.pos)
    #                 new_stack.boxes.append(n)
    #                 new_stack.boxes.append(self.box)
    #                 self.model.grid.place_agent(new_stack,n.pos)

    #                 self.carrying=False
    #                 self.box= None     
    #     if self.carrying==True:
    #         self.move()

    def advance(self):
        neighbors = self.model.grid.get_neighbors(self.pos,moore=True,include_center=False)

        for n in neighbors:
            if isinstance(n,Robot) and n.carrying==True and self.carrying==False:
                return

        if self.carrying==False:
            self.grabBox()
        else: self.stackBox()
 
        




        
