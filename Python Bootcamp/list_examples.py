
def square(lst):
    sq=[]
    for i in lst:
        sq.append(i**2)
        
    return sq




lst1=[1,2,3,12,13,4,19,5,6,15,7,8]

sqlist=square(lst1)

print("The original list is",lst1)

print('The square of each of the elements in the og list is',sqlist)
