#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# get_tt: Get (Attack) T(echniques) T(actics)
# Written by Francesco "dfirfpi" Picasso, Reality Net System Solutions
#
# Version: 20200831

import bisect
import sys
from attackcti import attack_client

# -----------------------------------------------------------------------------

CSV_SEPARATOR = ','
CSV_INTERNAL_SEPARATOR = '|'
NEWLINE = '\n'
UNSPECIFIED_TACTIC = 'unspecified'

# -----------------------------------------------------------------------------

class ATechnique():

    def __init__(self, identifier, name):

        # Due to sub-techniques, create a "new" column with the main technique.
        self._technique = identifier.split('.')[0]

        self._id = identifier
        self._name = '{} ({})'.format(name, self._id)
        self._tactics = []
        self._data_sources = []
        self._data_sources_num = 0

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def technique(self):
        return self._technique

    @property
    def tactics(self):
        return self._tactics

    @property
    def data_sources(self):
        return self._data_sources

    @property
    def data_sources_num(self):
        return self._data_sources_num

    def add_data_source(self, data_source):
        self._data_sources.append(data_source)
        self._data_sources_num += 1

    def add_tactic(self, tactic):
        self._tactics.append(tactic)

    def tactics_csv_row(self, newline=None):
        
        assert len(self.tactics) >= 1
        
        for tactic in self.tactics:
            row = CSV_SEPARATOR.join((tactic,
                                      self.technique,
                                      self.id,
                                      self.name))
            row = row + newline if newline else row
            yield row

    def techniques_csv_row(self, newline=None):
        
        assert len(self.tactics) >= 1
        tactics = self.tactics[0]
        if len(self.tactics) > 1:
            tactics = CSV_INTERNAL_SEPARATOR.join(x for x in self.tactics)

        if len(self.data_sources) == 1:
            data_sources = self.data_sources[0]
        elif len(self.data_sources) > 1:
            data_sources = CSV_INTERNAL_SEPARATOR.join(
                x for x in self.data_sources)
        else:
            data_sources = ''

        row = CSV_SEPARATOR.join((self.technique,
                                  self.id,
                                  self.name,
                                  tactics,
                                  data_sources,
                                  str(self.data_sources_num)))
        row = row + newline if newline else row
        return row
        
    def tactics_csv_header(newline=None):
        header = CSV_SEPARATOR.join(('name',
                                     'technique',
                                     'technique_id',
                                     'technique_name'))
        header = header + newline if newline else header
        return header

    def techniques_csv_header(newline=None):
        header = CSV_SEPARATOR.join(('technique',
                                     'id',
                                     'name',
                                     'tactics',
                                     'data_sources',
                                     'data_sources_num'))
        header = header + newline if newline else header
        return header
        
# -----------------------------------------------------------------------------

def get_techniques():

    lift = attack_client()
    all_enterprise = lift.get_enterprise(stix_format=False)
    
    data_sources_dict = {}
    techniques_dict =  {}

    for technique in all_enterprise['techniques']:
    
        technique_id = technique['technique_id']
        technique_name = technique['technique']
        
        technique_obj = ATechnique(technique_id, technique_name)
        
        if 'tactic' in technique:
            for tactic in technique['tactic']:
                technique_obj.add_tactic(tactic)
        else:
            technique_obj.add_tactic(UNSPECIFIED_TACTIC)

        if 'data_sources' in technique:
            for data_source in technique['data_sources']:
                technique_obj.add_data_source(data_source)
                if data_source not in data_sources_dict:
                    data_sources_dict[data_source] = data_source

        assert technique_id not in techniques_dict
        techniques_dict[technique_id] = technique_obj

    return techniques_dict, data_sources_dict

# -----------------------------------------------------------------------------

def save_data_sources(data_sources):

    with open('data_sources.csv', mode='w', encoding='utf-8') as fout:
        fout.write('data sources\n')
        for k, v in sorted(data_sources.items()):
            fout.write('{}\n'.format(k))

# -----------------------------------------------------------------------------

def save_tactis(techniques):

    with open('tactics.csv', mode='w', encoding='utf-8') as fout:
        fout.write(ATechnique.tactics_csv_header(NEWLINE))

        tactics_list = []
        for technique_id, technique in techniques.items():
            assert technique_id == technique.id
            for tactic in technique.tactics_csv_row(NEWLINE):
                bisect.insort(tactics_list, tactic)
        
        for tactic in tactics_list:
            fout.write(tactic)

# -----------------------------------------------------------------------------

def save_techniques(techniques):

    with open('techniques.csv', mode='w', encoding='utf-8') as fout:
        fout.write(ATechnique.techniques_csv_header(NEWLINE))
        
        for technique_id, technique in sorted(techniques.items()):
            assert technique_id == technique.id
            fout.write(technique.techniques_csv_row(NEWLINE))

# -----------------------------------------------------------------------------

if __name__ == '__main__':

    if sys.version_info[0] < 3:
        sys.exit('Python 3 or a more recent version is required.')

    techniques = {}
    techniques, data_sources = get_techniques()
    save_tactis(techniques)
    save_techniques(techniques)
    save_data_sources(data_sources)
