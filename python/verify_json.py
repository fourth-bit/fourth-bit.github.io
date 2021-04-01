import json

JSON = 'json/charities.json'
DIRECTIVES = ['[Category]', '[Skip]', '[Thrift Store]']

def main():
    fp = open(JSON)
    objs = json.load(fp)
    charities = objs['charities']
    items = objs['items']
    fp.close()

    all_items = set()

    for x in charities:
        for y in x['items']:
            for z in DIRECTIVES:
                if z in y:
                    break
            else:
                if y.find('(') != -1:
                    y = y[:y.find('(')].strip()
                all_items.add(y)
    
    for x in items:
        for y in x['items']:
            all_items.remove(y)
    
    if len(all_items) > 0:
        print(all_items)
        inp = input("Error with json. Continue website generation? [y/n]: ")
        if inp.lower() != 'y':
            raise SystemExit(128)

if __name__ == "__main__":
    main()