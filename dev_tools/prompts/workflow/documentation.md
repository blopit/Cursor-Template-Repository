# Documentation Standards & Guidelines Prompt

<!-- Created by: claude-3-5-sonnet-20241022 -->
<!-- Last edited: 2025-08-02 18:30:33 UTC by claude-3-5-sonnet-20241022 -->

## Documentation Hierarchy

### 1. README Files (Entry Points)

**Purpose**: First point of contact for any directory or project

```markdown
# Project/Component Name

Brief description (1-2 sentences)

## Quick Start

- Installation instructions
- Basic usage example
- Links to detailed docs

## Key Features

- Feature 1: Brief description
- Feature 2: Brief description
- Feature 3: Brief description

## Documentation

- [Detailed Guide](docs/guide.md)
- [API Reference](docs/api.md)
- [Examples](examples/)

## Contributing

- [Development Guide](docs/development.md)
- [Issue Templates](.github/ISSUE_TEMPLATE/)
```

### 2. Technical Documentation

**Location**: `docs/` directory
**Types**:

- Architecture overview
- API documentation
- Installation guides
- User manuals
- Development guides

### 3. Code Documentation

**Inline documentation within code files**

- Function/method docstrings
- Complex logic explanations
- API endpoint documentation
- Configuration explanations

### 4. Context Documentation

**Task and implementation context**

- Task context files (`TASK_XX_CONTEXT.md`)
- Implementation notes
- Decision records
- Lessons learned

## Writing Standards

### Structure and Format

```markdown
# Document Title

<!-- Metadata -->
<!-- Created by: [model] -->
<!-- Last edited: [date] by [model] -->

## Overview

Brief description of what this document covers.

## Prerequisites

What the reader should know or have before reading.

## Main Content

### Section 1

Content with examples and code blocks.

### Section 2

More content with proper formatting.

## Examples

Practical examples with expected outputs.

## Troubleshooting

Common issues and solutions.

## Related Documentation

Links to related docs and resources.
```

### Code Documentation Standards

```python
def process_user_data(user_data: dict, validate: bool = True) -> dict:
    """
    Process and validate user data for storage.

    This function takes raw user data, applies validation rules,
    and formats it for database storage. It handles both new user
    creation and existing user updates.

    Args:
        user_data (dict): Raw user data containing fields like
            'name', 'email', 'age', etc.
        validate (bool, optional): Whether to apply validation
            rules. Defaults to True.

    Returns:
        dict: Processed user data ready for database storage.
            Contains validated and formatted fields.

    Raises:
        ValidationError: If user_data contains invalid values
            and validate=True.
        KeyError: If required fields are missing from user_data.

    Example:
        >>> user_input = {"name": "John", "email": "john@example.com"}
        >>> result = process_user_data(user_input)
        >>> print(result['name'])
        'John'
    """
    # Implementation here
    pass
```

### API Documentation Format

````markdown
## POST /api/v1/users

Create a new user in the system.

### Request

```json
{
  "name": "string (required)",
  "email": "string (required, valid email)",
  "age": "integer (optional, min: 1, max: 120)"
}
```
````

### Response

**Success (201 Created)**

```json
{
  "data": {
    "id": "123",
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

**Error (422 Unprocessable Entity)**

```json
{
  "errors": [
    {
      "field": "email",
      "message": "Invalid email format",
      "code": "VALIDATION_ERROR"
    }
  ]
}
```

### Authentication

Requires valid JWT token in Authorization header:

```
Authorization: Bearer <jwt_token>
```

### Rate Limiting

- 100 requests per minute per user
- Returns 429 status when exceeded

````

## Content Guidelines

### Writing Style
- **Clear and Concise**: Use simple, direct language
- **Action-Oriented**: Start with verbs (Configure, Install, Create)
- **Consistent Terminology**: Use the same terms throughout
- **Example-Rich**: Include practical examples and code samples
- **User-Focused**: Write from the user's perspective

### Code Examples
- **Complete**: Show full, working examples
- **Commented**: Explain complex parts
- **Tested**: Ensure examples actually work
- **Relevant**: Match the documentation context
- **Updated**: Keep examples current with latest code

### Visual Elements
```markdown
# Use headers for structure

## Important notices
> **Note**: This is important information
> **Warning**: This could cause problems
> **Tip**: This is a helpful suggestion

## Code blocks with syntax highlighting
```python
def example():
    return "Hello, World!"
````

## Lists for clarity

- Step 1: Do this first
- Step 2: Then do this
- Step 3: Finally this

## Tables for structured data

| Field | Type   | Required | Description         |
| ----- | ------ | -------- | ------------------- |
| name  | string | Yes      | User's full name    |
| email | string | Yes      | Valid email address |

````

## Documentation Types

### 1. User Documentation
**Audience**: End users of the application
- Getting started guides
- Feature tutorials
- FAQ sections
- Troubleshooting guides

### 2. Developer Documentation
**Audience**: Developers working with/on the code
- API reference
- Code architecture
- Development setup
- Contributing guidelines

### 3. Administrator Documentation
**Audience**: System administrators and DevOps
- Installation procedures
- Configuration guides
- Monitoring setup
- Backup procedures

### 4. Context Documentation
**Audience**: AI agents and future developers
- Implementation context
- Decision rationale
- Lessons learned
- Integration patterns

## Maintenance Practices

### Regular Updates
- Review docs when code changes
- Update examples and screenshots
- Verify links and references
- Check for outdated information

### Version Control
- Track documentation changes in git
- Use meaningful commit messages for doc changes
- Tag documentation versions with releases
- Maintain changelog for major doc updates

### Quality Assurance
- Spell check and grammar review
- Test all code examples
- Verify all links work
- Ensure consistent formatting

### Feedback Integration
- Monitor user questions and issues
- Update docs based on common confusion
- Incorporate feedback from code reviews
- Track documentation usage analytics

## Documentation Tools

### Writing Tools
- Markdown for most documentation
- Mermaid for diagrams and flowcharts
- OpenAPI/Swagger for API docs
- JSDoc/Sphinx for code documentation

### Review Process
1. Write documentation alongside code changes
2. Include docs in pull request reviews
3. Test all examples and instructions
4. Get feedback from target audience
5. Update based on review comments

### Automated Checks
- Spell checking in CI pipeline
- Link validation
- Code example testing
- Format consistency checking

## Templates

### Feature Documentation Template
```markdown
# Feature Name

## Overview
Brief description of the feature and its purpose.

## Use Cases
- Primary use case 1
- Secondary use case 2
- Edge case handling

## Getting Started
Step-by-step guide to using the feature.

## Configuration
Available options and their effects.

## Examples
Practical examples with expected outcomes.

## Troubleshooting
Common issues and solutions.

## API Reference
Detailed API documentation if applicable.
````

### API Endpoint Template

````markdown
## METHOD /path/to/endpoint

Brief description of what this endpoint does.

### Parameters

- `param1` (type): Description
- `param2` (type, optional): Description with default

### Request Example

```json
{
  "example": "request"
}
```
````

### Response Examples

**Success**

```json
{
  "result": "success"
}
```

**Error**

```json
{
  "error": "description"
}
```

### Notes

Any special considerations or limitations.

```

## Quality Metrics
- Documentation coverage (% of features documented)
- User satisfaction with documentation
- Time to answer common questions
- Documentation freshness (last update date)
- Error rate in following documentation
```
