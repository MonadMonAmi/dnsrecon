#!/usr/bin/env python3
# Note: This script runs dnsrecon
import sys
import re
from os.path import join, exists

from dnsrecon.cli import main, print_status, print_error

from misc.get_dot import SUBDOMAIN_LIST_5000_WITHOUT_DOTS
from utils import main_executor, create_if_not_exists, OUTPUT_DIR, WILDCARD_FILE_NAME, INPUT_DIR


def batch_main(batch_name="default_batch", domain_list_path=None):
    batch_dir_name = batch_name
    if domain_list_path is None:
        domain_list_path = join(INPUT_DIR, batch_name + ".txt")
    create_if_not_exists(OUTPUT_DIR)
    batch_dir_path = join(OUTPUT_DIR, batch_dir_name)
    create_if_not_exists(batch_dir_path)

    wildcard_file_path = join(str(batch_dir_path), WILDCARD_FILE_NAME)
    print_status(f"Saving domains with wildcard to text file: {wildcard_file_path}")

    if exists(wildcard_file_path):
        print_status(f'File "{wildcard_file_path}" exists. Do you wish to continue? [Y/n]')
        i = input().lower().strip()
        if i not in ["y", "yes"]:
            print_error("Domain bruteforcing aborted.")
            return

    for domain in open(domain_list_path).readlines():
        domain_name = domain.strip()
        sys.argv = [
            './dnsrecon.py', '-d', domain_name, '-D', SUBDOMAIN_LIST_5000_WITHOUT_DOTS, '-t', 'brt', '-v', '-j',
            join(OUTPUT_DIR, batch_dir_name, domain_name + '.json'), '--aw', wildcard_file_path
        ]
        main()


if __name__ == '__main__':
    main_executor(batch_main)  # domain with wildcard
