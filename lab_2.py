import os                                             # Import the os module for file system operations
documents = os.listdir("documents")                    # Get a list of file names in the "documents" directory

#indexing docts
def index_docts(documents,key = 1, docs_dict = {}):    # Define a function to index documents
    for document in documents:                         # Iterate through each document in the list of documents
        docs_dict[key] = document                      # Assign a key-value pair to the dictionary for the document
        key +=1                                        # Increment the key for the next document
    return docs_dict                                    # Return the dictionary of indexed documents

#bool search
def boolean_search(query, index_docts):                # Define a function to perform a boolean search on indexed documents
    result = []                                        # Create an empty list to store the results
    for doc_key in index_docts:                        # Iterate through each indexed document
        with open(f"documents/{index_docts[doc_key]}", "r") as d:    # Open the document for reading
            doc = d.read()                                        # Read the contents of the document into a variable

        if all(q.lower() in doc.lower() for q in query):  # Check if all query terms are present in the document (case-insensitive)
            result.append(doc_key)                        # Add the key of the document to the results list
    return result                                         # Return the list of document keys that match the query

#
def main():
    documents = os.listdir("documents")                # Get a list of file names in the "documents" directory
    docs_dict = index_docts(documents)                 # Index the documents
    print(docs_dict)                                    # Print the dictionary of indexed documents
    query1 = ["Seek"]                                   # Define a query
    query2 = ["Realistic", "Goals"]
    query3 = ["available", "wellbeing", "workshops"]
    print(f"For query {query1} results found in {boolean_search(query1, docs_dict)} documents")  # Perform a boolean search for query1 and print the results
    print(f"For query {query2} results found in {boolean_search(query2, docs_dict)} documents")  # Perform a boolean search for query2 and print the results
    print(f"For query {query3} results found in {boolean_search(query3, docs_dict)} documents")  # Perform a boolean search for query3 and print the results

if __name__ == '__main__':
    main()                                               # Call the main function if the script is run directly
