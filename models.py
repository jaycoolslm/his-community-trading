import datetime
from typing import TypedDict
from pydantic import BaseModel


class AlgorithmData(BaseModel):
    algorithm_id: str
    initial_balance: float
    current_balance: float
    pair_a: str
    pair_b: str

class EventData:
    def __init__(self, algorithm_id: str, type: str, quantity: float, price: float, timestamp: datetime.datetime):
        self.algorithm_id = algorithm_id
        self.type = type
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "algorithm_id": self.algorithm_id,
            "type": self.type,
            "quantity": self.quantity,
            "price": self.price,
            "timestamp": self.timestamp.isoformat()  # Converts datetime to a string for better JSON compatibility
        }


class EventInput(TypedDict):
    algorithm_id: str
    pool: str
    timeframe: str
    aggregate: int
    limit: int