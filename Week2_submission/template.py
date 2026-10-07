"""
RECORD CHECK  -  my version
===========================

Name  :  MAUZAH 
Lane  :  AI 
Date  :  01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

dataset_name = input("Enter dataset name: ")  # : replace with an input() call
rowsloaded = float(input("Enter no.of rows loaded: "))   # : replace with an input() call, converted
rowsexpected = float(input("Enter no.of rows expected: "))  # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = rowsexpected - rowsloaded   
percent = (rowsloaded / rowsexpected) * 100  
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

if percent >= 100:
    print("OVER LIMIT")
elif percent >= 90:
    print("WARNING")
else:
    print("OK")


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
