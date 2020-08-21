import numpy as np
from cv2 import cv2
import time
import os
import re

def readData(ymlFile):
    fs = cv2.FileStorage(ymlFile,cv2.FileStorage_READ)
    if not fs.isOpened():
        print('Cannot open yml file, program exit')
        exit(-2)
    data = []
    simulationTime = fs.getNode('simulationTime').real()/60 # minutes
    toRight = fs.getNode('toRight').mat()/simulationTime
    toLeft = fs.getNode('toLeft').mat()/simulationTime
    toUp = fs.getNode('toUp').mat()/simulationTime
    toDown = fs.getNode('toDown').mat()/simulationTime
    
    toRight = cv2.resize(toRight,(512,512))
    toLeft = cv2.resize(toLeft,(512,512))
    toUp = cv2.resize(toUp,(512,512))
    toDown = cv2.resize(toDown,(512,512))

    data = np.concatenate((toRight[np.newaxis,:],toLeft[np.newaxis,:],toUp[np.newaxis,:],toDown[np.newaxis,:]),axis=0)
    fs.release()
    return data



testingIndex = np.array([i*10 + j for i in range(72) for j in [5] ])

# YMLFilePath = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/stateMapForCalculateInsideDiff5'
# varList = []
# for M in testingIndex:
#     print(M)
#     data = []
#     for p in range(10):
#         fileName = os.path.join(YMLFilePath,'EastSouth_M%d_P%d.yml'%(M,p))
#         data.append(readData(fileName))
#     data = np.array(data)
#     var = np.var(data,axis=0)
#     var = np.average(var)
#     varList.append(var)

# np.savetxt('SETestingVar.txt',varList)
# exit(0)
# # SEVar = np.average(varList)
# # print('EastSouth average variance = ',SEVar)


YMLFilePath = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/stateMapForCalculateInsideDiff5'
varList = []
for M in testingIndex:
    print(M)
    data = []
    for p in range(10):
        fileName = os.path.join(YMLFilePath,'East_M%d_P%d.yml'%(M,p))
        data.append(readData(fileName))
    data = np.array(data)
    var = np.var(data,axis=0)
    var = np.average(var)
    varList.append(var)
np.savetxt('E5TestingVar.txt',varList)

EVar = np.average(varList)
print('East average variance = ',EVar)
# print('EastSouth average variance = ',SEVar)
# print('Average variance = ',0.5*(EVar+SEVar))