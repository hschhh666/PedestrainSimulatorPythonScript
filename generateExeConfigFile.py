import os

# for i in range(1,721):


#     outName = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/iniFiles/Simulator%d.ini'%i


#     out = open(outName,'w')


#     context = "[param]\nvisualRate = 0 # 0 no visual, >0 visualRate.\nsimulationTime = 120 # seconds\nsimulationNum = 1 # simulating how many times\nbaseName = EastSouth_M%d_P\n\n\n[input]\nsceneFile = D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\satelliteMap\SEMask.yml\nsatelliteFile = D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\satelliteMap\SESatellite.png\npedestrianMatrix  = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/Matrixs/realMatrix6/SouthEastMatrix_%d.yml\n\n[output]\nvideo = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/tmp.avi #if don't want video , just keep this path empty\nstateMapDir = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/stateMapDir6/"%(i,i)

#     out.write(context)
#     out.close()



# for i in range(1,721):


#     outName = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/iniFiles2/Simulator%d.ini'%i


#     out = open(outName,'w')


#     context = "[param]\nvisualRate = 0 # 0 no visual, >0 visualRate.\nsimulationTime = 120 # seconds\nsimulationNum = 1 # simulating how many times\nbaseName = East_M%d_P\n\n\n[input]\nsceneFile = D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\satelliteMap\EMask.yml\nsatelliteFile = D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\satelliteMap\ESatellite.png\npedestrianMatrix  = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/Matrixs/realMatrix7/EastMatrix_%d.yml\n\n[output]\nvideo = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/tmp.avi #if don't want video , just keep this path empty\nstateMapDir = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/stateMapDir7/"%(i,i)

#     out.write(context)
#     out.close()





for i in range(72):
    outName = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/iniFiles3/Simulator%d.ini'%i
    out = open(outName,'w')


    context = "[param]\nvisualRate = 0 # 0 no visual, >0 visualRate.\nsimulationTime = 120 # seconds\nsimulationNum = 10 # simulating how many times\nbaseName = East_M%d_P\n\n\n[input]\nsceneFile = D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\satelliteMap\EMask.yml\nsatelliteFile = D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\satelliteMap\ESatellite.png\npedestrianMatrix  = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/Matrixs/realMatrix7/EastMatrix_%d.yml\n\n[output]\nvideo = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/tmp.avi #if don't want video , just keep this path empty\nstateMapDir = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/stateMapForCalculateInsideDiff7/"%(i*10+5,i*10+5)

    out.write(context)
    out.close()

# for i in range(72):


#     outName = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/iniFiles2/Simulator%d.ini'%i


#     out = open(outName,'w')


#     context = "[param]\nvisualRate = 0 # 0 no visual, >0 visualRate.\nsimulationTime = 120 # seconds\nsimulationNum = 10 # simulating how many times\nbaseName = EastSouth_M%d_P\n\n\n[input]\nsceneFile = D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\satelliteMap\SEMask.yml\nsatelliteFile = D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\satelliteMap\SESatellite.png\npedestrianMatrix  = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/Matrixs/realMatrix5/SouthEastMatrix_%d.yml\n\n[output]\nvideo = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/tmp.avi #if don't want video , just keep this path empty\nstateMapDir = D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/stateMapForCalculateInsideDiff5/"%(i*10+5,i*10+5)

#     out.write(context)
#     out.close()