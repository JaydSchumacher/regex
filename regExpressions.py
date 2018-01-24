import re

str = 'Hello Bob 555-555-5555'

#file_object = open('basics.txt')
#data = file_object.read()
#file_object.close()

#first = re.match('Four', data)
#liberty = re.search('Liberty', data)

def phone_numbers(str):
    return(re.findall(r'\d{3}-\d{3}-\d{4}', str))


def find_words(count, str):
    return(re.findall(r'\w{}{}{}{}'.format('{',count,',','}'), str))
    
def find_emails(str):
    return(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+', str))


print(find_emails("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk"))


