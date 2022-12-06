# Detailed Usage Examples

**Note:** This document assumes that you have defined the following environment variables:

```
APPDOME_API_KEY
APPDOME_TEAM_ID
APPDOME_IOS_FS_ID
APPDOME_ANDROID_FS_ID
```

To define them, you can use the following command:

```
export APPDOME_API_KEY=<your_api_key>
export APPDOME_TEAM_ID=<your_team_id>
export APPDOME_IOS_FS_ID=<your_ios_fusion_set_id>
export APPDOME_ANDROID_FS_ID=<your_android_fusion_set_id>
```

## Android whole process

```
python3 appdome_api.py --app <apk/aab file>
--sign_on_appdome
--keystore <keystore file>
--keystore_pass <keystore password>
--keystore_alias <key alias>
--key_pass <key password>
--output <output apk/aab>
--certificate_output <output certificate pdf>
```

## iOS whole process

```
python3 appdome_api.py --app <ipa file>
--sign_on_appdome --keystore <p12 file>
--keystore_pass <p12 password>
--provisioning_profiles <provisioning profile file> <another provisioning profile file if needed>
--entitlements <entitlements file> <another entitlements file if needed> --output <output ipa>
--certificate_output <output certificate pdf>
```

Private Signing and Auto-Dev Private Signing can also be invoked in the whole process commands
using the params `--private_signing` or `--auto_dev_private_signing` instead of `--sign_on_appdome`
and adjusting the required signing parameters.

___
## The next section details individual actions
___

## Upload

```
python3 upload.py --app <apk/aab/ipa file>
```

## Status
All of the actions from this point are asynchronous. You can check the status of the action with the following command:
```
python3 status.py --task_id <task_id_value>
```

## Build
[Possible overrides](https://apis.appdome.com/reference/post_tasks-build)

```
python3 build.py --app_id <app_id_value>
--fusion_set_id <fusion_set_id_value>
--build_overrides <overrides_json_file>
```

## Context
[Possible overrides](https://apis.appdome.com/reference/post_tasks-context)

```
python3 context.py --task_id <task_id_value>
--new_bundle_id <bundle_id_value>
--new_version <version_value>
--new_build_number <build_number_value>
--new_display_name <display_name_value>
--app_icon <app_icon_file>
--icon_overlay <icon_overlay_file>
```

## On Appdome Signing

[Possible overrides](https://apis.appdome.com/reference/post_tasks-sign)

**Android**

```
python3 sign.py --task_id <task_id_value>
--keystore <keystore file>
--keystore_pass <keystore password>
--keystore_alias <key alias>
--key_pass <key password>
--sign_overrides <overrides_json_file>
```

**iOS**

```
python3 sign.py --task_id <task_id_value>
--keystore <p12 file>
--keystore_pass <p12 password>
--sign_overrides <overrides_json_file>
--provisioning_profiles <provisioning profile file> <another provisioning profile file if needed>
--entitlements <entitlements file> <another entitlements file if needed>
```

## Private Signing

[Possible overrides](https://apis.appdome.com/reference/post_tasks-privatesign)

**Android**
```
python3 private_sign.py --task_id <task_id_value>
--signing_fingerprint <signing_fingerprint>
--sign_overrides <overrides_json_file>
--google_play_signing
```

**iOS**

```
python3 private_sign.py --task_id <task_id_value>
--sign_overrides <overrides_json_file>
--provisioning_profiles <provisioning profile file> <another provisioning profile file if needed>
```

## Auto-Dev Private Signing

[Possible overrides](https://apis.appdome.com/reference/post_tasks-autodev)

**Android**

```
python3 auto_dev_sign.py --task_id <task_id_value>
--signing_fingerprint <signing_fingerprint>
--google_play_signing
```

**iOS**

```
python3 auto_dev_sign.py --task_id <task_id_value>
--sign_overrides <overrides_json_file>
--provisioning_profiles <provisioning profile file> <another provisioning profile file if needed>
--entitlements <entitlements file> <another entitlements file if needed>
```

## Download

```
python3 download.py --task_id <task_id_value>
--output <output file>
--deobfuscation_script_output <deobfuscation_scripts_zip_file>
--sign_second_output <second_output_app_file>
```

## Download Certified Secure pdf file

```
python3 certified_secure.py --task_id <task_id_value>
--certificate_output <output certificate pdf>
```

## Download Certified Secure json file
```
python3 certified_secure_json.py --task_id <task_id_value>
--certificate_json <certificate_json_output_file>
```

## Validate App after local signing

```
python3 validate.py --validate_app <app file>
```
