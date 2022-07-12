from handler.base import BaseHandler


class MapperHandler(BaseHandler):

    def handle(self, env, tpl_conf=None):
        class_info = BaseHandler.get_class_info(env, "mapper")
        task = env['task']
        imports = BaseHandler.get_imports(env, {'domain.entity'})
        variables = {
            'author': task['author'],
            'datetime': task['datetime'],
            'package': class_info['pkg'],
            'path': class_info['path'],
            'imports': imports,
            'beanDesc': class_info['beanDesc'],
            'beanClassName': class_info['beanClassName'],
            'className': class_info['className'],
        }
        env[tpl_conf['key']] = variables


