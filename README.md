# 🚀 MVP Template Repository

**The fastest way to go from Product Requirements Document (PRD) to a fully-configured, development-ready MVP.**

Transform any product idea into a production-ready development environment in minutes, complete with:
- ✅ **30+ Architecture Options** - From React to Django, mobile to blockchain
- ✅ **Popular Tech Stacks** - MERN, T3, Django+React, Next.js+Supabase, and more
- ✅ **AI-Powered Task Management** - Taskmaster integration with intelligent task generation
- ✅ **Battle-Tested Rules** - 1000+ cursor rules from awesome-cursor-rules
- ✅ **Complete Development Workflows** - TDD, CI/CD, testing, deployment patterns

> **🎯 This is a GitHub Template Repository**  
> Click **"Use this template"** to create a new repository with all configuration pre-built for your MVP.

---

## 🏃‍♂️ Quick Start (2 Commands)

### **For Python Developers:**
```bash
python3 quick_start.py
```

### **For JavaScript/Node.js Developers:**  
```bash
node quick-start.js
```

**That's it!** The script will:
1. **Download awesome-cursor-rules** automatically
2. **Show 30+ architecture options** with descriptions
3. **Set up your chosen tech stack** with all dependencies
4. **Create architecture-specific `.env.example`** with relevant variables
5. **Generate comprehensive `.cursorrules`** file
6. **Archive unused template files** to keep your project clean
7. **Create `add_architecture.py/js`** for adding more stacks later

---

## 🏗️ Available Architectures

### **Popular Tech Stacks (Recommended)**
Perfect combinations for rapid MVP development:

| Stack | Description | Best For |
|-------|-------------|----------|
| **MERN** | MongoDB + Express + React + Node.js | Full JavaScript MVPs |
| **T3 Stack** | Next.js + tRPC + Prisma | Type-safe full-stack |
| **Django + React** | Python backend + React frontend | Content-heavy apps |
| **FastAPI + React** | Modern Python + React | AI/ML-powered apps |
| **Next.js + Supabase** | Full-stack with real-time | Social/collaborative apps |
| **JAMStack** | Next.js + Netlify Functions | Static sites + dynamic features |
| **Mobile Full-Stack** | React Native + Express | Mobile + backend APIs |

### **Individual Architectures (30+ Options)**

**🌐 Frontend Frameworks:**
- React + TypeScript, Vue 3, Angular, Svelte, SolidJS

**📱 Mobile Development:**  
- React Native + Expo, Flutter, Swift/SwiftUI, Android/Compose

**⚡ Backend APIs:**
- FastAPI, Django, Flask, Express.js, NestJS, Spring Boot, Rails, Laravel

**☁️ Serverless:**
- Vercel Functions, Netlify Functions, AWS Lambda

**🗄️ Database & ORM:**
- Prisma + PostgreSQL, Supabase integration

**🧪 Testing:**
- Cypress, Playwright end-to-end testing

**⛓️ Blockchain:**
- Solidity + Hardhat, Solidity + Foundry

**📝 Language-Specific:**
- Python, TypeScript, Go, Rust development setups

---

## 🎯 Complete MVP Development Workflow

### **1. PRD to Production Pipeline**
This template includes a comprehensive workflow that takes you from PRD to production-ready code:

```bash
# 1. Set up your architecture
python3 quick_start.py  # Choose from 30+ options

# 2. Follow the AI-powered MVP workflow  
# See: dev_tools/prompts/workflow/mvp_setup_workflow.md
```

**The MVP workflow handles:**
- ✅ **PRD Analysis** - Extract requirements, constraints, success criteria
- ✅ **Architecture Selection** - AI-recommended tech stacks based on requirements  
- ✅ **Environment Setup** - Complete dev environment with all tooling
- ✅ **Task Generation** - Break PRD into actionable development tasks
- ✅ **Context Creation** - Detailed task context documents for developers
- ✅ **Development Ready** - Immediate handoff to development team

### **2. Architecture-Specific Environment**
Every architecture includes optimized configuration:

