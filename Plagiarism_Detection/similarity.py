import nltk
import websearch
from difflib import SequenceMatcher
import pandas as pd
import numpy as np

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(nltk.corpus.stopwords.words('english')) 

def purifyText(string):
    words = nltk.word_tokenize(string)
    return (" ".join([word for word in words if word not in stop_words]))

def webVerify(string, results_per_sentence):
    sentences = nltk.sent_tokenize(string)
    matching_sites = []  #list of url come from websearch/searchBing
    for url in websearch.searchBing(query=string, num=results_per_sentence):
        matching_sites.append(url)
    for sentence in sentences:
        for url in websearch.searchBing(query = sentence, num = results_per_sentence):
            matching_sites.append(url)

    return (list(set(matching_sites)))

def similarity(str1, str2):
    return (SequenceMatcher(None,str1,str2).ratio())*100

def reports(text):

    matching_sites = webVerify(purifyText(text), 2)
    matches = {}

    for i in range(len(matching_sites)):
        matches[matching_sites[i]] = similarity(text, websearch.extractText(matching_sites[i]))

    matches = {k: v for k, v in sorted(matches.items(), key=lambda item: item[1], reverse=True)}

    return matches


def Table(dictionary):

    df = pd.DataFrame({'Similarity (%)': dictionary})
    # tot_avg = np.sum(v)
    #df = df.fillna(' ').T
    #df = df.transpose()
    html = df.to_html(classes='table table-striped', header="true")
    return html


if __name__ == '__main__':
    report('This is a pure test')
