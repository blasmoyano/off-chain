def generate_get_balance_me():
    return [
        {
            "id_str": "get_balance_me: ERROR Auth",
            "url": "get_by_id_balance_for_me",
            "auth": False,
            "user": 1,
            "data": {},
            "expected_result": {
                "status_code": 401,
                "status_response": {
                    "detail": "Authentication credentials were not provided."
                },
            },
        },
        {
            "id_str": "get_balance_me: ERROR User Auth",
            "url": "get_by_id_balance_for_me",
            "auth": True,
            "user": 2,
            "data": {},
            "expected_result": {
                "status_code": 403,
                "status_response": {"detail": "user path and user token not equal"},
            },
        },
        {
            "id_str": "get_balance_me: PASS",
            "url": "get_by_id_balance_for_me",
            "auth": True,
            "user": 1,
            "data": {},
            "expected_result": {"status_code": 200, "status_response": 1},
        },
    ]


def generate_get_balance_user():
    return [
        {
            "id_str": "get_balance_user: ERROR Auth",
            "url": "get_by_id_balance",
            "auth": False,
            "user": 1,
            "data": {},
            "expected_result": {
                "status_code": 401,
                "status_response": {
                    "detail": "Authentication credentials were not provided."
                },
            },
        },
        {
            "id_str": "get_balance_user: PASS",
            "url": "get_by_id_balance",
            "auth": True,
            "user": 1,
            "data": {},
            "expected_result": {"status_code": 200, "status_response": 1},
        },
        {
            "id_str": "get_balance_user: EMPTY",
            "url": "get_by_id_balance",
            "auth": True,
            "user": 10,
            "data": {},
            "expected_result": {"status_code": 200, "status_response": 0},
        },
    ]


def generate_post_balance():
    return [
        {
            "id_str": "post_balance: ERROR Auth",
            "url": "create_balance",
            "auth": False,
            "duplicate": False,
            "data": {},
            "expected_result": {
                "status_code": 401,
                "status_response": {
                    "detail": "Authentication credentials were not provided."
                },
            },
        },
        {
            "id_str": "post_balance: PASS",
            "url": "create_balance",
            "auth": True,
            "duplicate": False,
            "data": {"ticker_id": 1, "amount": 100},
            "expected_result": {"status_code": 201, "status_response": 100},
        },
        {
            "id_str": "post_balance: PASS Amount",
            "url": "create_balance",
            "auth": True,
            "duplicate": False,
            "data": {"ticker_id": 1, "amount": 10.4},
            "expected_result": {"status_code": 201, "status_response": 10.4},
        },
        {
            "id_str": "post_balance: DUPLICATE",
            "url": "create_balance",
            "auth": True,
            "duplicate": True,
            "data": {"ticker_id": 1, "amount": 10.4},
            "expected_result": {
                "status_code": 201,
                "status_response": 10.4,
                "duplicate_status_response": {
                    "message": "the balance with user and ticker exists"
                },
                "duplicate_status_code": 404,
            },
        },
        {
            "id_str": "post_balance: ERROR",
            "url": "create_balance",
            "auth": True,
            "duplicate": False,
            "data": {"ticker_id": 1},
            "expected_result": {
                "status_code": 400,
                "status_response": {"amount": ["This field is required."]},
            },
        },
        {
            "id_str": "post_balance: ERROR ticker",
            "url": "create_balance",
            "auth": True,
            "duplicate": False,
            "data": {"ticker_id": 10, "amount": 10.4},
            "expected_result": {
                "status_code": 400,
                "status_response": {
                    "ticker_id": ['Invalid pk "10" - object does not exist.']
                },
            },
        },
    ]
