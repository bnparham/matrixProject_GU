import copy
from CreateMatrix import *
from LU import *
from Determinant import *
from Determinantl_R_C import *
from Goas import *
from LU_goas_Jordan import *

print("===|Welcome To our Program|=== ")
print("\n----- Create Ax=b -----\n")
app = Matrix()
# create A,b and Matrix
mat_A , mat_b , mat_total = app.Create_Matrix()

mat_A_copy = copy.deepcopy(mat_A)
mat_A_copy2 = copy.deepcopy(mat_A)
mat_total_copy = copy.deepcopy(mat_total)

# create LU
lu = LU(mat_A)
mat_U,mat_L = lu.solve()

# determinant
deteminant = Determinant(mat_A)
det_answ = deteminant.determinantOfMatrix()


print(""" 
======Menu======
1) Print input matrix
2) Print and calculate LU of input matrix
3) Calculate equation with LU Method
4) Calculate Determinant with LU method
5) Calculate Ineverse of Matirs with LU method
6) Calculate Determinant By specifying the desired row or column number
7) Calculate equation with Goas Jordan method
8) Calculate LU with Goas Jordan method

      """)

menu = True
while(menu):    
    vorodi = int(input("\n\n Your Input : "))
    if vorodi == 1:
        print(f"your matrix is {mat_total}")
        print("Ax = b")
        print(f"A : {mat_A_copy}")
        print(f"b : {mat_b}")
        print("--------------------------")
        print(f"{mat_A_copy}x = {mat_b} ")
        
    if vorodi == 2:
        lu.print_LU(mat_U,mat_L)
        check = check_answer(mat_L,mat_U)
        check.check(mat_A_copy)

    if vorodi == 3:
        y_answers = []
        x_answers = []
        for i in range(len(mat_L)):
            y_answers.append([mat_L[i],mat_b[i]])
        keys_y = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
        for j in range(len(y_answers)):
            if j == 0:
                try:
                    keys_y["a"] = y_answers[0][1]/y_answers[0][0][0]
                except:
                    keys_y["a"] = y_answers[0][1]
            if j == 1:
                try:
                    keys_y["b"] = (y_answers[1][1] - (keys_y["a"]*y_answers[1][0][0]))/y_answers[1][0][1]
                except:
                    keys_y["b"] = (y_answers[1][1] - (keys_y["a"]*y_answers[1][0][0]))
            if j == 2:
                try:
                    keys_y["c"] = (y_answers[2][1] - (keys_y["a"]*y_answers[2][0][0] + keys_y["b"]*y_answers[2][0][1]))/y_answers[2][0][2]
                except:
                    keys_y["c"] = (y_answers[2][1] - (keys_y["a"]*y_answers[2][0][0] + keys_y["b"]*y_answers[2][0][1]))
            if j == 3:
                try:
                    keys_y["d"] = (y_answers[3][1] - (keys_y["a"]*y_answers[3][0][0] + keys_y["b"]*y_answers[3][0][1]+ keys_y["c"]*y_answers[3][0][2] ))/y_answers[3][0][3]
                except:
                    keys_y["d"] = (y_answers[3][1] - (keys_y["a"]*y_answers[3][0][0] + keys_y["b"]*y_answers[3][0][1]+ keys_y["c"]*y_answers[3][0][2] ))
            if j == 4:
                try:
                    keys_y["e"] = (y_answers[4][1] - (keys_y["a"]*y_answers[4][0][0] + keys_y["b"]*y_answers[4][0][1]+ keys_y["c"]*y_answers[4][0][2] + keys_y["d"]*y_answers[4][0][3] ))/y_answers[4][0][4]
                except:
                    keys_y["e"] = (y_answers[4][1] - (keys_y["a"]*y_answers[4][0][0] + keys_y["b"]*y_answers[4][0][1]+ keys_y["c"]*y_answers[4][0][2] + keys_y["d"]*y_answers[4][0][3] ))
            if j == 5:
                try:
                    keys_y["f"] = (y_answers[5][1] - (keys_y["a"]*y_answers[5][0][0] + keys_y["b"]*y_answers[5][0][1] + keys_y["c"]*y_answers[5][0][2] + keys_y["d"]*y_answers[5][0][3] + keys_y["e"]*y_answers[5][0][4] ))/y_answers[5][0][5]
                except:
                    keys_y["f"] = (y_answers[5][1] - (keys_y["a"]*y_answers[5][0][0] + keys_y["b"]*y_answers[5][0][1] + keys_y["c"]*y_answers[5][0][2] + keys_y["d"]*y_answers[5][0][3] + keys_y["e"]*y_answers[5][0][4] ))
            
        print(f"Ly=b Equation =>  {y_answers}")
        print(f"y_answers => {keys_y} ")
        mat_y = [i for i in keys_y.values()]
        
        
        keys_x = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
        
        for i in range(len(mat_U)):
            x_answers.append([list(reversed(mat_U[i])),mat_y[i]])
        
        x_answers = list(reversed(x_answers))
        
        for j in range(len(x_answers)):
            if j == 0:
                try:
                    keys_x["a"] = x_answers[0][1]/x_answers[0][0][0]
                except:
                    keys_x["a"] = x_answers[0][1]
            if j == 1:
                try:
                    keys_x["b"] = (x_answers[1][1] - (keys_x["a"]*x_answers[1][0][0]) )/x_answers[1][0][1]
                except:
                    keys_x["b"] = (x_answers[1][1] - (keys_x["a"]*x_answers[1][0][0]) )
            if j == 2:
                try:
                    keys_x["c"] = (x_answers[2][1] - (keys_x["a"]*x_answers[2][0][0] + keys_x["b"]*x_answers[2][0][1]))/x_answers[2][0][2]
                except:
                    keys_x["c"] = (x_answers[2][1] - (keys_x["a"]*x_answers[2][0][0] + keys_x["b"]*x_answers[2][0][1]))
            if j == 3:
                try:
                    keys_x["d"] = (x_answers[3][1] - (keys_x["a"]*x_answers[3][0][0] + keys_x["b"]*x_answers[3][0][1] + keys_x["c"]*x_answers[3][0][2] ) )/x_answers[3][0][3]
                except:
                    keys_x["d"] = (x_answers[3][1] - (keys_x["a"]*x_answers[3][0][0] + keys_x["b"]*x_answers[3][0][1] + keys_x["c"]*x_answers[3][0][2] ) )
            if j == 4:
                try:
                    keys_x["e"] = (x_answers[4][1] - (keys_x["a"]*x_answers[4][0][0] + keys_x["b"]*x_answers[4][0][1] + keys_x["c"]*x_answers[4][0][2] + keys_x["d"]*x_answers[4][0][3] ))/x_answers[4][0][4]
                except:
                    keys_x["e"] = (x_answers[4][1] - (keys_x["a"]*x_answers[4][0][0] + keys_x["b"]*x_answers[4][0][1] + keys_x["c"]*x_answers[4][0][2] + keys_x["d"]*x_answers[4][0][3] ))
            if j == 5:
                try:
                    keys_x["f"] = (x_answers[5][1] - (keys_x["a"]*x_answers[5][0][0] + keys_x["b"]*x_answers[5][0][1] + keys_x["c"]*x_answers[5][0][2] + keys_x["d"]*x_answers[5][0][3] + keys_x["e"]*x_answers[5][0][4] ))/x_answers[5][0][5]
                except:
                    keys_x["f"] = (x_answers[5][1] - (keys_x["a"]*x_answers[5][0][0] + keys_x["b"]*x_answers[5][0][1] + keys_x["c"]*x_answers[5][0][2] + keys_x["d"]*x_answers[5][0][3] + keys_x["e"]*x_answers[5][0][4] ))
        
        print(f"Ux=y Equation =>  {x_answers}")
        
        mat_x = list(reversed([i for i in keys_x.values() if i != 0]))
        if(len(mat_x) < len(x_answers)):
            diff = len(x_answers) - len(mat_x)
            for i in range(diff):
                mat_x.append(0)
                
        print("Answers : ")
        index = 0
        for i in mat_x:
            print(f"x[{index}] = {mat_x[index]}")
            index += 1
        print("==========================")
        print("Round Answers : ")
        index = 0
        for i in mat_x:
            print(f"x[{index}] = {round(mat_x[index])}")
            index += 1
    
    if vorodi == 4:
        print(f"Determinant of the matrix is : {det_answ}")

    if vorodi == 5:
        row_len = len(mat_A)
        identity_matrix = app.identity_matrix(row_len,row_len)
        
        # قرار دادن ماتریس های پایین مثلثی متناظر با هر سطر از ماتریس همانی
        d_answers_container = []
        for i in range(len(mat_L)):
            d_answers_container.append([mat_L,identity_matrix[i]])

        li_total = []
        for j in range(len(d_answers_container)):
            eq = d_answers_container[j]
            li = []
            # قرار دادن هر سطر ماتریس پایین مثلثی متناظر با هر درایه سطر متناظر از ماتریس همانی
            for i in range(len(eq[0])):
                li.append([eq[0][i],eq[1][i]])
            li_total.append(li.copy())
        
        d_keys = {
            0 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            1 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            2 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            3 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            4 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            5 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
        }
        
        index = 0
        for li in li_total:
            for j in range(len(li)):
                if j == 0:
                    try:
                        d_keys[index]["a"] = li[0][1]/li[0][0][0]
                    except:
                        d_keys[index]["a"] = li[0][1]
                if j == 1:
                    try:
                        d_keys[index]["b"] = (li[1][1] - (d_keys[index]["a"]*li[1][0][0]) )/li[1][0][1]
                    except:
                        d_keys[index]["b"] = (li[1][1] - (d_keys[index]["a"]*li[1][0][0]))
                if j == 2:
                    try:
                        d_keys[index]["c"] = (li[2][1] - (d_keys[index]["a"]*li[2][0][0] + d_keys[index]["b"]*li[2][0][1]))/li[2][0][2]
                    except:
                        d_keys[index]["c"] = (li[2][1] - (d_keys[index]["a"]*li[2][0][0] + d_keys[index]["b"]*li[2][0][1]))
                if j == 3:
                    try:
                        d_keys[index]["d"] = (li[3][1] - (d_keys[index]["a"]*li[3][0][0] + d_keys[index]["b"]*li[3][0][1] + d_keys[index]["c"]*li[3][0][2] ) )/li[3][0][3]
                    except:
                        d_keys[index]["d"] = (li[3][1] - (d_keys[index]["a"]*li[3][0][0] + d_keys[index]["b"]*li[3][0][1] + d_keys[index]["c"]*li[3][0][2] ))
                if j == 4:
                    try:
                        d_keys[index]["e"] = (li[4][1] - (d_keys[index]["a"]*li[4][0][0] + d_keys[index]["b"]*li[4][0][1] + d_keys[index]["c"]*li[4][0][2] + d_keys[index]["d"]*li[4][0][3] ))/li[4][0][4]
                    except:
                        d_keys[index]["e"] = (li[4][1] - (d_keys[index]["a"]*li[4][0][0] + d_keys[index]["b"]*li[4][0][1] + d_keys[index]["c"]*li[4][0][2] + d_keys[index]["d"]*li[4][0][3] ))
                if j == 5:
                    try:
                        d_keys[index]["f"] = (li[5][1] - (d_keys[index]["a"]*li[5][0][0] + d_keys[index]["b"]*li[5][0][1] + d_keys[index]["c"]*li[5][0][2] + d_keys[index]["d"]*li[5][0][3] + d_keys[index]["e"]*li[5][0][4] ))/li[5][0][5]
                    except:
                        d_keys[index]["f"] = (li[5][1] - (d_keys[index]["a"]*li[5][0][0] + d_keys[index]["b"]*li[5][0][1] + d_keys[index]["c"]*li[5][0][2] + d_keys[index]["d"]*li[5][0][3] + d_keys[index]["e"]*li[5][0][4] ))
            index += 1
        
        d_keys_list = []
        for i in range(row_len):
            d_keys_list.append(list(d_keys[i].values())[:row_len])
            

        # قرار دادن ماتریس های بالا مثلثی متناظر با هر سطر عناصر (دی) به دست آمده
        x_answers_container = []
        for i in range(len(mat_U)):
            x_answers_container.append([mat_U,d_keys_list[i]])
            
        li_total_2 = []
        for j in range(len(x_answers_container)):
            eq = x_answers_container[j]
            li = []
            # قرار دادن هر سطر ماتریس بالا مثلثی متناظر با هر درایه سطر متناظر عناصر (دی) به دست آمده
            for i in range(len(eq[0])):
                li.append([list(reversed(eq[0][i])),eq[1][i]])
            li_total_2.append(li.copy())
        

        
        x_keys = {
            0 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            1 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            2 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            3 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            4 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0},
            5 : {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
        }
        
        index = 0
        for li in li_total_2:
            li = list(reversed(li))
            for j in range(len(li)):
                if j == 0:
                    try:
                        x_keys[index]["a"] = li[0][1]/li[0][0][0]
                    except:
                        x_keys[index]["a"] = li[0][1]
                if j == 1:
                    try:
                        x_keys[index]["b"] = (li[1][1] - (x_keys[index]["a"]*li[1][0][0]) )/li[1][0][1]
                    except:
                        x_keys[index]["b"] = (li[1][1] - (x_keys[index]["a"]*li[1][0][0]) )
                if j == 2:
                    try:
                        x_keys[index]["c"] = (li[2][1] - (x_keys[index]["a"]*li[2][0][0] + x_keys[index]["b"]*li[2][0][1]))/li[2][0][2]
                    except:
                      x_keys[index]["c"] = (li[2][1] - (x_keys[index]["a"]*li[2][0][0] + x_keys[index]["b"]*li[2][0][1]))  
                if j == 3:
                    try:
                        x_keys[index]["d"] = (li[3][1] - (x_keys[index]["a"]*li[3][0][0] + x_keys[index]["b"]*li[3][0][1] + x_keys[index]["c"]*li[3][0][2] ) )/li[3][0][3]
                    except:
                        x_keys[index]["d"] = (li[3][1] - (x_keys[index]["a"]*li[3][0][0] + x_keys[index]["b"]*li[3][0][1] + x_keys[index]["c"]*li[3][0][2] ) )
                if j == 4:
                    try:
                        x_keys[index]["e"] = (li[4][1] - (x_keys[index]["a"]*li[4][0][0] + x_keys[index]["b"]*li[4][0][1] + x_keys[index]["c"]*li[4][0][2] + x_keys[index]["d"]*li[4][0][3] ))/li[4][0][4]
                    except:
                        x_keys[index]["e"] = (li[4][1] - (x_keys[index]["a"]*li[4][0][0] + x_keys[index]["b"]*li[4][0][1] + x_keys[index]["c"]*li[4][0][2] + x_keys[index]["d"]*li[4][0][3] ))
                if j == 5:
                    try:
                        x_keys[index]["f"] = (li[5][1] - (x_keys[index]["a"]*li[5][0][0] + x_keys[index]["b"]*li[5][0][1] + x_keys[index]["c"]*li[5][0][2] + x_keys[index]["d"]*li[5][0][3] + x_keys[index]["e"]*li[5][0][4] ))/li[5][0][5]
                    except:
                        x_keys[index]["f"] = (li[5][1] - (x_keys[index]["a"]*li[5][0][0] + x_keys[index]["b"]*li[5][0][1] + x_keys[index]["c"]*li[5][0][2] + x_keys[index]["d"]*li[5][0][3] + x_keys[index]["e"]*li[5][0][4] ))
            index += 1
            
        x_keys_list = []
        for i in range(row_len):
            x_keys_list.append(list(x_keys[i].values())[:row_len])
            
            
        reverse_matrix = []
        index = 0
        for i in range(len(x_keys_list)):
            li = []
            for j in range(len(x_keys_list)):
                li.append(x_keys_list[j][index])
            index += 1
            reverse_matrix.append(li.copy())
        reverse_matrix = list(reversed(reverse_matrix))
        
        print(f"mat_L : {mat_L}")
        print(f"identity_matrix : {identity_matrix}")
        print("\n----Placing the lower triangular matrix equal to the Each row of Identity Matrix ----")
        print(li_total)
        print("\n----find d answers for each Equations----")
        print(f"d keys in Dict format : {d_keys}")
        print(f"d keys in List format : {d_keys_list}")
        
        print("\n----Placing the upper triangular matrix equal to the Each answers of D ----")
        print(li_total_2)
        
        print("\n----find x answers for each Equations----")
        print(f"x keys in Dict format : {x_keys}")
        print(f"x keys in List format : {x_keys_list}")

        print(f"Inverse of matrix in LU method is => {reverse_matrix} ")
        print("\n\n======Inverse Matrix in LU method is======")
        for i in range(row_len):
            # Lower
            for j in range(row_len):
                print(reverse_matrix[i][j], end="\t")
            print("", end="\n")
            
    if vorodi == 6:
        error = True
        while(error):   
            try:
                q = input("Write c/r and number of that | ex: 'c 1' : ")
                if(len(q.split(" ")) == 2):
                    error = False
                else:
                    print("Wrong Value")
                    continue
            except:
                print("Wrong Value")
                continue
        a = Det_R_C()
        matrix__2 = a.changeMatrix_by_input(q.split(" "),mat_A_copy2)
        row__2 = matrix__2[0]
        print("Deteminant is : ")        
        print(a.solve(row=row__2,matrix=matrix__2))
        
    if vorodi == 7:
        matrix__3 = mat_total_copy
        matrix__3 = switch_zarib_1(matrix__3)
        matrix__3 = goas_jorden(matrix__3)
        matrix__3 = normalize_matrix(matrix__3)
        matrix__3 = check_is_eaual(matrix__3)
        matrix__3 = normalize_2(matrix__3)
        matrix__3 = final(matrix__3)
        
        li_total_goas = []
        
        for li in matrix__3:
            li_total_goas.append([li[:-1],li[-1]])    
        
        print(f"after goas jordan : {li_total_goas}")
        
        
        keys_y = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
        for j in range(len(li_total_goas)):
            if j == 0:
                try:
                    keys_y["a"] = li_total_goas[0][1]/li_total_goas[0][0][0]
                except:
                    keys_y["a"] = li_total_goas[0][1]
            if j == 1:
                try:
                    keys_y["b"] = (li_total_goas[1][1] - (keys_y["a"]*li_total_goas[1][0][0]))/li_total_goas[1][0][1]
                except:
                    keys_y["b"] = (li_total_goas[1][1] - (keys_y["a"]*li_total_goas[1][0][0]))
            if j == 2:
                try:
                    keys_y["c"] = (li_total_goas[2][1] - (keys_y["a"]*li_total_goas[2][0][0] + keys_y["b"]*li_total_goas[2][0][1]))/li_total_goas[2][0][2]
                except:
                    keys_y["c"] = (li_total_goas[2][1] - (keys_y["a"]*li_total_goas[2][0][0] + keys_y["b"]*li_total_goas[2][0][1]))
            if j == 3:
                try:
                    keys_y["d"] = (li_total_goas[3][1] - (keys_y["a"]*li_total_goas[3][0][0] + keys_y["b"]*li_total_goas[3][0][1]+ keys_y["c"]*li_total_goas[3][0][2] ))/li_total_goas[3][0][3]
                except:
                    keys_y["d"] = (li_total_goas[3][1] - (keys_y["a"]*li_total_goas[3][0][0] + keys_y["b"]*li_total_goas[3][0][1]+ keys_y["c"]*li_total_goas[3][0][2] ))
            if j == 4:
                try:
                    keys_y["e"] = (li_total_goas[4][1] - (keys_y["a"]*li_total_goas[4][0][0] + keys_y["b"]*li_total_goas[4][0][1]+ keys_y["c"]*li_total_goas[4][0][2] + keys_y["d"]*li_total_goas[4][0][3] ))/li_total_goas[4][0][4]
                except:
                    keys_y["e"] = (li_total_goas[4][1] - (keys_y["a"]*li_total_goas[4][0][0] + keys_y["b"]*li_total_goas[4][0][1]+ keys_y["c"]*li_total_goas[4][0][2] + keys_y["d"]*li_total_goas[4][0][3] ))
            if j == 5:
                try:
                    keys_y["f"] = (li_total_goas[5][1] - (keys_y["a"]*li_total_goas[5][0][0] + keys_y["b"]*li_total_goas[5][0][1] + keys_y["c"]*li_total_goas[5][0][2] + keys_y["d"]*li_total_goas[5][0][3] + keys_y["e"]*li_total_goas[5][0][4] ))/li_total_goas[5][0][5]
                except:
                    keys_y["f"] = (li_total_goas[5][1] - (keys_y["a"]*li_total_goas[5][0][0] + keys_y["b"]*li_total_goas[5][0][1] + keys_y["c"]*li_total_goas[5][0][2] + keys_y["d"]*li_total_goas[5][0][3] + keys_y["e"]*li_total_goas[5][0][4] ))
        
        print(keys_y)
        mat_x = [i for i in keys_y.values() if i != 0]
        if(len(mat_x) < len(li_total_goas)):
            diff = len(li_total_goas) - len(mat_x)
            for i in range(diff):
                mat_x.append(0)
                
        print("Answers : ")
        index = 0
        for i in mat_x:
            print(f"x[{index}] = {mat_x[index]}")
            index += 1
        print("==========================")
        
    if vorodi == 8 :
        lu_goas =  LU_goas()
        print("inverse is :")
        print(lu_goas.inverse(mat_A_copy2))
        if type(lu_goas.inverse(mat_A_copy2)) == list:
            mat = lu_goas.inverse(mat_A_copy2)
            row = len(mat)
            print("=====Inverse in Goas jordan method=====")
            for i in range(row):
                for j in range(row):
                    print(mat[i][j], end="\t")
                print("", end="\n")