# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import threatmapper
from threatmapper.paths.deepfence_diagnosis_agent_logs_status_node_id import put  # noqa: E501
from threatmapper import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDeepfenceDiagnosisAgentLogsStatusNodeId(ApiTestMixin, unittest.TestCase):
    """
    DeepfenceDiagnosisAgentLogsStatusNodeId unit test stubs
        Update Agent Diagnostic Logs Status  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
