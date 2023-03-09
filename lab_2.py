import os
documents = os.listdir("documents")

key = 1
docs_dict = {}

for document in documents:
    docs_dict[key] = document
    key +=1

print(docs_dict)

def boolean_search(query):
    result = []
    for doc_key in docs_dict:
        with open(f"documents/{docs_dict[doc_key]}", "r") as d:
            doc = d.read()

        if all(q.lower() in doc.lower() for q in query):
            result.append(doc_key)
    return result

query = ["says Librarian of"]

print(boolean_search(query))