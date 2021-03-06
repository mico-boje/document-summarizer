import os
import ast
import nltk
import json

print(os.getcwd())
#filename = r'C:\Users\miboj\Documents\Bachelor\Code\document-summarizer\data\raw\articles.json'
filename = r'/home/miboj/NLP/document-summarizer/data/raw/articles.json'
file = open(filename, encoding='ascii', errors='ignore')
text = file.read()
file.close()

d = ast.literal_eval(text)

remove1 = 'Sign up for the C4ISRNET newsletter about future battlefield technologies.'
remove2 = 'For more newsletters click here'
remove3 = 'Sign up for the C4ISRNET newsletter about future battlefield technologies.'
remove4 = 'By giving us your email, you are opting in to the C4ISRNET Daily Brief.'
remove5 = "Don't miss the top Air Force stories, delivered each afternoon"
remove6 = "For more newsletters click here"
remove7 = "Sign up for the Air Force Times Daily News Roundup to receive the top Air Force stories every afternoon."
remove8 = "By giving us your email, you are opting in to the Air Force Times Daily News Roundup."
remove9 = "Sign up for the Early Bird Brief, the defense industry's most comprehensive news and information, straight to your inbox."
remove10 = "By giving us your email, you are opting in to the Early Bird Brief."
remove11 = "Sign up for the Early Bird Brief - a daily roundup of military and defense news stories from around the globe."

test = [remove1, remove2, remove3, remove4, remove5, remove6, remove7, remove8, remove9, remove10, remove11]

def generator(articles, remove_list):
    sen_list = []
    for e, i in enumerate(articles):
        temp = []
        for enum, t in enumerate(i['content']):
            if t not in remove_list:
                temp.append(t)
        sen_list.append({'content': temp})
    return sen_list
    # yield {'content': i['content'], }


g = generator(d, test)
#with open(r'C:\Users\miboj\Documents\Bachelor\Code\document-summarizer\data\processed\articles.json', 'x') as f:
with open(r'/home/miboj/NLP/document-summarizer/data/processed/articles.json', 'x') as f:
    json.dump(g, f)

