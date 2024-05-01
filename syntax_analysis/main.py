from syntax_analysis.config import rules

def perform_syntax_anaylsis() -> None:
    tokens = ["begin", "if", "not", "openparen", "true", "closeparen", "and", "false", "or", "true", "then", "ident", "assignment", "openparen", "num", "minus", "ident", "closeparen", "plus", "ident", "semicolon", "semicolon", "end"]
    stack = ["PROGRAM"]
    number = 0
    token = tokens[number]
    while number != len(tokens):
        if token != stack[-1]:
            value = rules.get(stack[-1] + token, None)
            if value == None:
                print("No rule found for", stack[-1], token)
                break
            rule_list = value.split("=")[1].split(" ")
            stack.pop()
            for rule in rule_list[::-1]:
                if rule != "e":
                    stack.append(rule)
        else:
            print(token)
            stack.pop()
            if number == len(tokens)-1:
                if stack.length > 0:
                print("Stack is not empty")
                break
            number += 1
            token = tokens[number]
