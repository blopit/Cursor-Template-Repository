# Testing Strategy & Quality Assurance Prompt

<!-- Created by: claude-3-5-sonnet-20241022 -->
<!-- Last edited: 2025-08-02 18:30:33 UTC by claude-3-5-sonnet-20241022 -->

## Testing Pyramid Strategy

### 1. Unit Tests (Foundation)

**70% of total tests**

- Test individual functions and methods
- Mock external dependencies
- Fast execution (milliseconds)
- High coverage of business logic
- Test edge cases and error conditions
- Independent and isolated

#### Unit Test Checklist

- [ ] All public methods tested
- [ ] Edge cases covered (null, empty, boundary values)
- [ ] Error conditions and exceptions tested
- [ ] Mock objects used for dependencies
- [ ] Tests run independently
- [ ] Clear test names describing behavior

### 2. Integration Tests (Middle)

**20% of total tests**

- Test component interactions
- Real database/API calls in test environment
- Verify data flow between systems
- Test configuration and environment setup
- Validate external service integrations

#### Integration Test Checklist

- [ ] Database operations tested end-to-end
- [ ] API endpoints tested with real requests
- [ ] File I/O operations validated
- [ ] Third-party service integrations verified
- [ ] Configuration loading tested
- [ ] Environment-specific behavior validated

### 3. End-to-End Tests (Top)

**10% of total tests**

- Test complete user workflows
- Browser automation for web apps
- Full system integration validation
- Performance and load testing
- User acceptance scenarios

#### E2E Test Checklist

- [ ] Critical user journeys tested
- [ ] Authentication flows validated
- [ ] Data persistence across sessions
- [ ] Cross-browser compatibility (if web)
- [ ] Mobile responsiveness (if applicable)
- [ ] Performance benchmarks met

## Test-Driven Development (TDD)

### Red-Green-Refactor Cycle

1. **RED**: Write failing test first
2. **GREEN**: Write minimal code to pass
3. **REFACTOR**: Improve code quality without changing behavior

### TDD Best Practices

- Write tests before implementation
- Keep tests simple and focused
- Test behavior, not implementation
- Use descriptive test names
- Maintain test independence
- Refactor tests along with code

## Testing Tools & Frameworks

### Unit Testing

- **Python**: pytest, unittest
- **JavaScript**: Jest, Mocha, Vitest
- **React**: React Testing Library
- **TypeScript**: ts-jest

### Integration Testing

- **API Testing**: Postman, Newman, RestAssured
- **Database**: TestContainers, in-memory databases
- **Mocking**: WireMock, MockServer

### E2E Testing

- **Web**: Playwright, Cypress, Selenium
- **Mobile**: Appium, Detox
- **Performance**: k6, JMeter, Artillery

## Test Data Management

### Test Data Strategy

- Use realistic but anonymized data
- Create reusable test fixtures
- Implement data cleanup strategies
- Maintain test data independence
- Version control test datasets

### Database Testing

- Use separate test databases
- Implement transaction rollback
- Create seed data scripts
- Test migrations and schema changes
- Validate data integrity constraints

## Performance Testing

### Load Testing

- Test normal expected load
- Identify performance bottlenecks
- Validate response times
- Monitor resource usage
- Test auto-scaling behavior

### Stress Testing

- Test beyond normal capacity
- Find breaking points
- Validate error handling under load
- Test recovery mechanisms
- Identify memory leaks

### Performance Metrics

- Response time (p95, p99)
- Throughput (requests/second)
- Resource utilization (CPU, memory)
- Error rates under load
- Time to recover from failures

## Continuous Integration Testing

### CI Pipeline Tests

- Run all unit tests on every commit
- Run integration tests on pull requests
- Execute E2E tests on main branch
- Performance regression testing
- Security vulnerability scanning

### Quality Gates

- Minimum test coverage threshold (80%+)
- All tests must pass before merge
- Performance benchmarks must be met
- Security scans must pass
- Code quality metrics enforced

## Test Reporting & Metrics

### Coverage Metrics

- Line coverage
- Branch coverage
- Function coverage
- Statement coverage
- Path coverage

### Quality Metrics

- Test execution time
- Test stability (flakiness)
- Defect detection rate
- Time to feedback
- Test maintenance cost

## Testing Anti-Patterns to Avoid

- Testing implementation details instead of behavior
- Overly complex test setups
- Brittle tests that break with minor changes
- Ignoring test failures
- No test maintenance
- Testing everything through UI
- Shared test state causing dependencies
- Inadequate test data management

## Test Maintenance

- Regular test review and cleanup
- Update tests with feature changes
- Remove obsolete tests
- Refactor test code for clarity
- Monitor and fix flaky tests
- Keep test documentation current
