from sympy import *
equation = input()
x = Symbol('x')

def add_mult_sign(string):
    print("string: " + string)
    if '*' not in string:
        return string[0] + '*' + string[1]
    else:
        return string

new_eq = ''
i = 0
for ind in range(len(equation)):
    if i+1 <= len(equation):
        two_pc = ''
        if (equation[i] >= '0' and equation[i] <= '9') or equation[i] == 'x':
            two_pc += equation[i]
            if (equation[i + 1] >= '0' and equation[i + 1] <= '9') or equation[i + 1] == 'x':
                two_pc += equation[i + 1]
                i = i + 1
                new_eq += add_mult_sign(two_pc)
        elif equation[i] == '+' or equation[i] == '-' or equation[i] == '*' or equation[i] == '/':
            new_eq += equation[i]
        elif equation[i] == '^':
            new_eq += '**'
        elif equation[i] == 's' or equation[i] == 'c' or equation[i] == 't' or equation[i] == 'l' or equation[i] == 'e':
            if equation[i-1] != '+' and equation[i-1] != '-' and equation[i-1] != '*' and equation[i-1] != '/' and equation[i-1] != '^':
                new_eq += '*'
            if equation[i] == 's':
                new_eq += 'sin'
                i += 2
                if equation[i+1] == '(' and equation[i + 2] == 'x' and equation[i + 3] == ')':
                    new_eq += '(x)'
                    i += 2
            elif equation[i] == 'c':
                new_eq += 'cos'
                i += 2
                if equation[i+1] == '(' and equation[i + 2] == 'x' and equation[i + 3] == ')':
                    new_eq += '(x)'
                    i += 2
            elif equation[i] == 't':
                new_eq += 'tan'
                i += 2
                if equation[i+1] == '(' and equation[i + 2] == 'x' and equation[i + 3] == ')':
                    new_eq += '(x)'
                    i += 2
    elif i == len(equation)-1:
        new_eq += equation[i]
        break
    elif i == len(equation) or i > len(equation):
        break

    i = i + 1
    
print("Equation: ", equation)
print("Evaluated Equation: ",new_eq)
diffr = diff(new_eq)
print("Differentiation: ", diffr)