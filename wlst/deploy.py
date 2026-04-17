connect('weblogic','Welcome1','t3://host.docker.internal:7001')
edit()
startEdit()
deploy('hello-world',
       '/u01/oracle/hello-world.war',
       targets='AdminServer',
       stageMode='nostage')

save()
activate()

startApplication('hello-world')
