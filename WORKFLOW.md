# 🚀 MVP Quick-Start Workflow

A natural language guide for rapid MVP development using this template repository.

## Step 1: Choose Your MVP Architecture

**Ask yourself**: What type of product are you building?

### 📱 Mobile App → React Native + Expo
**Best for**: iOS/Android apps, mobile-first experiences, cross-platform development
- **Time to MVP**: 2-4 weeks
- **Complexity**: Medium
- **Skills needed**: React, JavaScript/TypeScript, mobile UI patterns

### 🌐 Web Application → Next.js Full Stack  
**Best for**: Web apps, dashboards, SaaS products, content sites
- **Time to MVP**: 1-3 weeks
- **Complexity**: Medium to High
- **Skills needed**: React, Next.js, web development, API design

### ⚡ API Backend → Vercel Functions + Python
**Best for**: Microservices, API-first products, serverless backends
- **Time to MVP**: 1-2 weeks  
- **Complexity**: Low to Medium
- **Skills needed**: Python, API design, cloud functions

### 🎯 Custom Stack → Mix & Match Rules
**Best for**: Unique requirements, specific tech preferences, experimental setups
- **Time to MVP**: Varies
- **Complexity**: Depends on selection
- **Skills needed**: Varies by chosen technologies

## Step 2: Run the Quick-Start Script

```bash
node quick-start.js
```

**The script will ask you**:
1. Which architecture? (Select 1-4)
2. Project name? (Enter your MVP name)
3. (If custom) Which rules do you want? (Select specific guidelines)

**What happens automatically**:
- ✅ Consolidates relevant Cursor rules into `.cursorrules`
- ✅ Sets up development prompts in `active_prompts/`  
- ✅ Creates `package.json` with correct scripts
- ✅ Generates architecture-specific `README.md`
- ✅ Provides next-step instructions

## Step 3: Initialize Your Development Environment

### For React Native (Mobile):
```bash
npm install
npm install -g @expo/cli  # If not already installed
npm run dev  # Starts Expo development server
```

### For Next.js (Web):
```bash
npm install
npm run dev  # Starts development server at localhost:3000
```

### For Vercel Functions (API):
```bash
npm install
pip install -r requirements.txt
npm run dev  # Starts local Vercel development
```

## Step 4: Understand Your Active Rules

**Check `.cursorrules`** - This file now contains all the coding standards, patterns, and best practices for your chosen architecture.

**Key rule categories you'll have**:
- 📝 **Code Writing Standards**: Formatting, naming, structure
- 🧪 **Testing Guidelines**: How to write and run tests
- 🔄 **Git Workflow**: Commit messages, PR patterns, automation
- 🏗️ **Architecture Patterns**: Component structure, API design
- 🛡️ **Security Practices**: Environment variables, data handling

## Step 5: Use Development Prompts

**Check `active_prompts/`** - These contain structured workflows for common development tasks.

### Execution Prompt (TDD Workflow)
Use this for systematic feature development:
1. **Load Context**: Understand what you're building
2. **Write Tests**: Define expected behavior
3. **Implement**: Build the minimum code to pass tests  
4. **Refactor**: Clean up and optimize
5. **Document**: Update docs and context

### PR Debug Prompt
Use this for code review and bug fixing:
1. **Analyze Issue**: Understand the problem
2. **Investigate**: Trace through code and logs
3. **Fix**: Implement solution
4. **Test**: Verify fix works
5. **Document**: Update relevant documentation

## Step 6: Start Building Your MVP

### Development Cycle:
1. **Plan Feature**: Use active prompts to structure your approach
2. **Code with Standards**: Let Cursor rules guide your coding style
3. **Test Early**: Follow testing guidelines from your rules
4. **Commit Often**: Use git automation patterns
5. **Deploy Fast**: Use architecture-specific deployment commands

### When You Get Stuck:
- **Check your rules**: `.cursorrules` has solutions for common patterns
- **Use prompts**: `active_prompts/` has structured problem-solving workflows  
- **Reference README**: Architecture-specific commands and patterns

## Step 7: Scale and Iterate

### Adding Features:
- Follow the same TDD workflow from execution prompts
- Use established patterns from your active rules
- Maintain consistency with your chosen architecture

### When Architecture Changes:
- Re-run `node quick-start.js` to select new rules
- Migrate existing code using new patterns
- Update documentation and tests

---

## Natural Language Decision Tree

### "I want to build something quickly" 
→ **Choose the architecture you know best** → Run quick-start → Start coding

### "I'm not sure which tech stack to use"
→ **Consider your target users and platform** → Mobile users? React Native. Web users? Next.js. Other developers? API Backend.

### "I want to try something new"  
→ **Select Custom Architecture** → Pick rules that match your experiment → Learn as you build

### "I need specific functionality"
→ **Check available rules first** → Do you see Gmail API, UI components, form handling? → Choose architecture that includes those rules

### "I'm working with a team"
→ **Choose based on team skills** → Everyone knows React? Next.js. Mobile focus? React Native. Backend specialists? Vercel Functions.

---

**💡 Pro Tip**: Start with what you know, then experiment. The quick-start script can be re-run to change architectures as your MVP evolves!