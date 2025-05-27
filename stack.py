string = input()
stack = []
for i in range(len(string)):
    if len(stack) == 0:
        stack.append(string[i])
        continue
    if string[i] == ']' and stack[len(stack) - 1] == '[' or \
        string[i] == ')' and stack[len(stack) - 1] == '(' or \
        string[i] == '}' and stack[len(stack) - 1] == '{' :
        stack.pop()
    else:
        stack.append(string[i])
if len(stack) == 0:
    print("True")
else:
    print("False")
# OUTPUT
'''
(){}[]
True
(({}
False
()
True
((((}}}}
False
(({}{})){}}
False
'''