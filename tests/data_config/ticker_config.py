def generate_create_ticker():
    return [
        {
            "id_str": "create_ticker: PASS",
            "url": "ticker",
            "auth": True,
            "data": {"name": "test_btc", "code": "TBT", "enable": True},
            "expected_result": {"status_code": 201},
        },
        {
            "id_str": "create_ticker: ERROR Field",
            "url": "ticker",
            "auth": True,
            "data": {"name": "test_btc", "enable": True},
            "expected_result": {
                "status_code": 400,
                "status_response": {"code": ["This field is required."]},
            },
        },
        {
            "id_str": "create_ticker: ERROR Field",
            "url": "ticker",
            "auth": True,
            "data": {"code": "TBT", "enable": True},
            "expected_result": {
                "status_code": 400,
                "status_response": {"name": ["This field is required."]},
            },
        },
        {
            "id_str": "create_ticker: ERROR Field",
            "url": "ticker",
            "auth": True,
            "data": {},
            "expected_result": {
                "status_code": 400,
                "status_response": {
                    "name": ["This field is required."],
                    "code": ["This field is required."],
                },
            },
        },
        {
            "id_str": "create_ticker: ERROR Code",
            "url": "ticker",
            "auth": True,
            "data": {"name": "test_btc", "code": "TBTD", "enable": True},
            "expected_result": {
                "status_code": 400,
                "status_response": {
                    "code": ["Ensure this field has no more than 3 characters."]
                },
            },
        },
        {
            "id_str": "create_ticker: ERROR Auth",
            "url": "ticker",
            "auth": False,
            "data": {"name": "test_btc", "code": "TBTD", "enable": True},
            "expected_result": {
                "status_code": 401,
                "status_response": {
                    "detail": "Authentication credentials were not provided."
                },
            },
        },
    ]


def generate_get_ticker():
    return [
        {
            "id_str": "list_ticker: ERROR Auth",
            "url": "ticker",
            "auth": False,
            "data": {},
            "expected_result": {
                "status_code": 401,
                "status_response": {
                    "detail": "Authentication credentials were not provided."
                },
            },
        },
        {
            "id_str": "list_ticker: PASS",
            "url": "ticker",
            "auth": True,
            "data": {},
            "expected_result": {
                "status_code": 200,
                "status_response": [
                    {"id": 2, "name": "Tether", "code": "USDT", "enable": True},
                    {"id": 4, "name": "Litecoin", "code": "LTC", "enable": True},
                    {"id": 3, "name": "Ethereum", "code": "ETH", "enable": True},
                    {"id": 1, "name": "Bitcoin", "code": "BTC", "enable": True},
                ],
            },
        },
    ]
