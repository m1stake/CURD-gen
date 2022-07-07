import config


class BaseHandler:

    def __init__(self):
        self.config = config

    def handle(self, env, tpl_conf=None):
        pass

    @staticmethod
    def get_path(base_path, pkg, conf):
        if 'basePath' in conf and conf['basePath']:
            base_path = conf['basePath']
        pkg_path = pkg.replace('.', '/')
        return base_path + '/src/main/java/' + pkg_path

    @staticmethod
    def get_package(base_pkg, conf):
        if 'basePackage' in conf and conf['basePackage']:
            base_pkg = conf['basePackage']
        if 'package' in conf and conf['package']:
            return base_pkg + "." + conf['package']
        else:
            return base_pkg

    @staticmethod
    def get_class_info(env, conf_key):
        project_conf = config.get_project_config()
        entity_conf = _get_from_project_conf(project_conf, conf_key)
        pkg = BaseHandler.get_package(project_conf['basePackage'], entity_conf)
        path = BaseHandler.get_path(project_conf['basePath'], pkg, entity_conf)

        table_info = env['tableInfo']
        bean_class_name = _bean_name(env, table_info['TABLE_NAME'])
        bean_name = bean_class_name[0].lower() + bean_class_name[1:]
        class_name = bean_class_name + entity_conf['suffix']
        return {
            "pkg": pkg,
            "path": path,
            "beanClassName": bean_class_name,
            "beanName": bean_name,
            "className": class_name,
            "beanDesc": table_info['TABLE_COMMENT']
        }

    @staticmethod
    def get_imports(env, tpl_conf_keys):
        imports = set()
        for key in tpl_conf_keys:
            variables = env[key]
            impt = variables['package'] + '.' + variables['className']
            imports.add(impt)
        return imports


def _bean_name(env, table_name):
    if 'beanName' in env['task']:
        return env['task']['beanName']
    else:
        pass
    # back to default
    return _snake_to_camel_case(table_name, True)


def _snake_to_camel_case(snake_words: str, first_upper: bool):
    words = snake_words.split('_')
    if first_upper:
        return ''.join(word.title() for word in words)
    else:
        first_word = words[0]
        return first_word + ''.join(word.title() for word in words[1:])


def _get_from_project_conf(project_conf, conf_key: str, ):
    key_seq = conf_key.split(".")
    conf = project_conf
    for key_seg in key_seq:
        conf = conf[key_seg]
    return conf
