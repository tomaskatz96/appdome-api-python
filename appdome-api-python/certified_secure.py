import argparse
import logging
from os.path import join

import requests

from utils import (url_with_team, TASKS_URL, request_headers, JSON_CONTENT_TYPE, validate_response,
                   debug_log_request, add_common_args, init_common_args)


def download_certified_secure(api_key, team_id, task_id):
    url = url_with_team(join(TASKS_URL, task_id, 'certificate'), team_id)
    headers = request_headers(api_key, JSON_CONTENT_TYPE)
    debug_log_request(url, headers=headers, request_type='get')
    return requests.get(url, headers=headers)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Download Certified Secure pdf file')
    add_common_args(parser, add_task_id=True)
    parser.add_argument('-co', '--certificate_output', required=True, metavar='certificate_output_path', help="Output of Certified Secure pdf")
    return parser.parse_args()


def main():
    args = parse_arguments()
    init_common_args(args)
    r = download_certified_secure(args.api_key, args.team_id, args.task_id)
    validate_response(r)
    with open(args.certificate_output, 'wb') as f:
        f.write(r.content)
    logging.info(f"Downloaded file to {args.certificate_output}")


if __name__ == '__main__':
    main()
