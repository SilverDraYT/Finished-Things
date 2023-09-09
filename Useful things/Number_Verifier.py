while True:
    number= input("Numero")
    try:
        if float(number)**2 >= 5000:
            print("True")
        else:
            print("False")
    except:
        if number=="done":
            break
        else:
            print("Try again")
    
    continue
print("done")
#Didn`t expect this to work
    
