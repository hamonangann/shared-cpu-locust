import time
import os
    
print("start")
start = time.time()
for i in range(200000000):
    pass
end = time.time()
CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
print("CPU Usage = " + CPU_Pct)
print("time elapsed", end-start)