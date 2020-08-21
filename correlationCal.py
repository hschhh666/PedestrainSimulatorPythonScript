import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

while(1):
    pointPointNum = 720
    y = [5,7,50,50,8,5,9,30,4,10,3,7,5,5,7,50,50,8,5,9,30,4,10,3,7,5] # correlate coefficient = 0.5

    # y = np.random.rand(12)
    # y = np.concatenate((y,y))
    # y = [0.99651466,0.58551034,0.77282716,0.04806611,0.3895887, 0.08065472,0.99742676,0.65559225,0.84796853,0.34554313,0.11367945,0.0472786,0.99651466,0.58551034,0.77282716,0.04806611,0.3895887, 0.08065472,0.99742676,0.65559225,0.84796853,0.34554313,0.11367945,0.0472786]# correlate coefficient = 0.84
    
    print(y)


    x = np.linspace(0,pointPointNum-1, len(y))
    y = np.array(y)

    smothFun = interp1d(x,y,kind=2)

    x_smothed = np.linspace(0,pointPointNum-1,pointPointNum)
    y_smothed = smothFun(x_smothed)


    mmin = min(y_smothed)
    mmax = max(y_smothed)
    y_smothed -= mmin
    y_smothed /= (mmax-mmin)
    y_smothed *= (55-5)
    y_smothed += 5


    # plt.plot(x,y,'o',x_smothed,y_smothed)
    # plt.xticks(range(0,pointPointNum,50))
    # plt.show()

    # exit(0)

    #############################                可调参数区                #############################
    T1 = [180,60,30] # minutes 人流波动周期
    A1 = [1,0.3,0.1]#每个周期对应的幅度

    T2 = [90,45,36] # minutes 人流波动周期
    A2 = [1,0.2,0.4]#每个周期对应的幅度



    max_people = 60#人最多时每分钟60个，最少时每分钟5个
    min_people = 5

    T3 = [360,120,60] # minutes 进入比例波动周期
    A3 = [1,0.3,0.1]#每个周期对应的幅度

    #############################                主程序                #############################

    times = np.array(list(range(720))) #单位，minutes ，一个矩阵表示一分钟，这里times表明这些矩阵代表的总时长

    feature1 = 0#定义人流曲线
    feature2 = 0

    for i,t in enumerate(T1):
        feature1 += A1[i] * np.sin((2*np.pi/t)*times)#用周期函数生成人流曲线
        
    for i,t in enumerate(T2):
        baseMove = 0
        curMove = T1[0]/T1[i]
        feature2 += A2[i] * np.sin((2*np.pi/t)*times + curMove * baseMove)#用周期函数生成人流曲线

    feature2 = y_smothed
    feature2 = np.copy(feature1) # correlate coefficient = 1

    # feature2 = 0
    # for i,t in enumerate(T3):
    #     feature2 += A3[i] * np.sin((2*np.pi/t)*times)

    #对人流曲线归一化，归一化到前面定义的最大最小值范围
    mmin = min(feature1)
    mmax = max(feature1)
    feature1 -= mmin
    feature1 /= (mmax-mmin)
    feature1 *= (65-5)
    feature1 += min_people

    # y = feature1[::43]
    # x = np.linspace(0,pointPointNum-1, len(y))
    # y = np.array(y)
    # smothFun = interp1d(x,y,kind=2)
    # x_smothed = np.linspace(0,pointPointNum-1,pointPointNum)
    # y_smothed = smothFun(x_smothed)
    # feature2 = y_smothed


    mmin = min(feature2)
    mmax = max(feature2)
    feature2 -= mmin
    feature2 /= (mmax-mmin)
    feature2 *= (55-5)
    feature2 += min_people



    # feature1 = feature1
    # feature2 = np.random.rand(720)

    correcof = []
    deltaT_range = 60
    for deltaT in range(-deltaT_range,deltaT_range + 1):
        if deltaT > 0:
            f1 = feature1[deltaT:]
            f2 = feature2[:-deltaT]
        elif deltaT < 0:
            deltaT = -deltaT
            f1 = feature1[0:-deltaT]
            f2 = feature2[deltaT:]
        else:
            f1 = feature1
            f2 = feature2

        corre = np.abs(np.corrcoef(f1,f2)[0][1])
        correcof.append(corre)

    correcof = np.array(correcof)
    corre = np.corrcoef(feature1,feature2)


    print('================================')
    print('deltaT=0 correlation coefficient = ',corre[0][1])
    print('deltaT max correlation coefficient = ',np.max(correcof))



    
    # if  0.72<corre[0][1] <0.75:
    plt.figure()
    plt.title('People num change of two gates')
    plt.plot(feature1)
    plt.plot(feature2)

    # np.savetxt('SE.txt',feature1)
    # np.savetxt('E100.txt',feature2)

    plt.legend(['SouthEast','East'])
    plt.yticks(range(5,80,30))
    plt.ylim([0,70])


    plt.figure()
    plt.plot(list(range(-deltaT_range,deltaT_range + 1)),correcof)
    plt.show()

