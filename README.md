# log-tasks

## Introduction

These two tasks show how to deal with log files in Python3.

## Requirements

- Python3 version 3.6 or later (you should have it in your OS).
- Packages included in [requirements.txt](requirements.txt).

## Installation

### Option 1 (recommended): use virtualenv and run the code from the project

You should use a virtualenv or some tool to avoid installing packages in your system.

This will create a python3 virtualenv with the name venv:

```bash
$ virtualenv -p python3 venv
```

Activate the virtualenv

```bash
$ source ./venv/bin/activate
```

Run the following command to install requirements:

```bash
(venv)$ pip install requirements.txt
```

(make sure pip is using python3)

Now you can run the scripts:

- traffic_to_host.py
- hourly_task.py

from the root directory.
 

### Option 2: install python package in dist directory

NOTE: this is not the recommended way of releasing a python package.
The package should be in a repository like [pypi](https://pypi.org/) but restricted to the members of the team
(Read [How to Create a Private Python Package Repository](https://www.linode.com/docs/applications/project-management/how-to-create-a-private-python-package-repository/)). 

Create a virtualenv (to not pollute the python system package)

Install the package (it is already commited to github in the **dist** directory):

```bash
(venv)$ pip3 install dist/log-tasks-1.0.tar.gz
```

Now you have two new python binaries directory and can run them it by typing:

```bash
(venv)$ python3 ./venv/bin/traffic_to_host.py
```

```bash
(venv)$ python3 ./venv/bin/hourly_task.py
```

## Tasks

**Move to the root directory of this project**,
i.e. the root directory of this repository should be your current working directory.

Note that running the scripts without parameters show how to use them.

### Traffic to host

Given the name of a file (with the format described above), an  init_datetime , an end_datetime , and a Hostname,
returns a list of hostnames connected to the given host during the given period.

```bash
python3 traffic_to_host.py -f log_reader/tests/data/input-file-10000.txt -init <start timestamp> -end <end timestamp> -host <Host to monitor traffic>
```

Note that if there is no hostnames connected to the given host, nothing will be printed by standard output.

#### Example

```bash
$ python3 traffic_to_host.py -f log_reader/tests/data/input-file-10000.txt -init 1565647313867 -end 1565733331098 -host Zoeann
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
$ python3 hourly_task.py -f log_reader/tests/data/input-file-10000.txt -wdh <watched_destination_host> -wsh <watched_source_host>
```

Where:
- watcher_destination_host is the host whose connected hosts this task will show.
- watcher_source_host is the host whose connections to other hosts this task will show.

Please, take in account that this script will not output anything if you don't have the correct dates in your log file.

#### Example

```bash
$ python3 hourly_task.py -f log_reader/tests/data/input-file-10000.txt -wdh Dekevious -wsh Zoeann
```

## Tests
Tests developed with pytest.

To run them, please, set your current directory to this repository root directory and type the following command.

```bash
$ pytest
```

Please note that pytest is a requirement for this project (it is already included in requirements.txt).

## TODO
- Review naming of modules. It could be improved.
- Make more tests.
