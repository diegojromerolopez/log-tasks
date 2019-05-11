# log-tasks

## Introduction

These two tasks show how to deal with log files in Python3.

## Requirements

- Python3 version 3.6 or later (you should have it in your OS).
- Packages included in [requirements.txt](requirements.txt).

You should use a virtualenv or some tool to avoid installing packages in your system.

This will create a python3 virtualenv with the name venv:

```bash
$ virtualenv -p python3 venv
```

Activate the virtualenv

```bash
$ ./venv/bin/activate
```

Run the following command to install requirements:

```bash
(venv)$ pip install requirements.txt
```

(make sure pip is using python3)

## Tasks

**Move your current working directory to the root directory of this project**,
i.e. the root directory of this repository (where this README.md file resides).

Note that running the scripts without parameters show how to use them.

### Traffic to host

Given the name of a file (with the format described above), an  init_datetime , an end_datetime , and a Hostname,
returns a list of hostnames connected to the given host during the given period.

```bash
python3 traffic_to_host.py log_reader/tests/data/input-file-10000.txt <start timestamp> <end timestamp> <Host to monitor traffic>
```

#### Example

```bash
$ python3 traffic_to_host.py log_reader/tests/data/input-file-10000.txt 1565647313867 1565733331098 Zoeann
```
Output:
```bash
Danyae
Sheylynn
Kalun
Brydin
Krikor
Temon
Djamila
Desaree
Wuilber
Augustina
Osualdo
Kayjah
Zaid
Aleece
Maigen
```

### Hourly task

```bash
$ python3 hourly_task.py log_reader/tests/data/input-file-10000.txt <watched_destination_host> <watched_source_host>
```

Where:
- watcher_destination_host is the host whose connected hosts this task will show.
- watcher_source_host is the host whose connections to other hosts this task will show.

Please, take in account that this script will not output anything if you don't have the correct dates in your log file.

#### Example

```bash
$ python3 hourly_task.py log_reader/tests/data/input-file-10000.txt Dekevious Zoeann
```

## Tests
Tests developed with pytest.

To run them, please, set your current directory to this repository root directory and type the following command.

```bash
$ pytest
```

Please note that pytest is a requirement for this project (it is already included in requirements.txt).