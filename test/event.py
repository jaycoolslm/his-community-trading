import requests, json, base64

data = {
    "algorithm_id": "test",
    "pool": "0xb4e267d955b0bbbc1ba5f39f9c92cc8369a1f712",
    "timeframe": "minute",
    "aggregate": 15,
    "limit": 300
}

url = "http://localhost:8080"

headers = {
    "Content-Type": "application/json",
    "ce-id": "123451234512345",
    "ce-specversion": "1.0",
    "ce-time": "2020-01-02T12:34:56.789Z",
    "ce-type": "google.cloud.pubsub.topic.v1.messagePublished",
    "ce-source": "//pubsub.googleapis.com/projects/MY-PROJECT/topics/MY-TOPIC"
}

bytes_data = json.dumps(data).encode('utf-8')

body = {
    "message": {
        "data": base64.b64encode(bytes_data).decode('utf-8'),
        "attributes": {
            "attr1": "attr1-value"
        }
    },
    "subscription": "projects/MY-PROJECT/subscriptions/MY-SUB"
}

response = requests.post(url, headers=headers, data=json.dumps(body))

# If you want to do something with the response
print(response.status_code)
print(response.text)

