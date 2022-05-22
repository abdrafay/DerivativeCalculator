from ast import Try
from distutils.dep_util import newer
from operator import eq
from warnings import catch_warnings
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


def checkExpr(equation, indd):
    print("Given equation: " + equation)
    print("Given Index: ", indd)
    global x, new_eq, i
    f_ind = indd
    two_pc = ''
    if (equation[f_ind] >= '0' and equation[f_ind] <= '9') or equation[f_ind] == 'x':
        print('getting here')
        two_pc += equation[f_ind]
        print(equation[f_ind])
        print(len(equation))
        # if i + 1 <= len(equation):
        if(f_ind+1 == len(equation)):
            new_eq += equation[f_ind]
            print(new_eq)
        elif equation[f_ind+1] != '*' and equation[f_ind + 1] != '=' and f_ind+1 < len(equation):
            if ((equation[f_ind + 1] >= '0' and equation[f_ind + 1] <= '9') or equation[f_ind + 1] == 'x'):
                print('insert if')
                two_pc += equation[f_ind + 1]
                f_ind += 1
                i = i + 1
                print('adding mult')
                new_eq += add_mult_sign(two_pc)
            elif((equation[f_ind+1] == '^')):
                new_eq += equation[f_ind]
                new_eq += '**'
                f_ind += 1
                i += 1
                print('making power')
        else:
            new_eq += equation[f_ind] + equation[f_ind + 1]
            print('else')
            two_pc = ''
    elif equation[f_ind] == '+' or equation[f_ind] == '-' or equation[f_ind] == '*' or equation[f_ind] == '/':
        new_eq += equation[f_ind]
    elif equation[f_ind] == '^':
        print('power')
        print(equation[f_ind])
        print(new_eq)
        new_eq += '**'
    elif equation[f_ind] == 's' or equation[f_ind] == 'c' or equation[f_ind] == 't' or equation[f_ind] == 'l' or equation[f_ind] == 'e':
        if equation[f_ind-1] != '+' and equation[f_ind-1] != '-' and equation[f_ind-1] != '*' and equation[f_ind-1] != '/' and equation[f_ind-1] != '^':
            if f_ind - 1 >= 0:
                new_eq += '*'
        if equation[f_ind] == 'l':
            new_eq += 'ln'
            i += 1
            f_ind += 1
            if equation[f_ind+1] == '(' and equation[f_ind + 2] == 'x' and equation[f_ind + 3] == ')':
                new_eq += '(x)'
                i += 2
                f_ind += 2
            elif equation[f_ind+1] == '(':
                new_eq += '('
                stack = []
                pos = f_ind
                for ab in equation[f_ind+1:len(equation)]:
                    print('Stack', stack)
                    if ab == '(':
                        stack.append(ab)
                        pos += 1
                    elif ab == ')':
                        pos += 1
                        if (len(stack) > 0 and ('(' == stack[len(stack)-1])):
                            stack.pop()
                    else:
                        pos += 1
                        print("Error")

                # ab = equation.index(')', i+1, len(equation))
                closeBracketInd = pos
                print("position of bracket", pos)
                # print('AB: ', ab)
                # print()
                print(equation[f_ind+2: closeBracketInd])
                f_ind += 1
                i += 1
                checkExpr(equation[f_ind+1:closeBracketInd], 0)
                new_eq += ')'
                f_ind += 1
                i += 1
        elif equation[f_ind] == 's':
            print('sin')
            new_eq += 'sin'
            i += 2
            f_ind += 2
            if equation[f_ind+1] == '(' and equation[f_ind + 2] == 'x' and equation[f_ind + 3] == ')':
                new_eq += '(x)'
                i += 2
                f_ind += 2
            elif equation[f_ind+1] == '(':
                new_eq += '('
                stack = []
                pos = f_ind
                for ab in equation[f_ind+1:len(equation)]:
                    print('Stack', stack)
                    if ab == '(':
                        stack.append(ab)
                        pos += 1
                    elif ab == ')':
                        pos += 1
                        if (len(stack) > 0 and ('(' == stack[len(stack)-1])):
                            stack.pop()
                    else:
                        pos += 1
                        print("Error")

                # ab = equation.index(')', i+1, len(equation))
                closeBracketInd = pos
                print("position of bracket", pos)
                # print('AB: ', ab)
                # print()
                print(equation[f_ind+2: closeBracketInd])
                f_ind += 1
                i += 1
                checkExpr(equation[f_ind+1:closeBracketInd], 0)
                new_eq += ')'
                f_ind += 1
                i += 1
        elif equation[f_ind] == 'c':
            print("========== entering cos ==============")
            new_eq += 'cos'
            i += 2
            f_ind += 2
            if equation[f_ind+1] == '(' and equation[f_ind + 2] == 'x' and equation[f_ind + 3] == ')':
                new_eq += '(x)'
                i += 2
                f_ind += 2
            elif equation[f_ind+1] == '(':
                new_eq += '('
                stack = []
                pos = f_ind
                for ab in equation[f_ind+1:len(equation)]:
                    print('Stack', stack)
                    if ab == '(':
                        stack.append(ab)
                        pos += 1
                    elif ab == ')':
                        pos += 1
                        if (len(stack) > 0 and ('(' == stack[len(stack)-1])):
                            stack.pop()
                    else:
                        pos += 1
                        print("Error")

                # ab = equation.index(')', i+1, len(equation))
                closeBracketInd = pos
                print("position of bracket", pos)
                # print('AB: ', ab)
                # print()
                print(equation[f_ind+2: closeBracketInd])
                f_ind += 1
                i += 1
                checkExpr(equation[f_ind+1:closeBracketInd], 0)
                new_eq += ')'
                f_ind += 1
                i += 1
                # i += equation[i+1:closeBracketInd]-1
        elif equation[f_ind] == 't':
            new_eq += 'tan'
            print("==================== Entering Tangent ====================")
            i += 2
            f_ind += 2
            if equation[f_ind+1] == '(' and equation[f_ind + 2] == 'x' and equation[f_ind + 3] == ')':
                new_eq += '(x)'
                i += 2
                f_ind += 2
            elif equation[f_ind+1] == '(':
                new_eq += '('
                stack = []
                pos = f_ind
                for ab in equation[f_ind+1:len(equation)]:
                    print('Stack', stack)
                    if ab == '(':
                        stack.append(ab)
                        pos += 1
                    elif ab == ')':
                        pos += 1
                        if (len(stack) > 0 and ('(' == stack[len(stack)-1])):
                            stack.pop()
                    else:
                        pos += 1
                        print("Error")

                # ab = equation.index(')', i+1, len(equation))
                closeBracketInd = pos
                print("position of bracket", pos)
                # print('AB: ', ab)
                # print()
                print(equation[f_ind+2: closeBracketInd])
                f_ind += 1
                i += 1
                checkExpr(equation[f_ind+1:closeBracketInd], 0)
                new_eq += ')'
                f_ind += 1
                i += 1
                # i += (closeBracketInd - (i+1))-1
# check for trig functions and evaluate them


# def trig_check(equation):
#     global x, new_eq, i
#     print('Index Inside Trig', i)
#     if equation[i] == 's' or equation[i] == 'c' or equation[i] == 't' or equation[i] == 'l' or equation[i] == 'e':


def add_mult_sign(string):
    print("string: " + string)
    if '*' not in string:
        return string[0] + '*' + string[1]
    else:
        return string


# try:
for ind in range(len(equation)):
    print('index')
    # print("OLD EQ", equation[i])
    print('equation iNDXE', i)
    if i == len(equation) or i > len(equation) or ind > len(equation) or ind == len(equation):
        print('indx')
        break
    if i+1 <= len(equation):
        print('most outer', i)
        checkExpr(equation, i)
    elif i == len(equation)-1:
        print('equation', i)
        print('len', len(equation))
        print('equation', equation[i])
        new_eq += equation[i]
        break
    i = i + 1
print("Equation: ", new_eq)
diffr = diff(new_eq)
print("Differentiation: ", diffr)
# except IndexError:
# print(ind)
# print(i)
# print("====================== Incorrect Format Entered =====================")
# except:
# print("Error")
