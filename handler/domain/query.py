from handler.base import BaseHandler


class QueryHandler(BaseHandler):

    def handle(self, env, tpl_conf=None):
        class_info = BaseHandler.get_class_info(env, "domain.query")
        task = env['task']
        entity_info = env['domain.entity']
        variables = {
            'author': task['author'],
            'datetime': task['datetime'],
            'package': class_info['pkg'],
            'path': class_info['path'] + "/" + class_info['className'] + ".java",
            'imports': [*entity_info['imports']],
            'beanDesc': class_info['beanDesc'],
            'beanClassName': class_info['beanClassName'],
            'className': class_info['className'],
        }
        env[tpl_conf['key']] = variables


