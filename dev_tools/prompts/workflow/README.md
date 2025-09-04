# Created by: claude-3.5-sonnet
# Last edited: 2024-12-19 15:30:00 UTC by claude-3.5-sonnet

# Workflow Prompts

This directory contains specialized workflow prompts for AI agents, guiding them through specific development processes, quality assurance workflows, and context management.

## Available Prompts

### Core Workflow Prompts

- **default.md**: Comprehensive task execution workflow with TDD methodology and CI debugging
- **execution_prompt.md**: Detailed Test-Driven Development execution prompt
- **PR_debug.md**: Comprehensive PR debugging and CI troubleshooting workflow
- **agent_handoff_workflow.md**: Complete context transfer protocol for agent handoffs

### Development Process Prompts

- **debugging.md**: Debug-first development methodology (investigate → plan → implement)
- **feature_scoping.md**: Feature planning and scoping requirements (plan before coding)
- **testing_strategy.md**: Comprehensive testing strategy (unit → integration → e2e)
- **code_review.md**: Code review checklist and quality assurance guidelines

### Technical Specialization Prompts

- **api_development.md**: REST API development best practices and patterns
- **security_review.md**: Security review checklist and best practices
- **documentation.md**: Documentation standards and writing guidelines

## Prompt Categories

### 1. Workflow Execution

- **Purpose**: Guide AI agents through specific development workflows
- **Examples**: TDD cycles, debugging processes, feature development, agent handoffs
- **Usage**: Reference during task execution for methodology guidance

### 2. Quality Assurance

- **Purpose**: Ensure code quality, security, and best practices
- **Examples**: Code review checklists, testing strategies, security audits
- **Usage**: Validation and verification during development

### 3. Planning & Design

- **Purpose**: Pre-implementation planning and design guidance
- **Examples**: Feature scoping, architecture planning, requirement analysis
- **Usage**: Before starting implementation work

### 4. Specialized Development

- **Purpose**: Domain-specific development guidance
- **Examples**: API development, security implementation, documentation writing
- **Usage**: When working on specific technical domains

## Usage Patterns

### Sequential Workflow

1. Start with **feature_scoping.md** for planning
2. Use **default.md** or **execution_prompt.md** for implementation
3. Apply **testing_strategy.md** during development
4. Follow **code_review.md** before completion
5. Use **security_review.md** for security validation
6. Apply **documentation.md** for documentation tasks
7. Use **agent_handoff_workflow.md** when transferring work between agents

### Debug-First Approach

1. Use **debugging.md** when encountering issues
2. Apply **PR_debug.md** for CI/CD problems
3. Follow systematic investigation before implementation

### API Development

1. Follow **feature_scoping.md** for planning
2. Use **api_development.md** for implementation
3. Apply **security_review.md** for security
4. Use **testing_strategy.md** for API testing

## Prompt Integration

These prompts are designed to work together and can be referenced using:

- `@prompt_name.md` syntax in conversations
- Direct file references in execution contexts
- Chained workflow execution across multiple prompts

## Best Practices

- Use appropriate prompt for the current phase of development
- Combine prompts for comprehensive coverage
- Reference prompts consistently across team
- Update prompts based on lessons learned
- Maintain prompt versioning and documentation

## File Structure

```
workflow/
├── default.md                    # Main task execution workflow
├── execution_prompt.md           # TDD execution methodology
├── PR_debug.md                  # CI/CD debugging workflow
├── agent_handoff_workflow.md    # Agent context transfer
├── debugging.md                  # Debug-first methodology
├── feature_scoping.md            # Feature planning requirements
├── testing_strategy.md           # Testing methodology
├── code_review.md               # Quality assurance checklist
├── api_development.md            # API development best practices
├── security_review.md            # Security guidelines
├── documentation.md              # Documentation standards
└── README.md                    # This file
```

**Note**: Duplicate files have been consolidated to maintain a clean, single-source-of-truth structure.
