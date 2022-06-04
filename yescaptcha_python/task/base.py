class BaseTask(object):
    type = 'BaseTask'
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
        self.websiteKey = website_key
        super(BaseTask, self).__init__(*args, **kwargs)
