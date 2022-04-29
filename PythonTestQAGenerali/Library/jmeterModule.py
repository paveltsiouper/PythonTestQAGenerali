import glob
from datetime import datetime


def list_log_errors(dirPath, filename, ext):
    """
    3. Create a python script that parses jmeter log files in CSV format,
       and in the case if there are any non-successful endpoint responses recorded in the log,
       prints out the label, response code, response message, failure message,
       and the time of non-200 response in human-readable format in PST timezone
       (e.g. 2021-02-09 06:02:55 PST).

       Please use Jmeter_log1.jtl, Jmeter_log2.jtl as input files for testing out your script
       (the files have .jtl extension but the format is  CSV).
    """
    flist = [f for f in glob.glob("" + dirPath + "/" + filename + "" + ext)]
    for file in flist:
        file = open(file, 'r')
        lines = file.read().splitlines()
        for line in range(1, len(lines)):
            if lines[line].split(',')[7] not in 'true':
                print(
                    f"label:{lines[line].split(',')[2]},response code:{lines[line].split(',')[3]},time-stamp:{datetime.fromtimestamp(int(lines[line].split(',')[0][:-3]))}")
        file.close()
