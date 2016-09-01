"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import unittest
from mock import MagicMock
from mock import Mock
import requests

from cloudcafe.objectstorage.objectstorage_api import behaviors
from cloudcafe.objectstorage.objectstorage_api import client as obj_client
from cloudcafe.objectstorage.objectstorage_api import config as obj_config
from metatests.objectstorage.objectstorage_api import test_client


class ApiBehaviorsTest(unittest.TestCase):

    def test_create_container(self):
        response = Mock(spec=requests.Response)
        response.ok = True

        client = Mock(spec=obj_client.ObjectStorageAPIClient)
        client.create_container = MagicMock(return_value=response)

        config = Mock(spec=obj_config.ObjectStorageAPIConfig)

        behavior = behaviors.ObjectStorageAPI_Behaviors(client, config)
        behavior.create_container(test_client.VALID_CONTAINER_NAME)
        client.create_container.assert_called_with(
            test_client.VALID_CONTAINER_NAME, headers={})

    def test_throws_exception_if_create_container_fails(self):
        response = Mock(spec=requests.Response)
        response.ok = False

        client = Mock(spec=obj_client.ObjectStorageAPIClient)
        client.create_container = MagicMock(return_value=response)

        config = Mock(spec=obj_config.ObjectStorageAPIConfig)

        behavior = behaviors.ObjectStorageAPI_Behaviors(client, config)
        with self.assertRaises(Exception):
            behavior.create_container(test_client.VALID_CONTAINER_NAME)
