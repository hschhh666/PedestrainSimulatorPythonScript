import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from scipy.interpolate import interp1d

#############################                输入参数区                #############################

# base_matrix_file = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/Matrixs/SouthEastBaseMatrix.npy'
# real_matrix_path = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastSouthGate/Matrixs/realMatrix6/'
# matrix_base_name = 'SouthEastMatrix_'

base_matrix_file = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/Matrixs/EastBaseMatrix.npy'
real_matrix_path = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/Matrixs/realMatrix7/'
matrix_base_name = 'EastMatrix_'

#############################                可调参数区                #############################
T1 = [180,60,30] # minutes 人流波动周期
A1 = [1,0.3,0.1]#每个周期对应的幅度

T2 = [60] # minutes 进出比例波动周期
A2 = [1,0.5,0.2]#每个周期对应的幅度

T3 = [360,120,60] # minutes 进入比例波动周期
A3 = [1,0.3,0.1]#每个周期对应的幅度

max_people = 60#人最多时每分钟60个，最少时每分钟5个
min_people = 5

max_in_and_out = 0.8#最多80%的人在进出，最少50%的人在进出
min_in_and_out = 0.5

max_in_vs_out = 0.9#最多80%的人在进，最少10%的人在进
min_in_vs_out = 0.1


#############################                主程序                #############################

base_matrix = np.load(base_matrix_file)#加载基础矩阵
matrix_num = np.shape(base_matrix)[0]#获取矩阵个数，这也是将要生成的真实矩阵的个数
times = np.array(list(range(matrix_num))) #单位，minutes ，一个矩阵表示一分钟，这里times表明这些矩阵代表的总时长

people_per_min_curve = 0#定义人流曲线
in_and_out_people_ratio = 0#定义进出占比曲线
in_vs_out_ratio = 0#定义进入占比曲线

for i,t in enumerate(T1):
    people_per_min_curve += A1[i] * np.sin((2*np.pi/t)*times)#用周期函数生成人流曲线

for i,t in enumerate(T2):
    in_and_out_people_ratio += A2[i] * np.sin((2*np.pi/t)*times)#用周期函数生成进出占比曲线



for i,t in enumerate(T3):
    baseMove = 0
    curMove = T3[0]/T3[i]
    in_vs_out_ratio += A3[i] * np.sin((2*np.pi/t)*times + curMove*baseMove)#用周期函数生成进入占比曲线

#对人流曲线归一化，归一化到前面定义的最大最小值范围
mmin = min(people_per_min_curve)
mmax = max(people_per_min_curve)
people_per_min_curve -= mmin
people_per_min_curve /= (mmax-mmin)
people_per_min_curve *= (max_people-min_people)
people_per_min_curve += min_people

people_per_min_curve = 65 - people_per_min_curve





pointPointNum = 720
y = [0.99651466,0.58551034,0.77282716,0.04806611,0.3895887, 0.08065472,0.99742676,0.65559225,0.84796853,0.34554313,0.11367945,0.0472786,0.99651466,0.58551034,0.77282716,0.04806611,0.3895887, 0.08065472,0.99742676,0.65559225,0.84796853,0.34554313,0.11367945,0.0472786]# correlate coefficient = 0.84
y = [5,7,50,50,8,5,9,30,4,10,3,7,5,5,7,50,50,8,5,9,30,4,10,3,7,5] # correlate coefficient = 0.5
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

people_per_min_curve = y_smothed




#对进出占比曲线归一化，归一化到前面定义的最大最小值范围
mmin = min(in_and_out_people_ratio)
mmax = max(in_and_out_people_ratio)
in_and_out_people_ratio -= mmin
in_and_out_people_ratio /= (mmax-mmin)
in_and_out_people_ratio *= (max_in_and_out-min_in_and_out)
in_and_out_people_ratio += min_in_and_out

in_and_out_people_ratio = np.ones([matrix_num])*0.8

#对进入占比曲线归一化，归一化到前面定义的最大最小值范围
mmin = min(in_vs_out_ratio)
mmax = max(in_vs_out_ratio)
in_vs_out_ratio -= mmin
in_vs_out_ratio /= (mmax-mmin)
in_vs_out_ratio *= (max_in_vs_out-min_in_vs_out)
in_vs_out_ratio += min_in_vs_out

in_vs_out_ratio = 1- in_vs_out_ratio

xlabel = []
for h in range(8,21):
    for m in [0]:
        h_s = str(h)
        m_s = str(m)
        if h < 10:
            h_s = '0' + h_s
        if m < 10:
            m_s = '0' + m_s
        time = h_s + ':' + m_s
        xlabel.append(time)


frame = plt.subplot(3,1,1)
plt.plot(people_per_min_curve)
# plt.title('total people number curve')
# plt.xlabel('time')
plt.ylabel('people num',rotation = 'horizontal',labelpad=40)
# plt.xticks(range(0,900,30),xlabel)
plt.xticks([])
plt.yticks(range(5,80,30))
plt.ylim([0,70])
plt.yticks(size=10)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
# plt.xticks(range(0,721,60))


frame = plt.subplot(3,1,2)
plt.plot(in_and_out_people_ratio)
# plt.title('inAndOut ratio curve')
# plt.xlabel('time')
plt.ylabel('inAndOut ratio',rotation = 'horizontal',labelpad=40)
# plt.xticks(range(0,900,30),xlabel)
plt.xticks([])
plt.yticks(np.arange(0.2,1,0.3))
plt.ylim([0,1])
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
# plt.xticks(range(0,721,60))

frame = plt.subplot(3,1,3)
plt.plot(in_vs_out_ratio)
# plt.title('in/(in+out) curve')
plt.xlabel('time',size = 20)
plt.ylabel('in/(in+out)',rotation = 'horizontal',labelpad=40)
# plt.xticks(range(0,721,60))
plt.xticks(range(0,721,60),xlabel)
plt.yticks(np.arange(0.2,1,0.3))
plt.ylim([0,1])
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


plt.show()

key = input('press y/Y to generate real matrix:')
if key in ['y','Y']:
    pass
else:
    exit(0)

for i,matrix in enumerate(base_matrix):
    people = people_per_min_curve[i]
    in_and_out = in_and_out_people_ratio[i]
    in_vs_out = in_vs_out_ratio[i]

    sum1 = np.sum(matrix[0,:])
    sum2 = np.sum(matrix[:,0])
    coefficient = in_vs_out*sum2/(sum1-in_vs_out*sum1) # 对于方程 ax/(ax+b) = c，求解x。其中sum1是a，sum2是b，in_vs_out是c
    matrix[0,:] = coefficient * matrix[0,:] #归一化进入占比

    sum1 = np.sum(matrix[0,:]) + np.sum(matrix[:,0])
    sum2 = np.sum(matrix) - sum1

    coefficient = in_and_out*sum2/(sum1-in_and_out*sum1)# 对于方程 ax/(ax+b) = c，求解x。其中sum1是a，sum2是b，in_and_out是c
    matrix[0,:] = coefficient * matrix[0,:]
    matrix[:,0] = coefficient * matrix[:,0]#归一化进出占比

    matrix = matrix / (np.sum(matrix))
    matrix = matrix * people#归一化人流总数

    matrix_file_name = matrix_base_name + str(i+1) +'.yml'
    matrix_file_name = os.path.join(real_matrix_path,matrix_file_name)

    fs = cv2.FileStorage(matrix_file_name,cv2.FileStorage_WRITE)#保存入文件中
    fs.write('matrix',matrix)
    fs.release()
    print('writing to ',matrix_file_name)

