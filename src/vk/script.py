import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from dataYaml import Data
import random
import openai
import logging

logging.basicConfig(level=logging.ERROR)

config = Data('config.yml')

bot = vk_api.VkApi(token=config.get_vk_token)
bot_api = bot.get_api()
api_key = config.get_open_ai_token


def run():
    while True:
        longpoll = VkBotLongPoll(bot, 218320896)
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.message.text.startswith('!') and event.chat_id == 3:
                        global api_key
                        openai.api_key = api_key

                        completion = openai.Completion.create(model="text-davinci-003",
                                                              prompt=event.message.text[1::],
                                                              temperature=0.7,
                                                              max_tokens=1000,
                                                              top_p=1.0,
                                                              frequency_penalty=0,
                                                              presence_penalty=0.0)

                        bot_api.messages.send(
                            random_id=random.getrandbits(32),
                            peer_id=event.obj.peer_id,
                            chat_id=event.chat_id,
                            message=completion.choices[0].text,
                        )
        except Exception as ex:
            logging.error(ex)



if __name__ == '__main__':
    run()