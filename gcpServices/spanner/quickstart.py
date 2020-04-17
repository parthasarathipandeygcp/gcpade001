

def run_quickstart():
    # [START spanner_quickstart]
    # Imports the Google Cloud Client Library.
    from google.cloud import spanner

    # Instantiate a client.
    spanner_client = spanner.Client()

    # Your Cloud Spanner instance ID.
    instance_id = 'my-instance-id'

    # Get a Cloud Spanner instance by ID.
    instance = spanner_client.instance(instance_id)

    # Your Cloud Spanner database ID.
    database_id = 'my-database-id'

    # Get a Cloud Spanner database by ID.
    database = instance.database(database_id)

    # Execute a simple SQL statement.
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql('SELECT 1')

        for row in results:
            print(row)
    # [END spanner_quickstart]


if __name__ == '__main__':
    run_quickstart()

