import json
import sys

import util

LIST_TEMPLATE = "templates/items-template.html"
ROOT_TEMPLATE = "templates/default.html"
ITEMS_JSON = "json/charities.json"

def gen_list_view():
    fp = open(ITEMS_JSON)
    objs: list = json.load(fp)['items']
    fp.close()

    fp = open(ROOT_TEMPLATE)
    template = fp.read()
    fp.close()

    template = template.replace('{INSERT}', 
    "<div class='container' id='content'><h1>Items</h1><div class='card-container'>{INSERT LIST}</div></div>"
    )

    for obj in objs:
        temp = util.subsitute_object(LIST_TEMPLATE, obj)
        for item in obj['items']:
            index = temp.find('{INSERT ITEMS}')
            temp = temp[:index] + f'<li>{item}</li>' + temp[index:]
        temp = temp.replace('{INSERT ITEMS}', '')

        index = template.find('{INSERT LIST}')
        template = template[:index] + temp + template[index:]
    
    template = template.replace('{INSERT LIST}', '')
    return template

def main():
    fp = open(sys.argv[1], 'w')
    fp.write(gen_list_view())
    fp.close()

if __name__ == "__main__":
    main()