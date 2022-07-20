import string

def postfix(equation: list):
    output = []
    stack = []

    op = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3, "(": 4, ")": 4}
    for element in equation:

        if element not in op:
            output.append(element)
        else:

            if element == ")":

                while True:
                    if stack[-1] == "(":
                        break

                    output.append(stack.pop())

                stack.pop()
            elif len(stack) == 0 or op[element] > op[stack[-1]]:
                stack.append(element)
            elif op[element] <= op[stack[-1]] and stack[-1] :

                while True:

                    if len(stack) != 0 and op[element] <= op[stack[-1]] and stack[-1] != "(":
                        output.append(stack.pop())
                        continue
                    break

                stack.append(element)

    else:
        output.extend(reversed(stack))

    return output

def powerful_split(input_: str):
    op = ["+", "-", "*", "/", "^", "(", ")", "%"]
    output = []

    x = ""
    for letter in input_:
        if letter == " ":
            continue
        elif letter in op:
            if x != "":
                output.append(x)
            output.append(letter)
            x = ""
        else:

            x += letter
    else:
        if x != "":
            output.append(x)

    return output



def calculate(input_: str, variables: dict=None):

        rpn = postfix(powerful_split(input_))

        while True:
            if len(rpn) == 1:
                return int(rpn[0]) if int(rpn[0]) - rpn[0] == 0 else rpn[0]

            mining_area = 0

            for index, x in enumerate(rpn):

                if x in ["+", "-", "*", "/", "%", "^"]:
                    mining_area = index - 2
                    break

            unprocessed_num1 = rpn.pop(mining_area)
            unprocessed_num2 = rpn.pop(mining_area)
            op = rpn.pop(mining_area)

            if not str(unprocessed_num1).replace(".", "").isnumeric() and unprocessed_num1 not in variables and unprocessed_num1 not in ["+", "-", "*", "/", "%", "^"]:
                return "Unknown Variable " + str(unprocessed_num1)
            elif not str(unprocessed_num2).replace(".", "").isnumeric() and unprocessed_num2 not in variables and unprocessed_num2 not in ["+", "-", "*", "/", "%", "^"]:
                return "Unknown Variable " + str(unprocessed_num2)

            num1 = variables[unprocessed_num1] if unprocessed_num1 in variables else float(unprocessed_num1)
            num2 = variables[unprocessed_num2] if unprocessed_num2 in variables else float(unprocessed_num2)

            if op == "+":
                rpn.insert(mining_area, num1 + num2)
            elif op == "-":
                rpn.insert(mining_area, num1 - num2)
            elif op == "*":
                rpn.insert(mining_area, num1 * num2)
            elif op == "/":
                rpn.insert(mining_area, num1 / num2)
            elif op == "^":
                rpn.insert(mining_area, num1 ** num2)
            elif op == "%":
                rpn.insert(mining_area, num1 % num2)





if "__main__" == __name__:
    while True:
        print(calculate(input(), variables={"a": 12, "b": 10}))
