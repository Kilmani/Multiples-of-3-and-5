N=1000
i=0
summary=0
while i < 1000:
    if (i%3 == 0) & (i/3 != 0):
        summary = summary + i
        print(i)

    if (i%5 == 0) & (i/5 != 0):
        summary = summary + i
        print(i)
    i=i+1
    
print(summary)