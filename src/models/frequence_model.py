import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
# from nltk.stem.porter import *
# Might use stemming to see the difference?
import string
import heapq

nltk.download('punkt')
nltk.download('stopwords')
raw_string = [" ROME — Defying reports that their planned partnership is ", "doomed to fail", ", France’s Naval Group and ", "Italy’s Fincantieri", " have announced a joint venture to build and export naval vessels. ", " The two ", "state-controlled shipyards", " said they were forming a 50-50 joint venture after months of talks to integrate their activities. The move comes as Europe’s fractured shipbuilding industry faces stiffer global competition. ", " The firms said in a statement that the deal would allow them to “jointly prepare winning offers for binational programs and export market,” as well as create joint supply chains, research and testing. ", " Naval Group and Fincantieri first announced talks on cooperation last year after the latter negotiated a controlling share in French shipyard STX. But the deal was reportedly losing momentum due to resistance from French industry and a political row between France and Italy over migrants. ", " The new deal falls short of the 10 percent share swap predicted by French Economy and Finance Minister Bruno Le Maire earlier this year, and far short of the total integration envisaged by Fincantieri CEO Giuseppe Bono. ", " The statement called the joint venture the “first steps” toward the creation of an alliance that would create “a more efficient and competitive European shipbuilding industry.”", " Naval Group CEO Hervé Guillou, speaking at the Euronaval trade expo in Paris on Oct. 24, said the alliance is based on “two countries sharing a veritable naval ambition.”", " The joint venture is necessary because the “context of the global market has changed drastically,” he added, specifically mentioning new market entrants Russia, China, Singapore, Ukraine, India and Turkey.", "Sign up for the Early Bird Brief, the defense industry's most comprehensive news and information, straight to your inbox.", "By giving us your email, you are opting in to the Early Bird Brief.", " When asked about an initial product to be tackled under the alliance, Guillou acknowledged: “The answer is simple: there is nothing yet.”", " However, the firms said they are working toward a deal to build four logistics support ships for the French Navy, which will be based on an Italian design. ", "Competition flares up for the follow-on portion of a deal previously won by the French shipbuilder.", " The firms also plan to jointly bid next year on work for midlife upgrades for Horizon frigates, which were built by France and Italy and are in service with both navies. The work would include providing a common combat management system. ", " The statement was cautious about future acceleration toward integration. “A Government-to-Government Agreement would be needed to ensure the protection of sovereign assets, a fluid collaboration between the French and Italian teams and encourage further coherence of the National assistance programs, which provide a framework and support export sales,” the statement said.", " But the firms were optimistic the deal would be “a great opportunity for both groups and their eco-systems, by enhancing their ability to better serve the Italian and French navies, to capture new export contracts, to increase research funding and, ultimately, improve the competitiveness of both French and Italian naval sectors.”", " ", "Sebastian Sprenger", " in Paris contributed to this report."]


def remove_empty_string(input_string):
    for e, i in enumerate(input_string):
        # if i == ' ' or None:
        #    del(string[e])
        if i[-1] == ' ' and input_string[e+1][-1] == ' ':
            input_string[e] = i.rstrip()
    joined_string = ''.join(input_string)
    for e, i in enumerate(joined_string):
        if i == ' ' and joined_string[e+1] == ' ':
            del i
    return joined_string



cleaned_string = remove_empty_string(raw_string)
sent_list = sent_tokenize(cleaned_string)
#test2 = word_tokenize(test[0])
stpwrds = stopwords.words('english') + list(string.punctuation) + ['—', '“', '”', "'", "’"]
print(list(string.punctuation))


word_freq = {}
for word in word_tokenize(cleaned_string):
    if word.lower() not in stpwrds:
        if word not in word_freq.keys():
            word_freq[word] = 1
        else:
            word_freq[word] += 1
max_freq = max(word_freq.values())

for word in word_freq.keys():
    word_freq[word] = (word_freq[word]/max_freq)

sentence_scores = {}
for sent in sent_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_freq.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_freq[word]
            else:
                sentence_scores[sent] += word_freq[word]
print(sentence_scores)
summary_max_len = int(len(sent_list)*0.3)
summary_sentences = heapq.nlargest(summary_max_len, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)

print('Original length: ', len(cleaned_string))
print('Summary length: ', len(summary))

print('Original: ', cleaned_string)
print('Summary: ', summary)


