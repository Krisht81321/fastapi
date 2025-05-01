# FastAPI Blog Application

A modern blog API built with FastAPI, featuring user authentication, blog post management, and SQLAlchemy integration.

## Live API
- API Documentation: [https://fastapi-blog-agpo.onrender.com/docs](https://fastapi-blog-agpo.onrender.com/docs)
- Base URL: [https://fastapi-blog-agpo.onrender.com](https://fastapi-blog-agpo.onrender.com)

## Features

- User authentication with JWT tokens
- Blog post CRUD operations
- SQLAlchemy ORM integration
- Password hashing with bcrypt
- API documentation with Swagger UI
- Database connection pooling
- GZIP compression for responses
- CORS enabled for frontend integration

## API Usage

### Authentication
1. Create a new user:
```bash
curl -X POST "https://fastapi-blog-agpo.onrender.com/user" \
-H "Content-Type: application/json" \
-d '{"name":"Your Name","email":"your@email.com","password":"your_password"}'
```

2. Login to get access token:
```bash
curl -X POST "https://fastapi-blog-agpo.onrender.com/login" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=your@email.com&password=your_password"
```

3. Use the token for authenticated requests:
```bash
curl -X GET "https://fastapi-blog-agpo.onrender.com/blog" \
-H "Authorization: Bearer your_access_token"
```

## API Endpoints

### Authentication
- `POST /login` - User login (returns JWT token)

### Users
- `POST /user` - Create new user
- `GET /user/{id}` - Get user details

### Blog Posts
- `POST /blog` - Create new blog post
- `GET /blog` - Get all blog posts
- `GET /blog/{id}` - Get specific blog post
- `PUT /blog/{id}` - Update blog post
- `DELETE /blog/{id}` - Delete blog post

## Installation for Local Development

1. Clone the repository:
```bash
git clone https://github.com/Krisht81321/fastapi.git
cd fastapi
```

2. Create a virtual environment:
```bash
python -m venv fastapi-env
```

3. Activate the virtual environment:
- Windows:
```bash
fastapi-env\Scripts\activate
```
- Unix or MacOS:
```bash
source fastapi-env/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

1. Start the server:
```bash
uvicorn blog.main:app --host 0.0.0.0 --port 8000 --reload
```

2. Access the API:
- API documentation: http://localhost:8000/docs
- Local access: http://localhost:8000
- Network access: http://<your-ip>:8000

## Project Structure

```
blog/
├── __init__.py
├── main.py           # FastAPI application and endpoints
├── database.py       # Database configuration
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic models
├── hashing.py        # Password hashing utilities
└── routers/         # API route modules
    ├── blog.py
    ├── user.py
    └── authentication.py
```

## Technical Details

### Performance Optimizations
- Connection pooling with SQLAlchemy
- GZIP compression for responses
- Multiple worker processes
- CORS middleware configuration
- Optimized database session management

### Security Features
- JWT token authentication
- Password hashing with bcrypt
- Database connection pooling
- Secure CORS configuration
- Environment variable configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 