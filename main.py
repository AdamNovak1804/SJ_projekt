import typer
import logging

from typing import Optional
from typing_extensions import Annotated

from logger.logger import setup_logger

from lexical_analysis.main import perform_lexical_anaylsis
from syntax_analysis.main import perform_syntax_anaylsis

setup_logger()

logger = logging.getLogger('logger')
app = typer.Typer()


@app.callback(invoke_without_command=True)
def full_analysis(context: typer.Context, lexical_mode: Annotated[Optional[bool], typer.Option('--skip/--correct')] = None, syntax_mode: Annotated[Optional[bool], typer.Option('--panic/--phrase')] = None) -> None:
    if context.invoked_subcommand is None:
        logger.info('Running full code analysis')
        perform_lexical_anaylsis(lexical_mode)
        perform_syntax_anaylsis(syntax_mode)


@app.command()
def lexical_analysis(lexical_mode: Annotated[Optional[bool], typer.Option('--skip/--correct')] = None) -> None:
    logger.info('Running lexical analysis only')
    perform_lexical_anaylsis(lexical_mode)


@app.command()
def syntax_analysis(syntax_mode: Annotated[Optional[bool], typer.Option('--panic/--phrase')] = None) -> None:
    logger.info('Running syntax analysis only')
    perform_syntax_anaylsis(syntax_mode)


if __name__ == '__main__':
    app()