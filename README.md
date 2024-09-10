# Event Management API
A Django REST API for managing events such as conferences, meetups, and other similar activities. This application allows users to create, view, update, and delete events, and it also supports user registration and event registrations.

# Features
- Event Management: Create, read, update, and delete events.
- User Authentication: Register, login, and manage user accounts using JWT authentication.
- Event Registration: Users can register for events.
- API Documentation: Auto-generated documentation using Swagger/OpenAPI.
- Admin panel on /admin.
- Docker Support: Easy setup and deployment with Docker.
- Bonus: Search and filter events based on criteria.

# Used technologies
- Programming language: Python
- Frameworks: Django, DRF
- Database: PosgreSQL

# How to use
To clone this project from GitHub, follow these steps:

Open your terminal or command prompt.
```shell
git clone git@github.com:NataliiaKorzh/event-manager.git

```
Run the following commands:
```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)

```

Fill your .env file using .env.sample as example

### Authentication (JWT)
User Registration
Users can register with the API using the /api/register/ endpoint.
After successful registration, they can log in to get their JWT token.

Login
Use the /api/login/ endpoint to obtain a JWT token for the user.
The token must be included in the Authorization header for all authenticated routes:

```
Authorization: Bearer <your_jwt_token>
```

### API Documentation
The project uses Swagger for API documentation.
You can access the interactive API documentation at the following URL when the server is running:
```
/api/doc/swagger/
```

# Run with Docker

Docker should be installed
```shell
docker-compose build
docker-compose up
```
