import numpy as np
import cv2

'''
输入：矩阵size、保存路径
输出：基础矩阵的npy文件

仿真时间从8::到21:30，本程序生成的是基础矩阵
首先每半小时生成一个矩阵，总共生成28个，要求这些矩阵和为1，且任意两个矩阵间的JS散度不低于某个阈值
然后在相邻两个矩阵间线性插值，生成每分钟的矩阵

'''
matrix_size = 5
# filePath = 'D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\EastSouthGate\Matrixs\SouthEastBaseMatrix.npy'
filePath = 'D:\Research\IV2020MapPrediction\Code\MapPrediction\GenerateFakeMap\datas\EastGate\Matrixs\EastBaseMatrix.npy'

matrixs = []
base_matrixs = []


def JS_divergence(a,b):
    KL1 = 0
    KL2 = 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            if a[i][j] * b[i][j] == 0:
                continue
            p = a[i][j]
            q = b[i][j]
            KL1 += p*np.log10(p/q)
            KL2 += q*np.log10(q/p)
    JS = (KL1 + KL2)/2
    return JS


for i in range(3):# 22-8 = 14,14*2 = 28
    count = 0
    while(1):
        count += 1
        tmp_matrix = np.random.uniform(0.001,1,(matrix_size,matrix_size))
        j = list([x for x in range(matrix_size)])
        tmp_matrix[j,j] = 0
        
        # # South East
        # tmp_matrix[3,4] = 0
        # tmp_matrix[3,5] = 0
        # tmp_matrix[4,3] = 0
        # tmp_matrix[4,5] = 0
        # tmp_matrix[5,4] = 0
        # tmp_matrix[5,3] = 0

        # East
        tmp_matrix[2,3] = 0
        tmp_matrix[3,2] = 0

        tmp_matrix = tmp_matrix/np.sum(tmp_matrix)

        # south east
        # sum1 = np.sum(tmp_matrix[0,:])
        # tmp_matrix[0,1] = sum1 * 0.2
        # tmp_matrix[0,2] = sum1 * 0.5
        # sum2 = tmp_matrix[0,3] +  tmp_matrix[0,4] +  tmp_matrix[0,5] 
        # tmp_matrix[0,3] = sum1 * 0.3 * tmp_matrix[0,3]/sum2
        # tmp_matrix[0,4] = sum1 * 0.3 * tmp_matrix[0,4]/sum2
        # tmp_matrix[0,5] = sum1 * 0.3 * tmp_matrix[0,5]/sum2

        # sum1 = np.sum(tmp_matrix[:,0])
        # tmp_matrix[1,0] = sum1 * 0.2
        # tmp_matrix[2,0] = sum1 * 0.5
        # sum2 = tmp_matrix[3,0] +  tmp_matrix[4,0] +  tmp_matrix[5,0] 
        # tmp_matrix[3,0] = sum1 * 0.3 * tmp_matrix[3,0]/sum2
        # tmp_matrix[4,0] = sum1 * 0.3 * tmp_matrix[4,0]/sum2
        # tmp_matrix[5,0] = sum1 * 0.3 * tmp_matrix[5,0]/sum2


        # east
        sum1 = np.sum(tmp_matrix[0,:])
        tmp_matrix[0,1] = sum1 * 0.1
        sum2 = tmp_matrix[0,2] + tmp_matrix[0,3] + tmp_matrix[0,4]
        tmp_matrix[0,2] = sum1 * 0.9 * tmp_matrix[0,2]/sum2
        tmp_matrix[0,3] = sum1 * 0.9 * tmp_matrix[0,3]/sum2
        tmp_matrix[0,4] = sum1 * 0.9 * tmp_matrix[0,4]/sum2

        sum1 = np.sum(tmp_matrix[:,0])
        tmp_matrix[1,0] = sum1 * 0.1
        sum2 = tmp_matrix[2,0] + tmp_matrix[3,0] + tmp_matrix[4,0]
        tmp_matrix[2,0] = sum1 * 0.9 * tmp_matrix[2,0]/sum2
        tmp_matrix[3,0] = sum1 * 0.9 * tmp_matrix[3,0]/sum2
        tmp_matrix[4,0] = sum1 * 0.9 * tmp_matrix[4,0]/sum2


        js = np.inf
        for matrix in base_matrixs:
            tmp_js = JS_divergence(matrix,tmp_matrix)
            if tmp_js<js:
                js = tmp_js
        if js > 0.3:
            base_matrixs.append(tmp_matrix)
            print('matrix %d loop %d times'%(i,count))
            break

base_matrixs.append(base_matrixs[0])
base_matrixs.append(base_matrixs[1])
base_matrixs.append(base_matrixs[2])
base_matrixs.append(base_matrixs[0])



for i in range(3):
    print(base_matrixs[i])
    print(np.sum(base_matrixs[i]))
    print()

for i in range(6):
    matrix1 = base_matrixs[i]
    matrix2 = base_matrixs[i+1]
    matrixs.append(matrix1)
    for j in range(1,120):
        tmp_matrix = (matrix2-matrix1)*j/120 + matrix1
        matrixs.append(tmp_matrix)

np.save(filePath,matrixs)