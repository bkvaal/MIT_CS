##Problem set 2
##Diophantine equation
##Problem 1

Solutions = []

#build list of all valid solutions

for a in range(0,9):
     for b in range(0,5):
         for c in range(0,3):
             sum = a*7 + b*8 + c*13
             Solutions.append([sum, a, b, c])
Solutions.sort(reverse = True)

bottom = 50
for s in Solutions:
    if s[0] <  bottom:
        if bottom - s[0] <= 1:
            bottom = s[0]
        else:
            missing = bottom-1    
            break
         
print "Largest missing number under 50 is ", missing
    

