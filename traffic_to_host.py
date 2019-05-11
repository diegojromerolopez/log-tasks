import sys
from log_reader.logio import LogIO
from log_reader.tasks.traffic_to_host_task import TrafficToHostTask


if __name__ == '__main__':
    # Build a tool, that given:
    # - the name of a file (with the format described above)
    # - an init_datetime, an end_datetime,
    # - and a Hostname
    # returns a list of hostnames connected to the given host during the given period
    
    try:
        file_path = sys.argv[1]
        start_timestamp = sys.argv[2]
        end_timestamp = sys.argv[3]
        desired_destination_host = sys.argv[4]
    except IndexError:
        print("Returns a list of hostnames connected to the given host during the given period")
        print("- Use: python3 traffic_to_host.py <file_path_of_log_file>" +
              "<start_timestamp> <end_timesFtamp> <desired_destination_host>")
        print("- Example of use: python3 traffic_to_host.py input-file-10000.txt 1565647313867 1565733331098 Zoeann")
        exit(1)

    task = TrafficToHostTask(file_path, start_timestamp, end_timestamp, desired_destination_host)
    result = task.run()
    
    for host_connected_to_desired_host in result.hosts_connected_to_desired_host:
        print(host_connected_to_desired_host)
