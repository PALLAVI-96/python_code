try:
    a=int(input("enter 1 num :"))
    b=int(input("enter 2 num :"))
    c=a+b
    d=a*b
    e=a/b
    
except NameError:
    print("user not defined variable")
except TypeError:
    print("please provide datatypes similar")
except ZeroDivisionError:
    print("enter a value greater than 0")
except Exception as ex:
    print(ex)
else:
    print(c)
    print(d)
    print(e)
finally:
    print("The execution is done")