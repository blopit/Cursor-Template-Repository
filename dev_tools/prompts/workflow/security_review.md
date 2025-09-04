# Security Review & Best Practices Prompt

<!-- Created by: claude-3-5-sonnet-20241022 -->
<!-- Last edited: 2025-08-02 18:30:33 UTC by claude-3-5-sonnet-20241022 -->

## Security Review Checklist

### 1. Authentication & Authorization

- [ ] Strong password requirements enforced
- [ ] Multi-factor authentication where appropriate
- [ ] Session management secure (timeout, invalidation)
- [ ] JWT tokens properly signed and validated
- [ ] OAuth2/OpenID Connect implemented correctly
- [ ] API keys secured and rotated regularly
- [ ] Role-based access control (RBAC) implemented
- [ ] Principle of least privilege followed

### 2. Input Validation & Sanitization

- [ ] All user inputs validated and sanitized
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS protection (output encoding)
- [ ] CSRF tokens implemented
- [ ] File upload restrictions and validation
- [ ] Rate limiting on API endpoints
- [ ] Input length limits enforced
- [ ] Whitelisting over blacklisting approach

### 3. Data Protection

- [ ] Sensitive data encrypted at rest
- [ ] Data encrypted in transit (HTTPS/TLS)
- [ ] PII handling compliant with regulations
- [ ] Database credentials secured
- [ ] API keys and secrets in environment variables
- [ ] No hardcoded credentials in code
- [ ] Secure data deletion procedures
- [ ] Regular security backups

### 4. API Security

- [ ] Authentication required for sensitive endpoints
- [ ] Rate limiting implemented
- [ ] Input validation on all parameters
- [ ] Proper HTTP status codes used
- [ ] CORS configured correctly
- [ ] API versioning strategy secure
- [ ] Request/response logging (without sensitive data)
- [ ] Error messages don't leak information

### 5. Infrastructure Security

- [ ] HTTPS enforced everywhere
- [ ] Security headers implemented (CSP, HSTS, etc.)
- [ ] Dependencies regularly updated
- [ ] Security patches applied promptly
- [ ] Firewall rules properly configured
- [ ] Monitoring and alerting in place
- [ ] Access logs maintained
- [ ] Regular security scans performed

### 6. Code Security

- [ ] No sensitive data in version control
- [ ] Secure coding practices followed
- [ ] Dependencies scanned for vulnerabilities
- [ ] Code review includes security assessment
- [ ] Static analysis tools used
- [ ] Dynamic security testing performed
- [ ] Secrets management system used
- [ ] Error handling doesn't expose internals

### 7. Privacy & Compliance

- [ ] GDPR compliance for EU users
- [ ] Privacy policy current and accessible
- [ ] Data retention policies defined
- [ ] User consent mechanisms in place
- [ ] Data anonymization where required
- [ ] Right to deletion implemented
- [ ] Data portability supported
- [ ] Regular compliance audits

## Security Testing

### Static Analysis

- Run SAST tools on codebase
- Check for known vulnerability patterns
- Validate dependency security
- Review configuration security

### Dynamic Testing

- Penetration testing on key endpoints
- Authentication bypass attempts
- Injection attack testing
- Session management testing

### Infrastructure Testing

- Network security assessment
- Server configuration review
- SSL/TLS configuration validation
- Firewall rule verification

## Incident Response Plan

1. **Detection**: Monitoring and alerting systems
2. **Assessment**: Determine scope and impact
3. **Containment**: Isolate affected systems
4. **Eradication**: Remove threat and vulnerabilities
5. **Recovery**: Restore systems and services
6. **Lessons Learned**: Post-incident review

## Security Metrics

- Time to detect security issues
- Time to patch vulnerabilities
- Number of security incidents
- Compliance audit results
- Security training completion rates

## Emergency Contacts

- Security team contact information
- Incident response team leads
- Legal/compliance contacts
- External security consultants
