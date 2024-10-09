
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

ENABLE_PROXY_FIX = True
FAB_ADD_SECURITY_API = True

# Allow SQLite databases
PREVENT_UNSAFE_DB_CONNECTIONS = False

#Uncomment this line to save the metadata in mysql database (SQLite is not recomended for production)
#SQLALCHEMY_DATABASE_URI ='mysql://<UserName>:<DBPassword>@<Database Host>/<Database Name>'

# Set the secret key
# A new secret key can be generated using:  python3 -c "import os; print(os.urandom(24).hex())"
SECRET_KEY = "c725f66775f7f568fa19bd00ceaf75b89a5fb43615b005eb"