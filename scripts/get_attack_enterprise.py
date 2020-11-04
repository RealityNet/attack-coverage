#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Written by Francesco "dfirfpi" Picasso, Reality Net System Solutions
#
# Version: 20200831

from attackcti import attack_client
lift = attack_client()
all_enterprise = lift.get_enterprise(stix_format=False)

for entry in all_enterprise:
    with open('attack_' + entry + '.txt', mode='w', encoding='utf-8') as fout:
        for subentry in all_enterprise[entry]:
            fout.write('{}\n'.format(subentry))