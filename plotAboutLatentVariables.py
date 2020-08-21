import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import time
# from tensorboardX import SummaryWriter
import os


# 可视化隐变量，和不同deltaT的隐变量间的mse
npz = 'D:/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/testingsetZ.npz'
Zs = np.load(npz)
Ez = Zs['Ez']
Sz = Zs['Sz']

# 可视化隐变量
t = [str(i) for i in range(72)]
plt.figure()
plt.scatter(Ez[:,0],Ez[:,1])
plt.scatter(Sz[:,0],Sz[:,1])
for i in range(72):
    plt.annotate(t[i],Ez[i])
    plt.annotate(t[i],Sz[i])

plt.legend(['Ez','Sz'])
# plt.show()

pass

# 可视化同一场景下不同deltaT的数据的隐变量mse
zDict = {}
for i in range(72):
    for j in range(i+1,72):
        data1 = Ez[i]
        data2 = Ez[j]
        diff1 = np.average(np.power((data1-data2),2))

        data1 = Sz[i]
        data2 = Sz[j]
        diff2 = np.average(np.power((data1-data2),2))

        deltaT = abs(int(i) - int(j))
        diff = (diff1 + diff2)/2

        zDict.setdefault(str(deltaT),[])
        zDict[str(deltaT)].append(diff)

zlist = np.zeros(72)
for key in zDict.keys():
    zDict[key] = np.average(zDict[key])
    zlist[int(key)] = zDict[key]
plt.figure()
plt.plot(zlist)
np.savetxt("zdiffWithDeltaT.txt",zlist)


plt.xlabel('deltaT/hour')
plt.ylabel('Distance')
# plt.title('The latent variables distance with different deltaT')
xlabel = np.array(list(range(0,72,3)))*10/60
plt.xticks(range(0,73,3),xlabel)
# plt.grid()

# 可视化两场景间不同deltaT下隐变量的mse
zDict = {}
for i in range(72):
    for j in range(72):
        data1 = Ez[i]
        data2 = Sz[j]
        diff = np.average(np.power((data1-data2),2))
        deltaT = abs(int(i) - int(j))

        zDict.setdefault(str(deltaT),[])
        zDict[str(deltaT)].append(diff)

zlist = np.zeros(72)
for key in zDict.keys():
    zDict[key] = np.average(zDict[key])
    zlist[int(key)] = zDict[key]
plt.figure()
plt.plot(zlist)
plt.xlabel('deltaT')
plt.ylabel('z-z mse')
plt.title('Ez-Sz mse with different deltaT')
plt.xticks(range(0,73,3))
plt.grid()

plt.show()


exit(0)############################################

# 可视化不同deltaT的数据的diff
E = np.load('D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/data5EastTestingMSEDeltaTArray.npy')
SE = np.load('D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/data5SouthEastTestingMSEDeltaTArray.npy')

avg = (E+SE)/2
print(avg[0])
print(avg[1])
print(avg[2])
print(avg[3])
print(avg[12])
# plt.plot(E)
# plt.plot(SE)
plt.plot(avg)
plt.legend(['E','SE','avg'])
plt.legend(['avg'])
plt.xlabel('DeltaT/minutes')
plt.ylabel('state diff')
plt.xticks(range(0,25))
plt.grid()
plt.show()

exit(0)############################################



r = 200
img = np.zeros((r*2+1,r*2+1,4))
for i in range(r*2+1):
    for j in range(r*2+1):
        x = j - r
        y = r - i
        lenth = np.sqrt(x*x + y*y)+0.1
        theta = np.arccos(x/lenth)*180/np.pi
        if y < 0:
            theta = 360-theta

        h = (theta/360.0)*180
        l = 128
        s =  (lenth/r)*255
        alpha = 255
        if lenth>r:
            alpha = 0

        img[i][j][0] = h
        img[i][j][1] = l
        img[i][j][2] = s
        img[i][j][3] = alpha

img = img.astype(np.uint8)
img[:,:,0:3] = cv2.cvtColor(img[:,:,0:3],cv2.COLOR_HLS2BGR)
cv2.imwrite('C://Users//A//Desktop/test.png',img)




exit(0)############################################



x = np.linspace(0,4,1000)

y1 = 1/(x+1)
y2 = np.exp(-0.55*x)

plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(['1/(x+1)','exp(-x)'])
plt.show()


exit(0)############################################


disRange = 2

theta = 0.4
x = np.linspace(-disRange,disRange,200)
z = x*x
f = np.exp(-z/(2*theta*theta))

plt.xticks(np.arange(-disRange,disRange,0.2))
plt.plot(x,f)
plt.grid()
plt.show()


exit(0)############################################

r = 500
size = r*2 + 1
img = np.ones((size,size,3))
img = img*255
for i in range(size):
    for j in range(size):
        x = j-r
        y = r-i
        r_ = math.sqrt(x**2 + y**2)
        if r_ > r:
            continue

        theta = 0
        if r_ != 0:
            theta = math.acos(x/r_)
            theta = theta*180/np.pi
            if y<0:
                theta = 360 - theta

        h = theta/2
        # h = int(h/20)*20
        s = 255
        l = 255 - r_/r*128
        img[i,j,:] = [h,l,s]


img = img.astype(np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_HLS2BGR)


cv2.imshow('img',img)
cv2.waitKey(0)
