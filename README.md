# Apache Superset Setup Using Docker

This repository provides a minimal setup for running Apache Superset using Docker.

## Some useful links

•	Connection to databases: https://superset.apache.org/docs/configuration/databases

•	Customizing Apache Superset Dashboards with CSS: https://preset.io/blog/customizing-superset-dashboards-with-css/

## Quick guide through the project

Basic setup inspired by the one made in this article: https://medium.com/towards-data-engineering/quick-setup-configure-superset-with-docker-a5cca3992b28.

### Create Superset Configuration Files:

#### Create superset-init.sh
Is a shell script that starts the initialization of Superset using Superset CLI to create admin user, set roles and permissions and start superset server.

**Step 1**: Create an admin user in Superset with details (username, first name, last name, email, and password). The values for these parameters can be passed through docker compose file or set manually before running the script. In this installation they are taken from the `.env` file.

**Step 2**: Upgrade the Superset Metastore to ensure we have the latest Superset version during the initialization process.

**Step 3**: Initialize Superset by setting up default roles and permissions.

**Step 4**: Finally, the /usr/bin/run-server.sh script is executed to start the server. This allows users to have access to the Superset web interface and start using the application.

#### Create superset_config.py
This file contains Superset-specific settings and customizations that can be use to override the default parameters that already come with Superset base image.

The SECRET_KEY parameter must be defined. This is a mandatory requirement of Superset (for more information: https://superset.apache.org/docs/configuration/configuring-superset#specifying-a-secret_key). It must be any long random string. It can be easily generated running the following code line: `python3 -c "import os; print(os.urandom(24).hex())`.
 
#### Dockerfile Configurations
The Dockerfile extends base image of Apache Superset. It define all the steps needed to build a custom Superset container image.

**Step 1**: Extend from the base image apache/superset:latest .

**Step 2**: Switch to root user to perform administrative tasks inside docker container.

**Step 3**: To connect to any database from Superset, the respective database driver is needed. For example, `mysqlclient` is a python package installed to connect MySQL to Superset.
All database drivers for superset can be found on this link: https://superset.apache.org/docs/configuration/databases/

**Step 4**: Mount `superset-init.sh` and `superset_config.py` into the docker container and specify `SUPERSET_CONFIG_PATH` to point to `superset_config.py` path inside the docker container.

**Step 5**: Define environment variables (username, admin and password could be defined here, but in this case they are defined in the `docker_compose.yml`).

**Step 6**: Switch back to superset user to run the Superset application.

**Step 7**: Specify the entrypoint for the container, which is the `superset-init.sh` script. This will initiate the superset setup.
 
#### Docker Compose Configurations

The `docker-compose.yml` file defines and configures multiple containers in the Docker project, specifying how they should interact and their dependencies. Individual configurations of each container and environment variables can be added also here. The environment variables are taken from the file `.env`.

The build context path, volumes for data persistence and port mapping between host and container are specified.

## Lunching Apache Superset

Clone the repository and run `docker compose up --build`. Once the container is created, open the browser and go to the port specified in the Docker Compose (`http://localhost:8088`).

Appart from the files needed to deploy Superset, the files `api_access_token.py` and `create_user.py` are added to the repository. `api_access_token.py` generates a token that allows the user to access to the API. `create_user.py` creates a new user through an API request (to do so, a new API token is generated in the script).


## Issues found

• If you are using Docker in Windows the docker entrypoint may not be found because of a default configuration of git in Windows. It replace the line endings in the files with Windows line endings (\r\n). This automatic conversion can be disabled:

`git config --global core.autocrlf input`

After doing so, reset the repository: 

`git rm --cached -r .`

`git reset --hard`

Source: https://stackoverflow.com/questions/38905135/why-wont-my-docker-entrypoint-sh-execute