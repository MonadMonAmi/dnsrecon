#!/usr/bin/env python3
# Note: This script runs dnsrecon
import sys
from os.path import join

from dnsrecon import __main__

from utils import main_executor, create_if_not_exists, OUTPUT_DIR

if __name__ == '__main__':
    create_if_not_exists(OUTPUT_DIR)

    # -d a1.com -D subdomains-top1mil-5000.txt -t brt -j a1.json"
    # TODO: threads ?
    # domain_name = 'bbc.com'
    # sys.argv = ['./custom_dnsrecon.py', '-d', domain_name, '-D', join('misc', 'subdomains-top1mil-5.txt'), '-t', 'brt', '-v', '-j',
    #             join(OUTPUT_DIR, domain_name + '_5.json')]
    # sys.argv = ['./custom_dnsrecon.py', '-d', domain_name, '-D', 'subdomains-top1mil-5000.txt', '-t', 'brt', '-j',
    #             join(OUTPUT_DIR, domain_name + '_5000.json')]
    # sys.argv = ['./custom_dnsrecon.py', '-d', domain_name, '-D', join('misc', 'subdomains-store-1.txt'), '-t', 'brt', '-v', '-j',
    #             join(OUTPUT_DIR, domain_name + '_store_1.json')]

    # domain with wildcard
    domain_name = 'employmenthero.com'
    sys.argv = ['./custom_dnsrecon.py', '-d', domain_name, '-D', 'subdomains-top1mil-5000.txt', '-t', 'brt', '-v', '-j',
                join(OUTPUT_DIR, domain_name + '_5000.json')]

    # print(sys.argv)
    main_executor(__main__.main)
