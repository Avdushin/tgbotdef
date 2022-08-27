<div align="center">
    <a href="https://t.me/<BOTNAME>" target="_blank">
        <img src="https://www.messengerpeople.com/wp-content/uploads/2022/04/telegram-bots-mp-blog-title-01.png" 
    />
    </a>
</div>

<h1 align="center">Default sources for Telegram bot with Aiogram!</h1>

#### Robin is always ready to keep you company and play with you!

### INSTALLATION

```
git clone https://github.com/Avdushin/tgbotdef
cd tgbotdef
make install
```

#### OR YOU CAN EDIT `.env` file:

```
BOT_TOKEN=your:token
```

You can get a **BOT TOKEN** from [@BotFather](https://t.me/BotFather)

#### To start bot please type `make` or `make start`

### DEPENDENCIES

```
aiogram==2.21
async-timeout==4.0.2
emoji==2.0.0
python-dotenv==0.20.0
```

### DEV TOOLS

#### If you upgraded bot then you should to build his new version. I creted some tools for this!

[DEV TOOLS](https://github.com/Avdushin/ROBIN/blob/main/Makefile)

### Windows build example
Use `make example-win` to build your own modified bot at the "examples" folder.

### Unix/Linix/Mac OS build example
Use `make example` to build your own modified bot at the "examples" folder. 

```Makefile
# --- dev tools ---
# Make "examples" folder (Unix)
example:
	cp -rv `ls -A | grep -vE ".git|.env|.gitignore|.vscode|README.md|__pycache__|examples|test"` examples
# Make "examples" folder (Windows)
example-win:
	robocopy "." "examples" /xf ".gitignore" ".env" "README.md" /xd "assets" "test" ".vscode" "__pycache__" "examples" ".git" /s
	echo -e "examples" folder was builded!
```

<p align="center">2022 © <a href="https://github.com/Avdushin" target="_blank">AVDUSHIN</a></p>