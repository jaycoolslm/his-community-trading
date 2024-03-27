import base64, json
from utils.datastore import get_last_event_timestamp, update_last_event_timestamp, get_algorithm_data
from utils.extraction import extract_ohlcv_to_df
from utils.trading_functions import custom_method
from utils.event_handler import handle_event
from datetime import datetime
from config import algorithm_id
from models import EventInput

def trade_hts(event):
# def trade_hts(event):
    print(f"Received event: {event}")
    decoded_json = base64.b64decode(event.data['message']['data']).decode('utf-8')
    data: EventInput = json.loads(decoded_json)

    # last event timestamp is useful if your logic should only be acted upon at a time after the previous one
    # you can update the last event timestamp with create_event_timestamp_entity() method
    id, last_event_timestamp = get_last_event_timestamp(data['pool'], data['timeframe'])
    
    # get data e.g. dummy account current balance for a given algorithm
    algorithm_id = data['algorithm_id']
    algorithm_data = get_algorithm_data(algorithm_id)
    
    # extract data from API - the data frame can be adjusted for your algorithm requirements
    df = extract_ohlcv_to_df(data['pool'], timeframe=data['timeframe'], aggregate=data['aggregate'], limit=data['limit'])
    # apply algorithm on data
    df['adjusted_data'] = custom_method(df['TokenA/TokenB'])

    # apply algorithm buy / sell logic here
    # please create Pull Request if you need some extra functionality built into the serverless fcn src
    condition = True
    if condition:
        # trigger sell event
        quantity_to_sell = algorithm_data.current_balance
        handle_event(
            algorithm_id,
            "sell",
            quantity=quantity_to_sell,
            price=5
        )
    else:
        # trigger buy event
        quantity_to_buy = algorithm_data.current_balance
        handle_event(
            algorithm_id,
            "buy",
            quantity=quantity_to_buy,
            price=10
        )