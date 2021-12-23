import requests
import json
from jsonforapi import jsonformatter


def fetch_api(url, *args):
    response = requests.get(url=url, json={'query': jsonformatter.fetching_query(*args)})
    parse_json = json.loads(response.text)
    detail = parse_json['data']['users']
    return detail, response.status_code


def delete_api(url, uuid):
    response = requests.post(url=url, json={'query': jsonformatter.delete_query(uuid=uuid)})
    return response.status_code


def create_api(url, **kwargs):
    response = requests.post(url=url, json={'query': jsonformatter.creation_query(**kwargs)})
    parse_json = json.loads(response.text)
    api_response = parse_json['data']['createUser']['ok']
    return api_response, response.status_code


def update_api(url, **kwargs):
    response = requests.post(url=url, json={'query':jsonformatter.update_query(**kwargs)})
    parse_json = json.loads(response.text)
    api_response = parse_json['data']['updateUser']['ok']
    return api_response, response.status_code


def filter_json_data(data_to_be_required, value_to_be_fetched):
    count = len(data_to_be_required)
    if count >= 2:
        last_value = json.loads(json.dumps(data_to_be_required[len(data_to_be_required)-1]))
        return last_value.get(value_to_be_fetched)
    else:
        string = json.dumps(data_to_be_required).replace("]", "").replace("[", "")
        get_value = json.loads(string)
        return get_value.get(value_to_be_fetched)


def fetch_respective_detail(fetched_response, to_fetched):
    uuid_list = []
    for uuid in json.loads(json.dumps(fetched_response)):
        if to_fetched in uuid:
            uuid_list.append(uuid.get(to_fetched))

    return uuid_list
