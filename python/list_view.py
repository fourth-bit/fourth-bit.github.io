import json
import sys

from . import util

CHARITIES_JSON = './json/charities.json'
LIST_TEMPLATE = './templates/list-template.html'
ROOT_TEMPLATE = './templates/default.html'

def gen_list_view() -> str:
    """Generates list view of charities. Returns string
    """

    fp = open(CHARITIES_JSON)
    charities: list = json.load(fp)['charities']
    fp.close()
    
    fp = open(ROOT_TEMPLATE)
    template: str = fp.read()
    fp.close()

    # Strings are immutable
    template = template.replace('{INSERT}', """<div class='container' id='content'>
    <h1 class='text-center'>Charities</h1>
    <div class='card-container'>{INSERT CHARITIES}</div>
    </div>""")

    for obj in charities:
        temp = util.subsitute_object(LIST_TEMPLATE, obj)
        insert_index = template.find('{INSERT CHARITIES}')
        template = template[:insert_index] + temp + '\n' + template[insert_index:]
    template = template.replace('{INSERT CHARITIES}', '')

    return template

def main():
    list_view = gen_list_view()
    for x in sys.argv[1:]:
        fp = open(x, 'w')
        fp.write(list_view)
        fp.close()

if __name__ == '__main__':
    main()
