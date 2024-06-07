# Power shell command to measure execution time of the python program
# Note: for ISP scripts are disabled 
(Measure-Command { python .\analizzatore_smf_123_2.py -f .\ZOSSMF123 -e .\ZOSSMF123.xlsx | Out-Default }).ToString()