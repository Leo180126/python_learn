def split_number(num):
    numbers = []
    while(num > 0):
        numbers.append(num % 10)
        num = int(num/10)
    return numbers
print(split_number(2141354))


def isPalindrome(num):
    nums = split_number(num)
    for i in range(len(nums)):
        if nums[i] != nums[len(nums) - i - 1]:
            return False
    return True
print(isPalindrome(12211))


def reverse_number(num):
    nums = split_number(num)
    result = 0
    base = 10**(len(nums) - 1)
    for i in range(len(nums)):
        result += nums[i]*base
        base /= 10
    return int(result)
print(reverse_number(1234))

def foo(a):
    _sum = a
    while(isPalindrome(_sum) == False):
        _sum += reverse_number(_sum)
    return _sum
print(foo(1234))