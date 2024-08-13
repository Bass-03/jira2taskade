import os
from jira2taskade.jira_conn import JiraConn
from unittest import mock


def test_init():
    with mock.patch("jira2taskade.jira_conn.JIRA") as mock_jira:
        test_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(test_dir, "test_config.json")
        jira = JiraConn(config_file)
        # Perform assertions or further testing with the mocked JIRA object
        assert mock_jira.called  # Check if the JIRA constructor was called
        assert mock_jira.call_args == mock.call(
            server="https://fake.atlassian.net/",
            basic_auth=("fake@fake.com", "fakeToken"),
        )  # Check if the JIRA constructor was called with the correct arguments

        assert jira.jira == mock_jira.return_value


def test_get_issues():
    with mock.patch("jira2taskade.jira_conn.JIRA"):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(test_dir, "test_config.json")
        jira = JiraConn(config_file)

        # Mock the return value of get_issues
        mock_issues = mock.MagicMock()
        mock_issues.return_value = ["ISSUE-1", "ISSUE-2", "ISSUE-3"]
        jira.jira.search_issues = mock_issues

        # Call the get_issues function
        issues = jira.get_issues()

        # Perform assertions
        assert mock_issues.called
        assert issues == ["ISSUE-1", "ISSUE-2", "ISSUE-3"]


def test_get_issues_empty():
    with mock.patch("jira2taskade.jira_conn.JIRA"):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(test_dir, "test_config.json")
        jira = JiraConn(config_file)

        # Mock the return value of get_issues to be an empty list
        mock_issues = mock.MagicMock()
        mock_issues.return_value = []
        jira.jira.search_issues = mock_issues

        # Call the get_issues function
        issues = jira.get_issues()

        # Perform assertions
        assert mock_issues.called
        assert issues == []
