c=int(input("Current year: "))
f=int(input("final year: "))
for i in range(c,f+1):
    if(i%4)==0 and (i%100)!=0 or (i%400)==0:
        print(i)
        i=i+1