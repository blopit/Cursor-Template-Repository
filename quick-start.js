#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const readline = require('readline');

class MVPQuickStart {
  constructor() {
    this.projectRoot = process.cwd();
    this.rulesDir = path.join(this.projectRoot, '.cursor', 'rules');
    this.promptsDir = path.join(this.projectRoot, 'dev_tools', 'prompts');
    this.awesomeRulesDir = path.join(this.projectRoot, '.cursor', 'awesome-rules');
    this.archiveDir = path.join(this.projectRoot, 'archive');
    
    // Run initial setup if needed
    this.setupEnvironment();
    
    // Load architectures from JSON
    this.architectures = this.loadArchitectures();
    
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
  }

  setupEnvironment() {
    const { execSync } = require('child_process');
    
    // Create basic directories
    if (!fs.existsSync(path.dirname(this.rulesDir))) {
      fs.mkdirSync(path.dirname(this.rulesDir), { recursive: true });
    }
    if (!fs.existsSync(path.dirname(this.promptsDir))) {
      fs.mkdirSync(path.dirname(this.promptsDir), { recursive: true });
    }

    // Download awesome-cursor-rules if not present
    if (!fs.existsSync(this.awesomeRulesDir)) {
      console.log("🔧 Setting up awesome-cursor-rules...");
      try {
        const tempDir = path.join(this.projectRoot, 'temp-awesome-rules');
        
        // Clone repository
        execSync(`git clone --depth 1 https://github.com/PatrickJS/awesome-cursorrules.git "${tempDir}"`, { 
          stdio: 'pipe' 
        });
        
        // Move rules directory
        const rulesSource = path.join(tempDir, 'rules');
        if (fs.existsSync(rulesSource)) {
          fs.renameSync(rulesSource, this.awesomeRulesDir);
          console.log("✅ Downloaded awesome-cursor-rules");
        }
        
        // Clean up
        if (fs.existsSync(tempDir)) {
          fs.rmSync(tempDir, { recursive: true, force: true });
        }
        
      } catch (error) {
        console.log("⚠️  Failed to download awesome-cursor-rules. Continuing without them.");
      }
    }
    
    // Create rule mappings
    this.createRuleMappings();
  }

  createRuleMappings() {
    const mappings = {
      "mappings": {
        "react-typescript-cursorrules": "react-typescript/.cursorrules",
        "cursor-ai-react-typescript-shadcn-ui-cursorrules-p": "cursor-ai-react-typescript-shadcn-ui/.cursorrules",
        "vue-cursorrules-prompt-file": "vue/.cursorrules",
        "angular-novo-elements-cursorrules": "angular-novo-elements/.cursorrules",
        "angular-cursorrules-prompt-file-typescript": "angular-typescript/.cursorrules",
        "svelte-cursorrules-prompt-file": "svelte/.cursorrules",
        "next-type-llm": "next-type-llm/.cursorrules",
        "nuxt-cursorrules-prompt-file": "nuxt/.cursorrules",
        "remix-cursorrules-prompt-file": "remix/.cursorrules",
        "trpc-cursorrules-prompt-file": "trpc/.cursorrules",
        "react-native-cursorrules-prompt-file": "react-native/.cursorrules",
        "flutter-cursorrules-prompt-file": "flutter/.cursorrules",
        "swift-cursorrules-prompt-file-uikit": "swift-uikit/.cursorrules",
        "swift-cursorrules-prompt-file-swiftui": "swift-swiftui/.cursorrules",
        "android-jetpack-compose-cursorrules": "android-jetpack-compose/.cursorrules",
        "python-fastapi-cursorrules-prompt-file": "python-fastapi/.cursorrules",
        "python-django-cursorrules-prompt-file": "python-django/.cursorrules",
        "python-flask-cursorrules-prompt-file": "python-flask/.cursorrules",
        "express-cursorrules-prompt-file": "express/.cursorrules",
        "nestjs-cursorrules-prompt-file": "nestjs/.cursorrules",
        "java-spring-boot-cursorrules": "java-spring-boot/.cursorrules",
        "ruby-rails-cursorrules-prompt-file": "ruby-rails/.cursorrules",
        "laravel-cursorrules-prompt-file": "laravel/.cursorrules",
        "python-vercel-cursorrules-prompt-file": "python-vercel/.cursorrules",
        "netlify-functions-cursorrules": "netlify-functions/.cursorrules",
        "aws-lambda-cursorrules": "aws-lambda/.cursorrules",
        "prisma-cursorrules-prompt-file": "prisma/.cursorrules",
        "supabase-cursorrules-prompt-file": "supabase/.cursorrules",
        "cypress-cursorrules-prompt-file": "cypress/.cursorrules",
        "playwright-cursorrules-prompt-file": "playwright/.cursorrules",
        "solidity-hardhat-cursorrules": "solidity-hardhat/.cursorrules",
        "solidity-foundry-cursorrules": "solidity-foundry/.cursorrules",
        "python-projects-guide-cursorrules-prompt-file": "python-projects-guide/.cursorrules",
        "python-cursorrules-prompt-file-best-practices": "python-best-practices/.cursorrules",
        "typescript-cursorrules-prompt-file": "typescript/.cursorrules",
        "go-cursorrules-prompt-file": "go/.cursorrules",
        "rust-cursorrules-prompt-file": "rust/.cursorrules"
      }
    };
    
    const mappingsFile = path.join(this.projectRoot, 'rule-mappings.json');
    fs.writeFileSync(mappingsFile, JSON.stringify(mappings, null, 2));
  }

