import os
import requests
import json


def main():
    alias_id_file_name = os.environ.get('INPUT_alias-ids-file')
    avrae_token = os.environ.get('INPUT_avrae-token')
    modified_files = json.loads(os.environ.get('INPUT_modified-files', '[]'))

    # alias_ids = {}
    # with open(alias_id_file_name, 'r') as f:
    #     alias_ids = json.loads(f.read())
    #
    all_environs = os.environ
    print(all_environs)


if __name__ == '__main__':
    main()
