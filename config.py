from typing import Union
import json
import yaml


_type_map = None
_bean_conf = None
_table_conf = None
_project_conf = None
_task_conf = None
_tpl_conf = None

# ./task_conf_xxx.yaml
task_conf_path: Union[str, None] = None


def get_type_map():
    global _type_map
    if not _type_map:
        with open('conf/type_map.json') as type_map_file:
            _type_map = json.load(type_map_file)
    return _type_map


def get_bean_config():
    global _bean_conf
    if not _bean_conf:
        with open('conf/bean_config.yaml') as config:
            _bean_conf = yaml.load(config, yaml.Loader)
    return _bean_conf


def get_table_config():
    global _table_conf
    if not _table_conf:
        with open('conf/table_config.yaml') as config:
            _table_conf = yaml.load(config, yaml.Loader)
    return _table_conf


def get_project_config():
    global _project_conf
    if not _project_conf:
        with open('conf/project_config.yaml') as config:
            _project_conf = yaml.load(config, yaml.Loader)
    return _project_conf


def get_task_config():
    global _task_conf
    if not _task_conf:
        with open('./db_conf.yaml') as db_config:
            db_conf = yaml.load(db_config, yaml.Loader)
            with open(task_conf_path) as config:
                _task_conf = yaml.load(config, yaml.Loader)
                _task_conf['db'].update(db_conf['dbs'][_task_conf['db']['id']])
    return _task_conf


def get_tpl_config():
    global _tpl_conf
    if not _tpl_conf:
        with open('conf/template_conf.json') as config:
            _tpl_conf = json.load(config)
    return _tpl_conf
