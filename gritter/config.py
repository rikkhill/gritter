import configparser
import os


def has_config(path):
    """Returns true if gritter config file exists."""
    return True if os.path.isfile(path) else False


def create_config(path):
    """Create the config file iff it doesn't exist."""
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    if not has_config(path):
        open(path, 'a').close()


def set_auth(path, args):
    """Sets auth args in config."""
    config = configparser.ConfigParser()
    config.read(path)
    # clobber old auth values
    config["auth"] = {}
    for k, v in args.items():
        config["auth"][k] = v

    with open(path, 'w') as configfile:
        config.write(configfile)


def get_auth(path):
    """Gets dict of auth args from config."""
    config = configparser.ConfigParser()
    config.read(path)
    return config["auth"]