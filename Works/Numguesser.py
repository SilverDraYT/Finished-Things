import random
while True:
    num=random.randint(1,10)
    #If there is not int() guess is a string and then it doesn't work   
    guess=int(input('Elige un numero del 1 al 10:'))
   
     #A lot of code stopped by a simple or, i love that      
    if guess < 1 or guess > 10:
        print('Pick a number between 1 and 10')
    else:
        if guess==num:
            print('Well done')
            break
        else:
            #I make it write the answer?
            print('Try again')
           

print('The end')
    
    
    
#The enter gives error, fix that
