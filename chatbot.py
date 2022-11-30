from nltk.chat.util import Chat, reflections
pairs=[
    ['need help',['how can i help you?']],
    ['what is your name',['I am chat Bot']]
 
]
 
chat=Chat(pairs,reflections)
chat.converse()