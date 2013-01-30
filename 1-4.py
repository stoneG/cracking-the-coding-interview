def url_spaces(string):
    while ' ' in string:
        string = string[:-2].replace(' ', '%20', 1)
    return string
