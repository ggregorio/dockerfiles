import os
import sys

WEBSPHERE_APP=os.environ.get('WEBSPHERE_APP');
WEBSPHERE_INSTANCENAME=os.environ.get('WEBSPHERE_INSTANCENAME');

appRun = None;
names = AdminControl.queryNames('type=Application,name='+ WEBSPHERE_APP +',*').splitlines();
if len(names) == 0 or (len(names) == 1 and names[0] == ''):
    print 'App not running on any server '+ WEBSPHERE_INSTANCENAME ;
    sys.exit(1);
else:
    for app in names:
        server = AdminControl.getAttributes(app, ['server']).split(' ')[1][:-1];
        serverName = AdminControl.getAttributes(server, ['name']).split(' ')[1][:-1];
        if serverName.strip() == WEBSPHERE_INSTANCENAME :
            appRun=app;
if appRun == None:
    print 'App not running on server ' + WEBSPHERE_INSTANCENAME;
else:
    print 'App is running on server ' + WEBSPHERE_INSTANCENAME;