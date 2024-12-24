def division(a,b):
    try:
        c=a/b
        print("Result = ",c)
    except:
        if b==0:
            print("Error: division by zero")


division(2,3)
division(2,0)