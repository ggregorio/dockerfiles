import os

EAR_PATH=os.environ.get('EAR_PATH')
WEBSPHERE_APP=os.environ.get('WEBSPHERE_APP')
WEBSPHERE_VIRTUAL_HOST=os.environ.get('WEBSPHERE_VIRTUAL_HOST')


print("Virtual Host = " + WEBSPHERE_VIRTUAL_HOST)


AdminApp.update( WEBSPHERE_APP, 'app', '[ -contents ' + EAR_PATH + ' -operation update ' + WEBSPHERE_VIRTUAL_HOST + ' ]')
AdminConfig.save()


