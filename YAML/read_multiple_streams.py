import yaml

filename = 'document.yml'

with open(filename) as f:
    #data = yaml.load(f, Loader = yaml.FullLoader)
    data = yaml.load_all(f, Loader = yaml.FullLoader)
    for streams in data:
        for keys, values in streams.items():
            print(keys , "---->", values , "----->" , type(values))