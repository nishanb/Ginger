from tokenize import String
import telegram
import logging

class Notifer:
    def __init__(self,token,chat_id):
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id
        logging.info(self.bot.get_me()['first_name'] + "is Started")

    def notify(self,message):
        try:
            self.bot.send_message(self.chat_id, message)
        except:
            pass
    
    def getLastChatId(self) -> String:
        try:
            return self.bot.get_updates()[-1].message.chat_id
        except:
            return 0