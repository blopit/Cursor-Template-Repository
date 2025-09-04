# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a template repository for rapid MVP development with architecture-specific rule and prompt assembly. The repository contains a comprehensive collection of Cursor rules and development prompts that can be dynamically assembled based on the chosen software architecture.

## Architecture

The repository is structured to support multiple development architectures and tech stacks:

### Available Rule Categories
- **Frontend Frameworks**: React Native (Expo), Next.js, general React patterns
- **Backend Solutions**: Vercel Functions (Python), Next.js API routes, serverless patterns
- **Testing Approaches**: React Native testing, general testing workflows, TDD patterns
- **Development Practices**: Git automation, PR workflows, CI/CD patterns, debugging
- **Code Quality**: DRY principles, naming conventions, documentation standards
- **Specialized Features**: Gmail API integration, mobile-first design, AI/LLM integration

### Rule Organization
```
.cursor/rules/
├── Core Development Rules
│   ├── code-writing-standards.mdc
│   ├── testing.mdc
│   ├── git-automation.mdc
│   └── pr-workflow-mandatory.mdc
├── Architecture-Specific Rules
│   ├── react-native-testing.mdc
│   ├── expo-development.mdc
│   ├── get-api-route.mdc (Vercel Functions)
│   └── mobile-first.mdc
├── Feature-Specific Rules
│   ├── gmail-api.mdc
│   ├── data-fetching.mdc
│   ├── form-handling.mdc
│   └── ui-components.mdc
└── Workflow Rules
    ├── taskmaster.mdc
    ├── dev_workflow.mdc
    └── context-first-workflow.mdc
```

### Prompt Templates
```
dev_tools/prompts/
├── workflow/
│   ├── execution_prompt.md (TDD workflows)
│   ├── agent_handoff_workflow.md
│   └── PR_debug.md
└── system/
    └── (Additional system prompts)
```

## Quick Start Assembly System

The repository is designed to support a quick-start script that will:

1. **Architecture Selection**: Choose from supported tech stacks
   - React Native + Expo + Vercel Functions
   - Next.js Full Stack
   - Custom architecture combinations

2. **Rule Assembly**: Automatically select and activate relevant rules based on architecture choice

3. **Prompt Configuration**: Set up appropriate development prompts and workflows

## Supported Tech Stacks

### Mobile-First Stack (React Native + Expo)
**Rules to activate:**
- expo-development.mdc
- react-native-testing.mdc
- mobile-first.mdc
- ui-components.mdc
- testing-workflow.mdc

**Key features:**
- File-based routing with Expo Router
- NativeWind for styling
- Comprehensive React Native testing setup
- Mobile-optimized development patterns

### Backend API Stack (Vercel Functions + Python)
**Rules to activate:**
- get-api-route.mdc
- environment-variables.mdc
- security.mdc
- testing.mdc

**Key features:**
- Python-based serverless functions
- Auth0 integration patterns
- Supabase database connections
- Structured API response patterns

### Full Stack Next.js
**Rules to activate:**
- project-structure.mdc (adapted for Next.js)
- data-fetching.mdc
- form-handling.mdc
- ui-components.mdc

## Development Commands

Since this is a template repository, specific build commands will depend on the chosen architecture:

### For React Native/Expo projects:
```bash
npm install
npx expo start
npm test
```

### For Next.js projects:
```bash
npm install
npm run dev
npm run build
npm test
```

### For Vercel Functions:
```bash
pip install -r requirements.txt
vercel dev
python -m pytest
```

## Rule Activation Strategy

The quick-start system should:

1. **Detect Architecture**: Based on user selection or project files
2. **Filter Rules**: Select only relevant rules for the chosen stack
3. **Configure Cursor**: Update `.cursorrules` or rule activation settings
4. **Setup Prompts**: Copy relevant prompts to active locations
5. **Initialize Project**: Set up basic project structure and dependencies

## Key Development Patterns

### Task Management Integration
- Taskmaster MCP integration for AI-driven development
- Context-first workflow with task documentation
- TDD execution prompts for structured development

### Code Quality Standards
- MDC format validation for documentation
- Automated PR title validation
- Comprehensive testing workflows
- Security-first development practices

### Architecture-Specific Optimizations
- Mobile-first responsive design patterns
- Serverless function optimization
- Type-safe API development
- Component reusability patterns

## Future Architecture Support

The template is designed to be extensible for additional tech stacks:
- Vue.js/Nuxt.js frontend patterns
- Django/Flask backend rules
- Docker/containerization workflows
- Cloud-specific deployment patterns (AWS, GCP, Azure)

## Configuration Management

- Environment variables handling per architecture
- Database connection patterns
- Authentication integration guides
- Deployment automation scripts

This template repository enables rapid MVP development by providing battle-tested rules and prompts tailored to specific technology choices, ensuring consistency and best practices from project initialization.