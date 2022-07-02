from yescaptcha.client import Client, Region
from environs import Env

env = Env()
env.read_env()

CLIENT_KEY = env.str('CLIENT_KEY')

client = Client(client_key=CLIENT_KEY, region=Region.CHINA)
soft_id = client.get_soft_id()
print('result', soft_id)
