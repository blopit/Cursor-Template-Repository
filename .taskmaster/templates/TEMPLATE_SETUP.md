# Template Setup Guide

Welcome to your new project! This template is pre-configured with Taskmaster AI for intelligent project management. Follow these steps to customize it for your specific project.

## Step 1: Rename Your Repository

If you cloned this template, consider renaming your repository to match your project:

### On GitHub:
1. Go to your repository settings
2. Scroll down to "Repository name"
3. Change from "Tiny-Heroes" to your project name
4. Click "Rename"

### Locally:
```bash
# Update your remote URL if you renamed on GitHub
git remote set-url origin https://github.com/yourusername/your-new-repo-name.git
```

## Step 2: Update Project Configuration

1. **Update Taskmaster project name:**
```bash
# This will open an interactive setup
task-master models --setup
```

Or manually edit `.taskmaster/config.json`:
```json
{
  "global": {
    "projectName": "Your Project Name"
  }
}
```

2. **Configure your AI models:**
Set up API keys in `.env`:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Step 3: Create Your Project Requirements Document (PRD)

1. **Copy the template:**
```bash
cp .taskmaster/templates/example_prd.txt .taskmaster/docs/your-project-prd.txt
```

2. **Customize your PRD:**
Edit `.taskmaster/docs/your-project-prd.txt` with:
- Your project overview
- Core features
- Technical requirements
- Development roadmap

3. **Generate initial tasks:**
```bash
task-master parse-prd .taskmaster/docs/your-project-prd.txt
```

## Step 4: Customize Development Rules

The template includes Cursor IDE rules in `.cursor/rules/`. Customize these to match your coding standards:

- **Add language-specific rules** (e.g., `python.mdc`, `react.mdc`)
- **Update existing rules** to match your team's conventions
- **Add project-specific patterns** as they emerge

## Step 5: Set Up Your Development Environment

1. **Initialize your project structure:**
```bash
# Create your main source directories
mkdir -p src components lib utils
```

2. **Set up your package.json (if needed):**
```bash
npm init -y
# Install your dependencies
```

3. **Configure additional tools:**
- ESLint/Prettier for code formatting
- Testing frameworks
- Build tools (Vite, Webpack, etc.)

## Step 6: Start Development

1. **View your tasks:**
```bash
task-master list
```

2. **Get your next task:**
```bash
task-master next
```

3. **Expand complex tasks:**
```bash
task-master analyze-complexity --research
task-master expand-all --research
```

## Advanced Features

### Multi-Context Development

For complex projects or team development:

```bash
# Create feature-specific contexts
task-master add-tag feature-auth --description="Authentication system"
task-master use-tag feature-auth

# Create experiment contexts
task-master add-tag experiment-ui-redesign --description="UI redesign exploration"
```

### Research Integration

Use Taskmaster's research capabilities for current best practices:

```bash
# Research before implementation
task-master research "best practices for React authentication 2024" --save-to 5.2

# Get context-aware implementation guidance
task-master research "how to implement JWT auth in Node.js" --id 5,6 --tree
```

## Cleaning Up Template Files

Once you've set up your project, you can optionally remove template-specific files:

```bash
# Remove this setup guide
rm .taskmaster/templates/TEMPLATE_SETUP.md

# Keep example_prd.txt as it's useful for creating new features
```

## Tips for Success

1. **Start with a comprehensive PRD** - The better your initial requirements, the better your generated tasks
2. **Use complexity analysis** - Let AI help break down complex tasks
3. **Leverage research** - Get current best practices and implementation guidance
4. **Use tags for organization** - Separate contexts for features, experiments, and team members
5. **Update tasks as you learn** - Use `update-subtask` to log discoveries and decisions

## Need Help?

- Check the [main README](../README.md) for detailed feature documentation
- Visit [Taskmaster documentation](https://github.com/taskmaster-ai/taskmaster) for advanced usage
- Use `task-master --help` for command reference

Happy coding! 🚀 