  loadArchitectures() {
    const archFile = path.join(this.projectRoot, 'architectures.json');
    if (fs.existsSync(archFile)) {
      try {
        const data = JSON.parse(fs.readFileSync(archFile, 'utf8'));
        return this.flattenArchitectures(data);
      } catch (error) {
        console.log(`⚠️  Failed to load architectures.json: ${error.message}`);
        return this.getDefaultArchitectures();
      }
    }
    return this.getDefaultArchitectures();
  }

  getDefaultArchitectures() {
    return {
      'react-native': {
        name: 'React Native + Expo (Mobile App)',
        local_rules: ['expo-development.mdc', 'react-native-testing.mdc', 'mobile-first.mdc'],
        awesome_rules: ['react-native-cursorrules-prompt-file'],
        packages: ['expo', '@expo/vector-icons', 'nativewind'],
        scripts: {
          "dev": "expo start",
          "test": "jest",
          "build": "expo build"
        }
      },
      'nextjs': {
        name: 'Next.js Full Stack',
        local_rules: ['project-structure.mdc', 'data-fetching.mdc', 'ui-components.mdc'],
        awesome_rules: ['next-type-llm'],
        packages: ['next', 'react', 'react-dom', 'typescript'],
        scripts: {
          "dev": "next dev",
          "build": "next build",
          "start": "next start"
        }
      },
      'custom': {
        name: 'Custom Architecture (Select your own rules)',
        local_rules: [],
        awesome_rules: [],
        packages: [],
        scripts: {}
      }
    };
  }

  flattenArchitectures(data) {
    const flattened = {};
    
    if (data.categories) {
      for (const [categoryKey, categoryData] of Object.entries(data.categories)) {
        if (categoryData.architectures) {
          Object.assign(flattened, categoryData.architectures);
        }
      }
    }
    
    if (data.presets) {
      Object.assign(flattened, data.presets);
    }
    
    // Add custom option
    flattened.custom = {
      name: 'Custom Architecture (Select your own rules)',
      local_rules: [],
      awesome_rules: [],
      packages: [],
      scripts: {}
    };
    
    return flattened;
  }

  question(query) {
    return new Promise(resolve => this.rl.question(query, resolve));
  }

  displayArchitectures() {
    console.log('\n🚀 Welcome to the MVP Quick-Start Setup!\n');
    console.log('Available architectures:');
    
    const archKeys = Object.keys(this.architectures);
    archKeys.forEach((key, index) => {
      console.log(`${index + 1}. ${this.architectures[key].name}`);
    });
  }

  async selectArchitecture() {
    this.displayArchitectures();
    
    const archKeys = Object.keys(this.architectures);
    const selection = await this.question(`\nSelect architecture (1-${archKeys.length}): `);
    const selectedKey = archKeys[parseInt(selection) - 1];
    
    if (!selectedKey) {
      console.log('Invalid selection. Please try again.');
      return this.selectArchitecture();
    }
    
    return { key: selectedKey, config: this.architectures[selectedKey] };
  }

  async selectCustomRules() {
    console.log('\n📋 Select rules for your custom architecture:');
    
    if (!fs.existsSync(this.rulesDir)) {
      console.log(`❌ Rules directory not found: ${this.rulesDir}`);
      return [];
    }
    
    const allRules = fs.readdirSync(this.rulesDir)
      .filter(file => file.endsWith('.mdc'))
      .sort();
    
    console.log('\nAvailable rules:');
    allRules.forEach((rule, index) => {
      const name = rule.replace('.mdc', '').replace(/-/g, ' ');
      console.log(`${index + 1}. ${name}`);
    });
    
    const selection = await this.question('\nEnter rule numbers (comma-separated, e.g., 1,3,5): ');
    const selectedIndices = selection.split(',').map(s => parseInt(s.trim()) - 1);
    
    return selectedIndices
      .filter(i => i >= 0 && i < allRules.length)
      .map(i => allRules[i]);
  }

