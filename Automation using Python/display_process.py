import psutil

def DispProc():

    proclist=[]

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            proclist.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return proclist

def main():
    print ("Process Monitor")

    processlist=DispProc()
    for row in processlist:
        print(row)
    print("Total number of processes are",len(processlist))


if __name__ == "__main__":
    main()
