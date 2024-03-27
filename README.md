# Custom Trading Algorithm Framework

Welcome to the Custom Trading Algorithm Framework! This repository provides a base for you to develop, test, and deploy your own trading algorithms. Follow the steps below to get started.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- [Functions Framework for Python](https://github.com/GoogleCloudPlatform/functions-framework-python)
- Any other dependencies listed in `requirements.txt`

### Clone the Repository

Start by cloning this repository to your local machine:

````git clone [URL_of_the_Repository]
cd [Repository_Name]```

## Customizing Your Trading Algorithm

To customize your trading algorithm, follow these steps:

### 1. Update Data Extraction Logic

If necessary, modify the logic in `extract_ohlcv_to_df` function to extract the relevant data (e.g., open, high, low, close, volume) needed for your algorithm.

### 2. Add Algorithm Logic

Implement your custom trading strategy in the `custom_method` function. This is where you define how your algorithm makes decisions.

### 3. Update Buy/Sell Logic

Revise the buy/sell logic in your algorithm to suit your strategy. Ensure that your logic aligns with the market conditions and indicators you're focusing on.

### 4. Run Tests

Test your algorithm to ensure it behaves as expected. Tests can be found in `test/event.py`. It's crucial to run these tests to validate your strategy under different scenarios.

## Running the Function Framework Server Locally

To run the Functions Framework server locally, execute the following command:

`OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES functions-framework --target=trade_hts --signature-type=cloudevent`


This command starts the server on your local machine, allowing you to send events and test your algorithm in a serverless function environment.

## Sending Events for Testing

Use the provided `test/event.py` script to send events to your function. This is an essential step to simulate real-world data and evaluate your algorithm's performance.

## Contributing

We encourage contributions to this repository! If you've developed an enhancement or fixed a bug, feel free to create a pull request.

## Support

If you encounter any issues or have questions, please file an issue in the repository's issue tracker.
````
