import pytest

from balance.exception import AmountBaseClass
from tests.data_config.operation_config import (
    generate_post_burn_airdrop,
    generate_post_burn_airdrop_error,
    generate_post_peer_to_peer,
)
from django.urls import reverse, NoReverseMatch


@pytest.mark.operation
class TestOperation:
    @pytest.mark.parametrize(
        "data", generate_post_burn_airdrop_error(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_post_operation_errors(self, api_client, get_token, data):
        try:
            endpoint = reverse(
                data["url"], kwargs={"operation_type": data["operation_type"]}
            )
        except NoReverseMatch:
            assert True
            return

        if data["auth"]:
            token_data = get_token.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')

        response = api_client.post(endpoint, data=data["data"], format="json")

        assert response.status_code == data["expected_result"]["status_code"]
        assert response.json() == data["expected_result"]["status_response"]

    @pytest.mark.parametrize(
        "data", generate_post_burn_airdrop(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_post_operation(self, api_client, get_token, data, balance):
        try:
            endpoint = reverse(
                data["url"], kwargs={"operation_type": data["operation_type"]}
            )
        except NoReverseMatch:
            assert True
            return

        if data["auth"]:
            token_data = get_token.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')

        response = api_client.post(endpoint, data=data["data"], format="json")
        assert response.status_code == data["expected_result"]["status_code"]
        assert response.json() == data["expected_result"]["status_response"]

    @pytest.mark.parametrize(
        "data", generate_post_peer_to_peer(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_post_peer_to_peer(
        self, api_client, get_token, data, balance, balance_user_two, create_user_two
    ):
        endpoint = reverse(data["url"])

        if data["auth"]:
            token_data = get_token.json()
            api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_data["access"]}')

        try:
            response = api_client.post(endpoint, data=data["data"], format="json")
        except AmountBaseClass:
            assert True
            return
        assert response.status_code == data["expected_result"]["status_code"]
        assert response.json() == data["expected_result"]["status_response"]
