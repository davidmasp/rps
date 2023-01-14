# :robot: Rock Paper Scissors

This is a discord bot to play Rock Paper Scissors with.

## :hammer: Build

To build you need a python3 installation and make. Simply run:

```
make all
```

This command will install the required dependencies and launch the bot.

### from scratch

To launch in an Alpine instance you will need to install:

```
apk add git
apk add py3-pip
apk add make
```

Then download the code using git, udate the `.env` file and execute `make all`.

## :heavy_check_mark: Todo

- See where to host (in pythonanywhere is not ok for free accounts)
- Make the logging server specific (?)

See this -> [URL](https://discord.com/api/oauth2/authorize?client_id=1063902147323904142&permissions=3136&scope=bot)
