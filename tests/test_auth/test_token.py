import pytest
from django.urls import reverse
from tests.data_config.authentication_config import (
    generate_create_token,
    generate_create_token_verify,
    generate_create_token_refresh,
)


@pytest.mark.token
class TestToken:
    @pytest.mark.parametrize(
        "data", generate_create_token(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_api_token(self, api_client, create_user, data):
        endpoint = reverse(data["url"])
        response = api_client.post(
            endpoint,
            data={"email": data["data"]["email"], "password": data["data"]["password"]},
            format="json",
        )
        assert response.status_code == data["expected_result"]["status_code"]

    @pytest.mark.parametrize(
        "data", generate_create_token_verify(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_api_token_verify(self, api_client, create_user, data):
        endpoint_token = reverse(data["url_token"])
        endpoint_verify = reverse(data["url"])

        response_token = api_client.post(
            endpoint_token,
            data={
                "email": data["data"]["user"]["email"],
                "password": data["data"]["user"]["password"],
            },
            format="json",
        )
        response = api_client.post(
            endpoint_verify,
            data={
                "token": response_token.json()["access"]
                if data["data"]["type"] == "PASS"
                else "token_error"
            },
            format="json",
        )
        assert response.status_code == data["expected_result"]["status_code"]

    @pytest.mark.parametrize(
        "data", generate_create_token_refresh(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_api_token_refresh(self, api_client, create_user, data):
        endpoint_token = reverse(data["url_token"])
        endpoint_refresh = reverse(data["url"])

        response_token = api_client.post(
            endpoint_token,
            data={
                "email": data["data"]["user"]["email"],
                "password": data["data"]["user"]["password"],
            },
            format="json",
        )
        response = api_client.post(
            endpoint_refresh,
            data={
                "refresh": response_token.json()["refresh"]
                if data["data"]["type"] == "PASS"
                else "token_error"
            },
            format="json",
        )
        assert response.status_code == data["expected_result"]["status_code"]