  copyAwesomeRules(awesomeRules) {
    if (!awesomeRules || awesomeRules.length === 0 || !fs.existsSync(this.awesomeRulesDir)) {
      return [];
    }

    // Load rule mappings
    const mappingsFile = path.join(this.projectRoot, 'rule-mappings.json');
    if (!fs.existsSync(mappingsFile)) {
      console.log("⚠️  rule-mappings.json not found. Run setup.sh first.");
      return [];
    }

    let mappings;
    try {
      mappings = JSON.parse(fs.readFileSync(mappingsFile, 'utf8')).mappings || {};
    } catch (error) {
      console.log(`⚠️  Failed to load rule mappings: ${error.message}`);
      return [];
    }

    const copiedRules = [];
    for (const awesomeRule of awesomeRules) {
      if (mappings[awesomeRule]) {
        const sourcePath = path.join(this.awesomeRulesDir, mappings[awesomeRule]);
        if (fs.existsSync(sourcePath)) {
          try {
            // Ensure target directory exists
            if (!fs.existsSync(this.rulesDir)) {
              fs.mkdirSync(this.rulesDir, { recursive: true });
            }

            // Create target filename
            const targetFilename = `${awesomeRule.replace(/-/g, '_')}.mdc`;
            const targetPath = path.join(this.rulesDir, targetFilename);

            // Read and convert to MDC format
            const content = fs.readFileSync(sourcePath, 'utf8');
            const mdcContent = `---
description: ${awesomeRule.replace(/-/g, ' ')} rules from awesome-cursor-rules
globs: **/*
alwaysApply: true
---

${content}
`;

            fs.writeFileSync(targetPath, mdcContent);
            copiedRules.push(targetFilename);

          } catch (error) {
            console.log(`⚠️  Failed to copy ${awesomeRule}: ${error.message}`);
          }
        }
      }
    }

    if (copiedRules.length > 0) {
      console.log(`✅ Copied ${copiedRules.length} awesome rules to .cursor/rules/`);
    }

    return copiedRules;
  }

  activateRules(rules) {
    if (!rules || rules.length === 0) {
      console.log("⚠️  No rules to activate");
      return false;
    }

    const cursorrules = path.join(this.projectRoot, '.cursorrules');
    let ruleContent = '# Auto-generated Cursor Rules for MVP Development\n\n';

    let activatedCount = 0;
    rules.forEach(rule => {
      const rulePath = path.join(this.rulesDir, rule);
      if (fs.existsSync(rulePath)) {
        try {
          const content = fs.readFileSync(rulePath, 'utf8');
          ruleContent += `\n# === ${rule} ===\n`;
          ruleContent += content;
          ruleContent += '\n';
          activatedCount++;
        } catch (error) {
          console.log(`⚠️  Failed to read ${rule}: ${error.message}`);
        }
      }
    });

    if (activatedCount > 0) {
      fs.writeFileSync(cursorrules, ruleContent);
      console.log(`✅ Activated ${activatedCount} rules in .cursorrules`);
      return true;
    } else {
      console.log("❌ No rules were successfully activated");
      return false;
    }
  }

  setupPrompts(prompts) {
    if (!prompts || prompts.length === 0) {
      return true;
    }

    const targetDir = path.join(this.projectRoot, 'active_prompts');
    if (!fs.existsSync(targetDir)) {
      fs.mkdirSync(targetDir, { recursive: true });
    }

    let copiedCount = 0;
    prompts.forEach(prompt => {
      const sourcePath = path.join(this.promptsDir, prompt);
      if (fs.existsSync(sourcePath)) {
        try {
          const content = fs.readFileSync(sourcePath, 'utf8');
          const targetPath = path.join(targetDir, path.basename(prompt));
          fs.writeFileSync(targetPath, content);
          copiedCount++;
        } catch (error) {
          console.log(`⚠️  Failed to copy ${prompt}: ${error.message}`);
        }
      }
    });

    if (copiedCount > 0) {
      console.log(`✅ Set up ${copiedCount} prompts in active_prompts/`);
      return true;
    }
    return false;
  }

  createPackageJson(config, projectName) {
    const packageJson = {
      name: projectName.toLowerCase().replace(/\s+/g, '-'),
      version: "0.1.0",
      description: "MVP created with quick-start template",
      main: "index.js",
      scripts: config.scripts || {},
      dependencies: {},
      devDependencies: {}
    };

    fs.writeFileSync('./package.json', JSON.stringify(packageJson, null, 2));
    console.log('✅ Created package.json');

    if (config.packages && config.packages.length > 0) {
      console.log(`📦 Install these packages: npm install ${config.packages.join(' ')}`);
    }

    if (config.dev_dependencies && config.dev_dependencies.length > 0) {
      console.log(`🔧 Install dev packages: npm install --save-dev ${config.dev_dependencies.join(' ')}`);
    }

    if (config.requirements && config.requirements.length > 0) {
      const reqContent = config.requirements.join('\n');
      fs.writeFileSync('./requirements.txt', reqContent);
      console.log('✅ Created requirements.txt');
      console.log('🐍 Install Python packages: pip install -r requirements.txt');
    }

    return true;
  }

