# Import requests library to send HTTP requests
import difflib
import json
def get_categories(response, txtmsg, coef: float):
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        data = dict(json.loads(response.content))
        a = data['data']
        categories = dict()
        for i in a:
            for j in i['child_categories']:
                cat_id = j['id']
                categories[cat_id] = list()
                for e in j['child_categories']:
                    categories[cat_id].append({e['id']: e['name']})

        categories_keys = set()
        categories_values = set()
        for key, value in categories.items():
            for j in value:
                str1 = txtmsg.lower().split()
                str2 = list(j.values())[0].lower()
                str3 = txtmsg.lower()
                if f' {str2}' in str3:
                    categories_keys.add(f"{key}:{list(j.keys())[0]}")  
                    categories_values.add(f"{list(j.values())[0]}")
                else:
                    a = difflib.get_close_matches(str2, str1, 3, coef) 
                    for i in a:
                        categories_keys.add(f"{key}:{list(j.keys())[0]}")  
                        categories_values.add(f"{list(j.values())[0]}")  
        return [categories_keys, categories_values]
    else:
        # Handle the error if the response status code is not 200 (OK)
        print("Error: ", response.status_code)
        return None