N=1000
i=0
summary=0
while i < 1000:
    if (i%3 == 0) | (i%5 == 0):
        summary+=i
        print(i)
    i+=1
    
print(summary)