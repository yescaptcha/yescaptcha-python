from utils import resize_base64_image_from_file
from yescaptcha.task import ImageToTextTask
from yescaptcha.client import Client
from environs import Env

env = Env()
env.read_env()

CLIENT_KEY = env.str('CLIENT_KEY')

client = Client(client_key=CLIENT_KEY)
captcha = 'images/image_to_text1.png'
task  = ImageToTextTask(resize_base64_image_from_file(captcha))
job = client.create_task(task)
print('result', job.get_solution_text())
