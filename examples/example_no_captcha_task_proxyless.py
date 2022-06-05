from yescaptcha.task import NoCaptchaTaskProxyless
from yescaptcha.client import Client
from environs import Env

env = Env()
env.read_env()

CLIENT_KEY = env.str('CLIENT_KEY')

website_url = 'https://www.google.com/recaptcha/api2/demo'
website_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'

client = Client(client_key=CLIENT_KEY, debug=True)
task  = NoCaptchaTaskProxyless(website_key=website_key, website_url=website_url)
job = client.create_task(task)
print('result', job.get_solution())
print('result', job.get_solution_recaptcha_response())
