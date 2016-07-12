import argparse
from pandas import DataFrame

class Connector:
    def __init__(self, fields):
        self.guid = fields[3]
        self.pin = fields[4]
        self.test_time = fields[5]
        self.result = fields[6]
        self.elapsed_time = fields[7]
        
    def __str__(self):
        return "Connector test " + ("=" * (80 - len("Connector test "))) + "\n" + \
            "GUID: %s\n" % (self.guid,) + \
            "Pin: %s\n" % (self.pin,) + \
            "Test time: %s\n" % (self.test_time,) + \
            "Result: %s\n" % (self.result,) + \
            "Elapsed time: %s\n" % (self.elapsed_time,)
        
class TXPO:
    def __init__(self, fields):
        self.guid = fields[3]
        self.transmit_antenna = fields[4]
        self.channel = fields[5]
        self.transmit_packet_count = fields[6]
        self.duty_cycle = fields[7]
        self.pm_avg_count = fields[8]
        self.offset = fields[9]
        self.data_rate = fields[10]
        self.txgc = fields[11]
        self.temp = fields[12]
        self.upper_limit = fields[13]
        self.lower_limit = fields[14]
        self.power = fields[15]
        self.test_time = fields[16]
        self.result = fields[17]
        self.elapsed_time = fields[18]
        
    def __str__(self):
        return "GUID: %s\n" % (self.guid,) + \
            "Tx Ant: %s\n" % (self.transmit_antenna,) + \
            "Channel: %s\n" % (self.channel,) + \
            "Packets: %s\n" % (self.transmit_packet_count,) + \
            "Duty cycle: %s\n" % (self.duty_cycle,) + \
            "Averages: %s\n" % (self.pm_avg_count,) + \
            "Offset: %s\n" % (self.offset,) + \
            "Data rate: %s\n" % (self.data_rate,) + \
            "TXGC: %s\n" % (self.txgc,) + \
            "Temp: %s\n" % (self.temp,) + \
            "Upper limit: %s\n" % (self.upper_limit,) + \
            "Lower limit: %s\n" % (self.lower_limit,) + \
            "Power: %s\n" % (self.power,) + \
            "Test time: %s\n" % (self.test_time,) + \
            "Result: %s\n" % (self.result,) + \
            "Elapsed time: %s\n" % (self.elapsed_time,)
            
        
parser = argparse.ArgumentParser(description='Read file names')
parser.add_argument('--logfile', help='IT data log file')

args = parser.parse_args()

infile = open(args.logfile)
lines = infile.readlines()
lines = lines[0].lstrip('|').rstrip('|').rstrip().split('||')

tests_connector = []
tests_txpo = []

for line in lines:
    fields = line.split('|')
    if (fields[1] == "Connector"):
        t = Connector(fields)
        tests_connector.append(t)
    if (fields[1] == "TXPO"):
        t = TXPO(fields)
        tests_txpo.append(t)
        