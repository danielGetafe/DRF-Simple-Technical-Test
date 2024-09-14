# joinup

## Getting Started

### Prerequisites

- Python 3.12

### Installing

1. Clone the repository
```bash
git clone https://github.com/daniel-code/joinup.git
```

2. Navigate to the project directory
```bash
cd joinup
```

3. Create a virtual environment
```bash
python -m venv venv
```

4. Install the dependencies
```bash
source venv/bin/activate
pip install -r requirements.txt
```

5. Run migrations
```bash
python manage.py migrate
```

6. Run the server
```bash
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