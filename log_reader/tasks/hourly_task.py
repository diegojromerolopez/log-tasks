from collections import defaultdict
from log_reader.logio import LogIO


class HourlyTask(object):
    """
    Represent the task that will be performed hourly over our log file
    """

    def __init__(self, file_path, start_timestamp, end_timestamp, watched_destination_host, watched_source_host):
        """
        The hourly task
        :param file_path: log file path
        :param start_timestamp: start date in UNIX timestamp
        :param end_timestamp: end date in UNIX timestamp
        :param watched_destination_host: host whose incoming connections will be monitored.
        :param watched_source_host:  host whose outgoing connections will be monitored.
        """
        self.file_path = file_path
        self.start_timestamp = int(start_timestamp)
        self.end_timestamp = int(end_timestamp)
        self.watched_destination_host = watched_destination_host
        self.watched_source_host = watched_source_host

    def run(self):
        """
        Run the task
        :return: A HourlyTaskResult object.
        """

        result = HourlyTaskResult()
        
        def reversed_extractor(log_line):
            """
            Lambda function that will be applied to each log line.
            :param log_line: LogLine object.
            :return: LogIO.STOP_READ if it must not be following reading the file.
            """
            # Assuming the log file is roughly sorted by timestamp (as it should be), as we are reading from the end of
            # the file, reading a log line with a timestamp (minus an offset) lesser than the start timestamp means
            # the read has been completed.
            if log_line.unix_timestamp - LogIO.MAX_TIME_OFFSET < self.start_timestamp:
                return LogIO.STOP_READ

            # Update the result
            if self.start_timestamp <= log_line.unix_timestamp <= self.end_timestamp:
                result.update(log_line, self.watched_destination_host, self.watched_source_host)
            
        log_io = LogIO(self.file_path)
        log_io.reversed_apply(reversed_extractor)

        return result


class HourlyTaskResult(object):
    """
    Stores a result of the hourly task
    """

    def __init__(self):
        """
        Constructs a hourly result.
        """
        self.hosts_connected_to_watched_destination_host = set()
        self.hosts_receiving_connections_from_watched_source_host = set()
        self.outgoing_connection_count_by_host = defaultdict(int)

    def update(self, log_line, watched_destination_host, watched_source_host):
        """
        Updates a hourly result based on a log_line and the watched destination and source host.
        :param watched_destination_host: host whose incoming connections will be monitored.
        :param watched_source_host:  host whose outgoing connections will be monitored.
        """
        if log_line.destination_host == watched_destination_host:
            self.hosts_connected_to_watched_destination_host.add(log_line.source_host)
        if log_line.source_host == watched_source_host:
            self.hosts_receiving_connections_from_watched_source_host.add(log_line.destination_host)
        self.outgoing_connection_count_by_host[log_line.source_host] += 1
