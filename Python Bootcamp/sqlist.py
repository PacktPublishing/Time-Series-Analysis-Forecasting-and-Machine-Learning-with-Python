#list comprehension

def squares(lst):
    return [i**2 for i in lst]

def even(lst):
    return [i for i in lst if i%2==0 and i>5]


nos=[4,5,6,7,8,9]
sq_list=squares(nos)

print(nos)
print(even(nos))
