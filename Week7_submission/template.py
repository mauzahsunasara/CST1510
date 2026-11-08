"""
RECORD CHECK  -  my version
===========================

Name  :  MAUZAH YUNUSALI SUNASARA 
Lane  :  AI 
Date  :  08/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.


def parse_line(raw_line):
    """ This function cleans the messy lines by removing unnecessary spaces, and adding those values to a dictionary"""
    raw_line = raw_line.strip()
    hostname_part, rest = raw_line.split(",", 1)     # hostname_part = "Srv-01 ", rest = " used=87 , total=100"
    hostname_part = hostname_part.strip().lower()     # hostname_part = "srv-01"
    rest1, rest2 = rest.split(",")     # rest1 = " used=87 ", rest2 = " total=100"
    key1, value1 = rest1.split("=")     # key1 = " used", value1 = "87 "
    key2, value2 = rest2.split("=")     # key2 = " total", value2 = "100"
    dictionary = {'hostname': hostname_part.title(), 'used': float(value1), 'total': float(value2)}
    status = status_of(value1, value2)
    dictionary["status"] = status
    return dictionary 

def status_of(value1, value2):
    """ This function returns status depending on the percent that we get by value1, value2"""
    percent = float(value1)/float(value2) * 100
    if percent >= 100:
        return "OVERLIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

print("File has data:")
with open("myfile.txt", "r") as file:
    for line in file:
        print(line)
print()     # this will print a blaank line to separate this data in the file from the rest of required output

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

raw_records = open("myfile.txt", "r")
flagged = 0
final = []     # we created a list to see hoe many records it has inside of it, to get no.of flagged records
s= 0     # variable to keep record of no.of total values 
for raw_record in raw_records:
    s += 1
    result = parse_line(raw_record)
    final.append(result)
    print(result)
    # status_of(value1, value2) has been called in parse_line(raw_record)

print(f"Final is: {final}")
print(f'No.of records: {len(final)} and no.of flagged records = {s - len(final)}')
    


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
