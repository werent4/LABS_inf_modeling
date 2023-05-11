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
    return_dict = {}
    for doc_key in index_docts:
        with open(f"documents/{index_docts[doc_key]}", "r") as d:
            doc = d.read()
        # Create bigrams
        tokens = nltk.word_tokenize(doc)
        bigrams_2 = list(nltk.bigrams(tokens))
        bigram_count = bigrams_2.count(search_bigram)

        if bigram_count > 0:
            # display documents containing the bigram first
            return_list.insert(0, doc_key)
            return_dict[doc_key] = f"bigram {search_bigram} was found {bigram_count} times"
        else:
            return_list.append(doc_key)
            return_dict[doc_key] = f"bigram {search_bigram} wasn't found"
    return return_dict, return_list

def main():
    # Creating indexes for docs
    documents = os.listdir("documents")
    docs_dict = index_docts(documents)
    # Creating search bigramm
    search_bigram = ('Realistic', 'Goals')
    return_dict, return_list = bigram_search(search_bigram, docs_dict)
    # Output
    for i in return_list:
        print("In document:", i,'-',docs_dict[i], return_dict[i])

if __name__ == '__main__':
    main()