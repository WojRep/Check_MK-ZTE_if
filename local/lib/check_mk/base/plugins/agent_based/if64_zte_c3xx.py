#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
from typing import List
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    all_of,
    contains,
    OIDBytes,
    register,
    SNMPTree,
    type_defs,
)
from cmk.base.plugins.agent_based.utils import if64, interfaces

def parse_if64_zte_c3xx(string_table: List[type_defs.StringByteTable]):
    preprocessed_lines = []
    for line in string_table[0]:
        if not line[18]:
            line[18] = line[1]
        line = line[:20]
        preprocessed_lines.append(line[:3] + [str(int(line[3]))] + line[4:])
    return if64.generic_parse_if64([preprocessed_lines])
register.snmp_section(
    name="if64_zte_c3xx",
    parse_function=parse_if64_zte_c3xx,
    parsed_section_name="interfaces",
    fetch=[
        SNMPTree(
            base=".1.3.6.1.2.1",
            oids=[
                "2.2.1.1",  # 0 - ifIndex
                "31.1.1.1.1", # 1 - ifName (zte_c3xx has no useful information if Descr)
                "2.2.1.3",  # 2 - ifType
                "2.2.1.5",  # 3 - ifSpeed              .. 1000 means 1Gbit
                "2.2.1.8",  # 4 - ifOperStatus
                "31.1.1.1.6",  # 5 - ifHCInOctets
                "31.1.1.1.7",  # 6 - ifHCInUcastPkts
                "31.1.1.1.8",  # 7 - ifHCInMulticastPkts
                "31.1.1.1.9",  # 8 - ifHCInBroadcastPkts
                "2.2.1.13",  # 9 - ifInDiscards
                "2.2.1.14",         # 10 - ifInErrors
                "31.1.1.1.10",      # - 11 ifHCOutOctets
                "31.1.1.1.11",      # - 12 ifHCOutUcastPkts
                "31.1.1.1.12",      # - 13 ifHCOutMulticastPkts
                "31.1.1.1.13",      # - 14 ifHCOutBroadcastPkts
                "2.2.1.19",         # 15 - ifOutDiscards
                "2.2.1.20",         # 16 - ifOutErrors
                "2.2.1.21",         # 17 - ifOutQLen
                "31.1.1.1.18",      # 18 - ifAlias
                OIDBytes("2.2.1.6"),  # 19 - ifPhysAddress
                "2.2.1.2",          # 20 - ifDescr
           ],
        ),
    ],
    detect=all_of(contains(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.3902.1082.1001"), if64.HAS_ifHCInOctets),
    supersedes=['if', 'if64'],
)
