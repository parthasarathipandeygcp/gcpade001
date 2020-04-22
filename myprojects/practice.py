#!/usr/bin/python3

"""This application demonstrates how to do basic operations using Cloud
Spanner.

For more information, see the README.rst under /spanner.
"""

import os
import argparse
import base64
import datetime

from google.cloud import spanner
from google.cloud.spanner_v1 import param_types

credential_path = "C:\secret\gcpade001user.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


# [START spanner_create_database]
def create_database(instance_id, database_id):
    """Creates a database and tables for sample data."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id, ddl_statements=[
        """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX)
        ) PRIMARY KEY (SingerId)""",
        """CREATE TABLE Albums (
            SingerId     INT64 NOT NULL,
            AlbumId      INT64 NOT NULL,
            AlbumTitle   STRING(MAX)
        ) PRIMARY KEY (SingerId, AlbumId),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE"""
    ])

    operation = database.create()

    print('Waiting for operation to complete...')
    operation.result()

    print('Created database {} on instance {}'.format(
       database_id, instance_id))



create_database("upspains", "up-db")
#insert_data("up-spanner-ins", "up-db")
#delete_data("up-spanner-ins", "up-db")
#query_data("up-spanner-ins", "up-db")
#read_data("up-spanner-ins", "up-db")
#alter_database("up-spanner-ins", "up-db")