import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = ["a", "an", "the", "in", "of", "at", "on", "is", "am", "are", "was", "were", "be", "been", "has", "have", "had", "do", "does", "did", "to", "from", "by", "for", "with", "and", "or", "not", "but", "this", "that", "which", "where", "when", "who", "whom", "how", "why", "can", "could", "may", "might", "shall", "should", "will", "would", "must", "there", "here", "so", "very", "too", "it"]

def index_docts(documents,key = 1, docs_dict = {}):
    for document in documents:
        docs_dict[key] = document
        key +=1
    list_of_docs_kyes = list(docs_dict.keys())
    return docs_dict, list_of_docs_kyes


def TF_IDF(docs_dict, stop_words= stop_words):
    list_of_docs = []

    for doc_key in docs_dict:
        with open(f"documents/{docs_dict[doc_key]}", "r") as d:
            doc = d.read()
            list_of_docs.append(doc)

    vectorizer = TfidfVectorizer(stop_words= stop_words)

    matrix_of_vals = vectorizer.fit_transform(list_of_docs)
    matrix_of_vals = matrix_of_vals.toarray()

    features = vectorizer.get_feature_names_out()

    return matrix_of_vals, features

def matrix_of_vals_to_DataFrame(matrix_of_vals, features, list_of_docs_kyes, data = {}):
    for doc_ind in range(0, len(matrix_of_vals)):
        for word_val in range(0, len(features)):
            if features[word_val] in list(data.keys()):
                data[features[word_val]].append(matrix_of_vals[doc_ind][word_val])
            else:
                data[features[word_val]] = list()
                data[features[word_val]].append(matrix_of_vals[doc_ind][word_val])
    df_tfidf = pd.DataFrame(data=data, index=list_of_docs_kyes)
    return df_tfidf

def search(query, df_tfidf, list_of_docs_kyes):
    val_dict = {}
    sorted_indexes = []
    mean_vals = []
    list_df_ind = df_tfidf.index
    sample = df_tfidf[query[0:]]


    for index in list_df_ind:
        mean_vals.append(sample.loc[index].mean())


    for key in list_of_docs_kyes:
        val_dict[key] = mean_vals[key - 1]


    for k in val_dict:
        if val_dict[k] == max(list(val_dict.values())):
            sorted_indexes.append(k)

    return sorted_indexes

documents = os.listdir("documents")
docs_dict, list_of_docs_kyes = index_docts(documents)
matrix_of_vals, features = TF_IDF(docs_dict)


df_tfidf = matrix_of_vals_to_DataFrame(matrix_of_vals, features, list_of_docs_kyes)
query2 = ["study", "effectively"]
query3 = ["available", "wellbeing", "workshops"]

result2 = search(query2, df_tfidf, list_of_docs_kyes)
for ind in result2:
    print(f"For query {query2} the suitable documets: {ind} : {docs_dict[ind]}")

result3 = search(query3, df_tfidf, list_of_docs_kyes)
for ind in result3:
    print(f"For query {query3} the suitable documets: {ind} : {docs_dict[ind]}")
