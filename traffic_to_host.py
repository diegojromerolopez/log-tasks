import sys
from log_reader.logio import LogIO

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
        print("- Use: python3 traffic_to_host.py <file_path_of_log_file> <start_timestamp> <end_timestamp> <desired_destination_host>")
        print("- Example of use: python3 traffic_to_host.py input-file-10000.txt 1565647313867 1565733331098 Zoeann")
        exit(1)
    
    start_timestamp = LogIO.convert_datetime_to_timestamp(start_timestamp)
    end_timestamp = LogIO.convert_datetime_to_timestamp(end_timestamp)

    those_connected_to_desired_host = set()
    def hosts_connected_to_desired_host_extractor(log_line):
        if start_timestamp <= log_line.unix_timestamp <= end_timestamp and log_line.destination_host == desired_destination_host:
            those_connected_to_desired_host.add(log_line.source_host)

    log_io = LogIO(file_path)
    log_io.apply(hosts_connected_to_desired_host_extractor)
    
    for this_connected_to_desired_host in those_connected_to_desired_host:
        print(this_connected_to_desired_host)
