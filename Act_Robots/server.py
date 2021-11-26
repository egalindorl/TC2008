from agent import StackOfBoxes, StackOfBoxes2, StackOfBoxes3, StackOfBoxes4, StackOfBoxes5
from model import RobotModel, Robot, ObstacleAgent, Box
from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

def RobotPortrayal(agent):
    if agent is None:
        return

    if (isinstance(agent, Box)):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Color": "brown"
        }
        if agent.carried== True:
            portrayal["w"]=0.4
            portrayal["h"]=0.4
            portrayal["Layer"]=2
            
        else:
            portrayal["w"]=0.7
            portrayal["h"]=0.7
            portrayal["Layer"]=0
            
    if (isinstance(agent, Robot)):
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "r": 0.5
        }
        if agent.carrying == False:
            portrayal["Color"] = "green"
            portrayal["Layer"] = 0
        else:
            portrayal["Color"] = "red"
            portrayal["Layer"] = 1

    if (isinstance(agent, ObstacleAgent)):
        portrayal = {
            "Shape": "circle",
            "Color": "grey",
            "Layer": 0,
            "Filled": "true",
            "r": 0.2
        }
    
    # if (isinstance(agent, StackOfBoxes)):
    #     portrayal = {
    #         "Shape": "rect",
    #         "w": 0.7,
    #         "h": 0.7,
    #         "Layer": 0,
    #         "Filled": "true"
    #     }
    #     if len(agent.boxes)==2:
    #         portrayal["Color"] = "yellow"
    #     elif len(agent.boxes)==3:
    #         portrayal["Color"] = "orange"
    #     elif len(agent.boxes)==4:
    #         portrayal["Color"] = "red"
    #     else:
    #         portrayal["Color"] = "purple"

    if (isinstance(agent, StackOfBoxes2)):
        portrayal = {
            "Shape": "rect",
            "w": 0.7,
            "h": 0.7,
            "Layer": 0,
            "Filled": "true",
            "Color": "yellow"
        }
    if (isinstance(agent, StackOfBoxes3)):
        portrayal = {
            "Shape": "rect",
            "w": 0.7,
            "h": 0.7,
            "Layer": 0,
            "Filled": "true",
            "Color": "orange"
        }
    if (isinstance(agent, StackOfBoxes4)):
        portrayal = {
            "Shape": "rect",
            "w": 0.7,
            "h": 0.7,
            "Layer": 0,
            "Filled": "true",
            "Color": "red"
        }
    if (isinstance(agent, StackOfBoxes5)):
        portrayal = {
            "Shape": "rect",
            "w": 0.7,
            "h": 0.7,
            "Layer": 0,
            "Filled": "true",
            "Color": "purple"
        } 
    return portrayal

model_parameters = {
    "nCajas":UserSettableParameter("slider", "Número de cajas",30,1,60,1), 
    "n_sliders": UserSettableParameter("slider", "Número de robots", 5, 1, 10, 1),
    "ancho": 10,
    "alto": 10,
    "tiempo": UserSettableParameter("slider", "Seconds",60,1,360,5)}

grid = CanvasGrid(RobotPortrayal, model_parameters["ancho"], model_parameters["alto"], 500, 500)

# tree_chart = ChartModule(
#     [{"Label": "Clean Tiles (in percentage)","Color": "green"}]
# )

# pie_chart = ChartModule(
#     [{"Label": "Movimientos" ,"Color": "orange"}]
# )
server = ModularServer(RobotModel,
                       [grid],
                       "Robot Cleaning",model_parameters)

server.port = 7979
server.launch()
    



