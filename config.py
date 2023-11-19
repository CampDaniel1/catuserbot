from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 11903991
    API_HASH = "7edc6552882ec6ce04c3386be7f97a1d"
    # the name to display in your alive message
    ALIVE_NAME = "UserBot"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://dvatlice:xOO8WX4ut2P3t2wufI1hWXdlFktA0wyy@flora.db.elephantsql.com/dvatlice"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOJoBu35FqixBxRhg6Ii-geO2eqDddzgERWAp_U6GAXojZoUXIMmQZp-i_TfR_ZoaZcpnOs3JJ0_Ir1YJtgoAwMsgMwNlCu4UXnTGzkQTpO2KtnxaWjtDUBPLe36ikCrSBEox6JoE2j3kP6BqV7fpn49kqe3UsXu3k79Lwxqzm-HN3vnh1I0gKm2oMVPl_mrG_cFHkAH6lxqZMtEPmOC-HwqecttZAuPP8jTnR0R3n2IE_NZDzkN0Wn0tOQeissfY8UuiXuEjy31rWvSg3qoSrzQJoLpZip4B6IJqUoX6L94pUmBnPgQ7f5CcO0cSrTF_EOET-0vcqe3IrxTlkW9TG_cu8HE="
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
