# TC2008B. Sistemas Multiagentes y Gráficas Computacionales
# Python flask server to interact with Unity. Based on the code provided by Sergio Ruiz.
# Octavio Navarro. October 2021

from flask import Flask, request, jsonify
from mesa import model
from agent import StackOfBoxes2, StackOfBoxes3, StackOfBoxes4, StackOfBoxes5
from model import *

# Size of the board:
nCajas = 30
nRobots=5
width = 10
height = 10
tiempo=60
trafficModel = None
currentStep = 0

app = Flask("Traffic example")

# @app.route('/', methods=['POST', 'GET'])

@app.route('/init', methods=['POST', 'GET'])
def initModel():
    global currentStep, trafficModel, number_agents, width, height

    if request.method == 'POST':
        currentStep = 0

        print(request.form)
        print(nRobots, width, height,nCajas,tiempo)
        trafficModel = RobotModel(nRobots, width, height,nCajas,tiempo)

        return jsonify({"message":"Parameters recieved, model initiated."})
    else: return jsonify({"message":":P, model initiated."})

'''
@app.route('/getAgents', methods=['GET'])
def getAgents():
    global trafficModel

    if request.method == 'GET':
        carPositions = [{"x": x, "y":y} for (a, x, y) in trafficModel.grid.coord_iter() if isinstance(a,Robot)]

        return jsonify({'positions':carPositions})
'''

@app.route('/getObstacles', methods=['GET'])
def getObstacles():
    global trafficModel

    if request.method == 'GET':
        carPositions = [{"x": x*10, "y":2.52,"z":y*10} for (a, x, y) in  trafficModel.grid.coord_iter()if isinstance(a, Box)]

        
        return jsonify({'positions':carPositions})

@app.route('/update', methods=['GET'])
def updateModel():
    global currentStep,trafficModel 
    if request.method == 'GET':
        trafficModel.step()
        currentStep += 1
        print("moves: ", trafficModel.count_moves(trafficModel))
        return jsonify({'message':f'Model updated to step {currentStep}.', 'currentStep':currentStep})

@app.route('/getAgents', methods=['GET'])
def getAgents():
    global trafficModel

    if request.method == 'GET':

        robots = [a for a in trafficModel.grid.coord_iter() if isinstance(a,Robot)]#.sort(key=lambda a: a[0].unique_id)
        print(robots)
        carPositions = [({"x": x*10, "y":2.52, "z": y*10}, a.unique_id) for (a,x,y) in trafficModel.grid.coord_iter() if isinstance(a,Robot)]
        sortedPositions = sorted(carPositions, key= lambda a: a[1])
        print(sortedPositions)

        carPositions = [p for (p,a) in sortedPositions] 
        return jsonify({'positions':carPositions})

@app.route('/getStack2', methods=['GET'])
def getAgents2():
    global trafficModel

    if request.method == 'GET':

        carPositions = [{"x": x*10, "y":9, "z": y*10} for (a, x, y) in trafficModel.grid.coord_iter() if isinstance(a,StackOfBoxes2)]
        return jsonify({'positions':carPositions})

@app.route('/getStack3', methods=['GET'])
def getAgents3():
    global trafficModel

    if request.method == 'GET':

        carPositions = [{"x": x*10, "y":2.52, "z": y*10} for (a, x, y) in trafficModel.grid.coord_iter() if isinstance(a,StackOfBoxes3)]
        return jsonify({'positions':carPositions})
@app.route('/getStack4', methods=['GET'])
def getAgents4():
    global trafficModel

    if request.method == 'GET':

        carPositions = [{"x": x*10, "y":2.52, "z": y*10} for (a, x, y) in trafficModel.grid.coord_iter() if isinstance(a,StackOfBoxes4)]
        return jsonify({'positions':carPositions})

@app.route('/getStack5', methods=['GET'])
def getAgents5():
    global trafficModel

    if request.method == 'GET':

        carPositions = [{"x": x*10, "y":2.52, "z": y*10} for (a, x, y) in trafficModel.grid.coord_iter() if isinstance(a,StackOfBoxes5)]
        return jsonify({'positions':carPositions})

@app.route('/updatelights', methods=['GET'])
def getLights():
    global trafficModel

    if request.method == 'GET':
        carPositions = [a for a in trafficModel.grid.coord_iter() if isinstance(a,Robot)]
        print("lights: ",carPositions)
        sortedPositions = sorted(carPositions, key= lambda a: a[1])
        print("sorted lights: ",sortedPositions)

        carPositions = [p for (p,a) in sortedPositions] 
        return jsonify({'positions':carPositions})

if __name__=='__main__':
    app.run(host="localhost", port=8585, debug=True)
