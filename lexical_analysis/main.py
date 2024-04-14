import logging

from automata.fa.dfa import DFA

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
        states = set(config['automata']['states']),
        input_symbols = config['automata']['input_symbols'],
        transitions = config['automata']['transitions'],
        initial_state = config['automata']['initial_state'],
        final_states = set(config['automata']['final_states'])
    )

    # read code to analyze with specified path
    logger.info('Reading program specified in config file')
    program_string = read_program(config['program_path'])

    # create a generator object that yields current state for every iteration until final state
    dfa_stepwise_generator = lexical_analyser.read_input_stepwise(input_str=program_string)

    for current_state in dfa_stepwise_generator:
        print(current_state)
