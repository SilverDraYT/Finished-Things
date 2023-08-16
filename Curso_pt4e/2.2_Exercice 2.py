nam=input('¿Hours?')
print(nam, 'hours')
print(type(nam)) #Comprobar que tipo es el dato

bam=input('How much?')
print('Is',bam)
print(type(bam)) #Comprobar que tipo es el dato
try:
    pay=(nam)*(bam)
    print(pay)
except:
    print('No pay')
