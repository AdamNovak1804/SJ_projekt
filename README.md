# SJ_projekt

## Reference document

Before we were able to construct the automatas and test them, we had to convert a specific subset of SMALL code BNF-form grammar rules to a LL1 form. The results of our conversion and the basis for our automatas can be viewed in a chronological order [here](https://docs.google.com/document/d/1wxjJOHf2RQpkMxK3qBfFl3yAnMiYRUSFHijHMCOACQ4/edit?usp=sharing).

## Requirements

In order to run this program and satisfy all dependency requirements, **Python** 3.8 version or newer is required.

## Installation

This project uses **Poetry** for dependency management. You can install it by running the command below:

```console
    python -m pip install poetry
```

Or by following the installation tutorial on the official Poetry website documentation [here](https://python-poetry.org/docs/).
To install other dependencies which are specified in the `pyproject.toml` file, run the following command:

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
├── lexical_analysis/
│   ├── config.json
│   └── lexical_analysis.py
├── syntax_analysis/
│   ├── config.json
│   └── syntax_analysis.py
├── logger/
│   └── logger.py
├── outputs/
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
- `logger` : contains `logger.py` file which specifies a custom logger configuration
- `outputs` : any files created as a result of the analysis will be stored here
- `syntax_analysis` : module for a syntax analyzer
    - `syntax_analysis.py` : performs the syntax analysis
    - `config.json` : holds configuration details for syntax analysis
- `main.py` : handles the command line input
- `pyproject.toml` : specifies the project build configuration