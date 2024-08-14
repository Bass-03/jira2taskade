import requests


class TaskadeConn:
    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_tasks(self, project_id):
        url = f"https://api.taskade.com/v1/projects/{project_id}/tasks"
        tasks = requests.get(url, headers=self.headers)
        return tasks.content

    def create_task(self, project_id, task_content):
        url = f"https://api.taskade.com/v1/projects/{project_id}/tasks"
        data = {
            "tasks": [
                {
                    "contentType": "text/markdown",
                    "content": "text",
                    "placement": "afterbegin"
                }
            ]
        }
        req = requests.post(url, headers=self.headers, json=data)
        req.raise_for_status()
        return req.content
