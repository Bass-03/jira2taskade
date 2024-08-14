import requests


class TaskadeConn:
    def __init__(self, token):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def get_tasks(self, project_id):
        url = f"https://taskade.com/api/v1/projects/{project_id}/tasks"
        tasks = requests.get(url, headers=self.headers)
        return tasks.json()

    def create_task(self, project_id, task_content):
        url = f"https://taskade.com/api/v1/projects/{project_id}/tasks"
        data = {
            "tasks": [
                {
                    "contentType": "text/markdown",
                    "content": "text",
                    "placement": "afterbegin"
                }
            ]
        }
        task = requests.post(url, headers=self.headers, json=data)
        task.raise_for_status()
        return task.json()
