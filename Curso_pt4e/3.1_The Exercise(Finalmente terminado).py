hours=input('¿Hours?')
print(hours, 'hours')

    
rate=input('¿Rate?')
print(rate,'rate')
try:
    fh=float(hours)
    fr=float(rate)
except:
    print('Error, please enter numeric input')
    quit()

if int(fh)>40:
    bonus= float(fh)-40
    maxhours= float(fh)-float(bonus)
    bonus2=float(bonus)+float(fr)
    CGP = float(maxhours)*float(fr)+float(bonus)*float(bonus2)

else:
    CGP = float(fh)*float(fr)

print('This is the CPG :', CGP)

#Quiero poner que abra el bloc de notras y ponga el resultado(Se vera mas adelante pero en un principio no)#
#Arrastrar a CMD para usar el codigo#
