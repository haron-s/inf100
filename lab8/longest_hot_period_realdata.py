from datetime import datetime, timedelta
from pathlib import Path
from longest_hot_period_realdata_helper import *
import requests

api_endpoint = 'https://frost.met.no/observations/v0.jsonld'
source_id = 'SN50540' # SN50540 er Florida målestasjon i Bergen

def response(client_id, source_id, start_date, end_date):
    start = f'{start_date.year}-{start_date.month}-{start_date.day}'
    end = f'{end_date.year}-{end_date.month}-{end_date.day}'
    response = requests.get(
        api_endpoint,
        params={
            'sources': source_id,
            'referencetime': f'{start}/{end}',
            'elements': 'mean(air_temperature P1D)',
            'levels': 'default',
            'timeoffsets': 'default',
        },
        headers={'User-Agent': 'inf100.ii.uib.no student'},
        auth=(client_id, '')
    )

    return response.json()

def longest_hot_period(client_id, source_id, start_date, end_date, threshold):
    json_data = response(client_id, source_id, start_date, end_date)

    temperatures = [
        json_data["data"][i]["observations"][0]["value"]
        for i in range(len(json_data["data"]))
        ]
    
    longest_period = hot_period(temperatures, threshold)
    
    start = convert(json_data["data"][longest_period[0]]["referenceTime"][0:10])
    end = convert(json_data["data"][longest_period[-1]]["referenceTime"][0:10]) + timedelta(days=1)

    return start, end

def test_longest_hot_period():
    client_id = Path('client_id.txt').read_text(encoding='utf-8').strip()
    start_date = datetime(year=2000, month=1, day=1)
    end_date = datetime(year=2024, month=1, day=1)
    threshold = 20
    source_id = 'SN50540' # Florida målestasjon i Bergen

    actual_start, actual_end = longest_hot_period(
        client_id, source_id, start_date, end_date, threshold
    )
    actual_start = actual_start.replace(tzinfo=None) # Fjerner tidssone
    actual_end = actual_end.replace(tzinfo=None) # Fjerner tidssone
    expected_start = datetime(year=2009, month=6, day=25)
    expected_end = datetime(year=2009, month=7, day=5)

    assert actual_start == expected_start
    assert actual_end == expected_end

if __name__ == '__main__':
    test_longest_hot_period()
