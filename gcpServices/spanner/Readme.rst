
#. Install the dependencies needed to run the samples.

        $ pip install -r requirements.txt

To run this sample:

.. code-block:: bash

    $ python spannercode.py

    usage: spannercode.py [-h] [--database-id DATABASE_ID]
                       instance_id
                       {create_database,insert_data,query_data,read_data,
                       read_stale_data,add_column,update_data,
                       query_data_with_new_column,read_write_transaction,
                       read_only_transaction,add_index,query_data_with_index,
                       read_data_with_index,add_storing_index,
                       read_data_with_storing_index,
                       create_table_with_timestamp,insert_data_with_timestamp,
                       add_timestamp_column,update_data_with_timestamp,
                       query_data_with_timestamp,write_struct_data,
                       query_with_struct,query_with_array_of_struct,
                       query_struct_field,query_nested_struct_field,
                       insert_data_with_dml,update_data_with_dml,
                       delete_data_with_dml,update_data_with_dml_timestamp,
                       dml_write_read_transaction,update_data_with_dml_struct,
                       insert_with_dml,query_data_with_parameter,
                       write_with_dml_transaction,
                       update_data_with_partitioned_dml,
                       delete_data_with_partitioned_dml,update_with_batch_dml,
                       create_table_with_datatypes,insert_datatypes_data,
                       query_data_with_array,query_data_with_bool,
                       query_data_with_bytes,query_data_with_date,
                       query_data_with_float,query_data_with_int,
                       query_data_with_string,
                       query_data_with_timestamp_parameter}
                       ...

    This application demonstrates how to do basic operations using Cloud
    Spanner.

  

    positional arguments:
      instance_id           Your Cloud Spanner instance ID.
      {create_database, insert_data, delete_data, query_data, read_data,
      read_stale_data, add_column, update_data, query_data_with_new_column,
      read_write_transaction, read_only_transaction, add_index,
      query_data_with_index, read_data_with_index, add_storing_index,
      read_data_with_storing_index, create_table_with_timestamp,
      insert_data_with_timestamp, add_timestamp_column,
      update_data_with_timestamp, query_data_with_timestamp,
      write_struct_data, query_with_struct, query_with_array_of_struct,
      query_struct_field, query_nested_struct_field, insert_data_with_dml,
      update_data_with_dml, delete_data_with_dml,
      update_data_with_dml_timestamp, dml_write_read_transaction,
      update_data_with_dml_struct, insert_with_dml, query_data_with_parameter,
      write_with_dml_transaction, update_data_with_partitioned_dml,
      delete_data_with_partitioned_dml, update_with_batch_dml, 
      create_table_with_datatypes, insert_datatypes_data,
      query_data_with_array, query_data_with_bool, query_data_with_bytes,
      query_data_with_date, query_data_with_float, query_data_with_int,
      query_data_with_string, query_data_with_timestamp_parameter}
        create_database     Creates a database and tables for sample data.
        insert_data         Inserts sample data into the given database. The
                            database and table must already exist and can be
                            created using `create_database`.
        delete_data         Deletes sample data from the given database. The
                            database, table, and data must already exist and
                            can be created using `create_database` and
                            `insert_data`.
        query_data          Queries sample data from the database using SQL.
        read_data           Reads sample data from the database.
        read_stale_data     Reads sample data from the database. The data is
                            exactly 15 seconds stale.
        add_column          Adds a new column to the Albums table in the example
                            database.
        update_data         Updates sample data in the database. This updates the
                            `MarketingBudget` column which must be created before
                            running this sample. You can add the column by running
                            the `add_column` sample or by running this DDL
                            statement against your database: ALTER TABLE Albums
                            ADD COLUMN MarketingBudget INT64
        query_data_with_new_column
                            Queries sample data from the database using SQL. This
                            sample uses the `MarketingBudget` column. You can add
                            the column by running the `add_column` sample or by
                            running this DDL statement against your database:
                            ALTER TABLE Albums ADD COLUMN MarketingBudget INT64
        read_write_transaction
                            Performs a read-write transaction to update two sample
                            records in the database. This will transfer 200,000
                            from the `MarketingBudget` field for the second Album
                            to the first Album. If the `MarketingBudget` is too
                            low, it will raise an exception. Before running this
                            sample, you will need to run the `update_data` sample
                            to populate the fields.
        read_only_transaction
                            Reads data inside of a read-only transaction. Within
                            the read-only transaction, or "snapshot", the
                            application sees consistent view of the database at a
                            particular timestamp.
        add_index           Adds a simple index to the example database.
        query_data_with_index
                            Queries sample data from the database using SQL and an
                            index. The index must exist before running this
                            sample. You can add the index by running the
                            `add_index` sample or by running this DDL statement
                            against your database: CREATE INDEX AlbumsByAlbumTitle
                            ON Albums(AlbumTitle) This sample also uses the
                            `MarketingBudget` column. You can add the column by
                            running the `add_column` sample or by running this DDL
                            statement against your database: ALTER TABLE Albums
                            ADD COLUMN MarketingBudget INT64
        read_data_with_index
                            Inserts sample data into the given database. The
                            database and table must already exist and can be
                            created using `create_database`.
        add_storing_index   Adds an storing index to the example database.
        read_data_with_storing_index
                            Inserts sample data into the given database. The
                            database and table must already exist and can be
                            created using `create_database`.
        create_table_with_timestamp
                            Creates a table with a COMMIT_TIMESTAMP column.
        insert_data_with_timestamp
                            Inserts data with a COMMIT_TIMESTAMP field into a
                            table.
        add_timestamp_column
                            Adds a new TIMESTAMP column to the Albums table in the
                            example database.
        update_data_with_timestamp
                            Updates Performances tables in the database with the
                            COMMIT_TIMESTAMP column. This updates the
                            `MarketingBudget` column which must be created before
                            running this sample. You can add the column by running
                            the `add_column` sample or by running this DDL
                            statement against your database: ALTER TABLE Albums
                            ADD COLUMN MarketingBudget INT64 In addition this
                            update expects the LastUpdateTime column added by
                            applying this DDL statement against your database:
                            ALTER TABLE Albums ADD COLUMN LastUpdateTime TIMESTAMP
                            OPTIONS(allow_commit_timestamp=true)
        query_data_with_timestamp
                            Queries sample data from the database using SQL. This
                            updates the `LastUpdateTime` column which must be
                            created before running this sample. You can add the
                            column by running the `add_timestamp_column` sample or
                            by running this DDL statement against your database:
                            ALTER TABLE Performances ADD COLUMN LastUpdateTime
                            TIMESTAMP OPTIONS (allow_commit_timestamp=true)
        write_struct_data   Inserts sample data that can be used to test STRUCT
                            parameters in queries.
        query_with_struct   Query a table using STRUCT parameters.
        query_with_array_of_struct
                            Query a table using an array of STRUCT parameters.
        query_struct_field  Query a table using field access on a STRUCT
                            parameter.
        query_nested_struct_field
                            Query a table using nested field access on a STRUCT
                            parameter.
        insert_data_with_dml
                            Inserts sample data into the given database using a
                            DML statement.
        update_data_with_dml
                            Updates sample data from the database using a DML
                            statement.
        delete_data_with_dml
                            Deletes sample data from the database using a DML
                            statement.
        update_data_with_dml_timestamp
                            Updates data with Timestamp from the database using
                            a DML statement.
        dml_write_read_transaction
                            First inserts data then reads it from within a
                            transaction using DML.
        update_data_with_dml_struct
                            Updates data with a DML statement and STRUCT
                            parameters.
        insert_with_dml     Inserts data with a DML statement into the
                            database.
        query_data_with_parameter
                            Queries sample data from the database using SQL
                            with a parameter.
        write_with_dml_transaction
                            Transfers part of a marketing budget from one
                            album to another.
        update_data_with_partitioned_dml
                            Update sample data with a partitioned DML
                            statement.
        delete_data_with_partitioned_dml
                            Delete sample data with a partitioned DML
                            statement.
        update_with_batch_dml
                            Updates sample data in the database using Batch
                            DML.
        create_table_with_datatypes
                            Creates a table with supported dataypes.
        insert_datatypes_data
                            Inserts data with supported datatypes into a table.
        query_data_with_array
                            Queries sample data using SQL with an ARRAY
                            parameter.
        query_data_with_bool
                            Queries sample data using SQL with a BOOL
                            parameter.
        query_data_with_bytes
                            Queries sample data using SQL with a BYTES
                            parameter.
        query_data_with_date
                            Queries sample data using SQL with a DATE
                            parameter.
        query_data_with_float
                            Queries sample data using SQL with a FLOAT64
                            parameter.
        query_data_with_int
                            Queries sample data using SQL with a INT64
                            parameter.
        query_data_with_string
                            Queries sample data using SQL with a STRING
                            parameter.
        query_data_with_timestamp_parameter
                            Queries sample data using SQL with a TIMESTAMP
                            parameter.

    optional arguments:
      -h, --help            show this help message and exit
      --database-id DATABASE_ID
                            Your Cloud Spanner database ID.
