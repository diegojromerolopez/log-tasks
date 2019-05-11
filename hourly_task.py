import operator
import sys
from log_reader.tasks.hourly_task import HourlyTask
from datetime import datetime, timedelta
from collections import defaultdict


if __name__ == '__main__':
    # The tool should both parse previously written log files and terminate or collect input from a new log file while it's being written and run indefinitely.
    # The script will output, once every hour:
    # a list of hostnames connected to a given (configurable) host during the last hour (watched_destination_host in the code)
    # a list of hostnames that received connections from a given (configurable) host during the last hour (watched_source_host in the code)
    # the hostname that generated most connections in the last hour

    # Remember to set in your crontab the following line to make it run each hour (at minute 0):
    # 0 * * * * python 3 <file_path_of_log_file>
    try:
        file_path = sys.argv[1]
        watched_destination_host = sys.argv[2]
        watched_source_host = sys.argv[3]
    except IndexError:
        print("A report of some important operations performed on the last hour")
        print("- Use: python3 hourly_task.py <file_path_of_log_file> <watched_destination_host> <watched_source_host>")
        print("- Example of use: python3 hourly_task.py input-file-10000.txt Zoeann Dekevious")
        exit(1)

    start_date = datetime.now() - timedelta(hours=1)
    start_timestamp = datetime.timestamp(start_date)
    end_date = datetime.now()
    end_timestamp = datetime.timestamp(end_date)
    
    #start_timestamp = 1565647313867
    #end_timestamp = 1565733331098

    task = HourlyTask(file_path, start_timestamp, end_timestamp, watched_destination_host, watched_source_host)
    result = task.run()

    if len(result.hosts_connected_to_watched_destination_host) > 0:
        print(f"Hosts connected to {watched_destination_host} during the last hour:")
        for hostname in result.hosts_connected_to_watched_destination_host:
            print(f"  {hostname}")
    else:
        print(f"No hosts connected to {watched_destination_host} during the last hour.")

    if len(result.hosts_receiving_connections_from_watched_source_host) > 0:
        print(f"Hosts that received connections from {watched_source_host} during the last hour:")
        for hostname in result.hosts_receiving_connections_from_watched_source_host:
            print(f"  {hostname}")
    else:
        print(f"No hosts received connections from {watched_source_host} during the last hour.")

    if len(result.outgoing_connection_count_by_host) > 0:
        host_with_max_outgoing_connections, max_outgoing_connections = max(result.outgoing_connection_count_by_host.items(), key=operator.itemgetter(1))
        print(f"Host that generated most connections in the last hour: {host_with_max_outgoing_connections} ({max_outgoing_connections} outgoing connections).")
    else:
        print(f"No hosts generated connections in the last hour.")
