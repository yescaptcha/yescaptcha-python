import time
from yescaptcha.exceptions import YesCaptchaException
from yescaptcha.settings import JOB_CHECK_INTERVAL
from loguru import logger


class Job(object):
    """
    A job used for waiting to finish and get result
    """
    client = None
    task_id = None
    _last_result = None

    def __init__(self, client, data):
        self.client = client
        self.data = data
        self._last_result = data
        self.task_id = data.get('taskId')
        
        # set logger level
        logger.level('DEBUG' if client.debug else 'INFO')

    def __str__(self):
        """
        job to string
        """
        return str(self._last_result)

    def _update(self):
        """
        update job's last result according to API response
        """
        logger.debug('try to get result of task %s' % (self.task_id,))
        self._last_result = self.client.get_task_result(self.task_id)
        logger.debug('task result %s' % (self._last_result))
        
    def check_is_ready(self):
        """
        check task is ready or not
        """
        self._update()
        return self._last_result.get('status') == 'ready'
   
    def get_solution(self):
        """
        return raw response json
        """
        return self._last_result.get('solution')

    def get_solution_objects(self):
        """
        get nest reuslt of objects
        """
        return self._last_result.get('solution', {}).get('objects')
    
    
    def get_solution_token(self):
        """
        get nest reuslt of token
        """
        return self._last_result.get('solution', {}).get('token')

    def get_solution_answers(self):
        """
        get nest result of answers
        """
        return self._last_result.get('solution', {}).get('answers')

    def get_solution_text(self):
        """
        get nest result of text
        """
        return self._last_result.get('solution', {}).get('text')

    def get_solution_recaptcha_response(self):
        """
        get nest result of gRecaptchaResponse
        """
        return self._last_result.get('solution', {}).get('gRecaptchaResponse')

    def join(self, maximum_time=None):
        """
        wait for job to finish, status is ready
        """
        start_time = int(time.time())
        while not self.check_is_ready():
            time.sleep(JOB_CHECK_INTERVAL)
            elapsed_time = int(time.time()) - start_time
            if elapsed_time is not None and elapsed_time > self.client.timeout_join:
                raise YesCaptchaException(
                    None,
                    'JOB_JOIN_TIMEOUT',
                    "The execution time exceeded a maximum time of {} seconds. It takes {} seconds.".format(
                        maximum_time, elapsed_time
                    ),
                )
