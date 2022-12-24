lst=[1,4,5,7,8,3,2,0]

def chop(lst):
    lst.pop(0)
    lst.pop(-1)

def middle(lst):
    return lst[1:-1]

print("chop: ", chop(lst))
print("middle: ", middle(lst))