import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


T1 = [180,60,30] # minutes 人流波动周期
A1 = [1,0.3,0.1]#每个周期对应的幅度

T2 = [60] # minutes 进出比例波动周期
A2 = [1,0.5,0.2]#每个周期对应的幅度

T3 = [360,120,60] # minutes 进入比例波动周期
A3 = [1,0.3,0.1]#每个周期对应的幅度

max_people = 65#人最多时每分钟60个，最少时每分钟5个
min_people = 5

max_in_and_out = 0.8#最多80%的人在进出，最少50%的人在进出
min_in_and_out = 0.5

max_in_vs_out = 0.9#最多80%的人在进，最少10%的人在进
min_in_vs_out = 0.1


#############################                主程序                #############################


times = np.array(list(range(720))) #单位，minutes ，一个矩阵表示一分钟，这里times表明这些矩阵代表的总时长

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

#对进出占比曲线归一化，归一化到前面定义的最大最小值范围
mmin = min(in_and_out_people_ratio)
mmax = max(in_and_out_people_ratio)
in_and_out_people_ratio -= mmin
in_and_out_people_ratio /= (mmax-mmin)
in_and_out_people_ratio *= (max_in_and_out-min_in_and_out)
in_and_out_people_ratio += min_in_and_out

# in_and_out_people_ratio = np.ones([matrix_num])*0.8

#对进入占比曲线归一化，归一化到前面定义的最大最小值范围
mmin = min(in_vs_out_ratio)
mmax = max(in_vs_out_ratio)
in_vs_out_ratio -= mmin
in_vs_out_ratio /= (mmax-mmin)
in_vs_out_ratio *= (max_in_vs_out-min_in_vs_out)
in_vs_out_ratio += min_in_vs_out

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

feature1 = people_per_min_curve
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
# ax.spines['bottom'].set_visible(False)
plt.xticks(range(0,721,60),xlabel)
# plt.show()










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


times = np.array(list(range(720))) #单位，minutes ，一个矩阵表示一分钟，这里times表明这些矩阵代表的总时长

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

#对进出占比曲线归一化，归一化到前面定义的最大最小值范围
mmin = min(in_and_out_people_ratio)
mmax = max(in_and_out_people_ratio)
in_and_out_people_ratio -= mmin
in_and_out_people_ratio /= (mmax-mmin)
in_and_out_people_ratio *= (max_in_and_out-min_in_and_out)
in_and_out_people_ratio += min_in_and_out

# in_and_out_people_ratio = np.ones([matrix_num])*0.8

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

feature2 = people_per_min_curve
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
# ax.spines['bottom'].set_visible(False)
plt.xticks(range(0,721,60),xlabel)

plt.legend(['South East','East'])
plt.title('Simulation people numble')
plt.xlabel('Time')

plt.show()

corre = np.corrcoef(feature1,feature2)
print('correlation coefficient = ',corre[0,1])

exit(0)


















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