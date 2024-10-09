# Use the latest version of the Apache Superset image from Docker Hub
FROM apache/superset:latest

# Switch to the root user to perform administrative tasks
USER root

# Install the mysqlclient package to enable MySQL database support
RUN pip install mysqlclient

# Copy the initialization script into the container
COPY ./superset-init.sh /superset-init.sh
# Make the initialization script executable
RUN chmod +x /superset-init.sh
# Change the ownership of the initialization script to the superset user
RUN chown superset /superset-init.sh

# Copy the Superset configuration file into the container
COPY superset_config.py /app/

# Set the environment variable to point to the configuration file path
ENV SUPERSET_CONFIG_PATH /app/superset_config.py

# Switch back to the superset user to run the application
USER superset

# Set the entrypoint to the initialization script to start Superset
ENTRYPOINT [ "/superset-init.sh" ]
