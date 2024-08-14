import os
from jira2taskade.config_read import ReadConfig


def test_read_config():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(test_dir, "test_config.json")
    # Call the read_config function
    config = ReadConfig(config_file)
    # Perform assertions
    config_data = {
        "jira_server": "https://fake.atlassian.net/",
        "jira_email": "fake@fake.com",
        "jira_token": "fakeToken",
        "jql": "assignee = currentUser() and sprint in openSprints() AND statusCategory != Done"
    }
    print(config.jira_token)
    assert config.jira_token == config_data["jira_token"]
    assert config.jql == config_data["jql"]
