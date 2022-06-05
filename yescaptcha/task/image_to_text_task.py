from yescaptcha.task.base import BaseTask


class ImageToTextTask(BaseTask):
    type = 'ImageToTextTask'

    def __init__(self, body):
        self.body = body

    def serialize(self):
        return {
            **super().serialize(),
            'body': self.body,
        }