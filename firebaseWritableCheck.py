#!/usr/bin/env python3
import requests
import argparse
import sys

__author__  = 'Regis SENET'
__email__   = 'regis.senet@bssi.fr'
__git__     = 'https://github.com/rsenet/firebaseWritableCheck'
__version__ = '0.1'
__license__ = 'GPLv3'
__pyver__   = '%d.%d.%d' % sys.version_info[0:3]
short_desc  = "Firebase Write Access Checker"

parser = argparse.ArgumentParser(description=short_desc)
parser.add_argument('--url', help="Specify the firebase URL")
u_args = parser.parse_args()

# Get variable
fire_url = u_args.url
fire_data = {"Exploitation": "Successfull", "Company": "BSSI"}

try:
    if fire_url:
        # Check if the URL is writable
        fire_write = requests.put(fire_url, json=fire_data)

        if fire_write.status_code == 200:
            print(">> %s has been created (write permission is allowed)" % fire_url)

            # Check if the created file is readable
            fire_read = requests.get(fire_url)

            if fire_read.status_code == 200:
                print(">> %s is readable (read permission is allowed)" % fire_url)
                print(fire_read.text)

            else:
                print(">> %s is NOT readable (read permission is NOT allowed)" % fire_url)

        else:
            print("Not vulnerable")

    else:
        parser.print_help()

except KeyboardInterrupt:
    print("\n[x] Leaving ...")
