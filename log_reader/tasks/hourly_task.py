from collections import defaultdict
from log_reader.logio import LogIO


class HourlyTask(object):

    def __init__(self, file_path, start_timestamp, end_timestamp, watched_destination_host, watched_source_host):
        self.file_path = file_path
        self.start_timestamp = int(start_timestamp)
        self.end_timestamp = int(end_timestamp)
        self.watched_destination_host = watched_destination_host
        self.watched_source_host = watched_source_host

    def run(self):
        result = HourlyTaskResult()
        def extractor(log_line):
            if not (self.start_timestamp <= log_line.unix_timestamp <= self.end_timestamp):
                return
            if log_line.destination_host == self.watched_destination_host:
                result.hosts_connected_to_watched_destination_host.add(log_line.source_host)
            if log_line.source_host == self.watched_source_host:
                result.hosts_receiving_connections_from_watched_source_host.add(log_line.destination_host)
            result.outgoing_connection_count_by_host[log_line.source_host] += 1
            
        log_io = LogIO(self.file_path)
        log_io.apply(extractor)

        return result


class HourlyTaskResult(object):
    def __init__(self):
        self.hosts_connected_to_watched_destination_host = set()
        self.hosts_receiving_connections_from_watched_source_host = set()
        self.outgoing_connection_count_by_host = defaultdict(int)