- **📦 Dependencies** - All required packages and dev dependencies
- **🔧 Scripts** - Dev server, build, test, deploy commands
- **📋 Environment Variables** - Architecture-specific `.env.example`
- **📏 Code Standards** - ESLint, Prettier, TypeScript configs
- **🧪 Testing Setup** - Jest, Cypress, framework-specific testing
- **📚 Documentation** - Setup guides and development workflows

### **3. AI-Powered Development**
Integration with Taskmaster AI for intelligent development:

- **🤖 Task Generation** - Auto-generate tasks from PRD
- **📊 Complexity Analysis** - AI analyzes and breaks down complex tasks
- **🔗 Dependency Management** - Automatic dependency tracking
- **📈 Progress Tracking** - Real-time status and completion tracking
- **🔍 Research Integration** - Access to current best practices

---

## 📁 Project Structure (After Setup)

```
my-mvp/                    # Your clean, production-ready project
├── src/                   # Source code (architecture-specific)
├── .cursorrules          # Consolidated rules for your architecture
├── .env.example          # Architecture-specific environment variables
├── .mvp-config.json      # Current architecture info (for other agents)
├── package.json          # Dependencies and scripts
├── requirements.txt      # Python dependencies (if applicable)
├── README.md             # Generated project documentation
├── active_prompts/       # Development workflow prompts
├── add_architecture.py   # Script to add more architectures later
└── archive/              # Original template files (archived)
```

**Template files are automatically archived** to keep your project clean!

---

## 🚀 Usage Examples

### **Web Application MVP**
```bash
python3 quick_start.py
# Choose: "Next.js + Supabase" 
# Result: Full-stack web app with auth, database, real-time features
```

### **Mobile App MVP**  
```bash
node quick-start.js
# Choose: "React Native + Expo"
# Result: Cross-platform mobile app with development tools
```

### **AI/ML Product MVP**
```bash
python3 quick_start.py  
# Choose: "FastAPI + React"
# Result: Python ML backend + React frontend
```

### **E-commerce MVP**
```bash
python3 quick_start.py
# Choose: "Django + React" 
# Result: Django backend + React storefront
```

---

## 🔄 Adding More Architectures Later

After initial setup, easily add additional architectures:

```bash
# Python projects
python3 add_architecture.py

# JavaScript projects  
node add_architecture.js
```

**Perfect for:**
- Adding mobile app to existing web product
- Adding admin dashboard to existing API
- Experimenting with new tech stacks
- Supporting multiple platforms

---

## 🌟 What Makes This Different

### **Battle-Tested Rules**
- **1000+ Cursor Rules** from awesome-cursor-rules repository
- **Architecture-Specific** - Only relevant rules for your chosen stack
- **Automatically Updated** - Rules are downloaded and mapped intelligently

### **Smart Environment Setup**
- **Architecture-Aware** `.env.example` with relevant variables only
- **No Generic Templates** - Each stack gets optimized configuration
- **Production-Ready** - All best practices built in

### **Complete Workflow Integration**
- **PRD → Tasks → Code** - Complete development pipeline
- **AI Task Management** - Intelligent breakdown of complex features
- **Context Documentation** - Every task includes detailed implementation guidance

### **Clean Handoff**
- **No Template Bloat** - Unused files automatically archived
- **Development Ready** - Team can start coding immediately
- **Extensible** - Easy to add more architectures later

---

## 📖 Documentation

- **[MVP Setup Workflow](dev_tools/prompts/workflow/mvp_setup_workflow.md)** - Complete PRD-to-development pipeline
- **[Natural Language Workflow](WORKFLOW.md)** - Human-friendly development guide  
- **[Architecture Definitions](architectures.json)** - Complete list of available stacks
- **[Development Prompts](dev_tools/prompts/)** - AI workflow templates

---

## 🤝 Contributing

1. Fork this repository
2. Add new architecture definitions to `architectures.json`
3. Create corresponding rules in `.cursor/rules/`
4. Test with both Python and Node.js quick-start scripts
5. Submit PR with documentation updates

---

## 📄 License

MIT License - Use this template for any project, commercial or personal.

---

**🎯 Ready to build your MVP? Run `python3 quick_start.py` or `node quick-start.js` and go from idea to development-ready in minutes!**
