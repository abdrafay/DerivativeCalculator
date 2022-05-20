from sympy import *
import numpy as np
print('s')  
x = Symbol('x')
y = Symbol('y')
# if there is no multiplication sign between the two numbers, add multiplication sign between them
print(diff("ln(x)"))
# vl = add_mult_sign('2x')
# print(vl)
# eval("2x")
# eq = diff("2*x*cos(x) + x**2")
# print(eq)


# # checking if the expression contains any special characters
# def specialCharCheck(expr):
#     for i in range(len(expr)):
#         if expr[i] == '(' or expr[i] == ')' or expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/' or expr[i] == '^':
#             special.append(expr[i])

# def twoCharCheck(ch1, ch2) {
#     #check if ch1 and ch2 contain any special character
#     if(ch1.find('(') != -1 or ch1.find(')') != -1 or ch1.find('+') != -1 or ch1.find('-') != -1 or ch1.find('*') != -1 or ch1.find('/') != -1 or ch1.find('^') != -1):
# }
# def check_splcharacter(chr):

#     # Make an RE character set and pass
#     # this as an argument in compile function

#     string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')

#     # Pass the string in search function
#     # of RE object (string_check).

#     if(string_check.search(chr) == None):
#         print("String does not contain Special Characters.")

#     else:
#         print("String contains Special Characters.")

# # Extract Symbol from an equation

# x, y, z, t = symbols('x,y,z,t')
# # check for trignometric functions in an expression


# def trigCheck(expr):
#     for i in range(len(expr)):
#         if expr[i] == 'sin' in expr[i]:
#             trig.append(expr[i])
#         elif expr[i] == 'cos':
#             trig.append(expr[i])
#         elif expr[i] == 'tan':
#             trig.append(expr[i])
#         elif expr[i] == 'sec':
#             trig.append(expr[i])
#         elif expr[i] == 'csc':
#             trig.append(expr[i])
#         elif expr[i] == 'cot':
#             trig.append(expr[i])
#         elif expr[i] == 'asin':
#             trig.append(expr[i])
#         elif expr[i] == 'acos':
#             trig.append(expr[i])
#         elif expr[i] == 'atan':
#             trig.append(expr[i])
#         elif expr[i] == 'asec':
#             trig.append(expr[i])
#         elif expr[i] == 'acsc':
#             trig.append(expr[i])
#         elif expr[i] == 'acot':
#             trig.append(expr[i])


# def get_symbol(eq):
#     return eq.free_symbols.pop()


# def valuesSeperator(expr):
#     # extract values in an array from an expression
#     for i in range(len(expr)):
#         if expr[i] == '':
#             print(expr[i])
#             identifier = 1
#             val.append(expr[i])
#             break


# def TrigCheckExpr(expr):
#     if 'cos' in expr or 'sin' in expr or 'tan' in expr:
#         if('cos' in expr):
#             ind = expr.index('cos')
#             for i in range(ind + 3, len(expr)):
#                 if expr[i] == '(':
#                     brSt = i
#                     for br in range(i, len(expr)):
#                         if expr[br] == ')':
#                             brCl = br
#                             TrigCheckExpr(expr[brSt:brCl])

#                 else:
#                     print("No Brackets")
#     else:
#         print("End of the check")
# # def symbol_extractor(expr):
# #     """
# #     Extracts the symbols from an expression.
# #     """
# #     symbols = []
# #     for i in expr:
# #         symbols.append(i)
# #     print(symbols)
# #     return symbols
# # check if equation does not contains * b/w two symbols
# #
# #


# # def check_for_multiplication(expr):
# #     for i in range(len(expr)):
# #         if expr[i] == '*':
# #             if expr[i - 1] == '*':
# #                 print("Multiplication is not allowed")
# #                 return False
# #             elif expr[i + 1] == '*':
# #                 print("Multiplication is not allowed")
# #                 return False
# #             else:
# #                 return True


# # f = 2* +'x'+  **2+3
# # print("Differentiating with respect to ")
# # sym = input()
# # x = Symbol(sym)
# print("Enter the expression")
# expr = input()
# x = Symbol('x')
# print(diff(2*x**2))


# identifier = 1
# # valuesSeperator(expr)
# # val = []
# # for i in expr:

# #     if(ord(i) > 47 and ord(i) < 58):

# #         val.append(int(i))
# #         print(val)
# #     else:
# #         val.append(i)
# # print(val)
# # if i == '+':
# #     val.append(i)
# # elif i == '-':
# #     val.append(i)
# # elif i == '*':
# #     val.append(i)
# # elif i == '/':
# #     val.append(i)
# # elif i == '^':
# #     val.append(i)
# # elif i == '(':
# #     val.append(i)
# # elif i == ')':
# #     val.append(i)
# # elif i == 'x':
# #     val.append(i)
# # elif i == ' ':
# #     val.append(i)
# # else:
# #     val.append(i)
# # print(val)

# # print("Enter the value of x")
# # x_val = input()
# # x_val = sympify(x_val)
# # print(expr)

# # sym = Symbol('x')
# #
