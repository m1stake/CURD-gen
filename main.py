from handler.pre import PreHandler
from handler.table_info import TableInfoHandler
import config
import importlib
import template_render
from pathlib import Path


def write_to_console(tpl, variables):
    class_name = variables['className']
    print(class_name + '.java')
    view = template_render.render(variables, tpl)
    print(view)


def write_to_out(tpl, variables):
    class_name = variables['className']
    view = template_render.render(variables, tpl)
    with open('./out/' + class_name + '.java', 'w', encoding='utf8') as f:
        f.write(view)


def write_to_real_path(tpl, variables, mkdir=True, overwrite='NO'):
    path = variables['path']
    if mkdir:
        p = Path(path)
        p.mkdir(parents=True, exist_ok=True)

    class_name = variables['className']

    file_path = path + "/" + class_name + '.java'
    file_exits = Path(file_path).is_file()
    if file_exits:
        if overwrite == 'NO':
            raise Exception('文件已经存在，不能覆盖，' + file_path)
        elif overwrite == 'SKIP':
            print('文件已经存在，%s，跳过' % file_path)
            return

    view = template_render.render(variables, tpl)
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(view)


def render(render_func, **kwargs):
    tpl_conf = config.get_tpl_config()

    env = {}
    PreHandler().handle(env)
    TableInfoHandler().handle(env)

    for conf in tpl_conf:
        module, handler = conf['handler'].rsplit('.', 1)
        module = "handler." + module
        getattr(importlib.import_module(module), handler)().handle(env, conf)

        _variables = env[conf['key']]
        render_func(conf['path'], _variables, **kwargs)


if __name__ == '__main__':
    config.task_conf_path = input("请输入配置文件地址（例：./task_conf_px.yaml）：")
    _task_conf = config.get_task_config()
    _render_out = _task_conf['render']['out']
    if _render_out == 'console':
        render(write_to_console)
    elif _render_out == 'real_path':
        _mkdir = _task_conf['file']['mkdir']
        _overwrite = _task_conf['file']['overwrite']
        render(write_to_real_path, mkdir=_mkdir, overwrite=_overwrite)
    elif _render_out == 'out':
        render(write_to_out)

# TODO 文件后缀类型
