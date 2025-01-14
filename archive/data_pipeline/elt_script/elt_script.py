import subprocess
import time

def wait_for_postgres(host, max_retries=5, delay_seconds=5):
    retries = 0
    while retries < max_retries:
        try:
            result = subprocess.run(
                ["pg_isready", "-h", host], check=True, capture_output=True, text=True
            )
            if "accepting connections" in result.stdout:
                print("Successfully connected to Postgres")
                return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to connect to Postgres: {e}")
            retries += 1
            print(f"Retrying in {delay_seconds} seconds...")
            time.sleep(delay_seconds)
    print("Max retries reached. Exiting.")
    return False


if not wait_for_postgres(host="source_postgres"):
    exit(1)

print("Starting ELT Script...")
source_config = {
    'dbname': 'source_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'source_postgres'
}

destination_config = {
    'dbname': 'destination_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'destination_postgres'
}

dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql',
    '-w' # Do not prompt for password
]

# set the PGPassword environment variable to avoid password prompt
subprocess_env = dict(PGPASSWORD=source_config['password'])

# execute the dump command
subprocess.run(
    dump_command,     # List containing pg_dump command and its arguments
    env=subprocess_env,  # Environment variables, including PGPASSWORD
    check=True        # Raise CalledProcessError if the command fails
)


# use psql to load the dumped SQL file into the destination database
load_command = [
    'psql',
    '-h', destination_config['host'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-a', '-f', 'data_dump.sql'
]

# set the PGPassword environment variable for the destination database
subprocess_env = dict(PGPASSWORD=destination_config['password'])

# Execute the load command
subprocess.run(
    load_command,   # List containing psql command and its arguments
    env=subprocess_env, # Environment variables, including PGPASSWORD
    check=True         # Raise CalledProcessError if the command fails
    
)

print("ELT Script completed successfully.")