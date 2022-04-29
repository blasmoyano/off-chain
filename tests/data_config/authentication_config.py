USER = {
    "username": "user@example.com",
    "last_name": "last_test",
    "first_name": "first_test",
    "password": "pass123",
    "email": "user@example.com",
}

USER_TWO = {
    "username": "user_two@example.com",
    "last_name": "last_test_two",
    "first_name": "first_test_two",
    "password": "pass123",
    "email": "user_two@example.com",
}


USER_ADMIN = {
    "username": "user_admin",
    "email": "admin@test.com",
    "password": "password123",
}


def generate_create_user():
    return [
        {
            "id_str": "create_user: PASS",
            "data": {"username": "test_user", "email": "testuser@test_user"},
            "expected_result": {
                "status_username": "test_user",
                "status_email": "testuser@test_user",
            },
        }
    ]


def generate_create_user_api():
    return [
        {
            "id_str": "create_user_api: ERROR Email",
            "url": "register",
            "data": {
                "last_name": "last_test",
                "first_name": "first_test",
                "password": "pass123",
                "email": "testuser@test_user",
            },
            "expected_result": {
                "status_code": 400,
                "status_response": {"email": ["Enter a valid email address."]},
            },
        },
        {
            "id_str": "create_user_api: ERROR SEND password",
            "url": "register",
            "data": {
                "last_name": "last_test",
                "first_name": "first_test",
                "email": "user@example.com",
            },
            "expected_result": {
                "status_code": 400,
                "status_response": {"password": ["This field is required."]},
            },
        },
        {
            "id_str": "create_user_api: ERROR SEND email",
            "url": "register",
            "data": {
                "last_name": "last_test",
                "first_name": "first_test",
                "password": "pass123",
            },
            "expected_result": {
                "status_code": 400,
                "status_response": {"email": ["This field is required."]},
            },
        },
        {
            "id_str": "create_user_api: PASS",
            "url": "register",
            "data": {
                "last_name": "last_test",
                "first_name": "first_test",
                "password": "pass123",
                "email": "user@example.com",
            },
            "expected_result": {
                "status_code": 201,
                "status_response": {
                    "first_name": "first_test",
                    "last_name": "last_test",
                    "email": "user@example.com",
                },
            },
        },
    ]


def generate_create_token():
    return [
        {
            "id_str": "generate token: PASS",
            "url": "token_obtain_pair",
            "data": USER,
            "expected_result": {"status_code": 200},
        },
        {
            "id_str": "generate token: ERROR AUTH",
            "url": "token_obtain_pair",
            "data": {"email": "test_error", "password": "sarsa"},
            "expected_result": {"status_code": 401},
        },
    ]


def generate_create_token_verify():
    return [
        {
            "id_str": "verify token: PASS",
            "url": "token_verify",
            "url_token": "token_obtain_pair",
            "data": {"user": USER, "type": "PASS"},
            "expected_result": {"status_code": 200},
        },
        {
            "id_str": "verify token: ERROR",
            "url": "token_verify",
            "url_token": "token_obtain_pair",
            "data": {"user": USER, "type": "ERROR"},
            "expected_result": {"status_code": 401},
        },
    ]


def generate_create_token_refresh():
    return [
        {
            "id_str": "verify token: PASS",
            "url": "token_refresh",
            "url_token": "token_obtain_pair",
            "data": {"user": USER, "type": "PASS"},
            "expected_result": {"status_code": 200},
        },
        {
            "id_str": "verify token: ERROR",
            "url": "token_verify",
            "url_token": "token_obtain_pair",
            "data": {"user": USER, "type": "ERROR"},
            "expected_result": {"status_code": 400},
        },
    ]
