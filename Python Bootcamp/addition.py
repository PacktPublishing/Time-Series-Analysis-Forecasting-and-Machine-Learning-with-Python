#Argument packing

def add(*nos):
    #print(type(nos))
    #print(nos)
    #return a+b
    s=0
    for n in nos:
        s+=n
    return s
