import os

WEBSPHERE_APP=os.environ.get('WEBSPHERE_APP')
WEBSPHERE_INSTANCENAME=os.environ.get('WEBSPHERE_INSTANCENAME')

clusterMembers = AdminConfig.list('ClusterMember', AdminConfig.getid('/ServerCluster:' + WEBSPHERE_INSTANCENAME + '/')).splitlines()
for member in clusterMembers:
    memberName = AdminConfig.showAttribute(member, 'memberName').strip();
    appRun = None;
    names = AdminControl.queryNames('type=Application,name=' + WEBSPHERE_APP + ',*').splitlines();
    if len(names) == 0 or (len(names) == 1 and names[0] == ''):
        print 'App not running on any server';
        sys.exit(1);
    else:
        for app in names:
            server = AdminControl.getAttributes(app, ['server']).split(' ')[1][:-1];
            serverName = AdminControl.getAttributes(server, ['name']).split(' ')[1][:-1];
            if serverName.strip() == memberName:
                appRun=app;
    if appRun == None:
        print 'App not running on server ' + memberName;
    else:
        print 'App is running on server ' + memberName;