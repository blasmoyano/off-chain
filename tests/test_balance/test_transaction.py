import pytest
from tests.data_config.transaction_config import generate_get_transaction
from django.urls import reverse


@pytest.mark.transaction
class TestTransaction:
    @pytest.mark.parametrize(
        "data", generate_get_transaction(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_get_transaction(self, api_client, get_token_admin, data, transaction):
        endpoint = reverse(data["url"], kwargs={"id": data["user"]})

        if data["auth"]:
            token_data = get_token_admin.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')
        response = api_client.get(endpoint)

        assert response.status_code == data["expected_result"]["status_code"]
        if data["auth"]:
            assert len(response.json()) == data["expected_result"]["status_response"]
        else:
            assert response.json() == data["expected_result"]["status_response"]
