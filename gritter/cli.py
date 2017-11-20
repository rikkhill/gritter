import click
import tweepy
import time
import gritter.config as config

CONF_PATH = click.get_app_dir("gritter") + "/.conf"


def get_friends(user_list):

    credentials = config.get_auth(CONF_PATH)
    auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    auth.set_access_token(credentials["access_token"], credentials["access_secret"])

    api = tweepy.API(auth)

    #with click.progressbar(user_list) as user_bar:
    for user in user_list:
        print(api.friends_ids(user))

    print(api.rate_limit_status()["resources"]["friends"])

@click.group()
def cli():
    click.echo("Does the CLI shell work?")
    click.echo(click.get_app_dir("gritter"))


@cli.command()
@click.argument("usernames", nargs=-1)
@click.option("--depth", default=1, type=int, help="Depth of connections to return (default 1)")
def users(usernames, depth):
    """Provide a list of usernames to get the graph for."""
    get_friends(usernames)
    click.echo("Depth %d" % depth)

@cli.command()
@click.argument("file", type=click.File("r"))
def userfile(file):
    """A file containing usernames, separated by newlines."""
    users = [u.strip() for u in file.readlines()]

    for user in users:
        click.echo(user)

@cli.command()
def authenticate():
    if config.has_config(CONF_PATH):
        click.confirm("Authentication details are already set on this machine. Do you wish to overwrite them?",
                      abort=True)

    config.create_config(CONF_PATH)
    click.echo("Please enter your Twitter API credentials")

    consumer_key = click.prompt("Consumer key")
    consumer_secret = click.prompt("Consumer secret")
    access_token = click.prompt("Access token")
    access_secret = click.prompt("Access secret")

    auth_args = {
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret,
        "access_token": access_token,
        "access_secret": access_secret,
    }

    config.set_auth(CONF_PATH, auth_args)


@cli.command()
def show_auth():
    """Don't have this in the finished product!."""

    for k, v in config.get_auth(CONF_PATH).items():
        click.echo("%s: %s" % (k, v))