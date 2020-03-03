#!/usr/bin/env python3

import subprocess
import json

instances = json.loads(subprocess.check_output('gcloud compute instances list --format=json'.split()))

def getIP(item):
    return item['networkInterfaces'][0]['accessConfigs'][0]['natIP']

def hasTag(item, tag):
	return tag in item['tags']['items']

def isApp(item):
	return hasTag(item, 'reddit-app')

def isDb(item):
	return hasTag(item, 'reddit-db')

apps = list(map(getIP, filter(isApp, instances)))
dbs = list(map(getIP, filter(isDb, instances)))
print(json.dumps({"app": {"hosts": apps}, "db": {"hosts": dbs}}))
