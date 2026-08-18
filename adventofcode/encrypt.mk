TXTS := $(wildcard ./*/*/input.txt ./*/*/data/input.txt)
TARGETS := $(TXTS:.txt=.txt.gpg)

.PHONY: all
all: $(TARGETS)

%.txt.gpg: %.txt
	gpg --yes --quiet --encrypt --default-recipient-self -o $@ $<
