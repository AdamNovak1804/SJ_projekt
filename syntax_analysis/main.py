def perform_syntax_anaylsis(num) -> None:
    stack = ["PROGRAM"]
    for token in tokens:
        if token != stack[-1]:
            value = rules[stack[-1] + token]
            if value == undefined:
                print("stack[-1] + token")
                break
            if value == "e":
                stack.pop()
                continue
            rule_list = value.split("=")[2].split(" ")
            stack.pop()
            for rule in rule_list[::-1]:
                stack.append(rule)
            print(value)
        else:
            stack.pop()
