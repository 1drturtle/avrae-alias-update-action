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
    print(f'{alias_id_file_name}\n{avrae_token is not None}\n{modified_files}')
    print(f"repo owner test: {os.environ.get('GITHUB_REPOSITORY_OWNER')}")


if __name__ == '__main__':
    main()
