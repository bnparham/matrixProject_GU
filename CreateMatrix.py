class Matrix:
    def __init__(self):
        self.matrix = None
        
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
    
    def create_A(self):
        # ----- Get ROW & COl Input From User
        Error_input = True
        while(Error_input):
            try:
                row_input = int(input("Enter size of Row : "))
                col_input = int(input("Enter size of Col : "))
                Error_input = False
            except:
                print("=== Invalid Input! - Try Again! ===")
                continue
            
        # ----- Create Matrix numbers
        matrix = self.zero_matrix(row_input,col_input)
        for r in range(row_input):
            for c in range(col_input):
                Error_select = True
                while(Error_select):
                    try:
                        q = float(input(f"Enter number of matrix[{r}][{c}] : "))
                        Error_select = False
                    except:
                        print(f"=== Invalid Input for matrix [{r}][{c}]! - Try Again! ===")
                        continue
                    
                matrix[r][c] = q  
                
        return matrix
    
    def Create_b(self):
        matrix = self.create_A()
        row_len = len(matrix)
        print("\n\n Ax=b \nYou have created 'A' side of This equation")
        print("Now Enter 'b' side of this equation")
        for i in range(row_len):
            Error =True
            while(Error):
                try:
                    q = float(input(f"Enter b{i} for row[{i}] : "))
                    Error = False
                except:
                    print(f"=== Invalid Input for b{i} in row[{i}]! - Try Again! ===")
                    continue
            matrix[i].append(q)
        return matrix

    def Create_Matrix(self):
        mat = self.Create_b()
        A = []
        b= []
        
        for r in mat:
            A.append(r[:-1])
        
        for r in mat:
            b.extend([r[-1]])
            
        return A,b,mat 