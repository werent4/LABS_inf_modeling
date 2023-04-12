import os
from lab_2 import index_docts, boolean_search

def test_index_docts():
    documents = os.listdir("documents")
    expected_output = {1: '9-tricks-help-you-study-better-google.txt',
                       2: 'how-to-become-a-more-effective-learner_Yahoo.txt',
                       3: 'how-to-study-in-college_bing.txt',
                       4: 'six-tips-studying-effectively_Duck_duck.txt',
                       5: 'tips-to-maximize-study-efficiency_dogpile.txt'}
    assert index_docts(documents) == expected_output

def test_boolean_search():
    documents_dir = "documents"
    query1 = ["seek"]
    query2 = ["seek", "and"]
    query3 = ["seek", "and", "find"]
    expected_output1 = [1, 3]
    expected_output2 = [1, 3]
    expected_output3 = [3]
    docs_dict = index_docts(os.listdir(documents_dir))

    assert boolean_search(query1, docs_dict) == expected_output1
    assert boolean_search(query2, docs_dict) == expected_output2
    assert boolean_search(query3, docs_dict) == expected_output3
