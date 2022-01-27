import argparse
import logging
from os.path import join

import requests

from utils import (url_with_team, TASKS_URL, request_headers, JSON_CONTENT_TYPE, validate_response,
                   debug_log_request, add_common_args, init_logging)


def download_certified_secure_json(api_key, team_id, task_id):
    url = url_with_team(join(TASKS_URL, task_id, 'certificate-json'), team_id)
    headers = request_headers(api_key, JSON_CONTENT_TYPE)
    debug_log_request(url, headers=headers, request_type='get')
    return requests.get(url, headers=headers)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Download Certified Secure json file')
    add_common_args(parser, True)
    parser.add_argument('-cj', '--certificate_json', required=True, help="Output of Certified Secure json")
    return parser.parse_args()


def main():
    args = parse_arguments()
    init_logging(args.verbose)

    r = download_certified_secure_json(args.api_key, args.team_id, args.task_id)
    validate_response(r)
    with open(args.certificate_json, 'wb') as f:
        f.write(r.content)
    logging.info(f"Downloaded file to {args.certificate_json}")


if __name__ == '__main__':
    main()
