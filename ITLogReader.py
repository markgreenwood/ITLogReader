import argparse
from pandas import DataFrame

RJUST_POSN = 15

class Connector:
    def __init__(self, fields):
        self.dataset_name = fields[1]
        (
            self.guid,
            self.pin,
            self.test_time,
            self.result,
            self.elapsed_time,
        ) = fields[3:]
        
    def __str__(self):
        return "Connector test " + ("=" * (80 - len("Connector test "))) + "\n" + \
            "GUID: ".rjust(RJUST_POSN) + ("%s\n" % (self.guid,)) + \
            "Pin: ".rjust(RJUST_POSN) + ("%s\n" % (self.pin,)) + \
            "Test time: ".rjust(RJUST_POSN) + ("%s\n" % (self.test_time,)) + \
            "Result: ".rjust(RJUST_POSN) + ("%s\n" % (self.result,)) + \
            "Elapsed time: ".rjust(RJUST_POSN) + ("%s\n" % (self.elapsed_time,))
        
class TXPO:
    def __init__(self, fields):
        self.dataset_name = fields[1]
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
        return "TXPO test " + ("=" * (80 - len("TXPO test "))) + "\n" + \
            "GUID: ".rjust(RJUST_POSN) + ("%s\n" % (self.guid,)) + \
            "Tx Ant: ".rjust(RJUST_POSN) + ("%s\n" % (self.transmit_antenna,)) + \
            "Channel: ".rjust(RJUST_POSN) + ("%s\n" % (self.channel,)) + \
            "Packets: ".rjust(RJUST_POSN) + ("%s\n" % (self.transmit_packet_count,)) + \
            "Duty cycle: ".rjust(RJUST_POSN) + ("%s\n" % (self.duty_cycle,)) + \
            "Averages: ".rjust(RJUST_POSN) + ("%s\n" % (self.pm_avg_count,)) + \
            "Offset: ".rjust(RJUST_POSN) + ("%s\n" % (self.offset,)) + \
            "Data rate: ".rjust(RJUST_POSN) + ("%s\n" % (self.data_rate,)) + \
            "TXGC: ".rjust(RJUST_POSN) + ("%s\n" % (self.txgc,)) + \
            "Temp: ".rjust(RJUST_POSN) + ("%s\n" % (self.temp,)) + \
            "Upper limit: ".rjust(RJUST_POSN) + ("%s\n" % (self.upper_limit,)) + \
            "Lower limit: ".rjust(RJUST_POSN) + ("%s\n" % (self.lower_limit,)) + \
            "Power: ".rjust(RJUST_POSN) + ("%s\n" % (self.power,)) + \
            "Test time: ".rjust(RJUST_POSN) + ("%s\n" % (self.test_time,)) + \
            "Result: ".rjust(RJUST_POSN) + ("%s\n" % (self.result,)) + \
            "Elapsed time: ".rjust(RJUST_POSN) + ("%s\n" % (self.elapsed_time,))
            
