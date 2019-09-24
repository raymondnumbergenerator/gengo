.PHONY: init
init:
	cd data/moedict && perl link2pack.pl a < a.txt
	cd data/moedict && perl link2pack.pl t < t.txt
	cd data/moedict && perl link2pack.pl h < h.txt
	mv data/moedict/a data/cmn
	mv data/moedict/t data/nan
	mv data/moedict/h data/hak
	rm -rf data/moedict
