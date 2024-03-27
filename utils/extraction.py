import requests
import pandas as pd
from datetime import datetime

base_url = 'https://api.geckoterminal.com/api/v2/networks/'

def extract_ohlcv_to_df(address, network='hedera-hashgraph', timeframe='hour', aggregate=1, limit=300):
    url = base_url + f'{network}/pools/{address}/ohlcv/{timeframe}?aggregate={aggregate}&limit={limit}'
    res = requests.get(url)
    data = res.json()
    # Extracting the OHLCV list
    ohlcv_list = data['data']['attributes']['ohlcv_list']
    
    # Preparing data for DataFrame
    # Here you can adjust usage of Open, High, Low, Close, Volume item depending on your algorithm needs
    data = {
        'date': [datetime.fromtimestamp(item[0]) for item in ohlcv_list],
        'TokenA/TokenB': [item[4] for item in ohlcv_list]
    }

    # Creating DataFrame
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date']).dt.tz_localize('UTC')
    df.set_index('date', inplace=True)
    return df