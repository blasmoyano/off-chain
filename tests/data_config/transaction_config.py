def generate_get_transaction():
    return [
        {
            "id_str": "get_transaction: ERROR Auth",
            "url": "get_transaction",
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
            "id_str": "get_transaction: EMPTY",
            "url": "get_transaction",
            "auth": True,
            "user": 0,
            "data": {},
            "expected_result": {"status_code": 200, "status_response": 0},
        },
        {
            "id_str": "get_transaction: PASS",
            "url": "get_transaction",
            "auth": True,
            "user": 1,
            "data": {},
            "expected_result": {"status_code": 200, "status_response": 1},
        },
    ]
