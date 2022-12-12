#To split a phrase
phrase = "This is super simple"
words = phrase.spli()
Type words
['This', 'is', 'super', 'simple']

#To split a URL for something specific
url = "https://example.com/user/CandaceH"
user = url.split('/')[-1]
Type user
'CandaceH'

#To split a URL in general
url = "https://example.com/user/CandaceH"
url.split('/')
['https:', '', 'example.com', 'users', 'CandaceH']

#To call the join method and create a string
phrase = "This is super simple"
", ".join(words)
'This, is, super, simple'

#To call the join method and create new lines
lines = ['First line', 'Second line', 'Third line']
Type output = '\n'.join(lines)
print(output)
=
First Line
Second Line
Third Line

#To call the format method
template = "Hello, my name is {}, and I enjoy {}, Have a nice day!"
template.format('CandaceH', 'Python')
'Hello, my nmae is CandaceH, and I enjoy Python, Have a nice day!'
