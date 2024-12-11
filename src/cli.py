import typer
from pathlib import Path

from tableau_images import tableau_images

app = typer.Typer()


@app.command()
def command(
    in_directory: Path = typer.Option(
        default=Path("./svg"), help="Input SVG path"
    ),
    out_directory: Path = typer.Option(
        default=Path("./png"), help="Input SVG path"
    ),
) -> None:
    tableau_images(in_directory=in_directory, out_directory=out_directory)


def main():
    app()


if __name__ == "__main__":
    main()
