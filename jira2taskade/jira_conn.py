import json
from jira import JIRA


class JiraConn:
    def __init__(self, config_file):
        # load config
        with open(config_file, "r") as f:
            config = json.load(f)
        self.jira = JIRA(
            server=config["jira_server"],
            basic_auth=(config["api_email"], config["api_token"]),
        )
        self.jql = config["jql"]

    def get_issues(self):
        issues = self.jira.search_issues(self.jql)
        return issues
