import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
#define stop words
stop_words = ["a", "an", "the", "in", "of", "at", "on", "is", "am", "are", "was", "were", "be", "been", "has", "have", "had", "do", "does", "did", "to", "from", "by", "for", "with", "and", "or", "not", "but", "this", "that", "which", "where", "when", "who", "whom", "how", "why", "can", "could", "may", "might", "shall", "should", "will", "would", "must", "there", "here", "so", "very", "too", "it"]

#function to index documents
def index_docts(documents,key = 1, docs_dict = {}):
    for document in documents:
        docs_dict[key] = document
        key +=1
    list_of_docs_kyes = list(docs_dict.keys())
    return docs_dict, list_of_docs_kyes

#function to calculate TF-IDF scores for documents
def TF_IDF(docs_dict, stop_words= stop_words):
    list_of_docs = []
    # loop through documents and append them to list_of_docs
    for doc_key in docs_dict:
        with open(f"documents/{docs_dict[doc_key]}", "r") as d:
            doc = d.read()
            list_of_docs.append(doc)

    # apply TfidfVectorizer to calculate the matrix of values
    vectorizer = TfidfVectorizer(stop_words= stop_words)
    matrix_of_vals = vectorizer.fit_transform(list_of_docs)
    matrix_of_vals = matrix_of_vals.toarray()

    # get the feature names
    features = vectorizer.get_feature_names_out()

    return matrix_of_vals, features

#function to convert matrix_of_vals to pandas DataFrame
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


#function to search for documents based on a query
def search(query, df_tfidf, list_of_docs_kyes):
    val_dict = {}
    sorted_indexes = []
    mean_vals = []
    list_df_ind = df_tfidf.index
    sample = df_tfidf[query[0:]]

    # calculate mean values for each document based on the query
    for index in list_df_ind:
        mean_vals.append(sample.loc[index].mean())

    # map mean values to document indexes
    for key in list_of_docs_kyes:
        val_dict[key] = mean_vals[key - 1]

    # sort document indexes based on mean values in descending order
    for k in val_dict:
        if val_dict[k] == max(list(val_dict.values())):
            sorted_indexes.append(k)

    return sorted_indexes

def main():
    # get list of documents
    documents = os.listdir("documents")
    docs_dict, list_of_docs_kyes = index_docts(documents)
    # calculate TF
    matrix_of_vals, features = TF_IDF(docs_dict)

    # matrix to dataframe
    df_tfidf = matrix_of_vals_to_DataFrame(matrix_of_vals, features, list_of_docs_kyes)
    query2 = ["study", "effectively"]
    query3 = ["available", "wellbeing", "workshops"]

    result2 = search(query2, df_tfidf, list_of_docs_kyes)
    for ind in result2:
        print(f"For query {query2} the suitable documets: {ind} : {docs_dict[ind]}")

    result3 = search(query3, df_tfidf, list_of_docs_kyes)
    for ind in result3:
        print(f"For query {query3} the suitable documets: {ind} : {docs_dict[ind]}")

if __name__ == '__main__':
    main()