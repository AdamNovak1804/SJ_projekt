import json
import logging

logger = logging.getLogger('logger')

default_program = 'inputs/sample_programs/PROGRAM1'


def read_config_json(src: str) -> dict:
    try:
        with open(src) as file:
            buffer_string = file.read()
            
            return json.loads(buffer_string)
    except IOError as e:
        logger.error(e.errno, e.strerror)


def read_program(src: str) -> str:
    try:
        with open(src) as file:
            buffer_string = file.read()

            return buffer_string
    except IOError:
        logger.warning(f'Specified file does not exist on path: {src}, using default: {default_program}')

        try: 
            with open(default_program) as file:
                buffer_string = file.read()

                return buffer_string
        except IOError as e:
            logger.error(e.errno, e.strerror)
