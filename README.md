# Discord Bot Template (Python)

[![HEROKUDEPLOY](https://img.shields.io/badge/%E2%86%91_Deploy_to-Heroku-7056bf.svg?style=for-the-badge)](https://heroku.com/deploy?template=https://github.com/krishaayjois21/discordpy-template)
[![PYTHON](https://img.shields.io/static/v1?label=PYTHON&message=3&color=1F4360&style=for-the-badge&logo=python)](https://python.org)
[![CODESTYLE](https://img.shields.io/static/v1?label=CODESTYLE&message=BLACK&color=000000&style=for-the-badge)](https://python.org)
[![LICENSE](https://img.shields.io/static/v1?style=for-the-badge&label=LICENSE&message=MIT)](https://github.com/krishaayjois21/discordpy-template/blob/main/LICENSE)
[![STARS](https://img.shields.io/github/stars/krishaayjois21/discordpy-template?style=for-the-badge)](https://github.com/krishaayjois21/discordpy-template/stargazers)
[![ISSUES](https://img.shields.io/github/issues/krishaayjois21/discordpy-template?style=for-the-badge)](https://github.com/krishaayjois21/discordpy-template/issues)
[![FORKS](https://img.shields.io/github/forks/krishaayjois21/discordpy-template?style=for-the-badge)]()

<HR>

### A template for creating discord bots using the discordpy library with support for cogs.

## Features:
- Supports Cogs
- Docker Support
- Heroku Support

## Requirements:
- [Git](https://git-scm.com/)
- [Python](https://python.org/)
- [Docker (Optional)](https://docker.com)

## Setup:

 - Download the template: `git clone https://github.com/krishaayjois21/discordpy-template.git <project-name>` 
 
    _Replace `<project-name>` with the name of the folder you want_

 - Install dependencies: `pip install -r requirements.txt`

## Config:
  - Replace `<token>` in `config/config.json` with the token from the [Discord Developer Portal](https://discord.com/developers/applications)

  - Replace `<prefix>` in `config/config.json` with the prefix for your bot

  - Delete the `.git` folder so you can use your own VCS

## Run the Bot

  - To run the bot:
    - Windows: `python main.py`
    - Linux/MacOS: `python main.py`

  - Run with Docker:
    - `docker-compose up --build`

## Adding extensions/cogs:
  - Add the python file for your extension/cog to the `extensions` folder. It can also be inside a subfolder to organise code as well.

  - Edit the `config/config.json` file. The list of extensions will intially look like this
  ```json
  {
      "extensions": [
        "extensions.ready"
    ]
  }
  ```
 
 - Adding an extension called `foo.py` , the config would look like this
  ```json
  {
      "extensions": [
        "extensions.ready",
        "extensions.foo"
    ]
  }
  ```

 - Adding an extension called `bar.py` inside a subfolder `foobar` , the config would look like this
  ```json
  {
      "extensions": [
        "extensions.ready",
        "extensions.foobar.bar"
    ]
  }
  ```

  - Restart the bot and your cog is now loaded

<hr>

_Some commonly used extensions can be found on [this respository](https://github.com/krishaayjois21/discord-cogs). It has documentation on how to add each of the cogs_
