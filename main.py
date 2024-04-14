import typer

from logger.logger import setup_logger

from lexical_analysis.main import perform_lexical_anaylsis
from syntax_analysis.main import perform_syntax_anaylsis

setup_logger()

app = typer.Typer()


@app.command()
def full_analysis() -> None:
    perform_lexical_anaylsis()
    perform_syntax_anaylsis()


@app.command()
def lexical_analysis() -> None:
    perform_lexical_anaylsis()


@app.command()
def syntax_analysis() -> None:
    perform_syntax_anaylsis()


if __name__ == '__main__':
    app()