import os
import pytest
from unittest import mock
from jira2taskade.jira_conn import JiraConn
from jira2taskade.config_read import ReadConfig


@pytest.fixture
def config():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(test_dir, "test_config.json")
    return ReadConfig(config_file)


def test_init(config):
    with mock.patch("jira2taskade.jira_conn.JIRA") as mock_jira:
        jira = JiraConn("sample_server", config.jira_email, config.jira_token)
        # Perform assertions or further testing with the mocked JIRA object
        assert mock_jira.called  # Check if the JIRA constructor was called
        assert mock_jira.call_args == mock.call(
            server="sample_server",
            basic_auth=(config.jira_email, config.jira_token),
        )  # Check if the JIRA constructor was called with the correct arguments

        assert jira.jira == mock_jira.return_value


def test_get_issues(config):
    with mock.patch("jira2taskade.jira_conn.JIRA"):
        jira = JiraConn("sample_server", config.jira_email, config.jira_token)
        # Mock the return value of get_issues
        mock_issue_1 = mock.Mock()
        mock_issue_1.key = "ISSUE-1"
        mock_issue_1.fields.summary = "Issue summary 1"

        mock_issue_2 = mock.Mock()
        mock_issue_2.key = "ISSUE-2"
        mock_issue_2.fields.summary = "Issue summary 2"

        mock_issue_3 = mock.Mock()
        mock_issue_3.key = "ISSUE-3"
        mock_issue_3.fields.summary = "Issue summary 3"

        mock_issues = [mock_issue_1, mock_issue_2, mock_issue_3]
        jira.jira.search_issues = mock.Mock(return_value=mock_issues)

        # Call the get_issues function
        issues = jira.get_issues(config.jql)

        # Perform assertions
        assert jira.jira.search_issues.called
        assert len(issues) == 3


def test_get_issues_empty(config):
    with mock.patch("jira2taskade.jira_conn.JIRA"):
        jira = JiraConn("sample_server", config.jira_email, config.jira_token)
        # Mock the return value of get_issues to be an empty list
        mock_issues = mock.MagicMock()
        mock_issues.return_value = []
        jira.jira.search_issues = mock_issues

        # Call the get_issues function
        issues = jira.get_issues(config.jql)

        # Perform assertions
        assert mock_issues.called
        assert issues == []
