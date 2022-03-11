## import statements

import psutil
import platform
from os import *
from datetime import datetime

## function to CPU OS info
def CPU_Info_OS():
    print ("----- CPU Info OS -----")
    if platform.system()=='Windows':
        return platform.processor()
    elif platform.system()=='Darwin':
        command='/usr/sbin/sysctl -n machdep.cpu.brand_string'
        return popen(command).read().strip()
    elif platform.system()=='Linux':
        command='cat /proc/cpuinfo'
        return popen(command).read().strip()
    return 'Platform not identified'

## function to get size
def get_size(bytes,suffix='B'):
    factor=1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes/=factor

## function to get platform info
def Plaform_Info():
    print ("----- Systems information -----")
    uname=platform.uname()
    print(f"System:{uname.system}")
    print(f"Node name:{uname.node}")
    print(f"Release:{uname.release}")
    print(f"Version:{uname.version}")
    print(f"Machine:{uname.machine }")
    print(f"Processor:{uname.processor}")

## function to get boot info
def Boot_info():
    print ("----- Boot time -----")
    boot_time_timestamp=psutil.boot_time()
    bt=datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot time:{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

## function to get CPU info
def CPU_Info():
    print("----- CPU info -----")
    print("Physical cores:",psutil.cpu_count(logical=False))
    print("Total cores:",psutil.cpu_count(logical=True))
    print("CPU usage per core")
    for i,percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core{i}:{percentage}%")
    print(f"Total CPU usage:{psutil.cpu_percent()}%")

## function to get RAM usage
def RAM_usage():
    print("----- Memory information -----")
    svmem=psutil.virtual_memory()
    print(f"Total : {get_size(svmem.total)}")
    print(f"Available : {get_size(svmem.available)}")
    print(f"Used : {get_size(svmem.used)}")
    print(f"Percentage : {get_size(svmem.percent)}%")

    print ("----- SWAP -----")
    swap=psutil.swap_memory()
    print(f"Total : {get_size(swap.total)}")
    print(f"Free : {get_size(swap.total)}")
    print(f"Used : {get_size(swap.total)}")
    print(f"Percentage : {get_size(svmem.percent)}")

## function to get Disk info
def Disk_info():
    print("----- Disk information -----")
    print ("Partitions and usage :")
    partitions=psutil.disk_partitions()

    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"Mountpoint :{partition.mountpoint}")
        print(f"File system type :{partition.fstype}")
        try:
            partition_usage=psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue

    print(f"Total size : {get_size(partition_usage.total)}")
    print(f"Used : {get_size(partition_usage.used)}")
    print(f"Free : {get_size(partition_usage.free)}")
    print(f"Percentage : {get_size(partition_usage.percent)}%")

    disk_io=psutil.disk_io_counters()
    print(f"Total read : {get_size(disk_io.read_bytes)}")
    print(f"Total write : {get_size(disk_io.write_bytes)}")

## main function
def main():
    CPU_Info_OS()
    Disk_info()
    RAM_usage()
    CPU_Info()
    Boot_info()
    Plaform_Info()

## starter
if __name__=="__main__":
    main()




