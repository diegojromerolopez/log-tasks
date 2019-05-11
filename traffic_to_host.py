import argparse
from log_reader.tasks.traffic_to_host_task import TrafficToHostTask


if __name__ == '__main__':
    # Build a tool, that given:
    # - the name of a file (with the format described above)
    # - an init_datetime, an end_datetime,
    # - and a Hostname
    # returns a list of hostnames connected to the given host during the given period

    parser = argparse.ArgumentParser(
        description='A report that returns the list of hostnames connected to the given host during a period of time'
    )
    parser.add_argument('-f', '--file_path', type=str, help='log file path', required=True)
    parser.add_argument('-init', '--init_datetime', type=int, help='Init datetime as an UNIX timestamp', required=True)
    parser.add_argument('-end', '--end_datetime', type=int, help='End datetime as an UNIX timestamp', required=True)
    parser.add_argument('-host', '--hostname', type=str, help='Hostname', required=True)
    args = parser.parse_args()

    task = TrafficToHostTask(args.file_path, args.init_datetime, args.end_datetime, args.hostname)
    result = task.run()
    
    for host_connected_to_desired_host in result.hosts_connected_to_desired_host:
        print(host_connected_to_desired_host)
