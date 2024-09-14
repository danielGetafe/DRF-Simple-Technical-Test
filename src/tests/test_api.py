import pytest
from rest_framework.test import APIClient

from src.users.models import User


class TestRegisterUserEndpoint:
    @pytest.mark.django_db()
    def test_register_user_ok(self) -> None:
        client = APIClient()

        response = client.post(
            "/api/users/register",
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@example.com",
                "phone_number": "+34123456789",
            },
        )

        assert response.status_code == 201
        assert response.data["first_name"] == "John"
        assert response.data["last_name"] == "Doe"
        assert response.data["email"] == "johndoe@example.com"
        assert response.data["phone_number"] == "+34123456789"
        assert User.objects.count() == 1
        user = User.objects.get(email="johndoe@example.com")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.phone_number == "+34123456789"
        assert user.is_email_verified is False
        assert user.is_phone_number_verified is False

    @pytest.mark.django_db()
    def test_register_user_email_already_exists(self) -> None:
        client = APIClient()
        User.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="+34123456789",
        )

        response = client.post(
            "/api/users/register",
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@example.com",
                "phone_number": "+34987654321",
            },
        )

        assert response.status_code == 400
        assert response.data["email"][0].code == "unique"
        assert (
            response.data["email"][0].__str__()
            == "user with this Email already exists."
        )

    @pytest.mark.django_db()
    def test_register_user_phone_number_already_exists(self) -> None:
        client = APIClient()
        User.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="+34123456789",
        )

        response = client.post(
            "/api/users/register",
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "nojohndoe@example.com",
                "phone_number": "+34123456789",
            },
        )

        assert response.status_code == 400
        assert response.data["phone_number"][0].code == "unique"
        assert (
            response.data["phone_number"][0].__str__()
            == "user with this Phone number already exists."
        )


class TestUserProfileEndpoint:
    @pytest.mark.django_db()
    def test_user_profile_ok(self) -> None:
        client = APIClient()
        user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="+34123456789",
        )

        response = client.get(f"/api/users/{user.id}")

        assert response.status_code == 200
        assert response.data["first_name"] == "John"
        assert response.data["last_name"] == "Doe"
        assert response.data["email"] == "johndoe@example.com"
        assert response.data["phone_number"] == "+34123456789"
        assert response.data["is_email_verified"] is False
        assert response.data["is_phone_number_verified"] is False

    @pytest.mark.django_db()
    def test_user_profile_not_found(self) -> None:
        client = APIClient()

        response = client.get("/api/users/1234")

        assert response.status_code == 404
        assert response.data["detail"].code == "not_found"
        assert response.data["detail"] == "No User matches the given query."
