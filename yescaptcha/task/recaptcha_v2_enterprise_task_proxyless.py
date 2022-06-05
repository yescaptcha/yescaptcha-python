from yescaptcha.task.base import BaseTaskProxyless


class RecaptchaV2EnterpriseTaskProxyless(BaseTaskProxyless):
    type = 'RecaptchaV2EnterpriseTaskProxyless'

    def __init__(self, website_url, website_key, enterprise_payload, *args, **kwargs):
        self.enterprise_payload = enterprise_payload
        super(RecaptchaV2EnterpriseTaskProxyless, self).__init__(
            website_url, website_key, *args, **kwargs)

    def serialize(self):
        return {
            **super().serialize(),
            'enterprisePayload': self.enterprise_payload,
        }
