"""
RECORD CHECK  -  my version
===========================

Name  :  Mauzah Yunusali Sunasara
Lane  :  AI       
Date  :  10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

def status_of(percent):
    """This function returns overlimit, warning or ok depending on the percent"""
    if percent >= 100:
        return "OVERLIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
def check(value, limit):
    """This function returns the difference and percent of the value and limit"""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """This function prints it all"""
    print(f"label = {label}")
    print(f"value = {value}")
    print(f"limit = {limit}")
    print(f"difference = {difference}")
    print(f"precent = {percent}")
    print(f"status = {status}")

# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

s=0

while True:
    dataset_name = input("Enter dataset name: ")  # : replace with an input() call

    if dataset_name == "quit":
        break

    rowsloaded = float(input("Enter no.of rows loaded: "))   # : replace with an input() call, converted
    rowsexpected = float(input("Enter no.of rows expected: "))  # : replace with an input() call, converted

    

    # ================================================================== PROCESS
    # 3. Work out the difference, the percentage, and the status.
    #
    #    Threshold : call status_of() to get the status. Work out the
    #                difference and percentage inline, not in a function.
    #    Typical   : call check() to get the difference and percentage instead.

    difference, percent = check(rowsloaded, rowsexpected)
    status = status_of(percent)
    if status = "OVERLIMIT":
        s+=1


    # =================================================================== OUTPUT
    # 4. Print the report.
    #
    #    Threshold : the three values you were given, plus status, inside a border
    #    Typical   : add difference and percent, 2 decimal places, right-aligned
    #    Excellent : call print_report() instead of printing directly here, and
    #                wrap sections 2-4 in a loop so you can check as many records
    #                as you like in one run - type "quit" as the label to stop.
    #                Keep count of how many came back OVER LIMIT and print that
    #                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {dataset_name}")
    print("=" * 34)

    print(f"  USED           - {rowsloaded: >10.2f}")
    print(f"  TOTAL          - {rowsexpected: >10.2f}")
    print(f"  FREE           - {difference: >10.2f}")
    print(f"  PERCENT        - {percent: >10.2f}")
    print(f"  STATUS         - {status: >10}")

    print("=" * 34)

print('No.of over limits = ', s)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
