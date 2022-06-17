import threading
import time
import os
import glob

WEBSPHERE_APP=os.environ.get('WEBSPHERE_APP')
WEBSPHERE_INSTANCENAME=os.environ.get('WEBSPHERE_INSTANCENAME')
MAX_THREADS = 60
COOLDOWN = 5

def process_member(member):
    memberName = AdminConfig.showAttribute(member, 'memberName').strip()
    appRun = None;
    names = AdminControl.queryNames('type=Application,name=' + WEBSPHERE_APP + ',*').splitlines()

    if len(names) == 0 or (len(names) == 1 and names[0] == ''):
        print('--- App not running on any server')
        exit(1)
    else:
        for app in names:
            server = AdminControl.getAttributes(app, ['server']).split(' ')[1][:-1]
            serverName = AdminControl.getAttributes(server, ['name']).split(' ')[1][:-1]
            if serverName.strip() == memberName:
                appRun = app
    outfile_name = "/tmp/check_app-ok-" + str(memberName) + ".log"
    outfile_error_name = "/tmp/check_app-error-" + str(memberName) + ".log"
    outfile = open(outfile_name, 'a')
    outfile_error = open(outfile_error_name, 'a')
    if appRun == None:
        outfile_error.write('App not running on server ' + memberName + '\n')
        print('--- App not running on server ' + memberName)
    else:
        outfile.write('App is running on server ' + memberName + '\n')
        print('*** App is running on server ' + memberName)
    outfile.close()


print("Borro archivos viejos...")
for filePath in glob.glob('check_app-*.log'):
    try:
        os.remove(filePath)
    except OSError:
        pass

print('*********************************')
print("Checking app " + WEBSPHERE_APP)
print('*********************************')
print("Creating threads")
threads = []

clusterMembers = AdminConfig.list('ClusterMember', AdminConfig.getid('/ServerCluster:' + WEBSPHERE_INSTANCENAME + '/')).splitlines()
for member in clusterMembers:
    print(member)
    #threads.append(threading.Thread(target=process_member, args=(member,)))
    t = threading.Thread(target=process_member, args=(member,))
    t.setDaemon(1)
    threads.append(t)

start_time = time.time()
print("Starting threads")
while len(threads) != 0:
    print("*There are " + str(len(threading.enumerate())) + " threads running, " +  str(len(threads)) + "/" + str ( len(clusterMembers)) + " remaining")
    if len(threading.enumerate()) < MAX_THREADS:
        threads.pop().start()
    else:
        time.sleep(1)
while len(threading.enumerate()) > 1:
    print("**There are " + str(len(threading.enumerate())) + " threads running, finishing up")
    time.sleep(COOLDOWN)

##Process OK
read_files = glob.glob("/tmp/check_app-ok-*.log")
read_files.sort()
file = open('/tmp/check_app-ok.log', "a")
for f in read_files:
    infile = open(f, 'r')
    file.write(infile.read())
    infile.close()
file.close()
print('###########################')
print('#######APPs OK#############')
f = open('/tmp/check_app-ok.log', 'r')
file_contents = f.read()
print (file_contents)
f.close()

##Process Errors
read_files = glob.glob("/tmp/check_app-error-*.log")
read_files.sort()
file = open('/tmp/check_app-error.log', "a")
for f in read_files:
    infile = open(f, 'r')
    file.write(infile.read())
    infile.close()
file.close()
print('###########################')
print('#######APPs NOT OK#############')
f = open('/tmp/check_app-error.log', 'r')
file_contents = f.read()
print (file_contents)
f.close()
print("Process time: "+ str(time.time() - start_time) + " seconds")

