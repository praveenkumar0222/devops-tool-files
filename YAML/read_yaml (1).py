import yaml

filename = 'document.yml'

with open(filename) as f:
    data = yaml.load(f, Loader = yaml.FullLoader)
    for keys, values in data.items():
        print(keys , "---->", values , "----->" , type(values))

    