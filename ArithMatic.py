
def Add(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def Sub(No1,No2):
    Ans=0
    Ans=No1-No2
    return Ans

def Mult(No1,No2):
    Ans=0
    Ans=No1*No2
    return Ans

 
def div1(No1,No2):
    return No1/No2

def ChkPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True