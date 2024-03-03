import random
while True:
    num=random.randint(1,10)
    #If there is not int() guess is a string and then it doesn't work   
    try: 
        while True:
            guess=int(input('Elige un numero del 1 al 10:'))
   
     #A lot of code without writting because of a simple 'or', i love that      
            if guess < 1 or guess > 10:
                print('Pick a number between 1 and 10')
            else:
                if guess==num:
                    print('Well done')
                    break
                else:
                    if guess < num:
                        print('Too low')
                    else:
                        print('Too high')    
            
                    print('Try again')
    except:
        print('Pick a number please')       
    
    print('The end')
    break


    
    
    
#The enter gives error, fix that(Fixed)
