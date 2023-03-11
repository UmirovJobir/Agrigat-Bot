import requests
import difflib
import json
from pprint import pprint

# url = "https://aztester.uz/api-announcement/v1/category/tree"

# response_ru = requests.get(url, headers={'language': "ru"})
# response_uz = requests.get(url, headers={'language': "uz_latn"})
# response_cyrl = requests.get(url, headers={'language': "uz_cyrl"})


def get_catalog(catalog):
    payload={}
    headers = {
        'content-type': 'application/json'
    }

    if catalog == 0:
        url = "https://aztester.uz/api-announcement/v1/category/tree"
        response = requests.request("GET", url, headers=headers, data=payload)
        # for i in response.json()['data']:
        #     print(i['name'], i['id'])

        return response.json()['data']
    else:
        url = f'https://aztester.uz/api-announcement/v1/category?category_id={catalog}'
        response = requests.request("GET", url, headers=headers, data=payload)
        # for i in response.json()['data'][0]['child_categories']:
        #     print(i['name'], i['id'])

        return response.json()['data'][0]['child_categories']

# get_catalog(catalog=1181)
get_catalog(catalog=813)