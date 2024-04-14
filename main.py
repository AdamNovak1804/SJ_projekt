import typer
import logging

from logger.logger import setup_logger

from lexical_analysis.main import perform_lexical_anaylsis
from syntax_analysis.main import perform_syntax_anaylsis

setup_logger()

logger = logging.getLogger('logger')
app = typer.Typer()


@app.callback(invoke_without_command=True)
def full_analysis(context: typer.Context) -> None:
    if context.invoked_subcommand is None:
        logger.info('Running full code analysis')
        perform_lexical_anaylsis()
        perform_syntax_anaylsis()


@app.command()
def lexical_analysis() -> None:
    logger.info('Running lexical analysis only')
    perform_lexical_anaylsis()


@app.command()
def syntax_analysis() -> None:
    logger.info('Running syntax analysis only')
    perform_syntax_anaylsis()


if __name__ == '__main__':
    app()