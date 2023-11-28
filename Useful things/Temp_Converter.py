while True:

    print('1. Cº a Fº')
    print('2. Fº a Cº')
    print('3. Cº a Kº')
    print('4. Kº a Cº')
    print('5. Exit the program')
    conversion=input('¿Que conversion?')

    try:   
        
        if conversion == ('1'):
            Celcius= input('Temperature?')
            Fahr= (int(Celcius)* 9/5)+32
            print(Fahr)


        if conversion == ('2'):
            Fahr=input('Temperature?')
            Fahr=(float(Fahr)-32)*5/9
            print(Fahr)


        if conversion ==('3'):
            celc= input('Temperature?')
            celc= float(celc)+ 273
            print(celc)


        if conversion ==('4'):
            kelv= input('Temperature')
            kelv= float(kelv)-273
            print(kelv)


        if conversion ==('5'):
            break

    except:
        print('Try another number')
        
            
    continue


    
    




#Negative dont work?
#Finished, but things can change
#Intentar meterle mas cosas(Si no funciona no hay ningun problema)
