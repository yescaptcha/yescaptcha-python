class BaseTask(object):
    type = 'BaseTask'
    website_url = None
    website_key = None

    def __init__(self, *args, **kwargs):
        super(BaseTask, self).__init__(*args, **kwargs)

    def serialize(self):
        return {
            'type': self.type
        }


class BaseTaskProxyless(BaseTask):
    type = 'BaseTaskProxyless'
    website_url = None
    website_key = None

    def __init__(
        self,
        website_url,
        website_key,
        *args,
        **kwargs
    ):
        self.website_url = website_url
        self.website_key = website_key
        super(BaseTaskProxyless, self).__init__(*args, **kwargs)

    def serialize(self):
        return {
            **super().serialize(),
            'websiteURL': self.website_url,
            'websiteKey': self.website_key
        }


class BaseTaskClassification(BaseTask):
    type = 'BaseTaskClassification'
    website_url = None
    website_key = None

    def __init__(self, *args, **kwargs):
        super(BaseTaskProxyless, self).__init__(*args, **kwargs)

    def serialize(self):
        return {
            **super().serialize()
        }
