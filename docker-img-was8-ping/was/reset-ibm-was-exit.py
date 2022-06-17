import sys
import time
import os

InstanceName=os.environ.get('WEBSPHERE_INSTANCENAME')
command=os.environ.get('WEBSPHERE_COMMAND')
logFile = open('/tmp/restartPY.log', 'a')
logFile.write('##########################################################################################' + '\n')

def now():
  return time.strftime("%c")

def getMember(InstanceName):
 logFile.write('----------' + '\n')
 memberList = []
 try:
  clusterID = AdminConfig.getid('/ServerCluster:' + InstanceName + '/')
  clusterList = AdminConfig.list('ClusterMember', clusterID)
  servers = clusterList.split("\n")
  logFile.write(now() + ' ' + 'Listado de instancias: ' + str(servers)  + '\n')
  for serverID in servers:
   serverName = AdminConfig.showAttribute(serverID, 'memberName')
   logFile.write(now() + ' ' + 'Nombre de instancia: ' + serverName + '\n')
   memberList.append(str(serverName))
 except:
  pass
 try:
  server = AdminConfig.getid('/Server:' + InstanceName + '/' )
  if len(server) > 0:
   logFile.write(now() + ' ' + 'Nombre de instancia: ' + InstanceName + '\n')
   memberList.append(InstanceName)
 except:
  pass
 if len(memberList) > 0:
  return memberList
 else:
  sys.exit(1)

def stopServer(serverName):
 logFile.write('----------' + '\n')
 logFile.write(now() + ' ' + 'Se inicia stop de: ' + serverName + '\n')
 server = AdminControl.completeObjectName('type=Server,name=' + serverName + ',*' )
 AdminControl.invoke(server, 'stop')
 time.sleep(10)

def startServer(serverName, nodeName):
 logFile.write('----------' + '\n')
 logFile.write(now() + ' ' + 'Se inicia start de: ' + serverName + '\n')
 AdminControl.startServer(serverName, nodeName, 5)
 return


def getNode(serverName):
 logFile.write('----------' + '\n')
 serverId = AdminConfig.getid('/Server:' + serverName)
 nodeName = str(serverId).split('nodes/')[1].split('/')[0]
 logFile.write(now() + ' ' + serverName + ': ' + nodeName + '\n')
 return nodeName


def getState(InstanceName):
 stateList = []
 try:
  getMember(InstanceName)
  logFile.write('----------' + '\n')
  logFile.write(now() + ' ' + 'Verificando estado de: ' + InstanceName + '\n')
  for i in range (0, 10):
   logFile.write(now() + ' ' + 'Iteracion: ' + str(i) + '\n')
   for x in getMember(InstanceName):
    logFile.write(now() + ' ' + 'Verificando estado de la instancia: ' + x + '\n')
    server = AdminControl.completeObjectName('type=Server,name=' + x + ',*' )
    if ( server == '' and command == 'start' ):
     if x not in stateList:
      logFile.write(now() + ' ' + 'Agregando instancia al listado de Error: ' + x + '\n')
      stateList.append( x )
    elif ( server != '' and command == 'stop' ):
     if x not in stateList:
      logFile.write(now() + ' ' + 'Agregando instancia al listado de Error: ' + x + '\n')
      stateList.append( x )
    elif ( server == '' and command == 'stop'):
     if x in stateList:
      logFile.write(now() + ' ' +'Eliminando instancia del listado de Error: ' + x + '\n')
      stateList.remove(x)
    elif ( server != '' and command == 'start'):
     if x in stateList:
      logFile.write(now() + ' ' + 'Eliminando instancia del listado de Error: ' + x + '\n')
      stateList.remove(x)
   if ( len(stateList) == 0 ):
    print 'Todas las instancias finalizaron correctamente'
    print getMember(InstanceName)
    logFile.write(now() + ' ' + 'Todas las instancias finalizaron correctamente' + '\n')
    break
 
   
   elif ( int(i) == 9 and len(stateList) > 0 ):
    print 'Las siguientes instancias no finalizaron correctamente: ' + str(stateList)
    logFile.write(now() + ' ' + 'Las siguientes instancias no finalizaron correctamente: ' + str(stateList) + '\n')
    print ' se ejecuta exit 1 '
 

   else:
    time.sleep(60)

 except SystemExit:
  print "Script Finalizado"
  logFile.write(now() + ' ' + 'Script finalizado por excepcion en funcion getState' + '\n')
  sys.exit(1)

#################
logFile.write(now() + ' ' + 'Comienzo de ejecucion' + '\n')

for member in getMember(InstanceName):
 try: 
  if command == 'stop':
   stopServer(member)
  elif command == 'start':
   nodeName = getNode(member)
   startServer(member, nodeName)
  else:
   print "Comando no valido"
 except:
   continue

getState(InstanceName)
logFile.close()