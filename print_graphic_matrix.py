def print_graphic_matrix(matrix):
        row = len(matrix)   
        for i in range(row):
            # Lower
            for j in range(row):
                print(matrix[i][j], end="\t")
            print("", end="\n")

# def matrix_reformat(mat1,mat2):
#     for i in range(len(mat1)):   
#         row1 = [f"{0:+8.4f}" for i in mat1]
#         row2 = [f"{0:+8.4f}" for i in mat2]
#         print(row1,"\t",row2)

def matrix_reformat(mat1,mat2):
    mat = mat1
    row = len(mat)
  

    for i in range(row):
        # Lower
        for j in range(row):
            print(mat1[i][j], end="\t")
        print("", end="\t")
        # Upper
        for j in range(row):
            print(mat2[i][j], end="\t")
        print("")

def transpose(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]