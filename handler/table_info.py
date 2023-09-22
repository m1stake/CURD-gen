import pymysql
from handler.base import BaseHandler


class TableInfoHandler(BaseHandler):

    def handle(self, env, tpl_conf=None):
        db_info = env['task']['db']
        args = {k: v for k, v in db_info.items() if v}
        env['tableInfo'] = _get_table_info(**args)


def _get_table_info(db_name, table, host='localhost', port=3306, user='root', password='123456'):

    table_info_sql = 'select table_name, table_comment ' \
                     'from information_schema.tables ' \
                     'where table_schema="%s" and table_name ="%s"' % (db_name, table)
    column_info_sql = 'select column_name, data_type, column_comment ' \
                      'from information_schema.columns ' \
                      'where table_schema="%s" and table_name ="%s"' \ 
                      'order by ordinal_position' % (db_name, table)

    conn = pymysql.connect(host=host, port=port, user=user, password=password, database=db_name,
                           cursorclass=pymysql.cursors.DictCursor)
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(table_info_sql)
            table_info = cursor.fetchone()

            cursor.execute(column_info_sql)
            column_info = cursor.fetchall()

            table_info['columns'] = column_info

            return table_info


if __name__ == '__main__':
    # from handler.pre import PreHandler
    # env = {}
    # PreHandler().handle(env)
    # print(env)
    # TableInfoHandler().handle(env)
    # print(env)
    print(_get_table_info('t_test', 't_idx_explain', 'localhost'))

