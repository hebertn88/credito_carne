def check_none(element, format=str):
    if (element != None):
        return format(element.text)
    
    if (format in (int, float)):
        return 0
    
    return None