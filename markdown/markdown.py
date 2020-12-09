import re

def get_heading(text):
    match = re.findall(r'^#+\ ', text)
    if match:
        hashes = len(match[0]) - 1
        return "<h" + str(hashes) + ">" + text[hashes+1:] + "</h" + str(hashes) + ">"
    else:
        return text

def check_bold(text):
    match = re.match('(.*)__(.*)__(.*)', text)
    return match.group(1) + '<strong>' +  match.group(2) + '</strong>' + match.group(3) if match else text

def check_italic(text):
    match = re.match('(.*)_(.*)_(.*)', text)
    return match.group(1) + '<em>' +  match.group(2) + '</em>' + match.group(3) if match else text

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        i = get_heading(i)
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                curr = m.group(1)
                curr = check_bold(curr)
                curr = check_italic(curr)
                i = '<ul><li>' + curr + '</li>'
            else:
                curr = m.group(1)
                curr = check_bold(curr)
                curr = check_italic(curr)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        i = check_bold(i)
        i = check_italic(i)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res