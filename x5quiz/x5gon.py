import json

import requests

BASE_URL = "https://platform.x5gon.org/api/v1/"


def search_documents(keyword):
    return json.loads(requests.get(BASE_URL + "search?text=" + keyword).content)["rec_materials"]
