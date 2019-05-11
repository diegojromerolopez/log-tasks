from log_reader.logio import LogIO


class TrafficToHostTask(object):
    def __init__(self, file_path, start_timestamp, end_timestamp, desired_destination_host):
        self.file_path = file_path
        self.start_timestamp = int(start_timestamp)
        self.end_timestamp = int(end_timestamp)
        self.desired_destination_host = desired_destination_host
    
    def run(self):
        result = TrafficToHostTaskResult()
        def hosts_connected_to_desired_host_extractor(log_line):
            if self.start_timestamp <= log_line.unix_timestamp <= self.end_timestamp and log_line.destination_host == self.desired_destination_host:
                result.update(log_line.source_host)

        log_io = LogIO(self.file_path)
        log_io.apply(hosts_connected_to_desired_host_extractor)

        return result


class TrafficToHostTaskResult(object):
    def __init__(self):
        self.hosts_connected_to_desired_host = set()
    
    def update(self, source_host):
        self.hosts_connected_to_desired_host.add(source_host)