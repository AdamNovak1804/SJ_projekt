import logging

from syntax_analysis.config import rules
from file_reader.file_reader import read_token_stream

logger = logging.getLogger('logger')

def perform_syntax_anaylsis() -> None:
    logger.info("Performing syntax analysis....")
    tokens = read_token_stream("outputs/token_stream")

    stack = ["PROGRAM"]
    number = 0
    token = tokens[number]
    while number != len(tokens):
        if token != stack[-1]:
            value = rules.get(stack[-1] + token, None)
            if value == None:
                logger.info("No rule found for", stack[-1], token)
                break
            rule_list = value.split("=")[1].split(" ")
            logger.info(f"Value in stack {stack[-1]} exchanged with {rule_list[::-1]}") 
            logger.info(f"Rule is epsilon, only pop {stack[-1]} from stack")
            stack.pop()
            for rule in rule_list[::-1]:
                if rule != "e":
                    stack.append(rule)
        else:
            logger.info(f"Value on top of the stack and token are the same. Pop {stack[-1]} from stack and go to next token")
            stack.pop()
            if number == len(tokens)-1:
                if len(stack) > 0:
                    logger.info("ERROR - Stack is not empty but end of file reached. Program is not valid.")
                else:
                    logger.info("End of file reached and stack is empty. Program is valid. ")
                break
            number += 1
            token = tokens[number]
