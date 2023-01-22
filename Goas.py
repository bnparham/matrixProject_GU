# یافتن ضریب یک و جابه جایی آن
def switch_zarib_1(matrix): 
    # سطر های ماتریس
    row = 0
    # درایه های ماتریس
    index = 0
    # تعداد تمام سطر های ماتریس
    total_row = len(matrix)
    # درایه فعلی انتخاب شده
    select = matrix[row][index]
    # بولین جهت یافتن و جابه جایی سطر اول با سطری با اولین درایه یک
    flag = False
    # تا زمانی که اولین درایه درایه فعلی انتخاب شده ( اولین درایه از سطر) یک نشده است ، عملیات را تکرار کن
    while(select != 1):
        row = row + 1
        # تعداد سطرهای اضافی نباید از تعداد سطر ماتریس بیشتر شود
        if(row < total_row):
            # انتخاب اولین درایه از سطر بعدی به امید یافتن ضریب یک
            select = matrix[row][index]
            # سطر بعدی ، اولین درایه اش ضریب یک دارد
            if(select == 1):
                # شماره سطری که  اولین درایه آن یک است به فلگ نسبت داده شود
                flag = row 
            # سطر فعلی اولین درایه آن عددی غیر از یک است بنابراین عملیات باید تکرار شود
            else:
                continue
        # اگر تعداد سطرهایی که اضافه شده است از تعداد کل سطر های ماتریس داده شده بیشتر است یعنی هیچ سطری یافت نشده که درایه اول آن یک باشد. بنابراین عملیات باید متوقف شود
        else:
            flag = False
            break
    # اگر متغیر فلگ شماره سطر در خود ذخیره کرده است یعنی سطر دیگری در اولین درایه اش درایه یک دارد و باید با سطر اول ماتریس داده شود جا به جا شود
    if(flag):
        matrix[0],matrix[flag] = matrix[flag],matrix[0]
    # حلقه وایل فعال نشده است
    else:
        # اگر درایه اول سطر اول غیر از یک بود ، تمام اعداد حاظر در سطر اول باید تقسیم بر اولین درایه شود تا ضریب یک به دست آید  
        if(matrix[0][0] != 1):
            new_row = [n / matrix[0][index] for n in matrix[0]]
            matrix[0] = new_row

    return(matrix)
        
# تابع برای جمع دو سطر یک ماتریس
def tafrigh(li1,li2):
    index = len(li1)
    li3 = []
    for i in range(index):
        li3.append(li1[i] + li2[i])
    return li3      

        
def goas_jorden(matrix):
    # ساخت یک کپی از ماتریس فعلی
    # سطر های ماتریس
    row = 0
    # درایه های ماتریس
    index = 0
    # تعداد تمام سطر های ماتریس
    total_row = len(matrix)
    
    # پیمایش در تمام سطر های ماتریس داده شده
    for r in range(total_row):
        # درایه فعلی انتخاب شده
        select = matrix[r][index]
        # پیمایش در سطر های هایی که غیر از سطر فعلی هستند
        # (یعنی ممکن است سطر های قبلی یا بعدی باشند)
        # print("=========================================")
        for j in range(total_row):
            if j != row:
                # print(f"other matrix is {matrix[j]}")
                # درایه مورد نظر را انتخاب کن - درایه متا
                meta = matrix[j][index]
                if(meta == 0):
                    continue
                # ضریب  درایه سطر انتخاب شده را تقسیم بر ضریب درایه سطر فعلی میکنیم
                try:
                    find = meta / select 
                except:
                    find = 1
                if((meta < 0 and select < 0 ) or (meta > 0 and select > 0)):
                    find *= -1
                else:
                    find *= -1
                # print(f"meta : {meta} | select : {select} | find : {find}")
                #  حالا این ضریب پیدا شده را در تمام عناصر سطر فعلی ضرب میکینم
                new_current_row = [n * find for n in matrix[row]]
                # اکنون زمان آن رسیده تا این سطر جدید به دست آمده را از سری جی ام کم کنیم تا ضریب ایندکس ام آن صفر شود
                # سپس سطر جی ام جدید را به دست می آوریم و جایگزین سطر فعلی ماتریس داده شده میکینم
                li = tafrigh(matrix[j],new_current_row)
                matrix[j] = li
        # print(matrix)
        # index += 1
        # row += 1
        
    return matrix
      

