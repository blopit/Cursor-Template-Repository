# Debug-First Development Workflow

<!-- Created by: claude-3-5-sonnet-20241022 -->
<!-- Last edited: 2025-08-02 18:30:33 UTC by claude-3-5-sonnet-20241022 -->

## Core Principle

Investigate thoroughly → Get multiple solutions → Choose best approach → Then implement

## Debug Process Steps

### 1. Investigation Phase

- Gather ALL error messages and logs
- Check system status and resource usage
- Review recent changes and git history
- Document current system state
- Identify error patterns and frequency

### 2. Context Analysis

- Read relevant documentation and context files
- Check dependencies and versions
- Review configuration files
- Analyze environment differences
- Examine related components

### 3. Solution Planning

- Research known solutions and workarounds
- List 3-5 possible approaches
- Evaluate each option for:
  - Complexity and effort required
  - Risk of side effects
  - Long-term maintainability
  - Compatibility with existing system

### 4. Implementation Strategy

- Choose the most appropriate solution
- Plan implementation steps
- Identify validation methods
- Prepare rollback strategy
- Document the chosen approach

### 5. Execution & Validation

- Implement the chosen solution
- Test thoroughly in development
- Verify fix addresses root cause
- Check for unintended side effects
- Update documentation

### 6. Learning & Documentation

- Document the problem and solution
- Update relevant troubleshooting guides
- Share learnings with team
- Update monitoring to catch similar issues
- Consider preventive measures

## Anti-Patterns to Avoid

- No blind fixes without understanding
- No partial testing of solutions
- No skipping documentation step
- No ignoring warning signs
- No rushing to implement first idea

## Success Metrics

- Problem fully understood before fixing
- Solution tested and validated
- Documentation updated
- Root cause addressed, not just symptoms
- Prevention measures considered
