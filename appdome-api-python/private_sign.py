import argparse
import logging

from utils import (cleaned_fd_list, add_provisioning_profiles_entitlements, run_task_action, add_google_play_signing_fingerprint,
                   ANDROID_SIGNING_FINGERPRINT_KEY, validate_response, add_common_args, init_common_args)

PRIVATE_SIGN_ACTION = 'seal'


def private_sign_android(api_key, team_id, task_id, signing_fingerprint, is_google_play_signing=False):
    overrides = {}
    if is_google_play_signing:
        add_google_play_signing_fingerprint(signing_fingerprint, overrides)
    else:
        overrides[ANDROID_SIGNING_FINGERPRINT_KEY] = signing_fingerprint

    return run_task_action(api_key, team_id, PRIVATE_SIGN_ACTION, task_id, overrides, None)


def private_sign_ios(api_key, team_id, task_id, provisioning_profiles_paths):
    overrides = {}
    files_list = []
    with cleaned_fd_list() as open_fd:
        add_provisioning_profiles_entitlements(provisioning_profiles_paths, None, files_list, overrides, open_fd)
        return run_task_action(api_key, team_id, PRIVATE_SIGN_ACTION, task_id, overrides, files_list)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Initialize private signing on Appdome')
    add_common_args(parser, add_task_id=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-pr', '--provisioning_profiles', nargs='+', help='Path to iOS provisioning profiles to use. Can be multiple profiles')
    group.add_argument('-cf', '--signing_fingerprint', help='SHA-1 or SHA-256 final Android signing certificate fingerprint.')
    parser.add_argument('-gp', '--google_play_signing', action='store_true', help='This Android application will be distributed via the Google Play App Signing program.')
    return parser.parse_args()


def main():
    args = parse_arguments()
    init_common_args(args)

    if args.signing_fingerprint:
        r = private_sign_android(args.api_key, args.team_id, args.task_id, args.signing_fingerprint, args.google_play_signing)
    else:
        r = private_sign_ios(args.api_key, args.team_id, args.task_id, args.provisioning_profiles)

    validate_response(r)
    logging.info(f"Private signing for Build id: {r.json()['task_id']} started")


if __name__ == '__main__':
    main()
