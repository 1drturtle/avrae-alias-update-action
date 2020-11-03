import os
import requests
import json
import collections

ToPublish = collections.namedtuple('ToPublish', ['filename', 'path'])


def main():
    alias_id_file_name = os.environ.get('INPUT_ALIAS_ID_FILE_NAME')
    path_to_files = os.environ.get('GITHUB_WORKSPACE')
    avrae_token = os.environ.get('INPUT_AVRAE_TOKEN')
    modified_files = json.loads(os.getenv('INPUT_MODIFIED-FILES', '[]'))

    with open(path_to_files + '/' + alias_id_file_name, 'r') as f:
        alias_ids = json.loads(f.read())

    to_publish = []
    for root, dirs, files in os.walk(path_to_files):
        # ignore hidden files
        files = [f for f in files if not f[0] == '.']

        for name in files:
            print('File Found: '+name)
            if name in modified_files:
                to_publish.append(ToPublish(name, os.path.join(root, name)))
    print(to_publish)


if __name__ == '__main__':
    main()
