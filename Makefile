VENV := venv
BIN := $(VENV)/bin

export DEFAULT_DATA_PATH := $(CURDIR)/data
export GENGO_SETTINGS := $(CURDIR)/settings/settings.py

$(VENV): requirements.txt
	python3 ./vendor/venv-update venv= venv -p python3 install= -r requirements.txt

.PHONY: init
init:
	git submodule init
	git submodule update init/moedict
	cd init/moedict && perl link2pack.pl a < a.txt
	cd init/moedict && perl link2pack.pl t < t.txt
	cd init/moedict && perl link2pack.pl h < h.txt
	mv init/moedict/a data/cmn
	mv init/moedict/t data/nan
	mv init/moedict/h data/hak

.PHONY: dev
dev:
	$(BIN)/python3 run.py
