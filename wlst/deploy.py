connect('weblogic','Welcome1','t3://host.docker.internal:7001')
edit()
startEdit()
deploy('hello-world',
       '/u01/oracle/hello-world.war',
       targets='ManagedServer1',
       stageMode='nostage')

save()
Activate()

startApplication('hello-world')
