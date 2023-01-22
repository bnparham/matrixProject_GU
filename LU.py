class LU:
    def __init__(self,matrix):
        self.matrix = matrix
        
    # ساخت ماتریس صفر
    def zero_matrix(self,row,col):
        li = []
        for r in range(row):
            li.append([])
            for c in range(col):
                li[-1].append(0)
        return li
    
    # متد محاسبه تجزیه به روش ال یو
    def solve(self):
        mat = self.matrix
        row = len(mat)
        col = len(mat[0])
        lower = self.zero_matrix(row,col)
        upper = self.zero_matrix(row,col)
        for i in range(row):
            
            # ساخت ماتریس بالا مثلثی
            for k in range(i, row):
                # Summation of L(i, j) * U(j, k)
                sum = 0
                for j in range(i):
                    sum += (lower[i][j] * upper[j][k])
                    

                # Evaluating U(i, k)
                upper[i][k] = mat[i][k] - sum
                
            # ساخت ماتریس پایین مثلثی
            for k in range(i, row):
                # قطر اصلی برابر یک
                if (i == k):
                    lower[i][i] = 1 # Diagonal as 1
                else:
                    # Summation of L(k, j) * U(j, i)
                    sum = 0
                    for j in range(i):
                        sum += (lower[k][j] * upper[j][i])

                    # Evaluating L(k, i)
                    try:
                        lower[k][i] = float((mat[k][i] - sum) /
                        upper[i][i])
                    except:
                        lower[k][i] = float(mat[k][i] - sum)          
        return upper,lower

    # متد نمایش تجزیه ال یو
    def print_LU(self,upper,lower):
        mat = self.matrix
        row = len(mat)
        # upper,lower = self.solve()
        
        print(f"Lower matrix is {lower}")
        print("============================================")
        print(f"Upper matrix is {upper}")
        print("============================================")    
    
        for i in range(row):
            # Lower
            for j in range(row):
                print(lower[i][j], end="\t")
            print("", end="\t")
            # Upper
            for j in range(row):
                print(upper[i][j], end="\t")
            print("")

class check_answer:
    def __init__(self,L,U):
        self.L = L
        self.U = U

    def zero_matrix(self,row,col):
        li = []
        for r in range(row):
            li.append([])
            for c in range(col):
                li[-1].append(0)
        return li
        
    def check(self,FirstMatrix):
        row = len(self.L)
        col = len(self.L[0])
        result = self.zero_matrix(row,col)
        B = self.U
        A = self.L
        for i in range(len(A)):
            # iterating by column by B
            for j in range(len(B[0])):
                # iterating by rows of B
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        
        print(f"result is : {result} ") 
        print(f"your first matrix is : {FirstMatrix} ")

        if(result == FirstMatrix):
            print("The calculations are correct")
        else:
            print("The calculations are not correct !!!")


# Tests
# matrix = [
#     [1,3,4],
#     [2,2,6],
#     [3,1,5]
# ]

# matrix = [
#     [1,1,2],
#     [2,3,1],
#     [3,-1,-1]
# ]


# app = LU(matrix)
# app.print_LU()
# # ..................
# L,U = app.solve()
# check = check_answer(L,U,matrix)
# check.check()

