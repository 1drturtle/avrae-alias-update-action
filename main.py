import os
import requests
import json
import collections
import fnmatch

ToPublish = collections.namedtuple('ToPublish', ['filename', 'abs_path', 'rel_path'])

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
            if rel_path in modified_files and rel_path in alias_ids:
                to_publish.append(ToPublish(name, abs_path=abs_path, rel_path=rel_path))

    out = []
    for alias in to_publish:
        # Load File
        with open(alias.abs_path, 'r') as f:
            code = f.read()
            data_post = {
                "content": code
            }
            # Make Requests
            auth = {'Authorization': avrae_token}
            root_request_url = 'https://api.avrae.io/workshop/{}/'
            # POST New Alias Code
            post_result = requests.post(url=(root_request_url + 'code').format(alias_ids[alias.rel_path]),
                                        data=json.dumps(data_post),
                                        headers=auth
                                        ).json()
            # PUT new alias code as active
            data_put = {
                'version': post_result['data']['version']
            }
            put_result = requests.put(url=(root_request_url + 'code').format(alias_ids[alias.rel_path]),
                                      data=json.dumps(data_put),
                                      headers=auth
                                      ).json()
            print(f'Result for {alias.filename} (Version #{data_put["version"]}) - '
                  f'POST Result: {post_result["success"]} '
                  f'PUT Result: {put_result["success"]}')


if __name__ == '__main__':
    main()
