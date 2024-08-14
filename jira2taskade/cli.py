import os
import typer
from typing import List, Optional
from jira2taskade.jira_conn import JiraConn
from jira2taskade.config_read import ReadConfig
from jira2taskade.taskade_conn import TaskadeConn

app = typer.Typer()


@app.callback()
def initialize():
    global CONFIG
    home_dir = os.path.expanduser("~")
    config_path = os.path.join(home_dir, ".config", "jira2taskade", "config.json")
    CONFIG = ReadConfig(config_path)


@app.command()
def tasks(project: str):
    """
        Get Tasks from Taskade
    """
    taskade = TaskadeConn(CONFIG.taskade_token)
    tasks = taskade.get_tasks(project)
    for task in tasks["items"]:
        if task.get("parentId") and not task["completed"]:
            # Print only not completed tasks
            typer.echo(task["text"])


@app.command()
def issues(server: str):
    """
        Get Issues from Jira
    """
    jira = JiraConn(server, CONFIG.jira_email, CONFIG.jira_token)
    issues = jira.get_issues(CONFIG.jql)
    for issue in issues:
        typer.echo(f"{issue['key']}: {issue['summary']}")


@app.command()
def issues_to_tasks(taskade_project: str, server: Optional[List[str]] = typer.Option(None)):
    """
        Get Tasks from Taskade and Issues from Jira
    """
    if not server:
        typer.echo("Please provide a list of Jira servers names")
        raise typer.Abort()
    for svr in server:
        server_url = "https://" + svr + ".atlassian.net"
        jira = JiraConn(server_url, CONFIG.jira_email, CONFIG.jira_token)
        issues = jira.get_issues(CONFIG.jql)
        taskade = TaskadeConn(CONFIG.taskade_token)
        tasks = taskade.get_tasks(taskade_project)
        if not tasks.get("ok"):
            typer.echo(f"Taskade Error: {tasks['message']}")
            raise typer.Abort()
        # Check Issues are not already tasks
        for issue in issues:
            typer.echo(f"Processing {issue['key']}")
            if all(issue['key'] not in task["text"] for task in tasks['items']):
                issue_url = f"https://{svr}.atlassian.net/browse/{issue['key']}"
                issue_link = f"[{issue['key']}]({issue_url})"
                task_text = f"{issue_link}: {issue['summary']}"
                # typer.echo(f"Task Text: {task_text}")
                taskade.create_task(taskade_project, task_text)
                typer.echo(f"Created Task for {issue['key']}")

            else:
                typer.echo(f"Task for {issue['key']} already exists")


if __name__ == "__main__":
    app()
