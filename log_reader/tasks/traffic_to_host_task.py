from log_reader.logio import LogIO


class TrafficToHostTask(object):
    """
    Traffic to host task
    """

    def __init__(self, file_path, start_timestamp, end_timestamp, desired_destination_host):
        """
        Constructs the traffic to host task.
        :param file_path: log file path
        :param start_timestamp: start date in UNIX timestamp.
        :param end_timestamp: end date in UNIX timestamp.
        :param desired_destination_host: host that is the destination of connections.
        """
        self.file_path = file_path
        self.start_timestamp = int(start_timestamp)
        self.end_timestamp = int(end_timestamp)
        self.desired_destination_host = desired_destination_host
    
    def run(self):
        """
        Run the task
        :return: LogIO.STOP_READ if the read must be stopped.
        """

        result = TrafficToHostTaskResult()

        def hosts_connected_to_desired_host_extractor(log_line):
            # Assuming the file is roughly ordered by timestamp (as any log file should be)
            # if the log line is has a greater date than the end timestamp (and the max allowed log line offset),
            # that line (and the next ones) must not be read. Our read is complete.
            if log_line.unix_timestamp + LogIO.MAX_TIME_OFFSET > self.end_timestamp:
                return LogIO.STOP_READ
            # Update the result only if the log line is in the date interval and its destination host is the desired one
            if (
                    self.start_timestamp <= log_line.unix_timestamp <= self.end_timestamp and
                    log_line.destination_host == self.desired_destination_host
               ):
                result.update(log_line.source_host)

        log_io = LogIO(self.file_path)
        log_io.apply(hosts_connected_to_desired_host_extractor)

        return result


# A traffic host task result
class TrafficToHostTaskResult(object):
    """
    A container that stores the result for the TrafficToHostTask
    """

    def __init__(self):
        """
        Construct a traffic host task result
        """

        self.hosts_connected_to_desired_host = set()
    
    def update(self, source_host):
        """
        Updates the result
        :param source_host: log file source host.
        """
        self.hosts_connected_to_desired_host.add(source_host)
