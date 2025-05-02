def is_nt(a):
    if a <= 1:
        return False
    for i in range(2, int(a**(1/2) + 1)):
        if a % i == 0:
            return False
    return True
#_____
print(is_nt(7))
print(is_nt(9))
#_____
def is_different(a):   
    s = set()
    for i in range(len(a)):
        if a[i] in s:
            return False
        else:
            s.add(a[i])
    return True
#_____
print(is_different([1, 5, 7, 9]))
print(is_different([2, 4, 5, 5, 7, 9]))
#_____
#OUTPUT
# True
# False
# True
# False