# تابعی برای برسی اینکه اعداد داخل لیست همگی به عدد خاصی بخش پذیر هستند یا خیر
def findCanDevideSmaller(n,list):
    for i in range(0 , len(list)):
        if(list[i] % n != 0):
            return False
    return [i // abs(n) for i in list]      

# نرمالایز کردن ماتریس خروجی بعد از عملیات گاوس جردن
# به وسیله تابع برسی بخش پذیری
def normalize_matrix(matrix):
    row_index = 0
    # به ازای تمام سطر های موجود در ماتریس عملیات باید تکرار شود
    for row in matrix:
        # بازه عددی از بین اعداد موجود در خود سطر فعلی انتخاب میشوند
        rng = [x for x in row]
        # اگر صفر در بازه وجود داشت حذف شود چون تاثیری در کوچک کردن اعداد نخواهد داشت
        while(0 in rng) : rng.remove(0)
        # اعداد از بزرگ به کوچک مرتب میشوند
        rng.sort(reverse=True)
        # به ازای اعداد موجود در بازه عملیات را تکرار کن
        for i in rng:
            if(findCanDevideSmaller(i,row)):
                matrix[row_index] = findCanDevideSmaller(i,row)
        row_index += 1
    return matrix


# تابعی برای برسی اینکه دو سطر مشابه هم هستند یا خیر. در این صورت سطر مشابه صفر میشود
def check_is_eaual(matrix):
    total_len = len(matrix)
    for i in range(total_len):
        if(i+1 in range(total_len)):
            if(matrix[i] == matrix[i+1]):
                matrix[i + 1] = [0 for n in matrix[i+1]]
    return matrix

# درایه های سطری اگر یک بودند حتما به صورت قدرمطلق نوشته شده باشند
def normalize_2(matrix):
    ii = 0
    for r in range(len(matrix)):
        if(matrix[r][ii] == 1):
            ii += 1
            continue
        elif(matrix[r][ii] == -1):
            new_mat = [-i for i in matrix[r]]
            matrix[r] = new_mat
            ii += 1
    return matrix       

# وظیفه این تابع ادامه دادن عملیات گاوس جردن است تا ماتریس به صورت فرم سطری پلکانی ایجاد شود
def final(matrix):
    total_len = len(matrix)
    row = 0
    index = 0
    # عملیات باید به اندازه تعداد سطر های ماتریس داده شده انجام شود
    for r in range(total_len):
        select = matrix[r][index]
        if(select != 0):
            for j in range(total_len):
                if r != j:
                    # این خط کد عملا در صورت شرط بالا کار تکراری برسی میکند
                    if(matrix[j][index] == 0):
                        continue
                    else:
                        # درایه مورد نظر را انتخاب کن - درایه متا
                        meta = matrix[j][index]
                        if(meta == 0):
                            continue
                        # ضریب  درایه سطر انتخاب شده را تقسیم بر ضریب درایه سطر فعلی میکنیم
                        try:
                            find = meta / select 
                        except:
                            find = 1
                        if((meta < 0 and select < 0 ) or (meta > 0 and select > 0)):
                            find *= -1
                        else:
                            find *= -1
                        # print(f"meta : {meta} | select : {select} | find : {find}")
                        #  حالا این ضریب پیدا شده را در تمام عناصر سطر فعلی ضرب میکینم
                        new_current_row = [n * find for n in matrix[row]]
                        # اکنون زمان آن رسیده تا این سطر جدید به دست آمده را از سری جی ام کم کنیم تا ضریب ایندکس ام آن صفر شود
                        # سپس سطر جی ام جدید را به دست می آوریم و جایگزین سطر فعلی ماتریس داده شده میکینم
                        li = tafrigh(matrix[j],new_current_row)
                        matrix[j] = li
                else:
                    continue
            index += 1
            row += 1
                    
    return matrix


# Tests

# matrix = [
#     [1,1,0,0,-1],
#     [0,1,2,1,3],
#     [1,0,-1,1,1]
# ]

# matrix = [
#     [6,8,6,3,-3],
#     [6,-8,6,-3,3],
#     [0,8,0,-6,6]
# ]

# matrix = [
#     [1,0,-1,0,-2],
#     [0,1,3,0,-1],
#     [2,0,-2,1,-3]
# ]

# matrix = [
#     [1,2,3],
#     [5,6,7],
#     [9,10,11]
# ]

# matrix = [
#     [1,1,1],
#     [0,-1,0],
#     [-1,1,-1]
# ]

# matrix = [
#     [1,1],
#     [9,-9]
# ]

# matrix = [
#     [3,-0.1,-0.2,7.85],
#     [0.1,7,-0.3,-19.3],
#     [0.3,-0.2,10,71.4]
# ]

# matrix = switch_zarib_1(matrix)
# matrix = goas_jorden(matrix)
# matrix = normalize_matrix(matrix)
# matrix = check_is_eaual(matrix)
# matrix = normalize_2(matrix)
# matrix = final(matrix)
# print(matrix)