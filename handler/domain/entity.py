from handler.base import BaseHandler
import config


class EntityHandler(BaseHandler):

    def handle(self, env, tpl_conf=None):
        class_info = BaseHandler.get_class_info(env, "domain.entity")
        task = env['task']
        fields, imports = _build_fields(env['tableInfo'])
        variables = {
            'author': task['author'],
            'datetime': task['datetime'],
            'package': class_info['pkg'],
            'path': class_info['path'] + "/" + class_info['className'] + ".java",
            'imports': imports,
            'beanDesc': class_info['beanDesc'],
            'tableName': task['db']['table'],
            'beanClassName': class_info['beanClassName'],
            'beanName': class_info['beanName'],
            'className': class_info['className'],
            'fields': fields,
        }
        env[tpl_conf['key']] = variables


_type_map = config.get_type_map()
_table_conf = config.get_table_config()


def _build_fields(table_info):
    imports = set()
    fields = []
    _remove_ignore_columns(table_info)
    for field in table_info['columns']:
        field_name = _snake_to_camel_case(field['COLUMN_NAME'], False)
        field_type = _translate_type(field['DATA_TYPE'])
        date_format = _date_format(field_type)
        if date_format:
            imports.add('org.springframework.format.annotation.DateTimeFormat')
        fields.append({
            'name': field_name,
            'comment': field['COLUMN_COMMENT'],
            'type': field_type,
            'dateFormat': date_format,
        })
        import_class = _import_class(field_type)
        if import_class:
            imports.add(import_class)
    return fields, imports


def _translate_type(data_type: str):
    data_type = data_type.lower()
    if data_type in _type_map:
        return _type_map[data_type]
    else:
        return None


def _snake_to_camel_case(snake_words: str, first_upper: bool):
    words = snake_words.split('_')
    if first_upper:
        return ''.join(word.title() for word in words)
    else:
        first_word = words[0]
        return first_word + ''.join(word.title() for word in words[1:])


def _import_class(field_type):
    if field_type in _type_map['_typeInfo']:
        if 'fullName' in _type_map['_typeInfo'][field_type]:
            return _type_map['_typeInfo'][field_type]['fullName']
        else:
            return None
    else:
        return None


def _date_format(field_type):
    if field_type in _type_map['_typeInfo']:
        if 'dateFormat' in _type_map['_typeInfo'][field_type]:
            return _type_map['_typeInfo'][field_type]['dateFormat']
        else:
            return None
    else:
        return None


def _remove_ignore_columns(table_info):
    if 'column' in _table_conf and 'ignores' in _table_conf['column'] and type(_table_conf['column']['ignores']) == list:
        ignore_columns = _table_conf['column']['ignores']
        for column in table_info['columns'][:]:
            if column['COLUMN_NAME'] in ignore_columns:
                table_info['columns'].remove(column)



