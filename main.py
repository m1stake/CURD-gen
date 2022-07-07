import table_info
import table_info_translator
import template_render
from pathlib import Path
import config


base_path = 'E:/workspace/project/sanitary-inspection-be/sanitary-inspection-core-biz'
base_package = 'com.microsun.inspection.core.biz'

tpl_s = [
    ('domain.entity.java.tpl', 'DO', 'domain.entity'),
    ('domain.dto.java.tpl', 'DTO', 'domain.dto'),
    ('domain.vo.java.tpl', 'VO', 'domain.vo'),
    ('domain.listVo.java.tpl', 'ListVO', 'domain.vo'),
    ('domain.query.java.tpl', 'Query', 'domain.dto'),
    ('mapper.java.tpl', 'Mapper', 'mapper'),
    ('service.java.tpl', 'Service', 'service'),
    ('serviceImpl.java.tpl', 'ServiceImpl', 'service.impl'),
    ('controller.java.tpl', 'Controller', 'com.microsun.web.controller.biz',
     'E:/workspace/project/sanitary-inspection-be/sanitary-inspection-admin'),
]


def write_to_out(tpl, variables, bean_class_name):
    view = template_render.render(variables, tpl[0])
    with open('./out/' + bean_class_name + tpl[1] + '.java', 'w', encoding='utf8') as f:
        f.write(view)


def write_to_real_path(tpl, variables, bean_class_name):
    if tpl[1] != 'Controller':
        package = base_package + "." + tpl[2]
        pkg_path = package.replace('.', '/')
        path = base_path + '/src/main/java/' + pkg_path
    else:
        package = tpl[2]
        pkg_path = package.replace('.', '/')
        path = tpl[3] + '/src/main/java/' + pkg_path

    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)

    variables['package'] = package
    view = template_render.render(variables, tpl[0])
    with open(path + "/" + bean_class_name + tpl[1] + '.java', 'w', encoding='utf8') as f:
        f.write(view)


if __name__ == '__main__':
    _bean_conf = config.get_bean_config()
    _bean_conf['beanName'] = 'GbItem'

    tbl_info = table_info.get_table_info('sanitary_inspection', 'tb_task_flow_inspection_gb_item', '192.168.2.55')
    _variables = table_info_translator.translate(tbl_info)
    _bean_class_name = _variables['beanClassName']
    for _tpl in tpl_s:
        # write_to_out(_tpl, _variables, _bean_class_name)
        write_to_real_path(_tpl, _variables, _bean_class_name)



