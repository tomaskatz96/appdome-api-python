# appdome-api-python
Python library for interacting with https://fusion.appdome.com/ tasks API

Each API endpoint has its own file and main for a single API call
appdome_api.py contains the whole flow of a task from upload to download.

All APIs are documented in https://www.appdome.com/how-to/dev-sec-tools/app-sec-release-automation/automate-single-tasks-using-automate-building-mobile-apps-appdome-rest-api/

The following environment variables can be defined in order to save passing on on each call:
APPDOME_API_KEY
APPDOME_TEAM_ID
APPDOME_IOS_FS_ID
APPDOME_ANDROID_FS_ID