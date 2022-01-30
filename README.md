# appdome-api-python
Python library for interacting with https://fusion.appdome.com/ tasks API

Each API endpoint has its own file and main for a single API call
appdome_api.py contains the whole flow of a task from upload to download.

All APIs are documented in https://www.appdome.com/how-to/dev-sec-tools/app-sec-release-automation/automate-single-tasks-using-automate-building-mobile-apps-appdome-rest-api/

The following environment variables can be defined in order to save passing them on each call:

* APPDOME_API_KEY
* APPDOME_TEAM_ID
* APPDOME_IOS_FS_ID
* APPDOME_ANDROID_FS_ID


Android Example (assuming the above environment variables are set):

python3 appdome_api.py --app_path <path to apk/aab file> --sign_on_appdome --keystore <path to keystore file> --keystore_pass <keystore password>
 --keystore_alias <key alias> --key_pass <key password> --output <path to output apk/aab> --certificate_output <path to output certificate pdf>
 
iOS Example (assuming the above environment variables are set):

python3 appdome_api.py --app_path <path to ipa file> --sign_on_appdome --keystore ~/Desktop/files/APPDOME_DISTRIBUTION_DEV.p12 --keystore_pass nf1101 
--provisioning_profiles <provisioning profile path> <another provisioning profile path if needed> --output <path to output ipa> --certificate_output <path to output certificate pdf>