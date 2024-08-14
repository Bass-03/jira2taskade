import os
import pytest
from unittest import mock
from jira2taskade.config_read import ReadConfig
from jira2taskade.taskade_conn import TaskadeConn


@pytest.fixture
def config():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(test_dir, "test_config.json")
    return ReadConfig(config_file)


def test_get_tasks(config):
    with mock.patch("jira2taskade.taskade_conn.requests.get") as mock_get:
        taskade = TaskadeConn(config.taskade_token)
        mock_response = mock.Mock()
        mock_response.json.return_value = {"tasks": ["task1", "task2", "task3"]}
        mock_get.return_value = mock_response

        tasks = taskade.get_tasks("project_id")

        assert mock_get.called3
        assert tasks == {"tasks": ["task1", "task2", "task3"]}


def test_create_task(config):
    with mock.patch("jira2taskade.taskade_conn.requests.post") as mock_post:
        taskade = TaskadeConn(config.taskade_token)
        mock_response = mock.Mock()
        mock_response.json.return_value = {"task_id": "123"}
        mock_post.return_value = mock_response

        task = taskade.create_task("project_id", "task_content")

        assert mock_post.called
        assert task == {"task_id": "123"}
