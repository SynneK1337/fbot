import fbchat
import configparser

class Config():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        self.login = config['credentials']['nickname']
        self.password = config['credentials']['password']
        self.conversation_id = config['settings']['conversation_id']

