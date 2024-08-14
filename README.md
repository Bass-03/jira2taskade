# jira2taskade

[![Python Basics](https://github.com/Bass-03/jira2taskate/actions/workflows/python-app.yml/badge.svg)](https://github.com/Bass-03/jira2taskate/actions/workflows/python-app.yml)

`jira2taskade` is a Python project that integrates with JIRA to fetch issues based on JQL queries.

## Table of Contents

- [jira2taskade](#jira2taskade)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Testing](#testing)
  - [Install the thing](#install-the-thing)
  - [License](#license)

## Installation

To install the project dependencies, use [Poetry](https://python-poetry.org/):

``` bash
poetry install
```

## Configuration

Create a configuration file config.json in the root directory of the project with the following structure:

``` json
{
    "jira_email": "your-email@example.com",
    "jira_token": "your-api-token",
    "jql": "your-jql-query",
    "taskade_token": "taskade-token"
}
```

You can use the provided config_sample.json as a template.

## Usage

To use the JiraConn class, import it and initialize it with the path to your configuration file:

``` python
from jira2taskade.jira_conn import JiraConn

config_file = "path/to/your/config.json"
jira_conn = JiraConn(config_file)

issues = jira_conn.get_issues()
for issue in issues:
    print(issue)
```

## Testing

To run the tests, use pytest:

``` bash
poetry run pytest
```

## Install the thing

Create a config file at `~/.config/jira2taskade/config.json` 

Install the package using pipx:

``` bash
poetry build
pipx install dist/jira2taskade-0.1.0-py3-none-any.whl

```

## License

This project is licensed under the MIT License.
