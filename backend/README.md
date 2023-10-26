# Backend Service

This service is responsible for real-time Twitter monitoring, data preprocessing, model training, decision making, and API endpoints.

## Setup

1. Install Python 3.8 or higher.
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Running the Service

To start the service, run:

```bash
python manage.py runserver
```

## Files

- `twitter_monitoring.py`: Contains the code for real-time Twitter monitoring.
- `data_preprocessing.py`: Contains the code for data preprocessing.
- `model_training.py`: Contains the code for model training.
- `decision_making.py`: Contains the code for decision making.
- `api.py`: Contains the code for API endpoints.
- `models.py`: Contains the database schema.
- `tests.py`: Contains the unit tests.
- `migrations/`: Contains the database migration files.
- `utils.py`: Contains utility functions.
- `settings.py`: Contains the settings for the Django application.

## API Endpoints

- `/get_recent_flags`: Fetches recent flags from the bot.
- `/audit_flag`: Allows manual auditing of a flag.

## Tests

To run the tests, use the following command:

```bash
python manage.py test
```

## Docker

A `Dockerfile` is included for building a Docker image of the service. To build the image, run:

```bash
docker build -t backend .
```

To run the service in a Docker container, use:

```bash
docker run -p 8000:8000 backend
```

## Contributing

Please follow the established code style and ensure all tests pass before submitting a pull request. Code reviews are required for all contributions.