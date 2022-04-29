import pytest
from tests.data_config.ticker_config import generate_create_ticker, generate_get_ticker
from django.urls import reverse


@pytest.mark.ticker
class TestTicker:
    @pytest.mark.parametrize(
        "data", generate_create_ticker(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_post_ticker(self, api_client, get_token_admin, data):
        endpoint = reverse(data["url"])
        if data["auth"]:
            token_data = get_token_admin.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')
        response = api_client.post(endpoint, data=data["data"], format="json")

        assert response.status_code == data["expected_result"]["status_code"]
        data_response = response.json()
        try:
            del data_response["id"]
            assert data_response == data["data"]
        except KeyError:
            assert data_response == data["expected_result"]["status_response"]

    @pytest.mark.parametrize(
        "data", generate_get_ticker(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_get_ticker(self, api_client, get_token_admin, data):
        endpoint = reverse(data["url"])
        if data["auth"]:
            token_data = get_token_admin.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')
        response = api_client.get(endpoint)
        assert response.status_code == data["expected_result"]["status_code"]
        assert response.json() == data["expected_result"]["status_response"]
