# pip3 install py-cpuinfo

import cpuinfo
print(cpuinfo.get_cpu_info()['brand_raw'])