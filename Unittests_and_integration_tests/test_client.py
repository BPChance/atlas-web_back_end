#!/usr/bin/env python3
""" client.py testing """


import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos, TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Test Github Org Client """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """ test that it returns correct value """
        test_payload = {"name": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """ test that it returns correct value """
        test_payload = {"repos_url": "https://expected.url"}

        # patch org property to return payload
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("testorg")
            result = client._public_repos_url
            # make sure result is = to expected URL
            self.assertEqual(result, test_payload["repos_url"])
            # ensure mock org property is called once
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ test public_repos returns repos and uses mock correctly """
        # data to be returned
        test_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache"}}
        ]
        mock_get_json.return_value = test_payload

        # mock the property so it returns predefined url
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            # set fake url to return
            mock_public_repos_url.return_value = "https://fake.url/repos"
            client = GithubOrgClient("test_org")
            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://fake.url/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ test has_license returns correctly """
        result = GithubOrgClient.has_license(repo, license_key)
        # verify return is as expected
        self.assertEqual(result, expected)

# [
#    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos}
#]
@parameterized_class(TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ test for integration of GithubOrgClient """

    @classmethod
    def mocked_requests_get(cls, url, *args, **kwargs):
        """ mock side_effect function fo requests.get """
        if "orgs" in url:
            mock_response = Mock()
            mock_response.json.return_value = org_payload
            return mock_response
        elif "repos" in url:
            mock_response.json.return_value = repos_payload
            return mock_response
        return None

    @classmethod
    def setUpClass(cls):
        """ set up mocks for requests.get """
        cls.get_patcher = patch('requests.get', side_effect=cls.mocked_requests_get)
        # start patcher and make mock available for tests
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ stop the patcher """
        # stop patcher so requests.get goes back to normal behavior
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ test public_repos """
        # create client with example org
        client = GithubOrgClient("example")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ test public_repos with license filter """
        client = GithubOrgClient("example")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
