# SJ_projekt

## Reference document

Before we were able to construct syntactical and lexical analyzers and test them, we had to convert a given subset of SMALL code BNF-form grammar rules to an LL1 form. The results of our conversion and the basis for our analyzers can be viewed in chronological order [here](https://docs.google.com/document/d/1wxjJOHf2RQpkMxK3qBfFl3yAnMiYRUSFHijHMCOACQ4/edit?usp=sharing). To see the syntax analysis spreadsheet table, where we defined rules for the syntax analyzer, access it [here](https://docs.google.com/spreadsheets/d/11r0xmxEgj-i0TbyMgCvOHaD8lxXuihsaAN7JyCsjUoU) by clicking the higlighted link.

## Overview

This project performs lexical and syntax analysis on a given stream of code. Some examples of this code are provided in the project file structure for testing purposes. In addition to the *lexical-analyzer* and *syntax-analyzer* modules, the source code also contains separate modules for file reading purposes and a logger module which provides a logging interface.

The lexical analyzer utilizes a *Deterministic Finite Automata (DFA)* for analysis. The provided automata is from the `automata-lib` Python library. The configuration of this automata can be found in the `config.json` file. If the given input is incorrect, or contains terminals which are not specified in the configuration, the program will create an exception and stop. This behaviour can be somewhat altered by using different recovery settings. The differentiation of functionality between the different modes is defined by different DFA configurations, specified in the `config-skip.json` & `config-correct.json` files. The configuration files also contain a *tokenizer*, which is a dictionary of state transitions-input terminals keys, which are paired with the corresponding token values. The output of the lexical analysis can be found in the `outputs/token_stream` file.

The syntax analyzer reads the output of the lexical analysis in the form of tokens. We also implemented a stack using a simple list. In each cycle of the syntax analyzer, the program takes an input symbol from the list of tokens and a symbol from the top of the stack. It combines these two symbols into one word and tries to find a value for such a combination of symbols in the dictionary. The dictionary contains combination of the symbols as a key and a rule we should apply as a value combination. If it finds a combination of symbols in the dictionary, it returns a rule that we apply by replacing the symbol from the top of the stack with symbols from the rule we want to apply. If the symbol from the top of the stack and the input symbol are equal, we discard the symbol from the top of the stack and move to the next input symbol. If there is no rule found for the combination of symbols the program returns an error message.

In addition to the default **no-recovery** setting, which does not utilize any recovery mechanisms in the case of an invalid input, there are two recovery modes for each analysis which can be selected by using the appropriate flags.

> **_NOTE:_**  The correct usage of flags will be demonstrated further down in the text.

### Lexical analysis recovery modes

- SKIP - (accessed via the `--skip` flag), will move to a special *collector* state after reading an invalid terminal symbol and switch back to the initial state once a space or NEW LINE symbol is read.
- CORRECT - (accessed via the `--correct` flag), will try to switch the first and second characters and check if the corrected stream of terminals can be parsed as a token.

### Syntax analysis recovery modes

- PANIC - (accessed via the `--panic` flag), if no rule is found for the combination of the input symbol and the symbol from the top of the stack, the panic recovery mode skips the input symbol and moves on to the next symbol. We also set the sync tokens `semicolon` and `end`.
- PHRASE - (accessed via the `--phrase` flag), if no rule is found for the combination of the input symbol and the symbol from the top of the stack, the phrase recovery mode adds a semicolon to the input at the place of the error. This happens only if the previous input symbol is `number`, `closeparen`, `semicolon`, or `ident`.

## Requirements

**Python** 3.10 version or newer is required to run this program and satisfy all dependency requirements. Additionally, the project uses **Poetry** for dependency management. You can install it by running the command below:

```console
    python -m pip install poetry
```

Or by following the installation tutorial on the official Poetry website documentation [here](https://python-poetry.org/docs/).

## Installation

After satisfying all the requirements, the additional dependencies can be installed via Poetry. These dependencies can be found in the `pyproject.toml` file, and can be installed by running the following command:

```console
    poetry install
```

## Running the program

You can perform a full lexical and syntax analysis by running this command:

```console
    poetry run python main.py
```

To see other options/commands, append the `--help` option to the command and run it:

```console
    poetry run python main.py --help
```

In addition to the full analysis, two additional commands exist which allow the user to specify which analysis is to be performed. A sole lexical analysis can be performed via this command:

```console
    poetry run python main.py lexical-analysis
```

The results of the lexical analysis can be found in the `outputs/` folder as `token_stream` file. To perform sole syntax analysis execute the following command:

```console
    poetry run python main.py syntax-analysis
```

> **_NOTE:_**  `token_stream` file in the `outputs/` folder is required to perform this, otherwise error will be given.

## Recovery settings

To run full analysis with both analyses recovery modes set, you can structure the command with both flags in a succession:

```console
    poetry run python main.py --skip --panic
```

Which will use the SKIP recovery mode option for the lexical analysis and the PANIC recovery mode for the syntax analysis.

You can also use recovery modes for partial analysis, such as:

```console
    poetry run python main.py lexical-analysis --correct
```

Which will only perform lexical analysis with the CORRECT recovery mode option.

## Project tree structure

The project boilerplate structure is visualized in a tree-like structure below.

```
.
├── file_reader/
│   └── file_reader.py
├── inputs/
│   ├── sample_programs/
│   │   ├── PROGRAM1
│   │   ├── PROGRAM2
│   │   ├── PROGRAM3
│   │   ├── PROGRAM4
│   │   ├── PROGRAM5
│   │   ├── PROGRAM6
│   │   ├── PROGRAM7
│   │   ├── PROGRAM8
│   │   ├── PROGRAM9
│   │   └── PROGRAM10
│   └── user_programs/
│   │   └── EXAMPLEPROG1
├── lexical_analysis/
│   ├── config-correct.json
│   ├── config-skip.json
│   ├── config.json
│   └── lexical_analysis.py
├── syntax_analysis/
│   ├── config.json
│   └── syntax_analysis.py
├── logger/
│   └── logger.py
├── outputs/
│   └── readme.txt
├── .gitignore
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

The project is structured into submodules containing utility functions or objects that can be separated from each other.

- `file_reader` : contains `file_reader.py` file which holds functions that deal with opening, reading, closing files and handling any exceptions that may occur in the process.
- `inputs` : contains source codes for validation
    - `sample_programs` : sample programs to use for validation, first five entries are gramatically correct, the rest contain mistakes
    - `user_programs` : insert your own programs here and configure path to them in `config.json` files
- `lexical_analysis` : module for a lexical analyzer
    - `lexical_analysis.py` : performs the lexical analysis
    - `config.json` : holds configuration details for lexical analysis
    - `config-skip.json` : holds configuration details for the SKIP recovery mode DFA
    - `config-correct.json` : holds configuration details for the CORRECT recovery mode DFA
- `logger` : contains `logger.py` file which specifies a custom logger configuration
- `outputs` : any files created as a result of the analysis will be stored here
- `syntax_analysis` : module for a syntax analyzer
    - `syntax_analysis.py` : performs the syntax analysis
    - `config.json` : holds configuration details for syntax analysis
- `main.py` : handles the command line input
- `pyproject.toml` : specifies the project build configuration

## Authors

- Nikola Blahovičová 
- Adam Novák
