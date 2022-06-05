from yescaptcha.task.base import BaseTaskClassification


class ReCaptchaV2Classification(BaseTaskClassification):
    type = 'ReCaptchaV2Classification'

    def __init__(self, image, question, *args, **kwargs):
        self.image = image
        self.question = question
        super(ReCaptchaV2Classification, self).__init__(
            *args, **kwargs)

    def serialize(self):
        return {
            **super().serialize(),
            'image': self.image,
            'question': self.question
        }
