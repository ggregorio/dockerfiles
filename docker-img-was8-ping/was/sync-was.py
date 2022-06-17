nodes = AdminControl.queryNames('WebSphere:type=NodeSync,*').splitlines()
for node in nodes:
	print "Synchronizing node : " + node
	worked = AdminControl.invoke(node, 'sync')
	if worked != "true":
		print "Synchronizing node failed : " + node
		sys.exit(1)
	else:
		print "Synchronization Successful"