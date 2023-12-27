## Project boilerplate: Fastapi + SQLModel + Alembic + Repository pattern ##

### Repository ###

Each Repository comes with a set of typed methods to perform common CRUD operations on your entities:

- `create`: Create a new record of an entity
- `create_batch`: Create a batch of records of an entity
- `get`: Get a single record by its ID
- `get_batch`: Get all records of an entity that match the given filters
- `get_batch_by_ids`: Get a batch of records by their IDs
- `get_all`: Get all records of an entity
- `update`: Update an entity instance
- `update_by_id`: Update an entity by its ID
- `update_batch`: Update a batch of entity instances with the same values
- `update_batch_by_ids`: Update a batch of entities by their IDs
- `delete`: Delete an entity instance
- `delete_by_id`: Delete an entity by its ID
- `delete_batch`: Delete a batch of entity instances
- `delete_batch_by_ids`: Delete a batch of entities by their IDs

### BaseRepository ###

If you require more flexibility, you may also use the BaseRepository which provides more granular operations. The BaseRepository provides the following methods:

- `create`: Create a new record of an entity
- `create_batch`: Create a batch of records of an entity
- `update`: Update an entity instance
- `update_batch`: Update a batch of entity instances with the same values
- `get`: Get a single record by its ID
- `get_batch`: Get all records of an entity that match the given filters
- `find`: Find all records of an entity that match the given filters
- `delete`: Delete an entity instance
- `delete_batch`: Delete a batch of entity instances