# Contributing to the Taskmaster Project Template

Thank you for your interest in improving this project template! This guide will help you contribute effectively.

## Ways to Contribute

- 🐛 **Report bugs** in the template setup or configuration
- 💡 **Suggest features** that would benefit most template users
- 📚 **Improve documentation** and setup guides
- 🔧 **Fix issues** with Taskmaster integration
- ✨ **Add new template configurations** for different project types

## Getting Started

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/yourusername/your-fork-name.git
   cd your-fork-name
   ```

3. **Set up the template locally:**
   ```bash
   # Install Taskmaster if you haven't already
   npm install -g task-master-ai
   
   # Set up API keys (optional for template testing)
   cp .env.example .env
   ```

4. **Test your changes:**
   - Try the template setup process from a user's perspective
   - Verify Taskmaster integration works correctly
   - Test with different AI model configurations

## Development Guidelines

### Template Principles

This template should be:
- **Universal** - Suitable for various project types
- **Minimal** - Include only essential, widely-useful configurations
- **Well-documented** - Clear setup instructions and examples
- **Taskmaster-optimized** - Leverage Taskmaster's full capabilities

### What to Include

✅ **Good additions:**
- Generic development configurations
- Widely-applicable Cursor rules
- Universal Taskmaster workflows
- Cross-language/framework patterns

❌ **Avoid adding:**
- Technology-specific configurations (unless very common)
- Personal preferences that aren't widely shared
- Complex setup requiring multiple external dependencies
- Experimental or unstable features

### Code Standards

- **Documentation:** All changes should include updated documentation
- **Examples:** Provide clear examples in the setup guide
- **Testing:** Test the template creation process manually
- **Backwards compatibility:** Don't break existing template users

## Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the guidelines above

3. **Update documentation:**
   - Update `README.md` if you add new features
   - Update `TEMPLATE_SETUP.md` for setup changes
   - Add examples for new capabilities

4. **Test thoroughly:**
   - Create a new repository from the template
   - Follow the setup process completely
   - Verify Taskmaster integration works

5. **Commit with clear messages:**
   ```bash
   git commit -m "feat: add support for xyz configuration
   
   - Added new template configuration for xyz
   - Updated setup guide with xyz instructions
   - Added example workflow for xyz usage"
   ```

6. **Push and create PR:**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a pull request using the provided template.

## Reporting Issues

When reporting bugs or issues:

1. **Use the issue templates** provided in `.github/ISSUE_TEMPLATE/`
2. **Provide context:** What were you trying to accomplish?
3. **Include environment details:** OS, Node.js version, Taskmaster version
4. **Steps to reproduce:** Detailed steps to recreate the issue
5. **Expected vs actual behavior:** What should have happened?

## Suggesting Features

For feature requests:

1. **Check existing issues** to avoid duplicates
2. **Consider scope:** Would this benefit most template users?
3. **Provide use cases:** Real-world scenarios where this would help
4. **Consider alternatives:** Are there existing ways to accomplish this?

## Template Testing Checklist

When testing changes to the template:

- [ ] Template creation process works smoothly
- [ ] All documentation links work correctly
- [ ] Taskmaster initializes without errors
- [ ] AI model configuration works
- [ ] PRD parsing generates tasks correctly
- [ ] Basic Taskmaster commands work (`list`, `next`, `show`)
- [ ] Cursor rules load properly (if using Cursor)
- [ ] Environment variable setup is clear

## Questions or Need Help?

- **Template usage questions:** Check the [README](README.md) and [setup guide](.taskmaster/templates/TEMPLATE_SETUP.md)
- **Taskmaster questions:** Visit the [Taskmaster documentation](https://github.com/taskmaster-ai/taskmaster)
- **Feature discussions:** Open a feature request issue
- **Quick questions:** Use GitHub discussions

## Recognition

Contributors will be recognized in the project README. Significant contributions may be highlighted in release notes.

Thank you for helping make this template better for everyone! 🚀 