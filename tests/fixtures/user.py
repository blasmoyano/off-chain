import pytest
from authentication.models import CustomUser
from tests.data_config.authentication_config import USER, USER_ADMIN
from django.urls import reverse


@pytest.fixture
def create_user():
    CustomUser.objects.create_user(**USER)
    return USER


@pytest.fixture()
def get_token_admin(api_client):
    CustomUser.objects.create_superuser(**USER_ADMIN)
    endpoint = reverse("token_obtain_pair")
    response = api_client.post(
        endpoint,
        data={"email": USER_ADMIN["email"], "password": USER_ADMIN["password"]},
        format="json",
    )
    return response


@pytest.fixture()
def get_token(api_client, create_user):

    endpoint = reverse("token_obtain_pair")
    response = api_client.post(
        endpoint,
        data={"email": USER["email"], "password": USER["password"]},
        format="json",
    )
    return response
