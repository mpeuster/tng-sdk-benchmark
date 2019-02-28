import model
from model import ietf_ped
from pyangbind.lib.serialise import pybindJSONDecoder
import pyangbind.lib.pybindJSON as pybindJSON
import yaml
import json

#
# re-generate the model 
# pyang --plugindir $PYBINDPLUGIN -f pybind -o model.py ietf-ped.yang 
#

#m = ietf_ped()
#print(ietf_ped)
#print(pybindJSON.dumps(m))

#
#pybindJSONDecoder.load_ietf_json(data, None, None, obj=m.ped())

# json version
#m2 = pybindJSON.load("example-instance.json", model, "ietf_ped")
#print(m2.ped.vendor)

# yaml version
data = yaml.load(open("example-instance.yml", "r"))
print(data)
m3 = pybindJSON.loads(data, model, "ietf_ped")
print(m3.ped.vendor)