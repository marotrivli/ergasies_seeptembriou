def skakiera(kinisi,t):
    kinisi=kinisi.upper()
    ar_N=kinisi.count("N")
    ar_S=kinisi.count("S")
    ar_W=kinisi.count("W")
    ar_E=kinisi.count("E")
    ar=ar_N + ar_S + ar_W + ar_E
    while ar_N>8 or ar_S>8 or ar_W>8 or ar_E>8 or ar >64:#tha elegksoume an einai lanthasmenos o arithmos kinisewn gt mia skakiera einai 8x8
        print "Dwsate lathos kinisi tou pioniou.Parakalw eisagete ksana tin kinisi tou "
        kinisi=raw_input("Dwste tin kinisi tou pioniou:")
        kinisi=kinisi.upper()
        ar_N=kinisi.count("N")
        ar_S=kinisi.count("S")
        ar_W=kinisi.count("W")
        ar_E=kinisi.count("E")
    arithmos_kinisewn=len(kinisi)
    tself=t
    if arithmos_kinisewn<=tself:
        t=True
    else:
        t=False
    return t

#print "Oi kiniseis einai mono oi N,W,E kai S kai den epitrepetai na emfanizetai panw apo 8 i kathe mia"
#sth skakiera de mporoun na uparxoyn parapanw apo 64 kiniseis sunolika logo tvn tetragwnwn kai parapanw apo 8 kiniseis to kathe gramma
#opote to anaferoume
#kinisi=raw_input("Dwste tin kinisi tou pioniou:") #mporoun na xrisimopoihthoun mono ta N,W,E kai S
#t=int(raw_input("Dwste to xrono se lepta,ston opoio thelete na ginoun oi kiniseis: "))

#print skakiera(kinisi,t)
