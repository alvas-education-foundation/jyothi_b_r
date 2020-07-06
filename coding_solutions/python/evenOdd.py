list=[2, 7, 5, 64, 14]
even=0
odd=0

for n in list:
    if n%2==0:
        even+=1
    else:
        odd+=1

print('even num:',even)
print('odd num:',odd)
