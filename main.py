from operator import eq
from sympy import *
equation = input()
x = Symbol('x')
# print("before: " + equation)
# equation = sympify(equation)
# print("after: " + equation)

new_eq = ''
i = 0

# def setEqInd(equation,ind):
#     i = ind
#     new_eq = equation
# add mult sign between two vals


def checkExpr(equation):
    global x, new_eq, i
    print('equation: ', len(equation))
    two_pc = ''
    print('index inside function: ', i)
    if (equation[i] >= '0' and equation[i] <= '9') or equation[i] == 'x':
        two_pc += equation[i]
        print('outx')
        # if i + 1 <= len(equation):
        if (equation[i + 1] >= '0' and equation[i + 1] <= '9') or equation[i + 1] == 'x':
            two_pc += equation[i + 1]
            print('before ', i)
            i = i + 1
            print('after ', i)
            print('ntx')
            new_eq += add_mult_sign(two_pc)
    elif equation[i] == '+' or equation[i] == '-' or equation[i] == '*' or equation[i] == '/':
        new_eq += equation[i]
    elif equation[i] == '^':
        new_eq += '**'
    elif equation[i] == 's' or equation[i] == 'c' or equation[i] == 't' or equation[i] == 'l' or equation[i] == 'e':
        print('Calling Trignometric Function')
        trig_check(equation)
# check for trig functions and evaluate them


def trig_check(equation):
    global x, new_eq, i
    print('Index Inside Trig', i)
    if equation[i] == 's' or equation[i] == 'c' or equation[i] == 't' or equation[i] == 'l' or equation[i] == 'e':
        if equation[i-1] != '+' and equation[i-1] != '-' and equation[i-1] != '*' and equation[i-1] != '/' and equation[i-1] != '^':
            new_eq += '*'
        if equation[i] == 's':
            print('sin')
            new_eq += 'sin'
            i += 2
            if equation[i+1] == '(' and equation[i + 2] == 'x' and equation[i + 3] == ')':
                new_eq += '(x)'
                i += 2
            elif equation[i+1] == '(':
                ab = equation.index(')', i+1, len(equation)) 
                closeBracketInd = ab
                # print('AB: ', ab)
                # print()
                checkExpr(equation[i+2:closeBracketInd+1])
                new_eq += ')'
                i += ( closeBracketInd -  (i+1))-1
        elif equation[i] == 'c':
            new_eq += 'cos'
            i += 2
            if equation[i+1] == '(' and equation[i + 2] == 'x' and equation[i + 3] == ')':
                new_eq += '(x)'
                i += 2
            elif equation[i+1] == '(':
                print("arrviing here")
                ab = equation.index(')', i+1, len(equation)) 
                closeBracketInd = ab
                # print('AB: ', ab)
                print(equation[i+2:closeBracketInd+1])
                # checkExpr()
                new_eq += ')'
                i += ( closeBracketInd -  (i+1))-1
                # i += equation[i+1:closeBracketInd]-1
        elif equation[i] == 't':
            new_eq += 'tan'
            i += 2
            if equation[i+1] == '(' and equation[i + 2] == 'x' and equation[i + 3] == ')':
                new_eq += '(x)'
                i += 2
            elif equation[i+1] == '(':
                ab = equation.index(')', i+1, len(equation)) 
                closeBracketInd = ab
                # print('AB: ', ab)
                # print()
                checkExpr(equation[i+2:closeBracketInd+1])
                new_eq += ')'
                i += ( closeBracketInd -  (i+1))-1


def add_mult_sign(string):
    print("string: " + string)
    if '*' not in string:
        return string[0] + '*' + string[1]
    else:
        return string


for ind in range(len(equation)):
    if i+1 <= len(equation):
        print('most outer', i)
        checkExpr(equation)
    elif i == len(equation)-1:
        print('equation', i)
        print('len', len(equation))
        print('equation', equation[i])
        new_eq += equation[i]
        break
    elif i == len(equation) or i > len(equation):
        break

    i = i + 1
    print('last ', i)

print("Equation: ",new_eq)
# diffr = diff(new_eq)
print("Differentiation: ", diffr)
