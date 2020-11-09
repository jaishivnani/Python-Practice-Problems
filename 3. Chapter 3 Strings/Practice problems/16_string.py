'''Write a Python function to create the HTML string with tags around the word(s). Go to the editor
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'''

# def add_tags(tag,str):
#     opening_tag='<'
#     closing_tag='>'
#     closing_tag1='</'
#
#     return opening_tag+tag+closing_tag+str+closing_tag1+tag+closing_tag
#
# print(add_tags('i','Python'))
# print(add_tags('b','Python Tutorial'))

def add_tags(tag,word):
    return "<%s>%s</%s>" % (tag,word,tag)

print(add_tags('i','Python'))
print(add_tags('b','Python Tutorial'))
