import pytest
from tests.data_config.balance_config import (
    generate_get_balance_me,
    generate_get_balance_user,
    generate_post_balance,
)
from django.urls import reverse


@pytest.mark.balance
class TestBalance:
    @pytest.mark.parametrize(
        "data", generate_get_balance_me(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_get_balance_me(self, api_client, get_token, data, balance):
        endpoint = reverse(data["url"], kwargs={"id": data["user"]})

        if data["auth"]:
            token_data = get_token.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')

        response = api_client.get(endpoint)

        assert response.status_code == data["expected_result"]["status_code"]
        if response.status_code == 200:
            assert len(response.json()) == data["expected_result"]["status_response"]
        else:
            assert response.json() == data["expected_result"]["status_response"]

    @pytest.mark.parametrize(
        "data", generate_get_balance_user(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_get_balance_user(self, api_client, get_token_admin, data, balance):
        endpoint = reverse(data["url"], kwargs={"id": data["user"]})

        if data["auth"]:
            token_data = get_token_admin.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')

        response = api_client.get(endpoint)

        assert response.status_code == data["expected_result"]["status_code"]
        if response.status_code == 200:
            assert len(response.json()) == data["expected_result"]["status_response"]
        else:
            assert response.json() == data["expected_result"]["status_response"]

    @pytest.mark.parametrize(
        "data", generate_post_balance(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_post_balance(self, api_client, get_token, data):
        endpoint = reverse(data["url"])

        if data["auth"]:
            token_data = get_token.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')

        response = api_client.post(endpoint, data=data["data"], format="json")
        if data["duplicate"]:
            response_2 = api_client.post(endpoint, data=data["data"], format="json")
            assert (
                response_2.status_code
                == data["expected_result"]["duplicate_status_code"]
            )
            assert (
                response_2.json()
                == data["expected_result"]["duplicate_status_response"]
            )

        assert response.status_code == data["expected_result"]["status_code"]
        if response.status_code == 201:
            assert (
                response.json()["amount"] == data["expected_result"]["status_response"]
            )
        else:
            assert response.json() == data["expected_result"]["status_response"]
