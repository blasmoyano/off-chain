import pytest
from tests.data_config.balance_config import (
    generate_get_balance_me,
    generate_get_balance_user,
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
