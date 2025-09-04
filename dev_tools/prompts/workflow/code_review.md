# Code Review & Quality Assurance Prompt

<!-- Created by: claude-3-5-sonnet-20241022 -->
<!-- Last edited: 2025-08-02 18:30:33 UTC by claude-3-5-sonnet-20241022 -->

## Review Checklist

### 1. Code Quality

- [ ] Follows established coding standards and style guides
- [ ] Proper error handling and edge case coverage
- [ ] Clear and meaningful variable/function names
- [ ] Appropriate comments explaining complex logic
- [ ] No code duplication (DRY principle)
- [ ] Functions are single-purpose and reasonably sized

### 2. Security & Safety

- [ ] Input validation and sanitization
- [ ] Proper authentication and authorization
- [ ] No sensitive data in logs or comments
- [ ] SQL injection and XSS prevention
- [ ] Secure API endpoints and data handling
- [ ] Environment variables for secrets

### 3. Performance & Efficiency

- [ ] Efficient algorithms and data structures
- [ ] Proper database queries (no N+1 problems)
- [ ] Appropriate caching strategies
- [ ] Resource cleanup (connections, files, etc.)
- [ ] Memory usage optimization
- [ ] Async/await patterns where appropriate

### 4. Testing & Validation

- [ ] Unit tests cover new functionality
- [ ] Integration tests for API endpoints
- [ ] Edge cases and error conditions tested
- [ ] Mock objects used appropriately
- [ ] Test coverage meets project standards
- [ ] Tests are clear and maintainable

### 5. Documentation & Context

- [ ] README updated if needed
- [ ] API documentation current
- [ ] Context documents reflect changes
- [ ] Inline documentation for complex logic
- [ ] Git commit messages are descriptive
- [ ] PR description explains changes clearly

### 6. Architecture & Design

- [ ] Follows established patterns and conventions
- [ ] Proper separation of concerns
- [ ] Clean interfaces between components
- [ ] Backward compatibility considered
- [ ] Scalability implications assessed
- [ ] Technical debt minimized

### 7. Dependencies & Integration

- [ ] New dependencies justified and secure
- [ ] Version compatibility checked
- [ ] Breaking changes identified
- [ ] Integration points tested
- [ ] Database migrations if needed
- [ ] Configuration changes documented

## Review Process

1. **Initial Scan**: Get overview of changes and scope
2. **Detailed Review**: Go through each file systematically
3. **Testing Review**: Verify test coverage and quality
4. **Documentation Check**: Ensure docs are current
5. **Integration Validation**: Check with existing systems
6. **Security Assessment**: Look for security implications
7. **Final Approval**: Confirm all criteria met

## Feedback Guidelines

- Be constructive and specific
- Suggest improvements, not just problems
- Explain the "why" behind feedback
- Acknowledge good practices
- Focus on code, not person
- Provide examples when possible
