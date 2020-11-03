import os
import requests
import json
import collections
import fnmatch

ToPublish = collections.namedtuple('ToPublish', ['filename', 'path'])

# alias suffixes:
ALIAS_SUFFIXES = ('.alias', 'snippet')

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
        files = [str(filename) for filename in files if str(filename).endswith(ALIAS_SUFFIXES)]

        for name in files:
            abs_path = os.path.join(root, name)
            shared = os.path.commonprefix([abs_path, path_to_files])
            rel_path = os.path.relpath(abs_path, shared)
            print('File Found: ' + rel_path)
            if rel_path in modified_files:
                to_publish.append(ToPublish(name, abs_path))
    print(to_publish)


if __name__ == '__main__':
    main()
