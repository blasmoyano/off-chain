import pytest
from authentication.models import CustomUser
from django.urls import reverse
from tests.data_config.authentication_config import (
    generate_create_user,
    generate_create_user_api,
)


@pytest.mark.account
class TestAuthentication:
    @pytest.mark.parametrize(
        "data", generate_create_user(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_create_user(self, data):
        user = CustomUser.objects.create_user(**data["data"])
        assert user.email == data["expected_result"]["status_email"]
        assert user.username == data["expected_result"]["status_username"]

    @pytest.mark.parametrize(
        "data", generate_create_user_api(), ids=lambda elem: elem["id_str"]
    )
    @pytest.mark.django_db
    def test_api_create_user(self, api_client, data):
        endpoint = reverse(data["url"])
        response = api_client.post(endpoint, data=data["data"], format="json")
        assert response.status_code == data["expected_result"]["status_code"]
        assert response.json() == data["expected_result"]["status_response"]
