import json
from dataclasses import dataclass


@dataclass
class Config:
    jira_email: str
    jira_token: str
    jql: str
    taskade_token: str


def read_config(config_file):
    with open(config_file, "r") as f:
        config = json.load(f)
    return config


class ReadConfig:
    def __new__(cls, config_file):
        config_dict = read_config(config_file)
        return Config(**config_dict)
