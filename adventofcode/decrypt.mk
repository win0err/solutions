GPGS := $(wildcard ./*/*/input.txt.gpg ./*/*/data/input.txt.gpg)
TARGETS := $(GPGS:.gpg=)

.PHONY: all
all: $(TARGETS)

%.txt: %.txt.gpg
	gpg --yes --quiet --decrypt -o $@ $<
	@touch -r $< $@
