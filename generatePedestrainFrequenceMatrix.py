import cv2
import numpy as np

# matrix = np.zeros([4,4],dtype = float)

# matrix[0][1] = 10
# matrix[0][2] = 10
# matrix[0][3] = 10

# matrix[1][0] = 10
# matrix[1][2] = 10
# matrix[1][3] = 10

# matrix[2][0] = 10
# matrix[2][1] = 10
# matrix[2][3] = 10

# matrix[3][0] = 10
# matrix[3][1] = 10
# matrix[3][2] = 10


# for k in range(3,101):
#     print(k)
#     matrix = np.random.randint(0,6,(4,4))*2
#     matrix = matrix.astype(np.float)

#     for i in range(4):
#         for j in range(4):
#             if i==j:
#                 matrix[i][j] = 0

#     matrixFile = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/EastGate/Matrixs/EastMatrix' + str(k) + '.yml'
#     fs = cv2.FileStorage(matrixFile,cv2.FileStorage_WRITE)
#     fs.write('matrix',matrix)
#     fs.release()



#     print(matrix)








matrix = np.ones([5,5],dtype = float) * 5

matrix[2][3] = 0
matrix[3][2] = 0


for i in range(5):
    matrix[i][i] = 0

matrixFile = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/satelliteMap/testMatrix.yml'
fs = cv2.FileStorage(matrixFile,cv2.FileStorage_WRITE)
fs.write('matrix',matrix)
fs.release()

print('hhh')
exit(0)


matrix = np.ones([5,5],dtype = float) * (-1)

matrix[0][1] = 3
matrix[0][4] = 1

matrix[1][0] = 0
matrix[1][2] = 2
matrix[1][3] = 2

matrix[3][1] = 2


matrixFile = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/datas/satelliteMap/EHiddenMatrix.yml'
fs = cv2.FileStorage(matrixFile,cv2.FileStorage_WRITE)
fs.write('HiddenMatrix',matrix)
fs.release()



print('hhh')
exit(0)




























exit(0)


matrix = np.zeros([4,4],dtype = float)

matrix[0][0] = 0
matrix[0][1] = 0
matrix[0][2] = 10
matrix[0][3] = 10


matrix[1][0] = 0
matrix[1][1] = 0
matrix[1][2] = 0
matrix[1][3] = 10


matrix[2][0] = 0
matrix[2][1] = 0
matrix[2][2] = 0
matrix[2][3] = 0


matrix[3][0] = 0
matrix[3][1] = 0
matrix[3][2] = 0
matrix[3][3] = 0


matrixFile = 'D:/Research/IV2020MapPrediction/Code/MapPrediction/GenerateFakeMap/C++/tmpMatrix/Matrix.yml'
fs = cv2.FileStorage(matrixFile,cv2.FileStorage_WRITE)
fs.write('matrix',matrix)
fs.release()



print(matrix)