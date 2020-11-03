import os
import requests
import json


def main():
    alias_id_file_name = os.environ.get('INPUT_ALIAS_IDS_FILE_NAME')
    avrae_token = os.environ.get('INPUT_AVRAE_TOKEN')
    modified_files = os.environ.get('INPUT_MODIFIED-FILES', '[]')

    alias_ids = {}
    with open(alias_id_file_name, 'r') as f:
        alias_ids = json.loads(f.read())

    print(alias_ids, '\n', modified_files)


if __name__ == '__main__':
    main()
