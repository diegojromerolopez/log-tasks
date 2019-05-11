import argparse
import operator
from log_reader.tasks.hourly_task import HourlyTask
from datetime import datetime, timedelta


if __name__ == '__main__':
    # The tool should both parse previously written log files and terminate or collect input from a new log file
    # while it's being written and run indefinitely.
    # The script will output, once every hour:
    # a list of host names connected to a given (configurable) host during the last hour (i.e. watched_destination_host)
    # a list of host names that received connections from a given (configurable)
    # host during the last hour (i.e. watched_source_host) the hostname that generated most connections in the last hour

    parser = argparse.ArgumentParser(description='A report of some important operations performed on the last hour')
    parser.add_argument('-f', '--file_path', type=str, help='log file path', required=True)
    parser.add_argument('-wdh', '--watched_destination_host', type=str, help='Host whose connected hosts will be shown', required=True)
    parser.add_argument('-wsh', '--watched_source_host', type=str, help='Host whose outgoing hosts will be shown', required=True)
    args = parser.parse_args()

    start_date = datetime.now() - timedelta(hours=1)
    start_timestamp = datetime.timestamp(start_date)
    end_date = datetime.now()
    end_timestamp = datetime.timestamp(end_date)

    task = HourlyTask(args.file_path, start_timestamp, end_timestamp, args.watched_destination_host, args.watched_source_host)
    result = task.run()

    if len(result.hosts_connected_to_watched_destination_host) > 0:
        print(f"Hosts connected to {args.watched_destination_host} during the last hour:")
        for hostname in result.hosts_connected_to_watched_destination_host:
            print(f"  {hostname}")
    else:
        print(f"No hosts connected to {args.watched_destination_host} during the last hour.")

    if len(result.hosts_receiving_connections_from_watched_source_host) > 0:
        print(f"Hosts that received connections from {args.watched_source_host} during the last hour:")
        for hostname in result.hosts_receiving_connections_from_watched_source_host:
            print(f"  {hostname}")
    else:
        print(f"No hosts received connections from {args.watched_source_host} during the last hour.")

    if len(result.outgoing_connection_count_by_host) > 0:
        host_with_max_outgoing_connections, max_outgoing_connections = max(
            result.outgoing_connection_count_by_host.items(), key=operator.itemgetter(1))
        print(
            f"Host that generated most connections in the last hour:" +
            " {host_with_max_outgoing_connections} ({max_outgoing_connections} outgoing connections)."
        )
    else:
        print(f"No hosts generated connections in the last hour.")
