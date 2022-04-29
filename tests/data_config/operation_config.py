def generate_post_burn_airdrop_error():
    return [
        # Airdrop
        {
            "id_str": "post_airdrop: ERROR airdrop",
            "url": "create_operation",
            "operation_type": "airdrop",
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
            "id_str": "post_airdrop: ERROR Balance",
            "url": "create_operation",
            "operation_type": "airdrop",
            "auth": True,
            "data": {"user": 1, "ticker_id": 1, "amount": 10},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
        # NO URL
        {
            "id_str": "post_not_url: ERROR URL",
            "url": "create_operation",
            "operation_type": "pepe",
            "auth": False,
            "data": {},
            "expected_result": {},
        },
        # Burn
        {
            "id_str": "post_burn: ERROR Auth",
            "url": "create_operation",
            "operation_type": "burn",
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
            "id_str": "post_burn: ERROR Balance",
            "url": "create_operation",
            "operation_type": "burn",
            "auth": True,
            "data": {"user": 1, "ticker_id": 1, "amount": 10},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
    ]


def generate_post_burn_airdrop():
    return [
        # Airdrop
        {
            "id_str": "post_airdrop: ERROR User",
            "url": "create_operation",
            "operation_type": "airdrop",
            "auth": True,
            "data": {"user": 10, "ticker_id": 1, "amount": 10},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
        {
            "id_str": "post_airdrop: ERROR Ticker",
            "url": "create_operation",
            "operation_type": "airdrop",
            "auth": True,
            "data": {"user": 1, "ticker_id": 10, "amount": 10},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
        {
            "id_str": "post_airdrop: ERROR ticker",
            "url": "create_operation",
            "operation_type": "airdrop",
            "auth": True,
            "data": {"user": 1, "ticker_id": "test", "amount": 1},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "ticker or amount required integer"},
            },
        },
        {
            "id_str": "post_airdrop: ERROR ticker",
            "url": "create_operation",
            "operation_type": "airdrop",
            "auth": True,
            "data": {"user": 1, "ticker_id": 1, "amount": "sdas"},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "ticker or amount required integer"},
            },
        },
        {
            "id_str": "post_airdrop: Pass",
            "url": "create_operation",
            "operation_type": "airdrop",
            "auth": True,
            "data": {"user": 1, "ticker_id": 1, "amount": 10},
            "expected_result": {
                "status_code": 200,
                "status_response": {"message": "operation airdrop success"},
            },
        },
        # Burn
        {
            "id_str": "post_burn: ERROR User",
            "url": "create_operation",
            "operation_type": "burn",
            "auth": True,
            "data": {"user": 10, "ticker_id": 1, "amount": 10},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
        {
            "id_str": "post_airdrop: ERROR Ticker",
            "url": "create_operation",
            "operation_type": "burn",
            "auth": True,
            "data": {"user": 1, "ticker_id": 10, "amount": 10},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
        {
            "id_str": "post_airdrop: ERROR ticker",
            "url": "create_operation",
            "operation_type": "burn",
            "auth": True,
            "data": {"user": 1, "ticker_id": "test", "amount": 1},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "ticker or amount required integer"},
            },
        },
        {
            "id_str": "post_airdrop: ERROR ticker",
            "url": "create_operation",
            "operation_type": "burn",
            "auth": True,
            "data": {"user": 1, "ticker_id": 1, "amount": "sdas"},
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "ticker or amount required integer"},
            },
        },
        {
            "id_str": "post_airdrop: Pass",
            "url": "create_operation",
            "operation_type": "burn",
            "auth": True,
            "data": {"user": 1, "ticker_id": 1, "amount": 10},
            "expected_result": {
                "status_code": 200,
                "status_response": {"message": "operation burn success"},
            },
        },
        {
            "id_str": "post_airdrop: Pass",
            "url": "create_operation",
            "operation_type": "burn",
            "auth": True,
            "data": {"user": 1, "ticker_id": 1, "amount": 20},
            "expected_result": {
                "status_code": 404,
                "status_response": {
                    "message": "The amount is higher than what you have"
                },
            },
        },
    ]


def generate_post_peer_to_peer():
    return [
        {
            "id_str": "post_peer_to_peer: ERROR auth",
            "url": "create_peer_to_peer",
            "auth": False,
            "data": {
                "amount": 100,
                "ticker_id": 1,
                "user_receiver_id": 1,
                "user_sender_id": 2,
            },
            "expected_result": {
                "status_code": 401,
                "status_response": {
                    "detail": "Authentication credentials were not provided."
                },
            },
        },
        {
            "id_str": "post_peer_to_peer: ERROR USER",
            "url": "create_peer_to_peer",
            "auth": True,
            "data": {
                "amount": 5,
                "ticker_id": 1,
                "user_receiver_id": 1,
                "user_sender_id": 1,
            },
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "users cannot be the same"},
            },
        },
        {
            "id_str": "post_peer_to_peer: ERROR STR",
            "url": "create_peer_to_peer",
            "auth": True,
            "data": {
                "amount": "pepe",
                "ticker_id": "pepe",
                "user_receiver_id": 1,
                "user_sender_id": 2,
            },
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "ticker or amount required integer"},
            },
        },
        {
            "id_str": "post_peer_to_peer: PASS",
            "url": "create_peer_to_peer",
            "auth": True,
            "data": {
                "amount": 5,
                "ticker_id": 1,
                "user_receiver_id": 1,
                "user_sender_id": 2,
            },
            "expected_result": {
                "status_code": 200,
                "status_response": {"message": "operation peer to peer success"},
            },
        },
        {
            "id_str": "post_peer_to_peer: ERROR TICKER",
            "url": "create_peer_to_peer",
            "auth": True,
            "data": {
                "amount": 5,
                "ticker_id": 3,
                "user_receiver_id": 1,
                "user_sender_id": 2,
            },
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
        {
            "id_str": "post_peer_to_peer: ERROR AMOUNT",
            "url": "create_peer_to_peer",
            "auth": True,
            "data": {
                "amount": 15,
                "ticker_id": 1,
                "user_receiver_id": 1,
                "user_sender_id": 2,
            },
            "expected_result": {
                "status_code": 200,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
        {
            "id_str": "post_peer_to_peer: ERROR USER",
            "url": "create_peer_to_peer",
            "auth": True,
            "data": {
                "amount": 5,
                "ticker_id": 1,
                "user_receiver_id": 10,
                "user_sender_id": 2,
            },
            "expected_result": {
                "status_code": 404,
                "status_response": {"message": "Balance matching query does not exist"},
            },
        },
    ]
