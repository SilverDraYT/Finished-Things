word= input('Your word:')
letra=input('Letra que contar:')
count=0
for letter in word:
    if letter == letra: #input('Letra que contar :'): (Te obliga a pasar por cada letra pero puede que eso se pueda aprovechar de alguna manera)
        count= count + 1
print(count)
quant=len(word)
index=quant
while index > 0:
    letter= word[index-1]
    print(letter)
    index= index-1
    if index== 0:
        break

print('The End')
input('Press enter to exit the program')

#¿2023? Solo tenia que darle un valor a la letra desde fuera de el codigo
#3/3/2024 Fusion bien hecha pero mejorable(los dos a la vez?)
