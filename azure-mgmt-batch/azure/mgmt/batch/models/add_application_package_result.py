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


class AddApplicationPackageResult(Model):
    """Response to an ApplicationOperations.AddApplicationPackage request.

    :param id: The id of the application.
    :type id: str
    :param version: The version of the application.
    :type version: str
    :param storage_url: The URL to which the application package binary file
     should be uploaded.
    :type storage_url: str
    :param storage_url_expiry: The UTC time at which the storage URL will
     expire.
    :type storage_url_expiry: datetime
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'storage_url': {'key': 'storageUrl', 'type': 'str'},
        'storage_url_expiry': {'key': 'storageUrlExpiry', 'type': 'iso-8601'},
    }

    def __init__(self, id=None, version=None, storage_url=None, storage_url_expiry=None):
        self.id = id
        self.version = version
        self.storage_url = storage_url
        self.storage_url_expiry = storage_url_expiry
