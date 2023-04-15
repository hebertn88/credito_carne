def check_none(element, format=str):
    if (element != None):
        return format(element.text)
    return None