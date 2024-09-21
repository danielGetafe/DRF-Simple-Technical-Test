# Django REST Framework simple technical test

## Context
In our company, we have a highly available (24/7) and high-performance (1500 - 2500 requests per minute) backend, so it is very important for us that requests to our backend are processed quickly to ensure it can handle them all. To achieve this, we focus on optimizing database queries, as they are typically the bottleneck for a server with these characteristic.

## Objective
Create a REST API using the following technologies: Python, Django, and Django Rest Framework. This API will initially consist of two endpoints: one for registration and another to access the user profile.

For the registration endpoint, the data will include: first name, last name, email, phone number, and a field where the user can write their hobbies. The registration endpoint will send an email and an SMS confirmation to validate both the email and the phone number.

Imagine you realize that both the email system and the SMS provider you have contracted are very slow, and since it is essential that all endpoints be fast: implement a solution so that both the email and SMS are sent asynchronously.

Both the email and SMS systems require a different configuration for the production environment than for the development/pre-production environment. In the latter, no actual emails or SMS will be sent.

It is not necessary to provide a real configuration for production, nor for sending emails or SMS. It can be left indicated, but it must be clear which configuration is for each environment, and that only in production, if a real configuration is set, both the email and SMS will be sent.

Additionally, implement an endpoint to retrieve the user profile. The data returned will be the same as the registration endpoint, plus two extra fields: validated email and validated phone number.

Create the test in a Git repository (GitHub or Bitbucket), either public or private. If it is private, you will need to share access with us.

Create a first version (tag 1.0.0) where both the email and SMS are sent synchronously, and another version (tag 1.1.0) where both the email and SMS are sent asynchronously.


## Getting Started

### Prerequisites

- Python 3.12

### Installing

1. Clone the repository
```bash
git clone git@github.com:danielGetafe/DRF-Simple-Technical.git
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Install the dependencies
```bash
source venv/bin/activate
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Install redis (optional)
```bash
sudo apt-get install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis
```

6. Run the server
```bash
redis-server
python manage.py runserver
```

## Running the tests

To run the tests, run the following command:
```bash
pytest -s
```


## Curl Examples

### Create a new user:

```bash
curl --location 'http://127.0.0.1:8000/api/users/register' \
--form 'first_name="John"' \
--form 'last_name="Doe"' \
--form 'email="johndoe@example.com"' \
--form 'phone_number="+34987654321"' \
--form 'hobbies="Watching Tv shows, practice football and programming, of course."'
```

### Get a user's profile:

```bash
curl --location 'http://127.0.0.1:8000/api/users/1'
```


## Next Steps...
1. Create github workflow to run tests when PR is created or updated...
2. Use different docker containers for drf, redis and postgres...
3. Inlcude more unit and integration tests...
4. Include implementation for SMS service...