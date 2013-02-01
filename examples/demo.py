#!/usr/bin/env python
'''
CybOX Common Indicator API Demo

Demonstrates the use of the Cybox Common Indicator API.
Creates a CybOX Observables document containing a
'''

import sys
from cybox import api

def main():
    '''Build a CybOX Observables document and write it to stdout'''
    domain = api.create_domain_name_observable('www.example.com')
    url = api.create_url_observable('http://www.example.com')
    ipv4 = api.create_ipv4_observable('127.0.0.1')
    email = api.create_email_address_observable('cybox@mitre.org')
    #hash = api.create_file_hash_observable('foo.bar','94f93e00fd122466d68a6ae3b8c7f908','MD5')

    observables_doc = api.create_observables_document([domain,
                                                        ipv4,
                                                        url,
                                                        email,
                                                        #hash,
                                                       ] )
    observables_doc.export(sys.stdout, 0)

if __name__ == "__main__":
    main()
    sys.exit()
