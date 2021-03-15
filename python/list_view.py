import json

CHARITIES_JSON = './json/charities.json'
LIST_TEMPLATE = './templates/list-template.html'
ROOT_TEMPLATE = './templates/default.html'

def subsitute_object(file, obj) -> str:
    """Subsitute fields of dictionatry into a copy of a file.
    This function will seek out all the keys in the form of {key}
    within the file, then it will subsitute the value into them.
    Returns a string, does not create nor edit files
    """
    template_file = open(file)
    template = template_file.read()
    template_file.close()

    for field in obj.keys():
        if template.find('{' + field + '}') == -1:
            continue

        # Strings are immutable
        template = template.replace('{' + field + '}', obj[field]) 
    return template

def gen_list_view() -> str:
    """Generates list view of charities. Returns string
    """

    fp = open(CHARITIES_JSON)
    charities: list = json.load(fp)
    fp.close()
    
    fp = open(ROOT_TEMPLATE)
    template: str = fp.read()
    fp.close()

    # Strings are immutable
    template = template.replace('{INSERT}', 
    '<div class=\'container\' id=\'content\'><div class=\'card-container\'>{INSERT CHARITIES}</div></div>')

    for obj in charities:
        temp = subsitute_object(LIST_TEMPLATE, obj)
        insert_index = template.find('{INSERT CHARITIES}')
        template = template[:insert_index] + temp + '\n' + template[insert_index:]
    template = template.replace('{INSERT CHARITIES}', '')

    return template

def main():
    print(gen_list_view())

if __name__ == '__main__':
    main()