"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Advancedlabcourse Utils."""


if __name__ == "__main__":
    main(prog_name="advancedlabcourse-utils")  # pragma: no cover
