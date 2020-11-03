import requests
import sys

if len(sys.argv) < 2:
    raise Exception('Must provide the collection id as the only argument')

print('Finding Aliases and Snippets. (Max Subcommand Depth - 1)')

collection_id = str(sys.argv[1])
collection = requests.get(url=f'https://api.avrae.io/workshop/collection/{collection_id}')
collection = collection.json()

if 'data' in collection:
    collection = collection['data']
    for alias_id in collection['alias_ids']:
        alias = requests.get(url='https://api.avrae.io/workshop/alias/'+alias_id).json()
        if alias['success']:
            alias = alias['data']
            print(f'Alias Name: {alias["name"]} | Alias ID: {alias["_id"]}')
            if alias['subcommand_ids']:
                for subcommand_id in alias['subcommand_ids']:
                    alias = requests.get(url='https://api.avrae.io/workshop/alias/'+subcommand_id).json()
                    if alias['success']:
                        alias = alias['data']
                        print(f'Alias Name: {alias["name"]} | Alias ID: {alias["_id"]}')
                    else:
                        print('Alias Error:\n',alias)
        else:
            print('Alias Error:\n',alias)
    for snippet_id in collection['snippet_ids']:
        snippet = requests.get(url='https://api.avrae.io/workshop/snippet/'+snippet_id).json()
        if snippet['success']:
            snippet = snippet['data']
            print(f'Snippet Name: {snippet["name"]} | Snippet ID: {snippet["_id"]}')
        else:
            print('Snippet Error:\n',snippet)
else:
    print('Collection Error:\n',collection)
