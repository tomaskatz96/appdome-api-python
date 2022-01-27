import argparse
import logging
from os.path import join

import requests

from utils import (url_with_team, SERVER_API_V1_URL, request_headers, validate_response,
                   debug_log_request, init_logging, add_common_args)


def direct_upload(api_key, team_id, file_path):
    url = url_with_team(join(SERVER_API_V1_URL, 'upload'), team_id)
    headers = request_headers(api_key)
    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f)}
        debug_log_request(url, headers=headers, files=files)
        return requests.post(url, headers=headers, files=files)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Upload app to directly to Appdome')
    add_common_args(parser)
    parser.add_argument('-a', '--app_path', required=True, help="Upload app in path")
    return parser.parse_args()


def main():
    args = parse_arguments()
    init_logging(args.verbose)
    r = direct_upload(args.api_key, args.team_id, args.app_path)
    validate_response(r)
    logging.info(f"Direct upload success: App id: {r.json()['id']}")


if __name__ == '__main__':
    main()
