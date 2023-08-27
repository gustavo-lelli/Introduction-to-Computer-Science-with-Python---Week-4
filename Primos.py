def eh_primo(x):
    i=x-1
    pri=0

    while(i>1):
        if(x%i==0):
            pri+=1
        i-=1
    
    return pri

def maior_primo(x):
    while(x>1):
        if(eh_primo(x)==0):
            return x
        x-=1

