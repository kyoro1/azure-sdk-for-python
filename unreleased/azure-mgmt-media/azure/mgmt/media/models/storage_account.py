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


class StorageAccount(Model):
    """The properties of a storage account associated with this resource.

    :param id: The id of the storage account resource.
    :type id: str
    :param is_primary: Is this storage account resource the primary storage
     account for the Media Service resource.
    :type is_primary: bool
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_primary': {'key': 'isPrimary', 'type': 'bool'},
    }

    def __init__(self, id=None, is_primary=None):
        self.id = id
        self.is_primary = is_primary
