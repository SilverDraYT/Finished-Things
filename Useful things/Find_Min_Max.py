largest=0
smallest=None
while True:
    lel=input('Number only:')
    if lel=='done':
        break
    try:
        if float(lel)>=float(largest):
            largest=lel
        if str(smallest) >=str(lel):
                 smallest=lel
    except:
        print('wrong input')
        continue

print('The largest number is',largest)
print('The smallest number is', smallest)
input('Press enter to exit program')

# :)
