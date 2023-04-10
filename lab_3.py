import os
import nltk

#indexing docts
def index_docts(documents,key = 1, docs_dict = {}):
    for document in documents:
        docs_dict[key] = document
        key +=1
    return docs_dict

# Tokenize the text, search bigrams
def bigram_search(search_bigram, index_docts):
    return_list = []
    for doc_key in index_docts:
        with open(f"documents/{index_docts[doc_key]}", "r") as d:
            doc = d.read()
        # Create bigrams
        tokens = nltk.word_tokenize(doc)
        bigrams_2 = list(nltk.bigrams(tokens))

        if search_bigram in bigrams_2:
            return_list.insert(0, doc_key)
    return return_list

documents = os.listdir("documents")
docs_dict = index_docts(documents)
print(docs_dict)
search_bigram = ('Realistic','Goals')
result = bigram_search(search_bigram, docs_dict)
print(result)