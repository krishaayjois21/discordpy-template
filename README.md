# Discord Bot Template (Python)

<!--Add Shields Here
Python 3
Code Style Black
Deploy to Heroku

-->

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