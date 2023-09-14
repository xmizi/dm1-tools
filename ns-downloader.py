#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time

# import math
# import pprint
# import datetime
# import sys

nsapidata = requests.get("https://NS-URL/api/v2/properties/")
d_nsapidata  = json.loads(nsapidata.content.decode("utf8"))

IOB = float(d_nsapidata["iob"]["iob"])
COB = float(d_nsapidata["cob"]["cob"])
PZ = float(d_nsapidata["pump"]["pump"]["reservoir"])
PB = d_nsapidata["pump"]["pump"]["battery"]["percent"]
MB = d_nsapidata["upbat"]["display"]
GL = d_nsapidata["bgnow"]["sgvs"][0]["scaled"]
DELTA = float(d_nsapidata["delta"]["scaled"])
#SENS = float(d_nsapidata["pump"]["openaps"]["suggested"]["sensitivityRatio"])
SENS = float(d_nsapidata["openaps"]["lastSuggested"]["sensitivityRatio"])
BAZ = d_nsapidata["basal"]["current"]["basal"]
TBR = d_nsapidata["basal"]["current"]["treatment"]["rate"]
PZ = float(d_nsapidata["pump"]["pump"]["reservoir"])
PB = d_nsapidata["pump"]["pump"]["battery"]["percent"]
MB = d_nsapidata["pump"]["uploader"]["battery"]

TIMEDELTA_R = time.time()
TIMEDELTA_P = (d_nsapidata["delta"]["times"]["recent"] / 1000)
TIMEDELTA = ((TIMEDELTA_R - TIMEDELTA_P) / 60)

#_isf_tmp = d_nsapidata["pump"]["openaps"]["suggested"]["reason"]
_isf_tmp = d_nsapidata["openaps"]["lastSuggested"]["reason"]
_isf_1 = _isf_tmp.split(", ")[3]
ISF = float(_isf_1.split(": ")[1])

print(round(COB, 1))
print(round(IOB, 1))
print(GL)
print(round(DELTA, 1))
print(round(TBR, 1))
print(round(BAZ, 2))
print(round(PZ, 1))
print(PB)
print(MB)
print(round(SENS, 1))
print(round(ISF, 1))
print(round(TIMEDELTA, 1))