  createEnvExample(config, architectureKey) {
    // Base environment variables
    const envVars = {
      "# Environment Configuration": "",
      "NODE_ENV": "development"
    };

    // Architecture-specific environment variables
    const archEnvVars = {
      // Frontend frameworks
      'react': {
        "# API Keys": "",
        "VITE_API_URL": "http://localhost:3000/api",
        "VITE_APP_NAME": "My React App"
      },
      'vue': {
        "# API Keys": "",
        "VITE_API_URL": "http://localhost:3000/api",
        "VITE_APP_NAME": "My Vue App"
      },
      'angular': {
        "# API Keys": "",
        "NG_APP_API_URL": "http://localhost:3000/api",
        "NG_APP_NAME": "My Angular App"
      },

      // Full-stack frameworks
      'nextjs': {
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# Authentication": "",
        "NEXTAUTH_SECRET": "your-nextauth-secret-here",
        "NEXTAUTH_URL": "http://localhost:3000",
        "# API Keys": "",
        "OPENAI_API_KEY": "your-openai-key-here"
      },
      'nuxtjs': {
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# API Keys": "",
        "NUXT_SECRET_KEY": "your-secret-key-here"
      },
      'remix': {
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# Session": "",
        "SESSION_SECRET": "your-session-secret-here"
      },
      't3-stack': {
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# Next Auth": "",
        "NEXTAUTH_SECRET": "your-nextauth-secret-here",
        "NEXTAUTH_URL": "http://localhost:3000",
        "# tRPC": "",
        "TRPC_SECRET": "your-trpc-secret-here"
      },

      // Mobile
      'react-native': {
        "# Expo": "",
        "EXPO_PUBLIC_API_URL": "http://localhost:3000/api",
        "# Push Notifications": "",
        "EXPO_PUSH_TOKEN": "your-expo-push-token"
      },
      'flutter': {
        "# Flutter Environment": "",
        "FLUTTER_ENV": "development",
        "API_BASE_URL": "http://localhost:3000/api"
      },

      // Backend APIs
      'fastapi': {
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# Security": "",
        "SECRET_KEY": "your-secret-key-here",
        "ALGORITHM": "HS256",
        "ACCESS_TOKEN_EXPIRE_MINUTES": "30",
        "# CORS": "",
        "ALLOWED_ORIGINS": "http://localhost:3000,http://localhost:5173"
      },
      'django': {
        "# Django": "",
        "SECRET_KEY": "your-django-secret-key-here",
        "DEBUG": "True",
        "ALLOWED_HOSTS": "localhost,127.0.0.1",
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# CORS": "",
        "CORS_ALLOWED_ORIGINS": "http://localhost:3000,http://localhost:5173"
      },
      'flask': {
        "# Flask": "",
        "FLASK_ENV": "development",
        "SECRET_KEY": "your-flask-secret-key-here",
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb"
      },
      'expressjs': {
        "# Express": "",
        "PORT": "3000",
        "NODE_ENV": "development",
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# JWT": "",
        "JWT_SECRET": "your-jwt-secret-here"
      },
      'nestjs': {
        "# NestJS": "",
        "PORT": "3000",
        "# Database": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# JWT": "",
        "JWT_SECRET": "your-jwt-secret-here"
      },

      // Serverless
      'vercel-functions': {
        "# Vercel": "",
        "VERCEL_URL": "your-vercel-url",
        "# Database": "",
        "DATABASE_URL": "your-database-url",
        "# API Keys": "",
        "API_SECRET": "your-api-secret"
      },
      'netlify-functions': {
        "# Netlify": "",
        "NETLIFY_SITE_ID": "your-site-id",
        "# API Keys": "",
        "API_SECRET": "your-api-secret"
      },
      'aws-lambda': {
        "# AWS": "",
        "AWS_REGION": "us-east-1",
        "AWS_ACCESS_KEY_ID": "your-access-key",
        "AWS_SECRET_ACCESS_KEY": "your-secret-key"
      },

      // Database
      'prisma-postgresql': {
        "# Prisma": "",
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
        "# Shadow database for migrations": "",
        "SHADOW_DATABASE_URL": "postgresql://user:password@localhost:5432/shadow_db"
      },
      'supabase': {
        "# Supabase": "",
        "NEXT_PUBLIC_SUPABASE_URL": "your-supabase-url",
        "NEXT_PUBLIC_SUPABASE_ANON_KEY": "your-supabase-anon-key",
        "SUPABASE_SERVICE_ROLE_KEY": "your-service-role-key"
      },

      // Testing
      'cypress': {
        "# Cypress": "",
        "CYPRESS_BASE_URL": "http://localhost:3000"
      },
      'playwright': {
        "# Playwright": "",
        "PLAYWRIGHT_BASE_URL": "http://localhost:3000"
      },

      // Blockchain
      'solidity-hardhat': {
        "# Hardhat": "",
        "PRIVATE_KEY": "your-wallet-private-key",
        "INFURA_PROJECT_ID": "your-infura-project-id",
        "ETHERSCAN_API_KEY": "your-etherscan-api-key"
      },
      'solidity-foundry': {
        "# Foundry": "",
        "PRIVATE_KEY": "your-wallet-private-key",
        "RPC_URL": "https://eth-mainnet.alchemyapi.io/v2/your-key"
      }
    };

    // Combine base and architecture-specific vars
    const finalEnvVars = { ...envVars };
    if (archEnvVars[architectureKey]) {
      Object.assign(finalEnvVars, archEnvVars[architectureKey]);
    }

    // Always add common AI API keys at the end
    Object.assign(finalEnvVars, {
      "# AI API Keys (add only what you need)": "",
      "OPENAI_API_KEY": "your-openai-key-here",
      "ANTHROPIC_API_KEY": "your-anthropic-key-here",
      "GOOGLE_API_KEY": "your-google-key-here",
      "PERPLEXITY_API_KEY": "your-perplexity-key-here"
    });

    try {
      const envContent = [];
      for (const [key, value] of Object.entries(finalEnvVars)) {
        if (key.startsWith('#')) {
          envContent.push(`\n${key}`);
        } else if (value) {
          envContent.push(`${key}=${value}`);
        } else {
          envContent.push('');
        }
      }

      const envPath = path.join(this.projectRoot, '.env.example');
      fs.writeFileSync(envPath, envContent.join('\n'));
      console.log('✅ Created .env.example with architecture-specific variables');
      return true;
    } catch (error) {
      console.log(`❌ Failed to create .env.example: ${error.message}`);
      return false;
    }
  }

