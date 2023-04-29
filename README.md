# Telessist

Telessist allows you to contact GPT3 directly from Telegram and not only that. Telessist also allows you to save your own personal data and later search and retrieve it using GPT3 to generate a response. In the examples folder, you can see several examples of how to use this bot so you don't have to remember anything ever again.


## Supported Features

* **No-Command**: This is the default mode. The bot will respond to any message you send it through the GPT3 regular completion API.

* **Commands**: This mode is activated by sending the bot a message starting with the command character. The default command character is /. 
    * Currently supported commands:
        * /h: Show a help message that lists all the commands
        * /s <message>: Save the message to the database
        * /q <question>: Ask a question about the database and get a response from GPT3.
        * /f <message>: Find related messages in the database.
        * /w: Get weather forecast from [IMS](https://ims.gov.il/he).
        * Send audio file for transcription (Multi-languages).
        * d/ <message>: Draw using Dall-E.
        * /c: Get OpenAI estimated costs
            * Today.
            * Yesterday.
            * Last 7 days.
            * Last 30 days.

## Components and Frameworks used in Telessist
* [Loguru](https://pypi.org/project/loguru/) For logging.
* [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) For the Bot.
* [weatheril](https://pypi.org/project/weatheril/) For Weather forecst.
* [OpenAI](https://pypi.org/project/openai/) OpenAI client for ChatGPT, Dall-E, and Whisper.



## How to use Telessist
Telessist can be installed and run as a system service or a Docker container.

1. Create new telegram bot and get the token
    Open [Telegram messenger](https://web.telegram.org/), sign in to your account or create a new one.

    Enter @Botfather in the search tab and choose this bot (Official Telegram bots have a blue checkmark beside their name.)

    [![@Botfather](https://github.com/t0mer/voicy/blob/main/screenshots/scr1-min.png?raw=true "@Botfather")](https://github.com/t0mer/voicy/blob/main/screenshots/scr1-min.png?raw=true "@Botfather")

    Click “Start” to activate BotFather bot.

    [![@start](https://github.com/t0mer/voicy/blob/main/screenshots/scr2-min.png?raw=true "@start")](https://github.com/t0mer/voicy/blob/main/screenshots/scr1-min.png?raw=true "@start")

    In response, you receive a list of commands to manage bots.
    Choose or type the /newbot command and send it.

    [![@newbot](https://github.com/t0mer/voicy/blob/main/screenshots/scr3-min.png?raw=true "@newbot")](https://github.com/t0mer/voicy/blob/main/screenshots/scr3-min.png?raw=true "@newbot")


    Choose a name for your bot — your subscribers will see it in the conversation. And choose a username for your bot — the bot can be found by its username in searches. The username must be unique and end with the word “bot.”

    [![@username](https://github.com/t0mer/voicy/blob/main/screenshots/scr4-min.png?raw=true "@username")](https://github.com/t0mer/voicy/blob/main/screenshots/scr4-min.png?raw=true "@username")


    After you choose a suitable name for your bot — the bot is created. You will receive a message with a link to your bot t.me/<bot_username>, recommendations to set up a profile picture, description, and a list of commands to manage your new bot.

    [![@bot_username](https://github.com/t0mer/voicy/blob/main/screenshots/scr5-min.png?raw=true "@bot_username")](https://github.com/t0mer/voicy/blob/main/screenshots/scr5-min.png?raw=true "@bot_username")






2. Set the following environment variables:
    * BOT_TOKEN=#Telegram bot Token generated in the previous step.
    * OPENAI_KEY= #OpenAPI API key
    * ALLOWED_IDS= #List of telegram id's allowed to communicate with the bot, comma-separated values.
3. If you want to run Telessist as a ***docker container***, copy the following code into your docker-compose.yaml:
    ```yaml
    version: "3.6"
    services:
    Telessist:
        image: techblog/Telessist
        container_name: Telessist
        restart: always
        ports:
        - 80:7020
        environment:
        - BOT_TOKEN= #Telegram bot Token.
        - OPENAI_KEY= #OpenAPI API key
        - ALLOWED_IDS= #List of telegram id's allowed to communicate with the bot, comma-separated values.
        volumes:
        - ./Telessist:/app/data
    ```
    **Make sure to set all the environment variables before running the *"docker-compose up -d"* command.
    
    
4. If you want to run Telessist as a systemd service, clone the repository using the following command:
    ```bash
    git clone https://github.com/t0mer/Telessist
    ```
    enter the *Telessist* folder and install the dipendencies:
    ```bash
    pip3 install -r requirements.txt
    ```

    Next, create a file names **"Telessist.service"** under **/etc/systemd/system"** and paste the following content:

    ```bash
    [Unit]
    Description=GPT Telegram 
    After=network-online.target
    Wants=network-online.target systemd-networkd-wait-online.service
    StartLimitIntervalSec=5
    StartLimitBurst=5

    [Service]
    EnvironmentFile=/etc/environment
    KillSignal=SIGINT
    WorkingDirectory=/opt/dev/Telessist/app/
    Type=simple
    User=root
    ExecStart=/usr/bin/python3 /opt/dev/Telessist/app/app.py
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```
    ***Make sure to adjust the path for "WorkingDirectory" and "ExecStart" accordingly to the path of the Telessist location***

    Next, run the following command to enable and start the service:
    ```bash
    systemctl enable assist. service
    systemctl start Telessist.service
    ```
    To check the status of the service, run the following command:
    ```bash
    systemctl status Telessist.servies
    ```


# Acknowledgments
Huge credit and a special thanks to [@mangate](https://github.com/mangate) for creating [SelfGPT](https://github.com/mangate/SelfGPT) which my code 
is based on.