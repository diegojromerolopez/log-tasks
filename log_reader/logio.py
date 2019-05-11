import csv
from collections import defaultdict
from datetime import datetime


# Assumptions:
# Log file is ordered in ascending date (timestamp) order.
# Log file stores its dates in UTC (not going to worry about timezones).
class LogIO(object):

    def __init__(self, file_path):
        self.file_path = file_path
    
    def apply(self, function):
        """
        Apply a function to each line of the log file.
        """
        with open(self.file_path, 'r') as log_file:
            for file_line in log_file:
                log_line = LogLine.build_from_line(file_line.strip())
                function(log_line)

    @staticmethod
    def convert_datetime_to_timestamp(_datetime):
        _datetime_type = type(_datetime)
        if _datetime_type == int:
            return _datetime        
        if _datetime_type == str:
            return int(_datetime)
        if _datetime_type == datetime:
            return datetime.timestamp(_datetime)
        raise ValueError(f"Invalid type for date interval limit {_datetime_type} ({_datetime})")


class LogLine(object):
    def __init__(self, unix_timestamp, source_host, destination_host):
        self.unix_timestamp = int(unix_timestamp)
        self.source_host = source_host
        self.destination_host = destination_host
    
    @staticmethod
    def build_from_line(line):
        unix_timestamp, source_host, destination_host = line.split(' ')
        return LogLine(unix_timestamp, source_host, destination_host)
