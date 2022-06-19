import re
def email_parse(email_address):
    email = email_address
    pattern_email = r'[a-zA-Z0–9]+@[a-zA-Z]+\.[a-zA-Z]+'
    dict = {}
    rezult = re.search(pattern_email,email)
    if rezult == None:
        raise ValueError(" wrong email", email)
    new_list = re.split('@', email)
    dict['username'] = new_list[0]
    dict['domain'] = new_list[1]
    return dict


print(email_parse('harin.gmail.com'))