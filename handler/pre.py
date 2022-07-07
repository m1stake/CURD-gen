from handler.base import BaseHandler
from datetime import datetime


class PreHandler(BaseHandler):

    def handle(self, env, tpl_conf=None):
        task_conf = self.config.get_task_config()
        env['task'] = {**task_conf}
        env['task']['datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return None
