# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FirewallRuleProperties(Model):
    """Data Lake Store firewall rule properties information.

    :param start_ip_address: the start IP address for the firewall rule.
    :type start_ip_address: str
    :param end_ip_address: the end IP address for the firewall rule.
    :type end_ip_address: str
    """ 

    _attribute_map = {
        'start_ip_address': {'key': 'startIpAddress', 'type': 'str'},
        'end_ip_address': {'key': 'endIpAddress', 'type': 'str'},
    }

    def __init__(self, start_ip_address=None, end_ip_address=None):
        self.start_ip_address = start_ip_address
        self.end_ip_address = end_ip_address
