import requests
import sys

if len(sys.argv) < 2:
    raise Exception('Must provide the collection id as the only argument')


def print_subaliases(alias, parent):
    parent = parent
    for subalias in alias['subcommands']:
        print(f'Sub-Alias !{" ".join(parent)} {subalias["name"]} found, ID: {subalias["_id"]}')
        this_parent = parent + [subalias['name']]
        print_subaliases(subalias, this_parent)


def main():
    print('Finding Aliases and Snippets.')

    collection_id = str(sys.argv[1])
    collection = requests.get(url=f'https://api.avrae.io/workshop/collection/{collection_id}/full')
    collection = collection.json()

    if collection['success']:
        collection = collection['data']
        for alias in collection['aliases']:
            print(f"Alias !{alias['name']} found, ID: {alias['_id']}")
            subaliases = alias['subcommands']
            print_subaliases(alias, [alias["name"]])
        for snippet in collection['snippets']:
            print(f"Snippet !{snippet['name']} found, ID: {snippet['_id']}")

    else:
        return print('Error in Collection: ', collection)


if __name__ == '__main__':
    main()
