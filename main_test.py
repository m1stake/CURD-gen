from handler.pre import PreHandler
from handler.table_info import TableInfoHandler
import config
import importlib


if __name__ == '__main__':

    tpl_conf = config.get_tpl_config()

    env = {}
    PreHandler().handle(env)
    TableInfoHandler().handle(env)

    for conf in tpl_conf:
        module, handler = conf['handler'].rsplit('.', 1)
        module = "handler." + module
        getattr(importlib.import_module(module), handler)().handle(env, conf)
    print(env)
