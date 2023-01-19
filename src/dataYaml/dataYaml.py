from yaml import safe_load


class Data:
    def __init__(self, path):
        # Load tokens from config.yml
        with open(path) as f:
            cfg = safe_load(f)

        telegram_tokens = cfg['VK']
        self.__vk_bot_token = telegram_tokens['VK_BOT_TOKEN']

        openai_tokens = cfg['OPEN_AI']
        self.__open_ai_token = openai_tokens['OPEN_AI_TOKEN']

    @property
    def get_open_ai_token(self):
        return self.__open_ai_token

    @property
    def get_vk_token(self):
        return self.__vk_bot_token
