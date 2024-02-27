x=0
while x==0:

    print('1. Cº a Fº')
    print('2. Fº a Cº')
    print('3. Cº a Kº')
    print('4. Kº a Cº')
    print('5. Exit the program')
    ans= None
    conversion=input('¿Que conversion?')
    
    try:   
        
        if conversion == ('1'):
            Celcius= input('Temperature?')
            Fahr= (float(Celcius)* 9/5)+32
            print(Fahr)
            ans= Fahr

        if conversion == ('2'):
            Fahr=input('Temperature?')
            Fahr=(float(Fahr)-32)*5/9
            print(Fahr)
            ans= Fahr

        if conversion ==('3'):
            celc= input('Temperature?')
            celc= float(celc)+ 273
            print(celc)
            ans= celc

        if conversion ==('4'):
            kelv= input('Temperature')
            kelv= float(kelv)-273
            print(kelv)
            ans= kelv

        if conversion ==('5'):
            print(ans)
            break

        if conversion==('ans'):
            print(ans)

                    
    except:
        print('Try another number')
        
            
    continue

 
    
    

#Hay que hacer que el ans se actualice
#Intentar meterle mas cosas(Si no funciona no hay ningun problema)
#Finished, but things can change



