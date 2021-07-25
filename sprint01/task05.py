def toPostFixExpression(expression):
    answer = []
    stack = []
    precedence = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1}
    for element in expression:
        if element.isdigit():
            answer.append(element)
            continue
        if element == '(':
            stack.append(element)
            continue
        if element == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                else:
                    answer.append(temp)
            continue
        while(
            stack
            and stack[-1] != '('
            and precedence[stack[-1]] >= precedence[element]
        ):
            answer.append(stack.pop())
        stack.append(element)
    answer.extend(stack[::-1])
    return answer
