from file_read_backwards import FileReadBackwards


# Assumptions:
# Log file is ordered in ascending date (timestamp) order.
# Log file stores its dates in UTC (not going to worry about timezones).
class LogIO(object):
    """
    Reads a log file efficiently (i.e. without storing it fully in memory).
    """

    # The log lines might be out of order by maximum 5 minutes (300 s)
    MAX_TIME_OFFSET = 300

    # Used as a signal to mark that the read must be stopped
    STOP_READ = "STOP READ"

    def __init__(self, file_path, encoding='utf-8'):
        """
        Construct a new LogIO object.
        """
        self.file_path = file_path
        self.encoding = encoding

    def apply(self, function):
        """
        Apply a function to each line of the log file starting from the begin of the file.
        """
        return self._apply(open, function)

    def reversed_apply(self, function):
        """
        Apply a function to each line of the log file starting from the ending of the file.
        """
        return self._apply(FileReadBackwards, function)

    def _apply(self, file_opener, function):
        """
        Apply a function to each line of the log file.
        :param file_opener A function that opens a file and returns a file descriptor.
        :param lambda A function that will be applied to each log line.
        """
        read_lines = 0
        with file_opener(self.file_path, encoding=self.encoding) as reversed_log_file:
            for file_line in reversed_log_file:
                log_line = LogLine.build_from_line(file_line.strip())
                read_lines += 1
                if function(log_line) == LogIO.STOP_READ:
                    break
        return read_lines


# A log line of the log file
class LogLine(object):
    """
    A log line
    """

    def __init__(self, unix_timestamp, source_host, destination_host):
        """
        Constructs a log line from its parts
        :param unix_timestamp: UNIX timestamp.
        :param source_host: source host
        :param destination_host: destination host
        """
        self.unix_timestamp = int(unix_timestamp)
        self.source_host = source_host
        self.destination_host = destination_host

    @staticmethod
    def build_from_line(line):
        """
        Static method that builds a LogLine object from a str (a log line).
        :param line: a str with a log line.
        :return: LogLine object.
        """
        unix_timestamp, source_host, destination_host = line.split(' ')
        return LogLine(unix_timestamp, source_host, destination_host)
