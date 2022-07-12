from handler.base import BaseHandler


class ControllerHandler(BaseHandler):

    def handle(self, env, tpl_conf=None):
        class_info = BaseHandler.get_class_info(env, "controller")
        task = env['task']
        imports = BaseHandler.get_imports(env, {
            'domain.dto',
            'domain.query',
            'domain.vo',
            'domain.listVo',
            'service',
        })
        variables = {
            'author': task['author'],
            'datetime': task['datetime'],
            'package': class_info['pkg'],
            'path': class_info['path'],
            'imports': imports,
            'beanDesc': class_info['beanDesc'],
            'beanClassName': class_info['beanClassName'],
            'className': class_info['className'],
            'beanName': class_info['beanName'],
            'reqMapping': task['reqMapping'],
        }
        env[tpl_conf['key']] = variables


