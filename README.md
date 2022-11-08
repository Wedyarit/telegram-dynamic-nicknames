# telegram-dynamic-nicknames

Script to generate dynamic Telegram nicknames

# Getting started

## Environment file

First of all you have to gain API_ID and API_HASH api_hash from [Telegram](https://my.telegram.org), under API Development.

Create a environment file based on sample
```bash
$ cp .env.sample .env
```

Configure .env file by pasting API_ID and API_HASH.
```bash
# ---------------
# Telegram config
# ---------------
API_ID=PASTE_YOUR_APP_ID_HERE
API_HASH=PASTE_YOUR_APP_HASH_HERE
```


## Configuration file 
All nickname's configurations are stored in [config.py](./src/config.py).
```python
# ---------------
# Nickname config
# ---------------

# Time interval in seconds between changing nicknames (default: 120)
change_interval = 60

# List of nicknames that will change, where 'emoji_symbol' (see below) is a random emoji
nicknames = [
    '{emoji} H {emoji} E {emoji} Y {emoji}',
    '{emoji} TEST {emoji}',
    '{emoji} {emoji} {emoji}',
    '{emoji} I love emojis {emoji}'
]

# Are emojis enabled (default: True)
emojis_enabled = True

# Emoji replacement symbol (default: '{emoji}')
emoji_symbol = '{emoji}'

```

## Launch the script

Make sure python [poetry](https://python-poetry.org/) is installed on your machine.

To install dependencies:
```bash
$ poetry install
```

To launch the script:
```bash
$ poetry run python -m src.app
```

# About the project 

## Privacy and security 
It is important to ensure that the telegram-dynamic-nickname.session file is restricted from third parties. This file contains system data and anyone who has access to it will have access to your Telegram account.

## Telegram API limitations
It is important not to set a short interval between nickname changes for two reasons:
1. Telegram API has its own limits on the number of requests per share of time
2. Telegram will not be able to update the nickname on the client with the desired speed and the result will be invisible.

## Emoji parser
In order to achieve the result with the largest number of random emojis, it was decided to use the unicode.org resource in order to obtain the latest versions of emojis.

# Requirements

Python 3.8+.

## Dependencies

Dependencies are defined in [`pyproject.toml`](./pyproject.toml) and specific versions are locked
into [`poetry.lock`](./poetry.lock). This allows for exact reproducible environments across
all machines that use the project, both during development and in production.

To install all dependencies into an isolated virtual environment:

> Append `--sync` to uninstall dependencies that are no longer in use from the virtual environment.

```bash
$ poetry install
```

To [activate](https://python-poetry.org/docs/basic-usage#activating-the-virtual-environment) the
virtual environment that is automatically created by Poetry:

```bash
$ poetry shell
```

To deactivate the environment:

```bash
(fact) $ exit
```

To upgrade all dependencies to their latest versions:

```bash
$ poetry update
```

# Licensing

Licensing for the project is defined in:

- [`LICENSE.txt`](./LICENSE.txt)
- [`pyproject.toml`](./pyproject.toml)

This project uses a common permissive license, the MIT license.

# Miscellaneous

## Shebang Line

The proper [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line for Python scripts is:

```py
#!/usr/bin/env python3
```

## Installing Newer Python on Ubuntu

Ubuntu releases come with a default `python3` executable. This is frozen for the life of the OS
and only receives security and bug fixes. To install a newer version of Python globally,
consider the [deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa).

```shell
sudo add-apt-repository ppa:deadsnakes
sudo apt update
sudo apt install python3.10
```

<hr>
Made by Wedyarit
