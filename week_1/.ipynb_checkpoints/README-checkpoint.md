# Data Engineering Zoomcamp


### NOTES
https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes

### Steps

1. Creating an ssh key
	- ```ssh-keygen -t rsa -f gcp -C <username-ssh> -b 2048```
2. Creating an Ubuntu GCP instance
3. Accessing GCP instance through terminal
	-  ```ssh -i ~/.ssh/gcp <username-ssh>@<external-ip-of-instance>```
4. Creating ssh config file for easy access to gcp vm
5. Connecting VScode to gcp
6. Docker
	A. Setting permissions in docker.
	B. Practicing docker
	C.
7. Postgres
	1. Setting up postgres in docker
	```
		docker run -it \
		-e POSTGRES_USER="root" \
		-e POSTGRES_PASSWORD="root" \
		-e POSTGRES_DB="ny_taxi" \
		-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
		-p 5432:5432 \
		postgres:13
	```
    2. Connection String
    ```
        pgcli -U root -h localhost -p 5432 -d ny_taxi_db
    ```
	2.2 Possible error when running postgres.
	```
	If you have problems like: ""FATAL: password authentication failed for user "root"":1.  Make sure that no container is running (if it's rinning, we will kill it)):

	sudo docker ps

	Look up in list or processes running on your nesessary port:

	sudo lsof -i :<port №>
	If some is running, remember its PID

	2. Kill the one which uses our port:

	kill -9  <PID № >

	3. Delete the folder, that's mapping our host file system to to container  file system ( here that is "ny_taxi_postgres_data)")4. Connect again with

	pgcli -h localhost -p <host mashine port №> -u root -d ny_taxi

	<host mashine port №> - the first number of two in docker run settings - when  you wrote smth like

	docker run -it \
	....  
	-p 5433:5432\ 

	-in this example hostmasine port is 5433! Remember this №, you must connect to DB using pgcli with THIS port!!!
	```
8. Uploading NYC Taxi data to Postgres DB.
