import yaml
import os

dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path=os.path.join(dir,"/robot2.0/config","basic_cfg.yaml")
f = open(config_path)
get_ctcdb_file = open('../cfg/ctcdb.yaml')
data_ctcdb = yaml.load(get_ctcdb_file)

host = data_ctcdb['host']
user = data_ctcdb['user']
password = data_ctcdb['pwd']
db = data_ctcdb['db']
port = data_ctcdb['port']
charset = data_ctcdb['charset']

setDB = data_ctcdb['setDB']
