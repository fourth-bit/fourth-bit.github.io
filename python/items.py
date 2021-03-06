import json
import sys

import util

DETAIL_TEMPLATE = "templates/items-detail-template.html"
CATEGORY_DETAIL_VIEW = "templates/categories-detail-view.html"
LIST_TEMPLATE = "templates/items-template.html"
ROOT_TEMPLATE = "templates/default.html"
CHARITY_LIST_VIEW = "templates/list-template.html"
ITEMS_JSON = "json/charities.json"

def get_charities_with_category(charities: list, category: str) -> list:
    """Get all the charities from the specified list which use the specific
    category using the [Category] directive.
    Parameters:
        1: List of Dictionaries (The charities)
        2: String (Name of the category, DO NOT put the [Category] on it
    Return Value:
        List of all  of the charities with the category
    """
    
    return_list = []

    for charity in charities:
        if category + ' [Category]' in charity['items']:
            return_list.append(charity)
    return return_list

def get_charities_with_item(charities: list, name: str) -> list:
    """Gets a charities with a certain item.
    Parameters:
        1: List of Dictionaries (The charities)
        2: String (The item we are looking for)
    Return Value:
        List of all of the charities (dictionaries) with the item
    """

    fp = open(ITEMS_JSON)
    items = json.load(fp)['items'] # Need this for category expansion
    fp.close()

    categories = [x['category'].lower() for x in items]

    answer = []
    for charity in charities:
        for item in charity['items']:
            p_index = item.find('(') if item.find('(') != -1 else len(item)
            b_index = item.find('[') if item.find('[') != -1 else len(item)
            index = min(p_index, b_index)
            stripped_item = item[:index].strip()
            if name == stripped_item:
                answer.append(charity)
                break
            elif '[Category]' in item:
                category = item[:item.find('[')].strip().lower()
                items_in_category = items[categories.index(category)]['items']
                if name in items_in_category:
                    answer.append(charity)
                    break
    return answer

def gen_list_view() -> str:
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
""")

    for count, obj in enumerate(objs):
        temp = util.subsitute_object(LIST_TEMPLATE, obj)
        obj['items'].sort()
        for item in obj['items']:
            index = temp.find('{INSERT ITEMS}')
            temp = temp[:index] + f'<li><a href="/items/{item.lower().replace(" ", "-")}.html">{item}</a></li>' + temp[index:]
        temp = temp.replace('{INSERT ITEMS}', '\n')

        index = template.find('{INSERT LIST}')
        template = template[:index] + temp + template[index:]

        if count == round(len(objs) / 2) - 1:
            index = template.find('{INSERT LIST}')
            template = template[:index] + """</div>\n\t<div class="col-md-6">""" + template[index:]

    template = template.replace('{INSERT LIST}', '')

    script_insert_index = template.find('</body>')
    template = template[:script_insert_index] + '<script src="js/dropdown.js"></script>' + template[script_insert_index:]

    template = template.replace("{TITLE}", "Items")

    return template


def gen_detail_views() -> dict:
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
{INSERT DETAIL VIEW}
""")

    return_dict = {}

    for name in [y for obj in objs for y in obj['items']]:
        fp = open(DETAIL_TEMPLATE)
        temp = fp.read()
        fp.close()
        temp = temp.replace('{name}', name)
        for charity in get_charities_with_item(charities, name):
            index = temp.find('{INSERT CHARITIES}')

            if len(charity['about']) > 150:
                charity['about'] = charity['about'][:147] + ' ...'

            temp = temp[:index]\
                + util.subsitute_object(CHARITY_LIST_VIEW, charity)\
                        .replace('{NAME LINK}',
                        charity['name'].replace(' ', '-').lower())\
                + temp[index:]
        temp = temp.replace('{INSERT CHARITIES}', '')
        temp = template.replace('{INSERT DETAIL VIEW}', temp).replace('{TITLE}', name)
        return_dict[name] = temp

    for obj in objs:
        temp = util.subsitute_object(CATEGORY_DETAIL_VIEW, obj)

        if get_charities_with_item(charities, obj['category']) == []:
            continue
        for charity in get_charities_with_category(charities, obj['category']):
            index = temp.find('{INSERT CHARITIES}')

            if len(charity['about']) > 150:
                charity['about'] = charity['about'][:147] + ' ...'

            temp = temp[:index]\
                + util.subsitute_object(CHARITY_LIST_VIEW, charity)\
                        .replace('{NAME LINK}',
                        charity['name'].replace(' ', '-').lower())\
                + temp[index:]
        temp = temp.replace('{INSERT CHARITIES}', '')

        for item in obj['items']:
            index = temp.find('{INSERT ITEMS}')
            formtatted_item = \
f"""<div class="col-sm-6 col-md-4 col-lg-3 p-0">
    <a class="text-dark" href="/items/{item.lower().replace(' ', '-')}.html">
        <p class="text-center m-1 border-dark border rounded bg-success">{item}</p>
    </a>
</div>"""
            temp = temp[:index] + formtatted_item + temp[index:]
        temp = temp.replace('{INSERT ITEMS}', '')

        return_dict[obj['category']] = template.replace('{INSERT DETAIL VIEW}', temp)

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

