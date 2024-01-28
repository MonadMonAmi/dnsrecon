import time
import os
import json
from datetime import datetime
from os.path import join

INPUT_DIR = "input"
OUTPUT_DIR = "output"
WILDCARD_FILE_NAME = "domains_with_wildcard.txt"


def create_if_not_exists(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name


def append_wildcard(domain_trg, testname, wildcard_set, append_wildcard_path=None):
    if wildcard_set:
        with open(append_wildcard_path, 'a') as wildcard_file:
            wildcard_file.write(str([domain_trg, testname, list(wildcard_set)]) + "\n")
            # to read:
            # from json import loads
            # st = loads(s.replace("'", '"'))


def main_executor(f):
    print(datetime.now())
    start_time = time.time()
    try:
        f()
    except Exception as e:
        raise e
    finally:
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Execution time: {execution_time:.2f} seconds')