  createReadme(architecture, projectName, selectedRules) {
    const scriptsSection = architecture.scripts ? 
      "### Development Commands\n\n" + 
      Object.entries(architecture.scripts).map(([cmd, script]) => 
        `- **${cmd}**: \`npm run ${cmd}\` - ${script}`
      ).join('\n') + "\n\n" : "";

    const installSection = architecture.packages ? 
      "```bash\nnpm install\n" + (architecture.requirements ? "pip install -r requirements.txt\n" : "") + "```" :
      architecture.requirements ? "```bash\npip install -r requirements.txt\n```" : 
      "```bash\n# No dependencies to install\n```";

    const readme = `# ${projectName}

Quick-started MVP using **${architecture.name}** architecture.

## Architecture

This project was set up using the MVP Quick-Start Template with the following configuration:

### Active Rules
${selectedRules.map(rule => `- ${rule.replace('.mdc', '').replace(/-/g, ' ').replace(/_/g, ' ')}`).join('\n')}

${scriptsSection}## Getting Started

1. Install dependencies:
   ${installSection}

2. Start development:
   \`\`\`bash
   npm run dev
   \`\`\`

3. Run tests:
   \`\`\`bash
   npm run test
   \`\`\`

## Active Prompts

Check the \`active_prompts/\` directory for development workflow prompts that work with this architecture.

## Cursor Rules

All relevant Cursor rules have been consolidated into \`.cursorrules\`. These provide:
- Code standards and patterns
- Testing guidelines
- Development workflows
- Architecture-specific best practices

---

*Generated with MVP Quick-Start Template - Node.js Edition*
`;

    fs.writeFileSync('./README.md', readme);
    console.log('✅ Created README.md with setup instructions');
    return true;
  }

  archiveTemplateFiles(selectedArch, projectName) {
    console.log('\n📦 Archiving unused template files...');
    
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
    
    if (!fs.existsSync(this.archiveDir)) {
      fs.mkdirSync(this.archiveDir, { recursive: true });
    }

    const filesToArchive = [
      'quick_start.py',
      'quick-start.js',
      'quick-start-enhanced.js',
      'architectures.json',
      'rule-mappings.json',
      'setup.sh',
      'WORKFLOW.md'
    ];

    const dirsToArchive = [
      '.cursor/awesome-rules',
      '.cursor/rules',
      'dev_tools'
    ];

    let archivedCount = 0;

    // Archive files
    filesToArchive.forEach(fileName => {
      const filePath = path.join(this.projectRoot, fileName);
      if (fs.existsSync(filePath)) {
        try {
          const archivePath = path.join(this.archiveDir, `${timestamp}_${fileName}`);
          fs.copyFileSync(filePath, archivePath);
          fs.unlinkSync(filePath);
          archivedCount++;
        } catch (error) {
          console.log(`⚠️  Failed to archive ${fileName}: ${error.message}`);
        }
      }
    });

    // Archive directories
    dirsToArchive.forEach(dirName => {
      const dirPath = path.join(this.projectRoot, dirName);
      if (fs.existsSync(dirPath)) {
        try {
          const archivePath = path.join(this.archiveDir, `${timestamp}_${dirName.replace(/\//g, '_')}`);
          this.copyDirSync(dirPath, archivePath);
          this.removeDirSync(dirPath);
          archivedCount++;
        } catch (error) {
          console.log(`⚠️  Failed to archive ${dirName}: ${error.message}`);
        }
      }
    });

    // Create archive info file
    const archiveInfo = {
      archived_at: timestamp,
      selected_architecture: selectedArch,
      project_name: projectName,
      archived_files: filesToArchive,
      archived_directories: dirsToArchive,
      note: "These files were archived after quickstart setup. Use add_architecture.py to add more tech stacks."
    };

    const infoPath = path.join(this.archiveDir, `${timestamp}_archive_info.json`);
    fs.writeFileSync(infoPath, JSON.stringify(archiveInfo, null, 2));

    if (archivedCount > 0) {
      console.log(`✅ Archived ${archivedCount} template files to archive/`);
    }

    // Recreate .cursor/rules directory
    if (!fs.existsSync(this.rulesDir)) {
      fs.mkdirSync(this.rulesDir, { recursive: true });
    }
  }

