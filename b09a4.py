#Issam Charaf, Ferdinand Martin Ottliczky, Svenja Bulle

def print_combo(wort):
    count=0
    
    while wort[0]==" " or wort[-1]==" ":
        if wort[0]==" ":
            wort=wort[1:]
            print("Schneidet Leerzeichen Vorne")
        elif wort[-1]==" ":   
            wort=wort[:-1]
            print("Schneidet Leerzeichen hinten")
    while wort!="":
        for j in range(1,len(wort)):
            count+=1
            
            print(wort[0]+wort[j])
            print("For wurde " , count , "mal betretten")
        wort=wort[1:]
        print("for wurde nicht betretten")

ein=input("Bitte Eingabe tätigen: ")  
print_combo(ein)