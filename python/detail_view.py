import json
import sys

import util

DETAIL_TEMPLATE_LOCATION = "templates/detail-template.html"
ROOT_TEMPLATE = "templates/default.html"
CHARITIES_JSON = 'json/charities.json'


def get_charity_items(charity: dict) -> list:
    """Gets all the items the charity accepts.
    Parameters:
        1: Dictionary (Target charity)
    Return Value:
        List of all items the charity accepts
    """

    items = []

    for item in charity['items']:
        """if '[Category]' in item:
            category = item[:item.find("[Category]")].strip().lower()
            items_in_category = items_json[categories.index(category)]['items']
            items.extend(items_in_category)
        elif '[Skip]' in item:
            continue"""
        if '[Skip]' in item:
            continue
        elif '[Category]':
            items.append(item.rstrip('[Category]').strip())
        else:
            items.append(item)

    items = list(set(items))  # Weed out duplicates
    return sorted(items)


def gen_detail_view(obj):
    fp = open(ROOT_TEMPLATE)
    template: str = fp.read()
    fp.close()

    alternates = {}

    for x in obj:
        if '[Alternate]' in obj[x]:
            alternates[x] = str(obj[x])
            obj[x] = f'{{Insert+{x}+alternate}}'

    temp = util.subsitute_object(DETAIL_TEMPLATE_LOCATION, obj)
    temp = temp.replace('{INSERT FORMATTED ADDRESS}', obj['address'].replace(' ', '+'))
    template = template.replace('{INSERT}', temp)  # Strings are immutable

    newlines = [y for y in range(len(template)) if template.startswith('\n', y)]  # The line ending is Unix, not \r\n

    for x in alternates:
        index = template.find(f'{{Insert+{x}+alternate}}')
        # Slice is upper bound exclusive
        before = max([line for line in newlines if line < index]) + 1
        after = min([line for line in newlines if line > index])
        template = template[:before] + \
            alternates[x].rstrip('[Alternate]').rstrip() + \
            template[after:]

    if obj['email'] == '':
        template = template.replace("Through email here:", '')

    if obj['items'][0] == '[Thrift Store]':
        template = template.replace('Items they accept:', 'This organization is a thrift store, for more information about what they accept, please visit their website').replace('{INSERT ITEMS}', '')
        return template

    for item in get_charity_items(obj):
        temp = \
f"""<div class="col-sm-6 col-md-4 col-lg-3 p-0">
    <a class="text-dark" href="/items/{item.lower().replace(' ', '-')}.html">
        <p class="text-center m-1 border-dark border rounded bg-success">{item}</p>
    </a>
</div>"""
        index = template.find("{INSERT ITEMS}")
        template = template[:index] + temp + template[index:]

    template = template.replace('{INSERT ITEMS}', '')

    return template


def main():
    fp = open(CHARITIES_JSON)
    objs = json.load(fp)['charities']
    fp.close()

    for obj in objs:
        detail_view = gen_detail_view(obj)
        fp = open(f"{sys.argv[1]}/{obj['name'].lower().replace(' ', '-')}.html", 'w')
        fp.write(detail_view)


if __name__ == "__main__":
    main()
