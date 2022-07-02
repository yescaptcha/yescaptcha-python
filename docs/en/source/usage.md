# Usage

This document describes the basic usage of YesCaptcha SDK.

## Preconditions

Before using, please go to [https://yescaptcha.com/](https://yescaptcha.com/) official website to register an account, and obtain the account key ClientKey, as shown in the figure:

![](https://qiniu.cuiqingcai.com/d2h50.png)

## All task types

YesCaptcha provides a variety of verification code recognition services, each service corresponds to a task, all task types refer to [official document](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/pages/164286).

This Python SDK provides the encapsulation of various tasks, making it easier for developers to interface with YesCaptcha services, instead of using libraries such as requests for development from 0.

## Basic usage

Here we take the GoogleCaptchaV2 verification code as an example, the sample address is [https://www.google.com/recaptcha/api2/demo](https://www.google.com/recaptcha/api2/demo), the specific For usage instructions, see [NoCaptchaTaskProxyless : reCaptcha V2 protocol interface](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/pages/229796/NoCaptchaTaskProxyless+reCaptcha+V2).

The sample code is as follows:

```python
from yescaptcha.task import NoCaptchaTaskProxyless
from yescaptcha.client import Client

CLIENT_KEY = <YOUR_CLIENT_KEY>
website_url = 'https://www.google.com/recaptcha/api2/demo'
website_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'

client = Client(client_key=CLIENT_KEY, debug=True)
task = NoCaptchaTaskProxyless(website_key=website_key, website_url=website_url)
job = client.create_task(task)
print('result', job.get_solution())
```

First, we need to introduce the `Client` class to initialize an operation object of the YesCaptcha service. At this time, we need to pass in the `client_key`, which is the account key ClientKey described above. In addition, we can pass in the `debug` parameter, Set the debug mode so that more debug information can be output during operation.

In addition, the `NoCaptchaTaskProxyless` class needs to be introduced. The name of the class is equivalent to the type mentioned in the document, as shown in the figure:

![](https://qiniu.cuiqingcai.com/67cfb.png)

In addition, reading the documentation we can find that this category of Task requires two parameters `websiteURL` and `websiteKey`, as shown:

![](https://qiniu.cuiqingcai.com/ldq5d.png)

Therefore, when initializing the `NoCaptchaTaskProxyless` class, we need to pass in the corresponding two parameters, the parameters need to be converted to [Snake nomenclature](https://en.wikipedia.org/wiki/Snake_case), the difference between word and word need to be separated by an underscore, that is, converted to `website_url` and `website_key`.

Next, we can use the `create_task` method of the client object to create a task whose return value is named `job`, and finally, we call the `get_solution` method to get the corresponding result.

The results are as follows:

```
2022-07-02 14:30:38.124 | DEBUG | yescaptcha.client:create_task:61 - construct result {'clientKey': '50a07aa563cf4688270a6a968086c80b4ef23baf78', 'task': {'type': 'NoCaptchaTaskProxyless', 'websiteURL': ' https://www.google.com/recaptcha/api2/demo', 'websiteKey': '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'}}
2022-07-02 14:30:39.435 | DEBUG | yescaptcha.job:_update:34 - try to get result of task 7cf17d74-f9d0-11ec-b008-ae8dd81878b9
2022-07-02 14:30:40.527 | DEBUG | yescaptcha.job:_update:36 - task result {'errorId': 0, 'errorCode': '', 'errorDescription': None, 'status': 'processing' , 'solution': None}
2022-07-02 14:30:41.528 | DEBUG | yescaptcha.job:_update:34 - try to get result of task 7cf17d74-f9d0-11ec-b008-ae8dd81878b9

2022-07-02 14:31:36.359 | DEBUG | yescaptcha.job:_update:36 - task result {'errorId': 0, 'errorCode': None, 'errorDescription': None, 'solution': {'gRecaptchaResponse' : '03AGdBq27gCf7UkBFO7Nsl5OqK6kiL911UYPYSyrbbYh9jQfvzp1qrsehq62UKgJ...2SNtTnWFJJ8TkXJs4AHIceSmE-JR8BSs_m--Qf5MtySwRPZnYewbKBOSOSHBCQarMPBFUj-dscgbI8rlfIpbG0hbgrF-MDJ3aHI6ZdgrahHtlRpB6PWDdWCXX1S1w'}
result 03AGdBq27gCf7UkBFO7Nsl5OqK6kiL911UYPYSyrbbYh9jQfvzp1qrsehq62UKgJB9s9x5bKk2pEg392DYy3HVTo1KbdBywk7UQK3RDcM1A4bGPByrCO0xlgMyX4GzDqvx...HBCQarMPBFUj-dscgbI8rlfIpbG0hbgrF-MDJ3aHI6ZdgrahHtlRpB6PWDdWCXX1S1w
```

## other tasks

For other tasks, the usage method is similar, we only need to refer to the document and introduce the corresponding Task object, for example, for [ReCaptchaV2Classification: reCaptcha V2 Image Recognition](https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA /pages/18055169/ReCaptchaV2Classification+reCaptcha+V2), all we need to introduce is:

```python
from yescaptcha.task import ReCaptchaV2Classification
```

When creating a Task, also refer to the parameter description of the documentation:

```
task = ReCaptchaV2Classification(image='<image payload>', question='<question>')
```

The image here is the Base64 encoded image, do not include "data:image/\*\*\*;base64,", the question parameter is the question ID, please check the table, start with /m/.

The final call is the same:

```python
job = client.create_task(task)
print('result', job.get_solution())
```

## async tasks

For some tasks, the recognition result of the verification code will not be returned immediately, but a processing process is required, such as tasks such as NoCaptchaTaskProxyless and RecaptchaV3TaskProxyless. For some image recognition tasks, the recognition process will be synchronous, such as ReCaptchaV2Classification, HCaptchaClassification and other tasks.

In order to facilitate the development of developers, for asynchronous tasks, this SDK does automatic waiting processing, that is, it will automatically poll and wait until the recognition result is returned. The reason is that when initializing the Client object, there is a default parameter `auto_join` that is True .

Therefore, if you do not want to enable automatic waiting, you can handle this process manually. In this case, you need to set `auto_join` to False when initializing the Client object, and then call the `join` method of the `job` object when appropriate. as follows:

```python
from yescaptcha.task import NoCaptchaTaskProxyless
from yescaptcha.client import Client

CLIENT_KEY = <YOUR_CLIENT_KEY>
website_url = 'https://www.google.com/recaptcha/api2/demo'
website_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'

client = Client(client_key=CLIENT_KEY, auto_join=False)
task = NoCaptchaTaskProxyless(website_key=website_key, website_url=website_url)
job = client.create_task(task)
job.join()
print('result', job.get_solution())
```

## non-task interface

In addition, this SDK also provides some interfaces that are not identified by verification codes, such as obtaining account information, obtaining developer ID, etc., which are listed as follows:

- get_balance: Get account balance
- get_soft_id: Get the developer ID

For example, for get_soft_id, the usage is as follows:

```python
from yescaptcha.client import Client

CLIENT_KEY = <YOUR_CLIENT_KEY>
client = Client(client_key=CLIENT_KEY)
soft_id = client.get_soft_id()
print('result', soft_id)
```

## Node settings

There are two service nodes behind the YesCaptcha service, one is an international node (default), but there may be problems accessing it in China, so for users in China, you can set up a dedicated Chinese node.

When setting, you only need to change the initialization parameter `region` of the Client object:

```python
from yescaptcha.client import Client, Region

CLIENT_KEY = <YOUR_CLIENT_KEY>
client = Client(client_key=CLIENT_KEY, region=Region.CHINA)
```
