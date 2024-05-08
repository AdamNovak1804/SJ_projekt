import logging

from automata.fa.dfa import DFA

from automata.fa.dfa import DFAStateT

from file_reader.file_reader import read_config_json
from file_reader.file_reader import read_program
from file_reader.file_reader import create_token_stream

logger = logging.getLogger('logger')


def preprocess_program_string(program_string: str) -> str:
    # for all given characters add whitespaces around
    characters = [';',':=','(',')','+','-',',']
    for char in characters:
        program_string = program_string.replace(char, ' ' + char + ' ')

    # terminal symbol, used to shut down DKA
    program_string += '$'

    # return modified program string back
    return program_string


def perform_lexical_anaylsis(lexical_mode: bool | None) -> None:
    # load lexical analysis configuration file
    logger.info('Extracting configuration dictionary from config file for lexical analyzer')

    config_path = 'lexical_analysis/'
    if lexical_mode is None:
        logger.info('Performing lexical analysis without any correction mode')
        config_path += 'config.json'
    elif lexical_mode is True:
        logger.info('Performing lexical analysis with SKIP correction mode')
        config_path += 'config-skip.json'
    else:
        logger.info('Performing lexical analysis with CORRECT correction mode')
        config_path += 'config-correct.json'

    config = read_config_json(config_path)

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

    # Add whitespaces between symbols and terminal symbol at the end
    program_string = preprocess_program_string(program_string)

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

        logger.info(f'Reading terminal {repr(terminal)}, moving from state {previous_state} to state {current_state}')

        # if the token_adept 'function' key is in the tokenizer dictionary, push the token
        if token_adept in tokenizer:
            token = tokenizer[token_adept]
            token_list.append(token)

            logger.info(f'Adding {token} to the list of tokens')

        # update the previous state and index
        previous_state = current_state
        index += 1

    create_token_stream(config['output_path'], token_list)
