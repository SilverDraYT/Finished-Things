num=0
tot=0.0
while True:
   lel=input('Number?(Remember Write done when finish)')
   if lel=='done':
       break
   try:
       change=float(lel)
   except:
      print('wrong input')
      continue
   num=num+1
   tot=tot+change
 

print('All done!')
print(num, tot, tot/num)
