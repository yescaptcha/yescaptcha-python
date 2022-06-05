from yescaptcha.task.base import BaseTaskProxyless


class RecaptchaV3TaskProxyless(BaseTaskProxyless):
    type = 'RecaptchaV3TaskProxyless'

    def __init__(self, website_url, website_key, page_action, min_score=0.3, *args, **kwargs):
        self.page_action = page_action
        self.min_score = min_score
        super(RecaptchaV3TaskProxyless, self).__init__(
            website_url, website_key, *args, **kwargs)

    def serialize(self):
        return {
            **super().serialize(),
            'pageAction': self.page_action,
            'minScore': self.min_score
        }
