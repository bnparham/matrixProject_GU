from Determinant import *
import copy

class Det_R_C:
    def __init__(self,matrix,command):
        self.matrix = matrix
        self.command = command
        
    def transpose(self,matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
                    
    def changeMatrix_by_input(self):
        matrix = copy.deepcopy(self.matrix)
        row = int(self.command[1])-1
        if(self.command[0] == "r"):
            matrix[0],matrix[row] = matrix[row],matrix[0]
            return matrix
        elif(self.command[0] == "c"):
            t_matrix = self.transpose(self.matrix)
            t_matrix[0],t_matrix[row] = t_matrix[row],t_matrix[0]
            return t_matrix
        
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
    
    def smaller_matrix(self,original_matrix, row, col):
        new_matrix = self.copy_matrix(original_matrix)
        new_matrix.remove(original_matrix[row])
        for i in range(len(new_matrix)):
            new_matrix[i].remove(new_matrix[i][col])
        return new_matrix
    
    def solve(self, row, matrix):
        li = []
        for i in range(len(matrix)):
            new_smaller_matrix = self.smaller_matrix(matrix,0,i)
            deteminant = Determinant(new_smaller_matrix)
            det = deteminant.determinantOfMatrix()
            num = int(self.command[1])
            li.append((row[i] * det) * pow(-1,i+1+num))

        answ = sum(li)
        deet = Determinant(self.matrix)
        deet = deet.determinantOfMatrix()
        print(f"deet {deet}")
        if(deet < 0):
            answ = abs(answ) * -1
        else:
            answ = abs(answ)
        
        return answ
    
    def show_calculation(self,row,matrix): 
        smaller_li = []
        for i in range(len(matrix)):
            new_smaller_matrix = self.smaller_matrix(matrix,0,i)
            smaller_li.append(new_smaller_matrix)
        index = 0
        print("\n\n")
        for li in smaller_li:
            if(self.command[0] == "c"):
                li = self.transpose(li)
            len_row = len(li)
            print(f"({(row[index]) * (pow(-1,index+2))})*")
            for i in range(len_row):
                # Lower
                for j in range(len_row):
                    print(li[i][j], end="\t")
                print("", end="\n")
            print("-----------------")
            index += 1
            

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,14]
]

app = Det_R_C(mat, "r 1".split(" "))

matrix = app.changeMatrix_by_input()
row = matrix[0]

print(app.solve(row,matrix))