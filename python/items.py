import json
import sys

import util

DETAIL_TEMPLATE = "templates/items-detail-template.html"
LIST_TEMPLATE = "templates/items-template.html"
ROOT_TEMPLATE = "templates/default.html"
ITEMS_JSON = "json/charities.json"

def gen_list_view():
    fp = open(ITEMS_JSON)
    objs: list = json.load(fp)['items']
    objs.sort(key=lambda x: x['category'])
    fp.close()

    fp = open(ROOT_TEMPLATE)
    template = fp.read()
    fp.close()

    template = template.replace('{INSERT}', 
"""
<div class='container' id='content'>
    <h1 class="text-center">Items</h1>
    <div class='items-container'>
        <div class="col-md-6">
            {INSERT LIST}
        </div>
    </div>
</div>
"""
    )

    for count, obj in enumerate(objs):
        temp = util.subsitute_object(LIST_TEMPLATE, obj)
        obj['items'].sort()
        for item in obj['items']:
            index = temp.find('{INSERT ITEMS}')
            temp = temp[:index] + f'<li><a href="/items/{item.lower().replace(" ", "-")}.html">{item}</a></li>' + temp[index:]
        temp = temp.replace('{INSERT ITEMS}', '\n')

        index = template.find('{INSERT LIST}')
        template = template[:index] + temp + template[index:]

        if count == 4:
            index = template.find('{INSERT LIST}')
            template = template[:index] + """</div>\n\t<div class="col-md-6">""" + template[index:]
    
    template = template.replace('{INSERT LIST}', '')
    return template

def gen_detail_views():
    fp = open(ITEMS_JSON)
    objs: list = json.load(fp)['items']
    fp.seek(0)
    charities: list = json.load(fp)['charities']
    fp.close()

    fp = open(ROOT_TEMPLATE)
    template = fp.read()
    fp.close()

    template = template.replace('{INSERT}', 
"""
<div class='container' id='content'>
    {INSERT DETAIL VIEW}
</div>
"""
    )

    return_dict = {}

    for x in objs:
        for name in x['items']: # 2-dimensional array
            fp = open(DETAIL_TEMPLATE)
            temp = fp.read()
            fp.close()
            temp = temp.replace('{name}', name)
            for charity in charities:
                if name in [item.split('(')[0].strip() for item in charity['items']]:
                    index = temp.find('{INSERT CHARITIES}')
                    temp = temp[:index] + \
f"""
<div>
    <p>{charity['name']}</p>
</div>
""" \
                           + temp[:index]
            temp = temp.replace('{INSERT CHARITIES}', '')
            return_dict[name] = template.replace('{INSERT DETAIL VIEW}', temp)
    return return_dict

def main():
    list_view = gen_list_view()

    fp = open(sys.argv[1], 'w')
    fp.write(list_view)
    fp.close()
    fp = open(f'{sys.argv[2]}/index.html', 'w')
    fp.write(list_view)
    fp.close()

    detail_views = gen_detail_views()
    for key in detail_views.keys():
        fp = open(f'{sys.argv[2]}/{key.lower().replace(" ", "-")}.html', 'w')
        fp.write(detail_views[key])
        fp.close()

if __name__ == "__main__":
    main()