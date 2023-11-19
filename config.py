from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 11903991
    API_HASH = "7edc6552882ec6ce04c3386be7f97a1d"
    # the name to display in your alive message
    ALIVE_NAME = "𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙘𝙚"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://dvatlice:xOO8WX4ut2P3t2wufI1hWXdlFktA0wyy@flora.db.elephantsql.com/dvatlice"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOI0Bu8UYa1InaUsdQm7MWQ8JHBnX_CVt_Bea-plpUSyUJ9s_-QoL66frycX18XvuMvk0ooKQoat-toEk4nhUFdGm16cVtvTXAQZrCv1asqwqhqetl5ybwizm-MGcB8lPZXM4SvA7-5IAROhQnQBRTDhxNlZ5VHrdV0M5_-OAfqbjOaJvZ-RQKGbTDF4R3I3UR6ZpXYB4ODOnQYxG7nAiR8x1yW_-eY1gTD9yZhBJshAjdhC3snjKe_FDdYgkHXNFO6Sz8wu2DG_JBRI4fdYVVheSLnD8Csz_kjoqkmz3F6vaLLZBDxuTZSzrTnQVF8ulALIAMc29Vb6K4vCjN1purmLEqTQ="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6710469512:AAFBH4mXqPp7hcZt9Z8DtldUm1hDcI-ef78"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002043549904
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
    CHROME_BIN = "/usr/bin/chromium-browser"
    CHROME_DRIVER = "/usr/bin/chromedriver"
