import os
documents = os.listdir("documents")

def boolean_search(query):
    result = []
    for doct in documents:
        with open(f"documents/{doct}", "r") as d:
            doc = d.read()

        if all(q.lower() in doc.lower() for q in query):
            result.append(documents.index(doct))
    return result

query = ["rules", "hate"]

print(boolean_search(query))