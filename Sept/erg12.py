
def math(a,b,c):
    tax=[a,b,c] #ftiaxnw th lista gia na tin taksinomisw kai na bgazei apotelesma gia opoia seiraa arithmwn kai na balw
    for i in range(3):
        for j in range(2,i,-1):
            if tax[j-1]>tax[j]:
                k=tax[j-1]
                tax[j-1]=tax[j]
                tax[j]=k
    a=tax[0]
    b=tax[1]
    c=tax[2]

    if a+b<c:
        return -1
    elif a**2+b**2>c**2:
         return 1
    elif a**2+b**2<c**2:
        return 2
    else :
        return 3

#a=int(raw_input("Dwste ton prwto arithmo: "))
#b=int(raw_input("Dwste ton deutero arithmo: "))
#c=int(raw_input("Dwste ton trito arithmo: "))

#print math(a,b,c)
