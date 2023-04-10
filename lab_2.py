import os
documents = os.listdir("documents")

#indexing docts
def index_docts(documents,key = 1, docs_dict = {}):
    for document in documents:
        docs_dict[key] = document
        key +=1
    return docs_dict

#bool search
def boolean_search(query, index_docts):
    result = []
    for doc_key in index_docts:
        with open(f"documents/{index_docts[doc_key]}", "r") as d:
            doc = d.read()

        if all(q.lower() in doc.lower() for q in query):
            result.append(doc_key)
    return result


documents = os.listdir("documents")
docs_dict = index_docts(documents)
print(docs_dict)
query = ["Seek"]
print(boolean_search(query, docs_dict))