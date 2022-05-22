from sympy import *
equation = input()
x = Symbol('x')

new_eq = ''
i = 0
evIndex = 0


def evExp(eq, indx):
    global i, new_eq, x, evIndex
    evIndex = indx
    for ind in range(len(eq)):
        if evIndex == len(eq) or evIndex > len(eq) or ind > len(eq) or ind == len(eq):
            break
        if evIndex+1 <= len(eq):
            checkExpr(eq, evIndex)
        elif evIndex == len(eq)-1:
            new_eq += eq[evIndex]
            break
        i = i + 1
        evIndex += 1


def checkExpr(equation, indd):
    global x, new_eq, i, evIndex
    f_ind = indd
    two_pc = ''
    if (equation[f_ind] >= '0' and equation[f_ind] <= '9'):
        two_pc += equation[f_ind]
        if(f_ind+1 == len(equation)) or equation[f_ind] == 'x':
            new_eq += equation[f_ind]
            print(new_eq)
            return
        elif equation[f_ind+1] != '*' and equation[f_ind + 1] != '=' and f_ind+1 < len(equation):
            if ((equation[f_ind + 1] >= '0' and equation[f_ind + 1] <= '9') or equation[f_ind + 1] == 'x'):
                two_pc += equation[f_ind + 1]
                f_ind += 1
                i = i + 1
                new_eq += add_mult_sign(two_pc)
            elif((equation[f_ind+1] == '^')):
                new_eq += equation[f_ind]
                new_eq += '**'
                f_ind += 1
                i += 1
        else:
            new_eq += equation[f_ind] + equation[f_ind + 1]
            two_pc = ''
    elif equation[f_ind] == '+' or equation[f_ind] == '-' or equation[f_ind] == '*' or equation[f_ind] == '/':
        new_eq += equation[f_ind]
    elif equation[f_ind] == '^':
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
                evIndex += 2
            elif equation[f_ind+1] == '(':
                new_eq += '('
                stack = []
                pos = f_ind
                for ab in equation[f_ind+1:len(equation)]:
                    if ab == '(':
                        stack.append(ab)
                        pos += 1
                    elif ab == ')':
                        pos += 1
                        if (len(stack) > 0 and ('(' == stack[len(stack)-1])):
                            stack.pop()
                    else:
                        pos += 1

                closeBracketInd = pos
                f_ind += 1
                i += 1
                evIndex += 1
                evExp(equation[f_ind+1:closeBracketInd], 0)

                new_eq += ')'
                f_ind += 1
                i += 1
                evIndex += 1
        elif equation[f_ind] == 's':
            new_eq += 'sin'
            i += 2
            f_ind += 2
            if equation[f_ind+1] == '(' and equation[f_ind + 2] == 'x' and equation[f_ind + 3] == ')':
                new_eq += '(x)'
                i += 2
                f_ind += 2
                evIndex += 2
            elif equation[f_ind+1] == '(':
                new_eq += '('
                stack = []
                pos = f_ind
                for ab in equation[f_ind+1:len(equation)]:
                    if ab == '(':
                        stack.append(ab)
                        pos += 1
                    elif ab == ')':
                        pos += 1
                        if (len(stack) > 0 and ('(' == stack[len(stack)-1])):
                            stack.pop()
                    else:
                        pos += 1

                closeBracketInd = pos
                f_ind += 1
                i += 1
                evIndex += 1
                evExp(equation[f_ind+1:closeBracketInd], 0)

                new_eq += ')'
                f_ind += 1
                i += 1
                evIndex += 1
        elif equation[f_ind] == 'c':
            new_eq += 'cos'
            i += 2
            f_ind += 2
            if equation[f_ind+1] == '(' and equation[f_ind + 2] == 'x' and equation[f_ind + 3] == ')':
                new_eq += '(x)'
                i += 2
                f_ind += 2
                evIndex += 2
            elif equation[f_ind+1] == '(':
                new_eq += '('
                stack = []
                pos = f_ind
                for ab in equation[f_ind+1:len(equation)]:
                    if ab == '(':
                        stack.append(ab)
                        pos += 1
                    elif ab == ')':
                        pos += 1
                        if (len(stack) > 0 and ('(' == stack[len(stack)-1])):
                            stack.pop()
                    else:
                        pos += 1
                closeBracketInd = pos
                f_ind += 1
                i += 1
                evIndex += 1
                evExp(equation[f_ind+1:closeBracketInd], 0)
                new_eq += ')'
                f_ind += 1
                i += 1
                evIndex += 1
        elif equation[f_ind] == 't':
            new_eq += 'tan'
            i += 2
            f_ind += 2
            if equation[f_ind+1] == '(' and equation[f_ind + 2] == 'x' and equation[f_ind + 3] == ')':
                new_eq += '(x)'
                i += 2
                f_ind += 2
                evIndex += 2
            elif equation[f_ind+1] == '(':
                new_eq += '('
                stack = []
                pos = f_ind
                for ab in equation[f_ind+1:len(equation)]:
                    if ab == '(':
                        stack.append(ab)
                        pos += 1
                    elif ab == ')':
                        pos += 1
                        if (len(stack) > 0 and ('(' == stack[len(stack)-1])):
                            stack.pop()
                    else:
                        pos += 1
                closeBracketInd = pos
                f_ind += 1
                i += 1
                evIndex += 1
                evExp(equation[f_ind+1:closeBracketInd], 0)

                new_eq += ')'
                f_ind += 1
                i += 1
                evIndex += 1
        elif equation[f_ind] == 'e':
            new_eq += 'e'
            i += 1


def add_mult_sign(string):
    if '*' not in string:
        return string[0] + '*' + string[1]
    else:
        return string


for ind in range(len(equation)):
    if i == len(equation) or i > len(equation) or ind > len(equation) or ind == len(equation):
        break
    if i+1 <= len(equation):
        checkExpr(equation, i)
    elif i == len(equation)-1:
        new_eq += equation[i]
        break
    i = i + 1


print("Generated Equation: ", new_eq)
diffr = diff(new_eq)
print("Differentiation: ", diffr)
