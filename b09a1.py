#Issam Charaf, Ferdinand Martin Ottliczky, Svenja Bulle

def string_funk(s1:str , s2:str):
    assert len(s1) >= 3
    assert len(s1)/2 == len(s2) 
    assert s1[:3:] == s2[:3:] 
    konkatenation = s1+s2
    return konkatenation


def nutzer_aufruf():
    s1 = str(input('Gebe eine String ein: '))
    s2 = str(input('Gebe eine String ein: '))
    try: 
        ergebnis = string_funk(s1,s2)
    except AssertionError:
        return 'Eingabe nicht zulässig'
    
    return ergebnis

print(nutzer_aufruf())