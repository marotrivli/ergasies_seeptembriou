alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

protasi=raw_input("Eisagete tin protasi: ")
protasi1=list(protasi)
print protasi1
grammata=len(protasi)
num=0
for i in protasi:
    count=0

    for j in alpha:
        if i==j:
            num=num+1
            #print "brethike"
            break
        else:
            count=count+1
            #print "den brethike"
        if count==52:
            x=protasi.find(i)

            print protasi[0] ,  x-2 , protasi[x-1] , i ,protasi[x+1] , grammata-x-3 , protasi[grammata-1]

    if num==grammata:
        print protasi[0] ,  grammata-2 , protasi[grammata-1]
