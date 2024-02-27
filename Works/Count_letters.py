word= input('Your word:')
letra=input('Letra que contar:')
count=0
for letter in word:
    if letter == letra: #input('Letra que contar :'): (Te obliga a pasar por cada letra pero puede que eso se pueda aprovechar de alguna manera)
        count= count + 1
print(count)
input('Press enter to exit the program')

#Solo tenia que darle un valor a la letra desde fuera de el codigo
