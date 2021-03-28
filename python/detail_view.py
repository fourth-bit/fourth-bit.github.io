import json
import sys

import util

DETAIL_TEMPLATE_LOCATION = "templates/detail-template.html"
ROOT_TEMPLATE = "templates/default.html"
CHARITIES_JSON = 'json/charities.json'

def gen_detail_view(obj):
    fp = open(ROOT_TEMPLATE)
    template: str = fp.read()
    fp.close()

    temp = util.subsitute_object(DETAIL_TEMPLATE_LOCATION, obj)
    template = template.replace('{INSERT}', temp) # Strings are immutable

    for item in obj['items']:
        temp = \
f"""<div class="col-6 col-sm-4 col-lg-3 p-0">
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
