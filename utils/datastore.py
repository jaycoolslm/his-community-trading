import time, datetime, pytz, os
from dotenv import load_dotenv
from google.cloud import datastore

from models import AlgorithmData

load_dotenv()

timestamp_kind = "hts-trading-timestamps"

algorithm_kind = "hts-trading-algorithms"

def get_algorithm_data(algorithm_id: str) -> AlgorithmData:
    # mock res local testing
    if os.getenv("ENV") != "GCLOUD":
        return AlgorithmData(
            algorithm_id="test",
            initial_balance=1000,
            current_balance=1000,
            pair_a="TokenA",
            pair_b="TokenB"
        )
    # query db for live execution
    client = datastore.Client()
    query = client.query(kind=algorithm_kind)
    query.add_filter('algorithm_id', '=', algorithm_id)
    res = list(query.fetch())
    if (len(res) == 0):
        print("No algorithm found for algorithm_id", algorithm_id)
        return None
    return res[0]

def get_last_event_timestamp(pool: str, timeframe: str):
    client = datastore.Client()
    query = client.query(kind=timestamp_kind)
    query.add_filter('pool', '=', pool)
    query.add_filter('timeframe', '=', timeframe)
    res = list(query.fetch())
    if (len(res) == 0):
        print("No last_event_timestamp found for pool", pool, "timeframe", timeframe)
        current_unix_timestamp = int(time.time())
        timestamp = datetime.datetime.fromtimestamp(current_unix_timestamp).replace(tzinfo=pytz.utc)
        key = create_event_timestamp_entity(pool, timeframe, timestamp)
        return key.id, timestamp
        
    last_event_timestamp = res[0]['last_event_timestamp']
    print("last_event_timestamp", last_event_timestamp)
    return res[0].key.id, last_event_timestamp

def create_event_timestamp_entity(pool: str, timeframe: str, timestamp: datetime.datetime):
    client = datastore.Client()
    key = client.key(timestamp_kind)
    task = datastore.Entity(key, exclude_from_indexes=("last_event_timestamp",))
    # Apply new field values and save the Task entity to Datastore
    task.update(
        {
            "pool": pool,
            "timeframe": timeframe,
            "last_event_timestamp": timestamp,
        }
    )
    client.put(task)
    return task.key

def update_last_event_timestamp(id, timestamp: datetime.datetime):
    client = datastore.Client()
    with client.transaction():
        # Create a key for an entity of the specified kind and with the supplied entity_id
        key = client.key(timestamp_kind, id)
        # Use that key to load the entity
        entity = client.get(key)

        if not entity:
            raise ValueError(f"Entity of kind '{timestamp_kind}' with ID {id} does not exist.")

        # Update the 'last_event_timestamp' field
        entity["last_event_timestamp"] = timestamp

        # Persist the change back to Datastore
        client.put(entity)