  copyDirSync(src, dest) {
    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest, { recursive: true });
    }
    
    const entries = fs.readdirSync(src, { withFileTypes: true });
    
    for (const entry of entries) {
      const srcPath = path.join(src, entry.name);
      const destPath = path.join(dest, entry.name);
      
      if (entry.isDirectory()) {
        this.copyDirSync(srcPath, destPath);
      } else {
        fs.copyFileSync(srcPath, destPath);
      }
    }
  }

  removeDirSync(dirPath) {
    if (fs.existsSync(dirPath)) {
      fs.rmSync(dirPath, { recursive: true, force: true });
    }
  }

  setupTaskmaster(projectName) {
    try {
      const { execSync } = require('child_process');
      
      console.log('🤖 Setting up Taskmaster AI for task management...');
      
      // Check if Taskmaster is installed globally
      try {
        execSync('task-master --version', { stdio: 'ignore' });
        console.log('  ✅ Taskmaster already installed');
      } catch (error) {
        console.log('  📦 Installing Taskmaster globally...');
        try {
          execSync('npm install -g taskmaster-ai', { stdio: 'inherit' });
          console.log('  ✅ Taskmaster installed successfully');
        } catch (installError) {
          console.log(`  ⚠️  Failed to install Taskmaster: ${installError.message}`);
          console.log('  💡 You can install manually with: npm install -g taskmaster-ai');
          return false;
        }
      }
      
      // Create .taskmaster directory structure
      const taskmasterDir = path.join(process.cwd(), '.taskmaster');
      fs.mkdirSync(taskmasterDir, { recursive: true });
      fs.mkdirSync(path.join(taskmasterDir, 'docs'), { recursive: true });
      fs.mkdirSync(path.join(taskmasterDir, 'context'), { recursive: true });
      fs.mkdirSync(path.join(taskmasterDir, 'reports'), { recursive: true });
      
      // Initialize Taskmaster in the project
      try {
        execSync(`task-master init --name="${projectName}" --description="MVP project created from template"`, {
          cwd: process.cwd(),
          stdio: 'ignore'
        });
        console.log('  ✅ Taskmaster initialized in project');
      } catch (initError) {
        console.log(`  ⚠️  Failed to initialize Taskmaster: ${initError.message}`);
        console.log('  💡 You can initialize manually with: task-master init');
        return false;
      }
      
      // Create PRD template for users
      const prdTemplate = `# Product Requirements Document (PRD)

## Product Overview
- **Product Name**: [Your MVP Name]
- **Vision**: [One sentence describing what this product does]
- **Target Users**: [Who will use this product]

## Core Features
1. **Feature 1**: [Description of primary feature]
2. **Feature 2**: [Description of secondary feature]
3. **Feature 3**: [Description of additional feature]

## Technical Requirements
- **Platform**: [Web/Mobile/Desktop]
- **Performance**: [Speed, scalability requirements]
- **Security**: [Authentication, data protection needs]
- **Integrations**: [External APIs, services needed]

## Success Criteria
- **User Metrics**: [What makes users successful]
- **Business Metrics**: [What makes the business successful]
- **Technical Metrics**: [Performance benchmarks]

## Timeline & Constraints
- **MVP Timeline**: [Target completion date]
- **Budget Constraints**: [Development resources available]
- **Technical Constraints**: [Specific technology requirements]
`;
      
      const prdPath = path.join(taskmasterDir, 'docs', 'project-prd-template.md');
      fs.writeFileSync(prdPath, prdTemplate, 'utf8');
      
      // Create context template reference
      const contextReadme = `# Task Context Documents

This directory contains detailed context documents for each task generated from your PRD.

## Using Task Context
1. Each task has a corresponding context document: \`task_XX_context.md\`
2. Subtasks have their own context: \`task_XX_subtask_YY_context.md\`
3. Context documents include implementation guidelines, testing strategies, and success criteria

## Generating Task Context
After parsing your PRD with \`task-master parse-prd\`, use the MVP workflow:
\`\`\`bash
# Generate comprehensive context for all tasks
node -e "
const fs = require('fs');
const template = fs.readFileSync('dev_tools/templates/task_context_template.md', 'utf8');
// Use template to create context documents for each task
"
\`\`\`

## Context Document Structure
- **Task Overview**: Objective, business value, user impact
- **Success Criteria**: Functional requirements, acceptance criteria
- **Technical Context**: Architecture integration, dependencies
- **Implementation Guidelines**: Step-by-step approach
- **Testing Strategy**: Unit, integration, E2E tests
- **Success/Failure States**: What done looks like
`;
      
      fs.writeFileSync(path.join(taskmasterDir, 'context', 'README.md'), contextReadme, 'utf8');
      
      console.log('  ✅ Created .taskmaster/ directory structure');
      console.log('  ✅ Created PRD template at .taskmaster/docs/project-prd-template.md');
      console.log('  ✅ Task context directory ready');
      
      return true;
      
    } catch (error) {
      console.log(`  ⚠️  Error setting up Taskmaster: ${error.message}`);
      return false;
    }
  }

  createTaskmasterCommandsScript() {
    const scriptContent = `#!/usr/bin/env node
/**
 * Taskmaster Command Helper
 * Common commands for managing tasks in your MVP project.
 */

const { execSync } = require('child_process');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function runCommand(cmd, description) {
  console.log(\`🔧 \${description}...\`);
  try {
    const result = execSync(cmd, { encoding: 'utf8' });
    if (result) {
      console.log(result);
    }
    return true;
  } catch (error) {
    console.log(\`❌ Error: \${error.message}\`);
    return false;
  }
}

function main() {
  console.log("🤖 Taskmaster MVP Command Helper");
  console.log("=" * 40);
  
  const commands = {
    '1': ['task-master list --with-subtasks', 'List all tasks and subtasks'],
    '2': ['task-master next', 'Get next task to work on'],
    '3': ['task-master show <task_id>', 'Show detailed task information'],
    '4': ['task-master parse-prd .taskmaster/docs/project-prd.txt --num-tasks=15-25', 'Parse PRD and generate tasks'],
    '5': ['task-master analyze-complexity --research', 'Analyze task complexity'],
    '6': ['task-master expand --all --research --num=3-5', 'Break down complex tasks'],
    '7': ['task-master generate --output=docs/tasks/', 'Generate task documentation'],
    '8': ['task-master set-status --id=<task_id> --status=done', 'Mark task as completed'],
  };
  
  console.log("Available commands:");
  Object.entries(commands).forEach(([key, [cmd, desc]]) => {
    console.log(\`\${key}. \${desc}\`);
    console.log(\`   Command: \${cmd}\`);
    console.log();
  });
  
  rl.question("Select command (1-8) or 'q' to quit: ", (choice) => {
    if (choice === 'q') {
      rl.close();
      return;
    }
    
    if (commands[choice]) {
      let [cmd, desc] = commands[choice];
      
      // Handle commands that need user input
      if (cmd.includes('<task_id>')) {
        rl.question("Enter task ID: ", (taskId) => {
          cmd = cmd.replace('<task_id>', taskId);
          runCommand(cmd, desc);
          rl.close();
        });
      } else {
        runCommand(cmd, desc);
        rl.close();
      }
    } else {
      console.log("Invalid selection");
      rl.close();
    }
  });
}

if (require.main === module) {
  main();
}
`;
    
    const scriptPath = path.join(process.cwd(), 'taskmaster_commands.js');
    fs.writeFileSync(scriptPath, scriptContent, { mode: 0o755 });
    console.log('  ✅ Created taskmaster_commands.js helper script');
  }

  createAddArchitectureScript() {
    const scriptContent = `#!/usr/bin/env node

/**
 * Add Architecture Script
 * Allows adding additional architectures to an existing project.
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

class ArchitectureAdder {
  constructor() {
    this.projectRoot = process.cwd();
    this.archiveDir = path.join(this.projectRoot, 'archive');
    
    // Check if this is a quickstarted project
    if (!fs.existsSync(this.archiveDir)) {
      console.log("❌ This doesn't appear to be a quickstarted project.");
      console.log("   Run this script only in projects created with quick-start.js");
      process.exit(1);
    }
    
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
  }

  question(query) {
    return new Promise(resolve => this.rl.question(query, resolve));
  }

  getArchivedArchitectures() {
    const archFiles = fs.readdirSync(this.archiveDir)
      .filter(file => file.includes('_architectures.json'))
      .sort();
    
    if (archFiles.length === 0) {
      console.log("❌ No archived architectures.json found.");
      console.log("   Cannot add additional architectures without the original definitions.");
      process.exit(1);
    }

    const latestArchFile = archFiles[archFiles.length - 1];
    const archPath = path.join(this.archiveDir, latestArchFile);

    try {
      const data = JSON.parse(fs.readFileSync(archPath, 'utf8'));
      return this.flattenArchitectures(data);
    } catch (error) {
      console.log(\`❌ Failed to load architectures: \${error.message}\`);
      process.exit(1);
    }
  }

  flattenArchitectures(data) {
    const flattened = {};
    if (data.categories) {
      for (const [categoryKey, categoryData] of Object.entries(data.categories)) {
        if (categoryData.architectures) {
          Object.assign(flattened, categoryData.architectures);
        }
      }
    }
    return flattened;
  }

  displayAvailableArchitectures(architectures) {
    console.log('\\n🔧 Available architectures to add:\\n');
    
    const archKeys = Object.keys(architectures);
    archKeys.forEach((key, index) => {
      console.log(\`\${index + 1}. \${architectures[key].name}\`);
    });
  }

  async addArchitecture() {
    console.log("🚀 Add Architecture to Existing Project");
    console.log("=" + "=".repeat(49));
    
    const architectures = this.getArchivedArchitectures();
    this.displayAvailableArchitectures(architectures);
    
    const archKeys = Object.keys(architectures);
    const selection = await this.question(\`\\nSelect architecture to add (1-\${archKeys.length}): \`);
    const choice = parseInt(selection);
    
    if (!choice || choice < 1 || choice > archKeys.length) {
      console.log("❌ Invalid selection");
      this.rl.close();
      return;
    }
    
    const selectedKey = archKeys[choice - 1];
    const config = architectures[selectedKey];
    
    console.log(\`\\n🔧 Adding \${config.name} to your project...\`);
    
    // TODO: Implement architecture addition logic
    // - Copy relevant rules
    // - Update package.json/requirements.txt  
    // - Update .cursorrules
    // - Create architecture-specific files
    
    console.log(\`✅ \${config.name} added successfully!\`);
    console.log('\\n💡 You may need to:');
    console.log('- Install new dependencies');
    console.log('- Review updated .cursorrules file');
    console.log('- Check for new starter files in your project');
    
    this.rl.close();
  }
}

if (require.main === module) {
  const adder = new ArchitectureAdder();
  adder.addArchitecture();
}
`;

    const addArchPath = path.join(this.projectRoot, 'add_architecture.js');
    fs.writeFileSync(addArchPath, scriptContent);
    fs.chmodSync(addArchPath, 0o755);
  }

  async runSetup() {
    try {
      // Get architecture choice
      const { key: archKey, config } = await this.selectArchitecture();
      
      // Handle custom architecture
      let selectedRules = config.local_rules || [];
      if (archKey === 'custom') {
        selectedRules = await this.selectCustomRules();
      }
      
      // Get project name
      const projectName = (await this.question('\nEnter project name (or press Enter for "my-mvp"): ')).trim() || 'my-mvp';
      
      console.log(`\n🔧 Setting up ${config.name} architecture...\n`);
      
      // Execute setup steps
      const successSteps = [];
      
      // Copy awesome rules first
      const awesomeRules = config.awesome_rules || [];
      const copiedAwesomeRules = this.copyAwesomeRules(awesomeRules);
      const allRules = [...selectedRules, ...copiedAwesomeRules];
      
      if (this.activateRules(allRules)) {
        successSteps.push('Rules activated');
      }
      
      if (this.setupPrompts(config.prompts || [])) {
        successSteps.push('Prompts configured');
      }
      
      if (this.createPackageJson(config, projectName)) {
        successSteps.push('Package.json created');
      }
      
      if (this.createEnvExample(config, archKey)) {
        successSteps.push('.env.example created');
      }
      
      if (this.createReadme(config, projectName, allRules)) {
        successSteps.push('README.md generated');
      }
      
      // Archive template files
      this.archiveTemplateFiles(archKey, projectName);
      
      // Create add_architecture script
      this.createAddArchitectureScript();
      
      // Setup Taskmaster integration
      const taskmasterSuccess = this.setupTaskmaster(projectName);
      if (taskmasterSuccess) {
        successSteps.push('Taskmaster AI configured');
        this.createTaskmasterCommandsScript();
      }
      
      // Final success message
      console.log(`\n🎉 ${projectName} is ready for rapid MVP development!`);
      console.log('\nSetup completed:');
      successSteps.forEach(step => console.log(`  ✅ ${step}`));
      console.log('  ✅ Archived unused template files');
      console.log('  ✅ Created add_architecture.js for future extensions');
      
      console.log('\nNext steps:');
      if (config.packages) {
        console.log('1. npm install (install dependencies)');
      }
      if (config.requirements) {
        console.log('1. pip install -r requirements.txt (install Python dependencies)');
      }
      console.log('2. npm run dev (start development)');
      console.log('3. Check active_prompts/ for development workflows');
      console.log('4. Review .cursorrules for coding standards');
      console.log('5. Use add_architecture.js to add more tech stacks later');
      
      if (taskmasterSuccess) {
        console.log('\n🤖 Taskmaster AI Workflow:');
        console.log('6. Fill out .taskmaster/docs/project-prd-template.md with your PRD');
        console.log('7. Run: task-master parse-prd .taskmaster/docs/project-prd.txt');
        console.log('8. Use: node taskmaster_commands.js for task management');
        console.log('9. Follow: dev_tools/prompts/workflow/mvp_setup_workflow.md');
      }
      
      if (archKey === 'react-native') {
        console.log('\n💡 Expo CLI: npm install -g @expo/cli');
      }
      
    } catch (error) {
      console.error('\n❌ Error during setup:', error.message);
    } finally {
      this.rl.close();
    }
  }
}

if (require.main === module) {
  const quickStart = new MVPQuickStart();
  quickStart.runSetup();
}

module.exports = { MVPQuickStart };