
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you",
 "go"          : "gone",
 "hello"      : "hey there"
}

from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Jarvis and I'm a chatbot !",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"What can you do ?",
        ["I can assist, guide and spend time with you",]
    ],
    [
        r"how do I look like?",
        ["you are looking Gorgeous",]
    ],
    [
        r" What are your Hobbies?",
        ["Most of the time I spend with you, you my whole world",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hai|hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?|(.*) old are you?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) weather today ?",
        ["'it's pretty good","it's worser than ever"]
    ],
    [
        r"(.*) created ?",
        ["Sarang created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Kozhikode, Kerala',]
    ],
    [
        r"(.*) hobbies ?",
        ["My hobbies are spending time with you", "you are my world",]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football and batminton",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony","Neymar"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["our own Lal ettan"]
    ],
    [
        r"What (.*) time now",
        ["it's a good time for you, you are a lucky charm"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def Friday():
        print("Hi, I'm Friday and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
        chat = Chat(pairs, reflections)
        chat.converse()
if __name__ == "__main__":
    Friday()




