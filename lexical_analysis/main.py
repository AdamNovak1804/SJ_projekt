import logging

from automata.fa.dfa import DFA

from automata.fa.dfa import DFAStateT

from file_reader.file_reader import read_config_json
from file_reader.file_reader import read_program

logger = logging.getLogger('logger')


def perform_lexical_anaylsis() -> None:
    # load lexical analysis configuration file
    logger.info('Extracting configuration dictionary from config file for lexical analyzer')
    config = read_config_json('lexical_analysis/config.json')

    # TODO: change configuration file to perform SMALL language lexical analysis
    # creating DFA with args from config file
    logger.info('Setting up deterministic state automata')
    lexical_analyser = DFA(
        allow_partial=True,
        states = set(config['automata']['states']),
        input_symbols = config['automata']['input_symbols'],
        transitions = config['automata']['transitions'],
        initial_state = config['automata']['initial_state'],
        final_states = set(config['automata']['final_states'])
    )

    tokenizer = config['tokenizer']
    token_list = []

    # read code to analyze with specified path
    logger.info('Reading program specified in config file')
    program_string = read_program(config['program_path'])

    # add terminal symbol for the program
    program_string += '$'

    # create a generator object that yields current state for every iteration until final state
    dfa_stepwise_generator = lexical_analyser.read_input_stepwise(input_str=program_string)

    # declare & initialize helping temporary variables
    index = 0
    previous_state: DFAStateT = next(dfa_stepwise_generator)

    # move through all states in the DFA
    for current_state in dfa_stepwise_generator:
        # obtain the current terminal
        terminal = program_string[index]
        # create a 'function' which will be used in tokenizer lookup table
        token_adept = '_'.join([previous_state, current_state, terminal])

        print(repr(token_adept))

        # if the token_adept 'function' key is in the tokenizer dictionary, push the token
        if token_adept in tokenizer:
            token_list.append(tokenizer[token_adept])

        # update the previous state and index
        previous_state = current_state
        index += 1

    print(token_list)
