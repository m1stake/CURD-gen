from jinja2 import Environment, FileSystemLoader
import config


def get_env():
    task_conf = config.get_task_config()
    if 'tpl' in task_conf and 'basePath' in task_conf['tpl']:
        tpl_base = task_conf['tpl']['basePath']
    else:
        tpl_base = './tpl'
    return Environment(loader=FileSystemLoader(tpl_base))


_env = get_env()


def render(variables, tpl):
    bean_tpl = _env.get_template(tpl)
    return bean_tpl.render(**variables)



