# Python program to find Determinant of a matrix
class Determinant:
    def __init__(self, matrix):
        self.matrix = matrix

    def zero_matrix(self,row,col):
        li = []
        for r in range(row):
            li.append([])
            for c in range(col):
                li[-1].append(0)
        return li
    

    def determinantOfMatrix(self):
        mat = self.matrix
        n = len(self.matrix)

        temp = self.zero_matrix(n,n)
        total = 1
        det = 1 # initialize result

        # loop for traversing the diagonal elements
        for i in range(0, n):
            index = i # initialize the index

            # finding the index which has non zero value
            while(index < n and mat[index][i] == 0):
                index += 1

            if(index == n): # if there is non zero element
                # the determinant of matrix as zero
                continue

            if(index != i):
                # loop for swapping the diagonal element row and index row
                for j in range(0, n):
                    mat[index][j], mat[i][j] = mat[i][j], mat[index][j]

                # determinant sign changes when we shift rows
                # go through determinant properties
                det = det*int(pow(-1, index-i))

            # ||LOG||
            # print(mat)
            
            # storing the values of diagonal row elements
            for j in range(0, n):
                temp[j] = mat[i][j]

            # traversing every row below the diagonal element
            for j in range(i+1, n):
                num1 = temp[i]	 # value of diagonal element
                num2 = mat[j][i] # value of next row element

                # traversing every column of row
                # and multiplying to every row
                for k in range(0, n):
                    # multiplying to make the diagonal
                    # element and next row element equal

                    mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])

                total = total * num1 # Det(kA)=kDet(A);

                # || LOG ||
                # print(f"total : {total}")
        
        # multiplying the diagonal elements to get determinant
        for i in range(0, n):
            det = det*mat[i][i]

        return int(det/total) # Det(kA)/k=Det(A);