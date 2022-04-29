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
