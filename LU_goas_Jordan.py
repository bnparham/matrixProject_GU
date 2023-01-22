# ---> Parham Baradaran Noveiry
# --- calculate inverse of matrix project with gauss-Jordan method | python ---

# ---| in matrix class there are methods that calculating zero & identity matrix , determinant of matrix , create copy of desired matrix , break big matrix into smaller freagments , and finally inverse of matrix with gauss-Jordan method---|

# ---|| duty of start function is starting program with out any error such as bad inputs (for example getting string instead of number) ||---

class LU_goas:
    def zero_matrix(self,row,col):
        li = []
        for r in range(row):
            li.append([])
            for c in range(col):
                li[-1].append(0)
        return li

    def identity_matrix(self,row,col):
        li = self.zero_matrix(row,col)
        row = len(li)
        count = 0
        for i in li :
            i[count] = 1
            count += 1
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

    def determinant(self,matrix):
        num_rows = len(matrix)
        for row in matrix:
            if(len(row) != num_rows):
                return("Not a square matrix")
        if(len(matrix) == 2):
            simple_determinant = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
            return simple_determinant
        else:
            answer = 0
            num_cols = num_rows
            for j in range(num_cols):
                res = (-1) ** (j) * matrix[0][j] * self.determinant(self.smaller_matrix(matrix, 0, j))
                answer += res
            return answer
    
    def inverse(self,matrix):
        if(len(matrix) == len(matrix[0])):
            if(self.determinant(matrix) != 0):
                A_copy = self.copy_matrix(matrix)
                I_matrix = self.identity_matrix(len(matrix),len(matrix))
                I_matrix_copy = self.copy_matrix(I_matrix)
                
                indices = list(range(len(matrix)))
                
                for fd in range(len(matrix)):
                    fdScaler = 1.0 / A_copy[fd][fd]
                        
                    for j in range(len(matrix)):
                        A_copy[fd][j] *= fdScaler
                        I_matrix_copy[fd][j] *= fdScaler
                    
                    for i in indices[0:fd] + indices[fd+1:]:
                        crScaler = A_copy[i][fd]
                        
                        for j in range(len(matrix)):
                            A_copy[i][j] = A_copy[i][j] - crScaler * A_copy[fd][j]
                            I_matrix_copy[i][j] = I_matrix_copy[i][j] - crScaler * I_matrix_copy[fd][j]
                return I_matrix_copy
            
            else:
                return("The determinant of this matrix is 0")
        else:
            return("Not a square matrix")

# def start():
#     print("please enter col and row |ex: 4 4")
#     error_1 = True
#     while error_1:
#         try:
#             q = [int(i) for i in input("your input : ").split(" ")]
#             error_1 = False                
#         except:
#             print("please enter number !")
#     total = []
#     for i in range(q[0]):
#         row = []
#         for j in range(q[1]):
#             error_2 = True
#             while error_2 :
#                 try:
#                     num = int(input(f"row {i+1} | col {j+1} : "))
#                     error_2 = False
#                     row.append(num)
#                 except:
#                     print("Enter number Please!!")
#         total.append(row)
#         print("-----------")

#     m = matrix()
#     print(m.inverse(total))
# start()