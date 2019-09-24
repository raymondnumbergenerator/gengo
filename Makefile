.PHONY: init
init:
	git submodule init
	git submodule update data/moedict
	cd data/moedict && perl link2pack.pl a < a.txt
	cd data/moedict && perl link2pack.pl t < t.txt
	cd data/moedict && perl link2pack.pl h < h.txt
	mv data/moedict/a data/cmn
	mv data/moedict/t data/nan
	mv data/moedict/h data/hak
