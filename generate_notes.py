import json

import click

from discharge_notes.constants import GENERATOR_INSTRUCTIONS
from discharge_notes.discharger import DischargeNoteBuilder
from discharge_notes.generators.openai import OpenAIGenerator

GENERATORS = {
    "openai": OpenAIGenerator(context=GENERATOR_INSTRUCTIONS),
}


@click.command()
@click.argument("input_file")
@click.option("--output-file", type=click.Path(), default=None)
@click.option("--generator", type=click.Choice(GENERATORS.keys()), default="openai")
def generate_notes(
    input_file: click.Path, output_file: click.Path = None, generator: str = "openai"
):
    with open(input_file) as input_f:
        data = json.load(input_f)

    generator_obj = GENERATORS.get(generator)
    if not generator_obj:
        raise ValueError(f"Invalid generator: {generator}")

    builder = DischargeNoteBuilder(generator_obj)
    result = builder.build_discharge_note(data)

    if output_file:
        with open(output_file, "w") as output_f:
            json.dump(result, output_f)
    else:
        click.echo(result)


if __name__ == "__main__":
    generate_notes()
