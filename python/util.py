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