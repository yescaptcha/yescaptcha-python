# yescaptcha-python

This is SDK for YesCaptcha.

## Installation

```
pip3 install yescaptcha
```

## Usage

Below are some simple exmaples for Recaptcha, Image2Text:

### NoCaptchaTaskProxyless

```python
from yescaptcha.task import NoCaptchaTaskProxyless
from yescaptcha.client import Client

CLIENT_KEY = <YOUR_CLIENT_KEY>
website_url = 'https://www.google.com/recaptcha/api2/demo'
website_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'

client = Client(client_key=CLIENT_KEY, debug=True)
task  = NoCaptchaTaskProxyless(website_key=website_key, website_url=website_url)
job = client.create_task(task)
print('result', job.get_solution())
```

### ImageToText

```python
from utils import resize_base64_image_from_file # see examples/utils.py
from yescaptcha.task import ImageToTextTask
from yescaptcha.client import Client

CLIENT_KEY =  <YOUR_CLIENT_KEY>
IMAGE_PATH = <IMAGE_PATH>

client = Client(client_key=CLIENT_KEY)
task  = ImageToTextTask(resize_base64_image_from_file(IMAGE_PATH))
job = client.create_task(task)
print('result', job.get_solution_text())
```

Please check [http://yescaptcha.readthedocs.org](http://yescaptcha.readthedocs.org) to get more details.
