import yaml

f = open('data.yaml')
for data in yaml.load_all(f):
    print(data)