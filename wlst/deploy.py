connect('weblogic','Welcome1','t3://host.docker.internal:7001')
edit()
startEdit()

try:
    undeploy('hello-world', targets='AdminServer')
    print('Old deployment removed')
except:
    print('No existing deployment')


deploy('hello-world',
       '/u01/oracle/hello-world.war',
       targets='AdminServer',
       stageMode='nostage')

save()
activate()

startApplication('hello-world')
