# API Development Best Practices Prompt

<!-- Created by: claude-3-5-sonnet-20241022 -->
<!-- Last edited: 2025-08-02 18:30:33 UTC by claude-3-5-sonnet-20241022 -->

## API Design Principles

### 1. RESTful Design

- Use HTTP methods correctly (GET, POST, PUT, DELETE, PATCH)
- Resource-based URLs (/users, /orders, /products)
- Stateless operations
- Consistent naming conventions
- Proper HTTP status codes
- HATEOAS where appropriate

### 2. URL Structure

```
GET    /api/v1/users          # List all users
GET    /api/v1/users/123      # Get specific user
POST   /api/v1/users          # Create new user
PUT    /api/v1/users/123      # Update entire user
PATCH  /api/v1/users/123      # Partial user update
DELETE /api/v1/users/123      # Delete user
```

### 3. HTTP Status Codes

- **200 OK**: Successful GET, PUT, PATCH
- **201 Created**: Successful POST
- **204 No Content**: Successful DELETE
- **400 Bad Request**: Invalid input
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Permission denied
- **404 Not Found**: Resource doesn't exist
- **422 Unprocessable Entity**: Validation errors
- **500 Internal Server Error**: Server error

## Request/Response Format

### Request Structure

```json
{
  "data": {
    "type": "user",
    "attributes": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

### Response Structure

```json
{
  "data": {
    "id": "123",
    "type": "user",
    "attributes": {
      "name": "John Doe",
      "email": "john@example.com",
      "created_at": "2024-01-01T00:00:00Z"
    }
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "version": "1.0"
  }
}
```

### Error Response Format

```json
{
  "errors": [
    {
      "code": "VALIDATION_ERROR",
      "message": "Email is required",
      "field": "email",
      "timestamp": "2024-01-01T00:00:00Z"
    }
  ]
}
```

## Input Validation

### Validation Checklist

- [ ] Required fields validation
- [ ] Data type validation
- [ ] Format validation (email, phone, etc.)
- [ ] Length constraints
- [ ] Range validation for numbers
- [ ] Enum value validation
- [ ] Custom business rule validation
- [ ] Sanitization of input data

### Python Example (FastAPI + Pydantic)

```python
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v

    @validator('age')
    def age_must_be_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Age must be positive')
        return v
```

## Authentication & Authorization

### JWT Implementation

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

### Permission Checking

```python
def require_permission(permission: str):
    def decorator(func):
        async def wrapper(*args, current_user=Depends(get_current_user), **kwargs):
            if not user_has_permission(current_user, permission):
                raise HTTPException(status_code=403, detail="Insufficient permissions")
            return await func(*args, **kwargs)
        return wrapper
    return decorator
```

## Error Handling

### Global Exception Handler

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "code": "VALIDATION_ERROR",
            "message": error["msg"],
            "field": ".".join(str(x) for x in error["loc"]),
            "timestamp": datetime.utcnow().isoformat()
        })

    return JSONResponse(
        status_code=422,
        content={"errors": errors}
    )
```

## Rate Limiting

### Redis-based Rate Limiting

```python
import redis
from fastapi import HTTPException
import time

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def rate_limit(key: str, limit: int, window: int):
    current_time = int(time.time())
    pipeline = redis_client.pipeline()

    # Clean old entries
    pipeline.zremrangebyscore(key, 0, current_time - window)

    # Count current entries
    pipeline.zcard(key)

    # Add current request
    pipeline.zadd(key, {str(current_time): current_time})

    # Set expiration
    pipeline.expire(key, window)

    results = pipeline.execute()
    current_count = results[1]

    if current_count >= limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
```

## Database Integration

### Connection Management

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
```

### Repository Pattern

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class UserRepository(ABC):
    @abstractmethod
    async def create(self, user_data: dict) -> User:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    async def list(self, limit: int = 100, offset: int = 0) -> List[User]:
        pass

    @abstractmethod
    async def update(self, user_id: int, user_data: dict) -> Optional[User]:
        pass

    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        pass
```

## API Documentation

### OpenAPI Schema

```python
from fastapi import FastAPI

app = FastAPI(
    title="User Management API",
    description="API for managing users in the system",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations with users"
        }
    ]
)

@app.post("/users/", tags=["users"], summary="Create a new user")
async def create_user(user: UserCreate):
    """
    Create a new user with the following information:

    - **name**: User's full name
    - **email**: User's email address
    - **age**: User's age (optional)
    """
    # Implementation here
    pass
```

## Testing API Endpoints

### Unit Testing

```python
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "John Doe", "email": "john@example.com"}
    )
    assert response.status_code == 201
    assert response.json()["data"]["attributes"]["name"] == "John Doe"

def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
```

## Performance Optimization

### Caching Strategy

```python
import redis
import json
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_result(expiration: int = 300):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"

            # Try to get from cache
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return json.loads(cached_result)

            # Execute function and cache result
            result = await func(*args, **kwargs)
            redis_client.setex(cache_key, expiration, json.dumps(result))

            return result
        return wrapper
    return decorator
```

### Database Query Optimization

- Use database indexes effectively
- Implement pagination for large datasets
- Use select_related/prefetch_related in ORMs
- Optimize N+1 query problems
- Use database connection pooling
- Implement read replicas for read-heavy operations

## API Versioning

### URL Versioning

```python
from fastapi import APIRouter

v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")

@v1_router.get("/users/{user_id}")
async def get_user_v1(user_id: int):
    # Version 1 implementation
    pass

@v2_router.get("/users/{user_id}")
async def get_user_v2(user_id: int):
    # Version 2 implementation with enhanced features
    pass
```

## Monitoring & Logging

### Request Logging Middleware

```python
import time
import logging
from fastapi import Request

logger = logging.getLogger(__name__)

async def log_requests(request: Request, call_next):
    start_time = time.time()

    logger.info(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    process_time = time.time() - start_time
    logger.info(f"Response: {response.status_code} - {process_time:.4f}s")

    return response
```

### Health Check Endpoint

```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }
```

## Security Best Practices

- Always use HTTPS in production
- Implement proper authentication and authorization
- Validate and sanitize all inputs
- Use parameterized queries to prevent SQL injection
- Implement rate limiting to prevent abuse
- Log security events for monitoring
- Keep dependencies updated
- Use security headers (CORS, CSP, etc.)
- Implement proper error handling that doesn't leak information
