#  Copyright (c) 2019 Manuel Peuster <manuel@peuster.de
#  Copyright (c) 2019 SONATA-NFV, 5GTANGO, Paderborn University
# ALL RIGHTS RESERVED.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Neither the name of the SONATA-NFV, 5GTANGO, Paderborn University
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has also been performed in the framework of the 5GTANGO project,
# funded by the European Commission under Grant number 761493 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.5gtango.eu).
.DEFAULT_GOAL := all

DOC_DIR := "doc"
PYBINDPLUGIN := $(shell python -c 'import pyangbind; import os; print("{}/plugin".format(os.path.dirname(pyangbind.__file__)))')

validate:
	# generate doc
	pyang ietf-ped.yang -f tree -o "$(DOC_DIR)/ietf-ped.tree"
	pyang ietf-ped.yang -f jstree -o "$(DOC_DIR)/ietf-ped.html"
	pyang ietf-ped.yang -f uml -o "$(DOC_DIR)/ietf-ped.uml"
	# finally validate
	pyang ietf-ped.yang --ietf

build:
	# generate / compile python model
	pyang --plugindir $(PYBINDPLUGIN) -f pybind -o ietf_ped_model.py ietf-ped.yang

test:
	# test the example ped files against the model
	pytest -v

all: validate build test

clean:
	rm doc/*