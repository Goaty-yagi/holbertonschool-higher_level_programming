PY = python3
PCSTYLE = pycodestyle
SRC = $(wildcard *.py)

TEST_DIR = tests
TEST_FILES = test0 test1 test10
BINARIES = $(TEST_FILES:%=%)

all: $(BINARIES)

# Rule to run a specific test file
$(BINARIES): %: $(TEST_DIR)/%.py
	$(PY) $<

# Rule to check code style
style:
	$(PCSTYLE) $(SRC)

.PHONY: all style
