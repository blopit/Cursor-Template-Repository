# Project Template with Taskmaster

A modern project template equipped with [Taskmaster AI](https://github.com/taskmaster-ai/taskmaster) for intelligent task management and development workflow automation.

> **🎯 This is a GitHub Template Repository**  
> Click **"Use this template"** to create a new repository with all the files and configuration pre-configured for your project. You'll get a clean repository with no history, ready to customize for your specific needs.

## What's Included

- 🤖 **Taskmaster AI Integration** - AI-powered task generation, management, and workflow optimization
- 📝 **PRD Templates** - Product Requirements Document templates for structured project planning
- 🏷️ **Tag-Based Task Management** - Multi-context task organization for features, branches, and experiments
- ⚙️ **Pre-configured Development Environment** - Ready-to-use configuration for modern development workflows
- 📊 **Task Complexity Analysis** - AI-driven analysis to break down complex tasks into manageable subtasks

## Quick Start

### 1. Use This Template

**Option A: Use Template Button (Recommended)**
1. Click the green **"Use this template"** button at the top of this repository
2. Choose "Create a new repository"
3. Give your project a name and description
4. Click "Create repository from template"

**Option B: Clone Manually**
```bash
git clone <your-repo-url>
cd <your-project-name>
```

### 2. Install Taskmaster (if not already installed)
```bash
npm install -g task-master-ai
```

### 3. Configure Your Project
The template comes pre-initialized with Taskmaster. Configure your AI models:
```bash
task-master models --setup
```

### 4. Create Your Project Requirements
1. Copy the example PRD template:
```bash
cp .taskmaster/templates/example_prd.txt .taskmaster/docs/my-project-prd.txt
```

2. Edit your PRD with your project details
3. Generate initial tasks from your PRD:
```bash
task-master parse-prd .taskmaster/docs/my-project-prd.txt
```

### 5. Start Development
```bash
# View your tasks
task-master list

# Get the next task to work on
task-master next

# View specific task details
task-master show <task-id>
```

## Features

### Intelligent Task Management
- **AI-Powered Task Generation** - Automatically generate tasks from PRD documents
- **Complexity Analysis** - AI analyzes task complexity and suggests optimal breakdown
- **Dependency Management** - Automatic dependency tracking and validation
- **Progress Tracking** - Real-time status updates and completion tracking

### Multi-Context Development
- **Tagged Task Lists** - Separate task contexts for different features, branches, or experiments
- **Git Integration** - Automatic tag creation from branch names
- **Team Collaboration** - Isolated contexts prevent merge conflicts

### Research-Backed Development
- **Live Research Integration** - Access to current best practices and up-to-date information
- **Implementation Guidance** - Context-aware suggestions based on your project files
- **Technology Updates** - Stay current with the latest library versions and security patches

## Project Structure

```
your-project/
├── .taskmaster/           # Taskmaster configuration and data
│   ├── config.json       # AI models and settings
│   ├── state.json        # Current tag context and state
│   ├── templates/        # PRD and other templates
│   ├── docs/            # Project documentation and PRDs
│   ├── tasks/           # Generated task files
│   └── reports/         # Complexity analysis reports
├── .cursor/             # Cursor IDE rules and configuration
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore patterns
└── README.md           # This file
```

## Workflow Examples

### Feature Development
```bash
# Create a new feature context
task-master add-tag feature-auth --description="User authentication system"

# Switch to the feature context
task-master use-tag feature-auth

# Generate tasks for the feature
task-master parse-prd docs/auth-feature-prd.txt --tag feature-auth

# Start development
task-master next
```

### Multi-Developer Teams
```bash
# Each developer creates their own context
task-master add-tag alice-work --copy-from-current
task-master use-tag alice-work

# Work independently without conflicts
# Merge contexts when ready
```

### Experiment Management
```bash
# Try out new technologies safely
task-master add-tag experiment-nextjs --description="Next.js migration experiment"
task-master use-tag experiment-nextjs

# If successful, promote to main
# If not, simply delete the tag
task-master delete-tag experiment-nextjs
```

## Customization

### AI Models
Configure different AI models for different purposes:
- **Main Model** - Primary task generation and updates
- **Research Model** - Live research and current best practices
- **Fallback Model** - Backup when primary model is unavailable

```bash
task-master models --set-main claude-3-7-sonnet-20250219
task-master models --set-research sonar-pro
task-master models --set-fallback gpt-4
```

### Rules and Patterns
The template includes Cursor IDE rules for consistent development patterns. Customize `.cursor/rules/` to match your coding standards.

## Environment Variables

Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
```

Required API keys (add the ones you'll use):
- `ANTHROPIC_API_KEY` - For Claude models
- `OPENAI_API_KEY` - For GPT models  
- `PERPLEXITY_API_KEY` - For research capabilities
- `GOOGLE_API_KEY` - For Gemini models

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Use Taskmaster to manage your development: `task-master add-tag feature-amazing-feature --from-branch`
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Taskmaster Documentation](https://github.com/taskmaster-ai/taskmaster)
- [Cursor IDE](https://cursor.sh/)
- [AI Development Best Practices](https://docs.taskmaster.dev/best-practices)
