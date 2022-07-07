from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('./tpl'))


def render(variables, tpl):
    bean_tpl = env.get_template(tpl)
    return bean_tpl.render(**variables)



