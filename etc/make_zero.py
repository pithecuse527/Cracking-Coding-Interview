test_cases = int(input())

def dfs(operators, numbers):
    # base cae
    # when # numbers is 4 then # operators should be 3
    if len(operators) == len(numbers)-1:    
        expression = ""
        for i in range(len(operators)):
            expression += str(numbers[i]) + operators[i]
        expression += str(numbers[-1])
        
        if eval(expression.replace(' ', '')) == 0:
            print(expression)
        return
    
    # append each of the operator
    for c in [' ', '+', '-']:
        operators.append(c)
        dfs(operators, numbers)
        operators.pop()

for _ in range(test_cases):
    N = int(input())
    numbers = [x for x in range(1, N+1)]
    dfs([], numbers)
    print()
