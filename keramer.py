import copy
from Determinant import Determinant

class cramer:
    def __init__(self):
        pass

    def transpose(self,matrix):
            return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def zero_matrix(self,row,col):
        li = []
        for r in range(row):
            li.append([])
            for c in range(col):
                li[-1].append(0)
        return li

    def copy_matrix(self,matrix):
        row = len(matrix)
        col = len(matrix[0])
        li = self.zero_matrix(row,col)
        for r in range(row):
            for c in range(col):
                li[r][c] = matrix[r][c]
        return li


    def ceramer(self,matrix,b):
        x_answers = []
        mat = self.transpose(matrix)
        mat_copy = copy.deepcopy(mat)
        total_mat_change = []
        for i in range(len(matrix)):
            mat[i] = b
            total_mat_change.append(self.transpose(mat))
            mat = mat_copy
        det_mat_asli = Determinant(matrix)
        det_mat_asli = det_mat_asli.determinantOfMatrix()
        for li in total_mat_change:
            det_mat_cramer = Determinant(li)
            det_mat_cramer = det_mat_cramer.determinantOfMatrix()
            x_answers.append(det_mat_cramer/det_mat_asli)
        return x_answers
        
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,14]
]
b = [1,1,1]

a = cramer()
print(a.ceramer(matrix,b))
