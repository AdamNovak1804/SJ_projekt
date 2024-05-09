import logging

from syntax_analysis.config import rules
from file_reader.file_reader import read_token_stream

logger = logging.getLogger('logger')

def perform_syntax_anaylsis(syntax_mode: bool | None) -> None:
    tokens = read_token_stream("outputs/token_stream")
    error_correction = 0

    if syntax_mode is None:
        logger.info('Performing syntax analysis without any correction mode')
    elif syntax_mode is True:
        logger.info('Performing syntax analysis with Panic Mode Recovery correction mode')
    else:
        logger.info('Performing syntax analysis with Phrase level correction mode')

    stack = ["PROGRAM"]
    number = 0
    token = tokens[number]
    correction = False
    while number != len(tokens):
        if token != stack[-1]:
            value = rules.get(stack[-1] + token, None)
            if value == None:
                if syntax_mode is True:
                    if token != "semicolon" and token!= "end":
                        logger.info(f"No rule found for {stack[-1]} {token}. Skipping token")
                        number += 1
                        token = tokens[number]
                        continue
                    else:
                        logger.info(f"No rule found for {stack[-1]} {token}. {token} is synchronization token. Program is not valid.")
                        break
                elif syntax_mode is False and not correction:
                    if tokens[number-1] not in ("number", "closeparen", "semicolon", "ident"):
                        logger.info(f"No rule found for {stack[-1]} {token}. Adding semicolon")
                        tokens.insert(number, "semicolon")
                        token = tokens[number]
                        correction = True
                        continue
                
                logger.info(f"No rule found for {stack[-1]} {token}")
                break
            rule_list = value.split("=")[1].split(" ")
            logger.info(f"Value in stack {stack[-1]} exchanged with rule {value}") 
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
            correction = False
