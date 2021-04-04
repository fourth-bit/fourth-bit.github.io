import json
import sys

import util

CHARITIES_JSON = './json/charities.json'
LIST_TEMPLATE = './templates/list-template.html'
ROOT_TEMPLATE = './templates/default.html'

def gen_list_view() -> str:
    """Generates list view of charities. Returns string
    """

    fp = open(CHARITIES_JSON)
    charities: list = sorted(json.load(fp)['charities'],
        key=lambda x: x['name'])
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
        alternates = {}
        for x in obj:
            if '[Alternate]' in obj[x]:
                alternates[x] = str(obj[x])
                obj[x] = f'{{Exclude+{x}}}'
        temp = util.subsitute_object(LIST_TEMPLATE, obj)
        temp = temp.replace('{NAME LINK}', obj['name'].lower().replace(' ', '-'))

        newlines = [y for y in range(len(temp)) if temp.startswith('\n', y)] # The line ending is Unix, not \r\n
        for x in alternates:
            index = temp.find(f'{{Exclude+{x}}}')
            # Slice is upper bound exclusive
            before = max([line for line in newlines if line < index]) + 1
            after = min([line for line in newlines if line > index])
            temp = temp[:before] + temp[after:]

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
