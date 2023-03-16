import requests
import difflib
import json
from pprint import pprint

url = "https://aztester.uz/api-announcement/v1/category/tree"

response_ru = requests.get(url, headers={'language': "ru"})
response_uz = requests.get(url, headers={'language': "uz_latn"})
response_cyrl = requests.get(url, headers={'language': "uz_cyrl"})


def get_catalog(catalog, lan):
    payload={}
    headers = {
        'content-type': 'application/json',
        'language': f"{lan}"
    }
    if catalog == 0:
        url = "https://aztester.uz/api-announcement/v1/category/tree"
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()['data']
    else:
        url = f'https://aztester.uz/api-announcement/v1/category?category_id={catalog}'
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()['data'][0]


def get_catalog_by_id(catalog, lan):
    payload={}
    headers = {
        'content-type': 'application/json',
        'language': f"{lan}"
    }
    url = f'https://aztester.uz/api-announcement/v1/category?category_id={catalog}'
    response = requests.request("GET", url, headers=headers, data=payload)
    for i in response.json()['data']:
        return i['name']


get_catalog(catalog=0, lan='ru')
# get_catalog_by_id(catalog=1140, lan='uz_latn')