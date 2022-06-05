from yescaptcha.task.base import BaseTaskClassification


class HCaptchaClassification(BaseTaskClassification):
    type = 'HCaptchaClassification'

    def __init__(self, queries, question, coordinate, *args, **kwargs):
        self.queries = queries
        self.question = question
        self.coordinate = coordinate
        super(HCaptchaClassification, self).__init__(
            *args, **kwargs)

    def serialize(self):
        base = super().serialize()
        return {
            **base,
            'queries': self.queries,
            'question': self.question,
            'coordinate': self.coordinate
        }
