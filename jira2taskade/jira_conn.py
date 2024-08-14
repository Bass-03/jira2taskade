from jira import JIRA


class JiraConn:
    def __init__(self, server, email, token):
        self.jira = JIRA(
            server=server,
            basic_auth=(email, token),
        )

    def get_issues(self, jql):
        issues = self.jira.search_issues(jql)
        result = []
        for issue in issues:
            result.append({"key": issue.key, "summary": issue.fields.summary})
        return result
