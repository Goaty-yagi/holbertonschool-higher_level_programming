PY = python3
PCSTYLE = pycodestyle
SRC = $(wildcard *.py)

TEST_DIR = tests
TEST_FILES = test0 test1 test2 test3 test4 test5 test6 test7 test8 test9 test10 test11
BINARIES = $(TEST_FILES:%=%)

all: $(BINARIES)

# Rule to run a specific test file
$(BINARIES): %: $(TEST_DIR)/%.py
	$(PY) $<

# Rule to check code style
style:
	$(PCSTYLE) $(SRC)

.PHONY: all style
