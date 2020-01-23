import json

import requests

BASE_URL = "https://platform.x5gon.org/api/v1/"


def search_documents(keyword):
    query = BASE_URL + "search?text=" + keyword
    print("Running query: " + query)
    return json.loads(requests.get(query).content)["rec_materials"]


def get_document(document_id):
    query = BASE_URL + "oer_materials/" + document_id
    print("Running query: " + query)
    return json.loads(requests.get(query).content)["oer_materials"]


def get_document_content(document_id):
    query = BASE_URL + "oer_materials/" + document_id + "/contents"
    print("Running query: " + query)
    return json.loads(requests.get(query).content)["oer_contents"]
