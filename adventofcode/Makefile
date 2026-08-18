MAKEFLAGS += --no-print-directory

.DEFAULT_GOAL := usage
.PHONY: usage encrypt decrypt

usage:
	@echo "usage: make encrypt | make decrypt"

encrypt:
	$(MAKE) -f encrypt.mk

decrypt:
	$(MAKE) -f decrypt.mk
