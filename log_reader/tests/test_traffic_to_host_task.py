import operator
import os
from log_reader.tasks.traffic_to_host_task import TrafficToHostTask


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = f"{CURRENT_DIRECTORY}/data"


def test_run():
    """
    Test basic run of TrafficToHostTask
    """
    test_log_path = f"{DATA_DIR}/input-file-10000.txt"
    start_timestamp = 1565647313867
    end_timestamp = 1565733331098
    desired_destination_host = "Zoeann"

    task = TrafficToHostTask(test_log_path, start_timestamp, end_timestamp, desired_destination_host)
    result = task.run()
    expected_hosts_connected_to_desired_host = {'Kalun', 'Zaid', 'Sheylynn', 'Kayjah', 'Wuilber', 'Temon', 'Brydin',
                                                'Osualdo', 'Djamila', 'Maigen', 'Krikor', 'Aleece', 'Desaree',
                                                'Augustina', 'Danyae'}
    assert expected_hosts_connected_to_desired_host == result.hosts_connected_to_desired_host
