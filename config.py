from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 24185140
    API_HASH = "a4ffcafc1a4b57f9993b04321babacd5"
    # the name to display in your alive message
    ALIVE_NAME = "UserBot"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://dvatlice:xOO8WX4ut2P3t2wufI1hWXdlFktA0wyy@flora.db.elephantsql.com/dvatlice"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOI4BuyHK5qs-ObdHA5w76_BhuIMOgZ_JTjSb9OVdfLjl5W2v_zzvf76SBTk02W8dPJvV_K0crt2KIz8xB_uo_ZQOXRwe9f05uAz8qAOaTaKIXNAwafRuF3qpph7Ysapyu4psULKVd7-za8Bz7yWuoEFe774Azyz4ukjYs7QPDJHRRl0cwju20Cgh-CwaDcnfV0TrPmVdWLAmTyNxEyOVpgBcA-uKJKusLhLFTEfSHwXoj-KQ9OdFAyTbKghP_arYPc6m63TsntIgmQDb3BrD1d7CB8H_m207te-VhJQeCGARwT1NZ_Xxm29l3DjtXRRusKr23cN4uNHf29G1UYO3Kc7M_uo="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6710469512:AAFBH4mXqPp7hcZt9Z8DtldUm1hDcI-ef78"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002143037796
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
