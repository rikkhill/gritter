import click


@click.group()
def cli():
    click.echo("Does the CLI shell work?")


@cli.command()
@click.argument("usernames", nargs=-1)
@click.option("--depth", default=1, type=int, help="Depth of connections to return (default 1)")
def users(usernames, depth):
    """Provide a list of usernames to get the graph for."""
    click.echo("Usernames:")
    for user in usernames:
        click.echo("\t%s" % user)
    click.echo("Depth %d" % depth)

@cli.command()
@click.argument("file", type=click.File("r"))
def userfile(file):
    """A file containing usernames, separated by newlines."""
    users = [u.strip() for u in file.readlines()]

    for user in users:
        click.echo(user)