"""
RECORD CHECK  -  my version
===========================

Name  :  MAUZAH YUNUSALI SUNASARA 
Lane  :  AI 
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """This function returns the difference and percent of the value and limit"""
    difference = limit - value
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVERLIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status 

def print_report(label, value, limit, difference, percent, status):
    """This function prints it all"""
    print(f"label = {label}")
    print(f"value = {value}")
    print(f"limit = {limit}")
    print(f"difference = {difference}")
    print(f"precent = {percent}")
    print(f"status = {status}")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    records = []
    with open(path, "r") as file:
        for i in file:
            label, value, limit = i.split(",")
            record_d = {"label": label, "value": value, "limit": limit}
            records.append(record_d)

        with open("newfile", "w") as f:
            for i in records:
                difference, percent, status = check_record(float(i['value']), float(i["limit"]))
                f.write(f"{i["label"]} , {status} \n")
                print(f"{i["label"]} : {status}")

load_records("madebyme.txt")


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

with open("madebyme.txt", "r") as file:
      for i in file:
            difference, percent, status = check_record(float(i["value"]), float(i["limit"]))
            print_report(i["label"], i["value"], i["limit"], difference, percent, status)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
