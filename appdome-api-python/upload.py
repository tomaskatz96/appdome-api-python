import argparse
import logging
from os.path import join, basename

import requests

from utils import (url_with_team, SERVER_API_V1_URL, request_headers, empty_files,
                   validate_response, debug_log_request, add_common_args, log_and_exit, init_common_args)


def get_upload_link(api_key, team_id):
    url = url_with_team(join(SERVER_API_V1_URL, 'upload-link'), team_id)
    headers = request_headers(api_key)
    debug_log_request(url, headers, request_type='get')
    return requests.get(url, headers=headers)


def put_file_in_aws(file_path, aws_url):
    with open(file_path, 'rb') as f:
        debug_log_request(aws_url, request_type='put')
        return requests.put(aws_url, data=f.read())


def upload_using_link(api_key, team_id, file_id, file_name):
    url = url_with_team(join(SERVER_API_V1_URL, 'upload-using-link'), team_id)
    headers = request_headers(api_key)
    body = {'file_app_id': file_id, 'file_name': file_name}
    debug_log_request(url, data=body)
    return requests.post(url, headers=headers, data=body, files=empty_files())


def upload(api_key, team_id, file_path):
    logging.info(f"Preparing to upload [{file_path}]")
    upload_link_response = get_upload_link(api_key, team_id)
    validate_response(upload_link_response)
    upload_link_json = upload_link_response.json()
    aws_url = upload_link_json.get('url')
    file_id = upload_link_json.get('file_id')
    if not aws_url or not file_id:
        log_and_exit('Error in upload link response: ' + upload_link_response.text)

    logging.info(f"Uploading file id {file_id} to url: {aws_url}")
    aws_put_response = put_file_in_aws(file_path, aws_url)
    validate_response(aws_put_response)
    return upload_using_link(api_key, team_id, file_id, basename(file_path))


def parse_arguments():
    parser = argparse.ArgumentParser(description='Upload app to Appdome')
    add_common_args(parser)
    parser.add_argument('-a', '--app_path', required=True, metavar='application_path', help="Upload app input path")
    return parser.parse_args()


def main():
    args = parse_arguments()
    init_common_args(args)
    r = upload(args.api_key, args.team_id, args.app_path)
    validate_response(r)
    logging.info(f"Upload success: App id: {r.json()['id']}")


if __name__ == '__main__':
    main()
