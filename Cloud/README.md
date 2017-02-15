Cloud Info:

Use ssh key (gcloud.ppk or gcloud.pub) and connect to 'sdpspot@104.196.123.57'.

Connect to MySQL db using 'mysql -h 104.154.44.50 -u root'.  Password is the usual.


Django:
    Start SQL Proxy: cloud_sql_proxy.exe -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
    
myinstance (Alien-Walker)
    ipAddress: 104.154.44.50
    connectionName: alien-walker-157903:us-central1:myinstance
    SQL Proxy: cloud_sql_proxy.exe -instances=alien-walker-157903:us-central1:myinstance=tcp:3306