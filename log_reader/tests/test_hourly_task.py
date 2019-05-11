import operator
import os
from log_reader.tasks.hourly_task import HourlyTask


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = f"{CURRENT_DIRECTORY}/data"


def test_run():
    """
    Test basic run of HourlyTask
    """
    test_log_path = f"{DATA_DIR}/input-file-10000.txt"
    start_timestamp = 1565647313867
    end_timestamp = 1565733331098
    watched_destination_host = "Dekevious"
    watched_source_host = "Zoeann"
    task = HourlyTask(test_log_path, start_timestamp, end_timestamp, watched_destination_host, watched_source_host)
    result = task.run()

    expected_hosts_connected_to_watched_destination_host = {"Akaycia", "Tyjai", "Aubreanna", "Saraii", "Syrae",
                                                            "Sarenity", "Breylyn", "Caniyah"}
    assert expected_hosts_connected_to_watched_destination_host == result.hosts_connected_to_watched_destination_host
    assert len(result.hosts_receiving_connections_from_watched_source_host) == 0

    host_with_max_outgoing_connections, max_outgoing_connections =\
        max(result.outgoing_connection_count_by_host.items(), key=operator.itemgetter(1))
    assert "Dristen" == host_with_max_outgoing_connections
    assert 7 == max_outgoing_connections
    assert 6285 == len(result.outgoing_connection_count_by_host)


