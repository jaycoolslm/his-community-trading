import os, json, logging, requests, datetime
from google.cloud import datastore
from dotenv import load_dotenv
from models import EventData
import math

load_dotenv()

kind = "hts-trading-tests"

def handle_event(algorithm_id: str, type: str, quantity: float, price: float):
    # mock res local testing
    if os.getenv("ENV") != "GCLOUD":
        print(f"Triggered {type} event")
        return
    client = datastore.Client()
    key = client.key(kind)
    task = datastore.Entity(key, exclude_from_indexes=[])
    # create the event
    event = EventData(
        algorithm_id=algorithm_id,
        type=type,
        quantity=quantity,
        price=price,
        timestamp=datetime.datetime.now()
    ).to_dict()
    task.update(event)
    client.put(task)