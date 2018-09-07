import yaml
import pymysql

f = open('config/ctcdb.yaml')
data = yaml.load(f)

__host = data['localhost']
__user = data['localuser']
__password = data['localpwd']
__db = data['localdb']
__port = data['port']
__charset = data['charset']

def execute(sql_str):
    if sql_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(sql_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = pymysql.connect(host=__host, user=__user, passwd=__password, db=__db,
                               port=__port, charset=__charset)
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql_str)
        data = cur.fetchall()
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data
    except Exception as e:
        raise e