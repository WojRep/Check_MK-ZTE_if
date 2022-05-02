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
