**OAUTH IN DOCKER**

Below are the steps to deploy containers to work correctly with the service.

1) Go to the project folder and execute 
`docker-compose -f docker\docker-compose.yml build`  to build and pull the images
specified in the docker-compose file

2) To run built images in containers: 
`docker-compose -f docker\docker-compose.yml up -d`

Thus, after executing these commands, you will run three containers:

    * oauth service, port: 5000
    * DB with identities
    * DB client (pgAdmin4), running on 80 port
    
To connect to the database via the pgAdmin4, 
you must add the identities server to the server group.