class CalibrationRecord:
    def __init__(self, fields):
        self.dataset_name = fields[1]
        (
            self.guid,
            self.target_power,
            self.step,
            self.transmit_antenna,
            self.channel,
            self.transmit_packet_count,
            self.duty_cycle,
            self.pm_avg_count,
            self.offset,
            self.data_rate,
            self.txgc,
            self.power,
            self.temp,
            self.M,
            self.B,
            self.txgc0calc,
            self.txgc1calc,
            self.pwr0calc,
            self.pwr1calc,
            self.min_temp_lim,
            self.max_temp_lim,
            self.min_temp_calc,
            self.max_temp_calc,
            self.target_discovery_accuracy,
            self.warning_msg,
            self.test_time,
            self.result,
            self.elapsed_time,
        ) = fields[3:]
        
    def __str__(self):
        title = "%s record " % self.dataset_name
        return title + ("=" * (80 - len(title))) + "\n" + \
            "GUID: ".rjust(RJUST_POSN) + ("%s\n" % (self.guid,)) + \
            "Target pwr: ".rjust(RJUST_POSN) + ("%s\n" % (self.target_power,)) + \
            "Step: ".rjust(RJUST_POSN) + ("%s\n" % (self.step,)) + \
            "Tx Ant: ".rjust(RJUST_POSN) + ("%s\n" % (self.transmit_antenna,)) + \
            "Channel: ".rjust(RJUST_POSN) + ("%s\n" % (self.channel,)) + \
            "Packets: ".rjust(RJUST_POSN) + ("%s\n" % (self.transmit_packet_count,)) + \
            "Duty cycle: ".rjust(RJUST_POSN) + ("%s\n" % (self.duty_cycle,)) + \
            "Averages: ".rjust(RJUST_POSN) + ("%s\n" % (self.pm_avg_count,)) + \
            "Offset: ".rjust(RJUST_POSN) + ("%s\n" % (self.offset,)) + \
            "Data rate: ".rjust(RJUST_POSN) + ("%s\n" % (self.data_rate,)) + \
            "TXGC: ".rjust(RJUST_POSN) + ("%s\n" % (self.txgc,)) + \
            "Power: ".rjust(RJUST_POSN) + ("%s\n" % (self.power,)) + \
            "Temperature: ".rjust(RJUST_POSN) + ("%s\n" % (self.temp,)) + \
            "M: ".rjust(RJUST_POSN) + ("%s\n" % (self.M,)) + \
            "B: ".rjust(RJUST_POSN) + ("%s\n" % (self.B,)) + \
            "First TXGC: ".rjust(RJUST_POSN) + ("%s\n" % (self.txgc0calc,)) + \
            "Second TXGC: ".rjust(RJUST_POSN) + ("%s\n" % (self.txgc1calc,)) + \
            "First TxPo: ".rjust(RJUST_POSN) + ("%s\n" % (self.pwr0calc,)) + \
            "Second TxPo: ".rjust(RJUST_POSN) + ("%s\n" % (self.pwr1calc,)) + \
            "Min temp lim: ".rjust(RJUST_POSN) + ("%s\n" % (self.min_temp_lim,)) + \
            "Max temp lim: ".rjust(RJUST_POSN) + ("%s\n" % (self.max_temp_lim,)) + \
            "Min temp calc: ".rjust(RJUST_POSN) + ("%s\n" % (self.min_temp_calc,)) + \
            "Max temp calc: ".rjust(RJUST_POSN) + ("%s\n" % (self.max_temp_calc,)) + \
            "Target disc acc: ".rjust(RJUST_POSN) + ("%s\n" % (self.target_discovery_accuracy,)) + \
            "Warning msg: ".rjust(RJUST_POSN) + ("%s\n" % (self.warning_msg,)) + \
            "Test time: ".rjust(RJUST_POSN) + ("%s\n" % (self.test_time,)) + \
            "Result: ".rjust(RJUST_POSN) + ("%s\n" % (self.result,)) + \
            "Elapsed time: ".rjust(RJUST_POSN) + ("%s\n" % (self.elapsed_time,))        
 
parser = argparse.ArgumentParser(description='Read file names')
parser.add_argument('--logfile', help='IT data log file')

args = parser.parse_args()

infile = open(args.logfile)
lines = infile.readlines()
lines = lines[0].lstrip('| ').rstrip('| ').split('||')

tests = []

for line in lines:
    fields = line.split('|')
    if (fields[1] == "Connector"):
        t = Connector(fields)
        tests.append(t)
    if (fields[1] == "TXPO"):
        t = TXPO(fields)
        tests.append(t)
    if (fields[1] == "Calibration"):
        t = CalibrationRecord(fields)
        tests.append(t)
        
caltablefile = open('caltable.csv','w')

calfields = (
    "GUID",
    "Target power",
    "Step",
    "Transmit antenna",
    "Channel",
    "Transmit packet count",
    "Duty cycle",
    "PM avg count",
    "Offset",
    "Data rate",
    "TXGC",
    "Power",
    "Temperature",
    "M",
    "B",
    "First TXGC calc",
    "Second TXGC calc",
    "First pwr calc",
    "Second pwr calc",
    "Min temp limit",
    "Max temp limit",
    "Min temp calc",
    "Max temp calc",
    "Target discovery accuracy",
    "Warning msg",
    "Test time",
    "Result",
    "Elapsed time",
)

caltablefile.write(",".join(calfields) + "\n")

for test in tests:
    if (test.dataset_name == "Calibration"):
        caltablefile.write(
            ",".join((
                test.guid,
                test.target_power,
                test.step,
                test.transmit_antenna,
                test.channel,
                test.transmit_packet_count,
                test.duty_cycle,
                test.pm_avg_count,
                test.offset,
                test.data_rate,
                test.txgc,
                test.power,
                test.temp,
                test.M,
                test.B,
                test.txgc0calc,
                test.txgc1calc,
                test.pwr0calc,
                test.pwr1calc,
                test.min_temp_lim,
                test.max_temp_lim,
                test.min_temp_calc,
                test.max_temp_calc,
                test.target_discovery_accuracy,
                test.warning_msg,
                test.test_time,
                test.result,
                test.elapsed_time,
            )) + "\n"
        )
                
caltablefile.close()