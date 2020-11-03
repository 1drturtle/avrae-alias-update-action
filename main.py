import os
import requests
import json


def main():
    alias_id_file_name = os.environ.get('alias-ids-file')
    avrae_token = os.environ.get('avrae-token')
    modified_files = json.loads(os.environ.get('modified-files', '[]'))

    alias_ids = {}
    with open(alias_id_file_name, 'r') as f:
        alias_ids = json.loads(f.read())

    print(alias_ids)


if __name__ == '__main__':
    main()
