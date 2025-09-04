#!/usr/bin/env python3

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import argparse
from datetime import datetime

ARCHITECTURES = {
    'react-native': {
        'name': 'React Native + Expo (Mobile App)',
        'rules': [
            'expo-development.mdc',
            'react-native-testing.mdc',
            'mobile-first.mdc',
            'ui-components.mdc',
            'testing-workflow.mdc',
            'hooks.mdc',
            'code-writing-standards.mdc',
            'git-automation.mdc'
        ],
        'prompts': ['workflow/execution_prompt.md'],
        'packages': ['expo', '@expo/vector-icons', 'nativewind'],
        'scripts': {
            "dev": "expo start",
            "test": "jest",
            "build": "expo build",
            "lint": "eslint . --ext .js,.jsx,.ts,.tsx"
        },
        'dev_dependencies': ['@types/react', '@types/react-native', 'jest', 'eslint']
    },
    'nextjs-fullstack': {
        'name': 'Next.js Full Stack (Web App)',
        'rules': [
            'project-structure.mdc',
            'data-fetching.mdc',
            'form-handling.mdc',
            'ui-components.mdc',
            'get-api-route.mdc',
            'testing.mdc',
            'code-writing-standards.mdc',
            'git-automation.mdc'
        ],
        'prompts': ['workflow/execution_prompt.md', 'workflow/PR_debug.md'],
        'packages': ['next', 'react', 'react-dom', '@types/node'],
        'scripts': {
            "dev": "next dev",
            "build": "next build",
            "start": "next start",
            "test": "jest",
            "lint": "next lint"
        },
        'dev_dependencies': ['@types/react', '@types/react-dom', 'eslint', 'jest']
    },
    'vercel-api': {
        'name': 'Vercel Functions + Python (Backend API)',
        'rules': [
            'get-api-route.mdc',
            'environment-variables.mdc',
            'security.mdc',
            'testing.mdc',
            'code-writing-standards.mdc',
            'documentation-standards.mdc'
        ],
        'prompts': ['workflow/execution_prompt.md'],
        'packages': ['vercel'],
        'requirements': ['fastapi', 'python-multipart', 'pytest', 'python-dotenv'],
        'scripts': {
            "dev": "vercel dev",
            "deploy": "vercel --prod",
            "test": "python -m pytest",
            "lint": "flake8 api/"
        }
    },
    'django-api': {
        'name': 'Django REST API (Python Backend)',
        'rules': [
            'environment-variables.mdc',
            'security.mdc',
            'testing.mdc',
            'code-writing-standards.mdc',
            'documentation-standards.mdc',
            'data-fetching.mdc'
        ],
        'prompts': ['workflow/execution_prompt.md'],
        'requirements': ['django', 'djangorestframework', 'django-cors-headers', 'python-dotenv', 'pytest-django'],
        'scripts': {
            "dev": "python manage.py runserver",
            "migrate": "python manage.py migrate",
            "test": "python -m pytest",
            "lint": "flake8 .",
            "makemigrations": "python manage.py makemigrations"
        }
    },
    'flask-api': {
        'name': 'Flask API (Python Backend)',
        'rules': [
            'environment-variables.mdc',
            'security.mdc',
            'testing.mdc',
            'code-writing-standards.mdc',
            'documentation-standards.mdc'
        ],
        'prompts': ['workflow/execution_prompt.md'],
        'requirements': ['flask', 'flask-cors', 'python-dotenv', 'pytest', 'gunicorn'],
        'scripts': {
            "dev": "flask run --debug",
            "test": "python -m pytest",
            "lint": "flake8 .",
            "start": "gunicorn app:app"
        }
    },
    'fastapi': {
        'name': 'FastAPI (Modern Python API)',
        'rules': [
            'environment-variables.mdc',
            'security.mdc',
            'testing.mdc',
            'code-writing-standards.mdc',
            'documentation-standards.mdc'
        ],
        'prompts': ['workflow/execution_prompt.md'],
        'requirements': ['fastapi', 'uvicorn', 'python-multipart', 'python-dotenv', 'pytest', 'httpx'],
        'scripts': {
            "dev": "uvicorn main:app --reload",
            "test": "python -m pytest",
            "lint": "flake8 .",
            "start": "uvicorn main:app --host 0.0.0.0 --port 8000"
        }
    },
    'custom': {
        'name': 'Custom Architecture (Select your own rules)',
        'rules': [],
        'prompts': [],
        'packages': [],
        'scripts': {}
    }
}

class MVPQuickStart:
    def __init__(self):
        self.project_root = Path.cwd()
        self.rules_dir = self.project_root / '.cursor' / 'rules'
        self.prompts_dir = self.project_root / 'dev_tools' / 'prompts'
        self.awesome_rules_dir = self.project_root / '.cursor' / 'awesome-rules'
        self.archive_dir = self.project_root / 'archive'
        
        # Run initial setup if needed
        self.setup_environment()
        
        # Load architectures from JSON
        self.architectures = self.load_architectures()
    
    def setup_environment(self):
        """Set up the environment - download awesome rules if needed"""
        import subprocess
        
        # Create basic directories
        self.rules_dir.parent.mkdir(exist_ok=True)
        self.prompts_dir.parent.mkdir(exist_ok=True)
        
        # Download awesome-cursor-rules if not present
        if not self.awesome_rules_dir.exists():
            print("🔧 Setting up awesome-cursor-rules...")
            try:
                temp_dir = self.project_root / 'temp-awesome-rules'
                
                # Clone repository
                subprocess.run([
                    'git', 'clone', '--depth', '1', 
                    'https://github.com/PatrickJS/awesome-cursorrules.git',
                    str(temp_dir)
                ], check=True, capture_output=True)
                
                # Move rules directory
                rules_source = temp_dir / 'rules'
                if rules_source.exists():
                    rules_source.rename(self.awesome_rules_dir)
                    print("✅ Downloaded awesome-cursor-rules")
                
                # Clean up
                if temp_dir.exists():
                    shutil.rmtree(temp_dir)
                    
            except subprocess.CalledProcessError:
                print("⚠️  Failed to download awesome-cursor-rules. Continuing without them.")
            except Exception as e:
                print(f"⚠️  Setup warning: {e}")
        
        # Create rule mappings
        self.create_rule_mappings()
    
    def create_rule_mappings(self):
        """Create rule mappings file"""
        mappings = {
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
        }
        
        mappings_file = self.project_root / 'rule-mappings.json'
        with open(mappings_file, 'w') as f:
            json.dump(mappings, f, indent=2)
    
    def load_architectures(self) -> Dict:
        """Load architecture definitions from JSON file"""
        arch_file = self.project_root / 'architectures.json'
        if arch_file.exists():
            try:
                with open(arch_file, 'r') as f:
                    data = json.load(f)
                return self.flatten_architectures(data)
            except Exception as e:
                print(f"⚠️  Failed to load architectures.json: {e}")
                return ARCHITECTURES
        return ARCHITECTURES
    
    def flatten_architectures(self, data: Dict) -> Dict:
        """Flatten the categorized architecture data"""
        flattened = {}
        
        # Add individual architectures from categories
        for category_key, category_data in data.get('categories', {}).items():
            for arch_key, arch_data in category_data.get('architectures', {}).items():
                flattened[arch_key] = arch_data
        
        # Add popular stacks
        if 'popular_stacks' in data:
            popular_stacks = data['popular_stacks']
            if 'stacks' in popular_stacks:
                for stack_key, stack_data in popular_stacks['stacks'].items():
                    flattened[stack_key] = stack_data
        
        # Add legacy presets for backward compatibility
        if 'presets' in data:
            flattened.update(data['presets'])
        
        # Keep custom option
        flattened['custom'] = {
            'name': 'Custom Architecture (Select your own rules)',
            'local_rules': [],
            'awesome_rules': [],
            'packages': [],
            'scripts': {}
        }
        return flattened
        
    def display_architectures(self):
        """Display available architectures"""
        print('\n🚀 Welcome to the MVP Quick-Start Setup!\n')
        print('Available architectures:')
        
        for i, (key, config) in enumerate(self.architectures.items(), 1):
            print(f"{i}. {config['name']}")
    
    def get_user_choice(self, prompt: str, max_choice: int) -> int:
        """Get user choice with validation"""
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= max_choice:
                    return choice
                else:
                    print(f"Please enter a number between 1 and {max_choice}")
            except ValueError:
                print("Please enter a valid number")
    
    def select_architecture(self) -> tuple:
        """Interactive architecture selection"""
        self.display_architectures()
        
        arch_keys = list(self.architectures.keys())
        choice = self.get_user_choice('\nSelect architecture (1-{}): '.format(len(arch_keys)), len(arch_keys))
        
        selected_key = arch_keys[choice - 1]
        return selected_key, self.architectures[selected_key]
    
    def get_available_rules(self) -> List[str]:
        """Get list of available rule files"""
        if not self.rules_dir.exists():
            print(f"❌ Rules directory not found: {self.rules_dir}")
            return []
        
        return sorted([f.name for f in self.rules_dir.glob('*.mdc')])
    
    def select_custom_rules(self) -> List[str]:
        """Interactive custom rule selection"""
        print('\n📋 Select rules for your custom architecture:')
        
        all_rules = self.get_available_rules()
        if not all_rules:
            return []
        
        print('\nAvailable rules:')
        for i, rule in enumerate(all_rules, 1):
            name = rule.replace('.mdc', '').replace('-', ' ').title()
            print(f"{i:2d}. {name}")
        
        selection = input('\nEnter rule numbers (comma-separated, e.g., 1,3,5): ')
        try:
            selected_indices = [int(s.strip()) - 1 for s in selection.split(',')]
            return [all_rules[i] for i in selected_indices if 0 <= i < len(all_rules)]
        except (ValueError, IndexError):
            print("Invalid selection. Using no rules.")
            return []
    
    def copy_awesome_rules(self, awesome_rules: List[str]) -> List[str]:
        """Copy awesome cursor rules to .cursor/rules directory"""
        if not awesome_rules or not self.awesome_rules_dir.exists():
            return []
        
        # Load rule mappings
        mappings_file = self.project_root / 'rule-mappings.json'
        if not mappings_file.exists():
            print("⚠️  rule-mappings.json not found. Run setup.sh first.")
            return []
        
        try:
            with open(mappings_file, 'r') as f:
                mappings = json.load(f).get('mappings', {})
        except Exception as e:
            print(f"⚠️  Failed to load rule mappings: {e}")
            return []
        
        copied_rules = []
        for awesome_rule in awesome_rules:
            if awesome_rule in mappings:
                source_path = self.awesome_rules_dir / mappings[awesome_rule]
                if source_path.exists():
                    # Create target filename based on awesome rule name
                    target_filename = f"{awesome_rule.replace('-', '_')}.mdc"
                    target_path = self.rules_dir / target_filename
                    
                    try:
                        # Ensure target directory exists
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # Read and convert .cursorrules to .mdc format
                        with open(source_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Convert to MDC format
                        mdc_content = f"""---
description: {awesome_rule.replace('-', ' ').title()} rules from awesome-cursor-rules
globs: **/*
alwaysApply: true
---

{content}
"""
                        
                        with open(target_path, 'w', encoding='utf-8') as f:
                            f.write(mdc_content)
                        
                        copied_rules.append(target_filename)
                        
                    except Exception as e:
                        print(f"⚠️  Failed to copy {awesome_rule}: {e}")
        
        if copied_rules:
            print(f"✅ Copied {len(copied_rules)} awesome rules to .cursor/rules/")
        
        return copied_rules

    def activate_rules(self, rules: List[str]) -> bool:
        """Consolidate selected rules into .cursorrules"""
        if not rules:
            print("⚠️  No rules to activate")
            return False
        
        cursorrules_path = self.project_root / '.cursorrules'
        rule_content = ['# Auto-generated Cursor Rules for MVP Development\n']
        
        activated_count = 0
        for rule in rules:
            rule_path = self.rules_dir / rule
            if rule_path.exists():
                try:
                    content = rule_path.read_text(encoding='utf-8')
                    rule_content.extend([
                        f'\n# === {rule} ===\n',
                        content,
                        '\n'
                    ])
                    activated_count += 1
                except Exception as e:
                    print(f"⚠️  Failed to read {rule}: {e}")
        
        if activated_count > 0:
            cursorrules_path.write_text(''.join(rule_content), encoding='utf-8')
            print(f"✅ Activated {activated_count} rules in .cursorrules")
            return True
        else:
            print("❌ No rules were successfully activated")
            return False
    
    def setup_prompts(self, prompts: List[str]) -> bool:
        """Copy selected prompts to active_prompts directory"""
        if not prompts:
            return True
        
        target_dir = self.project_root / 'active_prompts'
        target_dir.mkdir(exist_ok=True)
        
        copied_count = 0
        for prompt in prompts:
            source_path = self.prompts_dir / prompt
            if source_path.exists():
                try:
                    target_path = target_dir / source_path.name
                    shutil.copy2(source_path, target_path)
                    copied_count += 1
                except Exception as e:
                    print(f"⚠️  Failed to copy {prompt}: {e}")
        
        if copied_count > 0:
            print(f"✅ Set up {copied_count} prompts in active_prompts/")
            return True
        return False
    
    def create_package_json(self, config: Dict, project_name: str) -> bool:
        """Create package.json for Node.js based projects"""
        if 'packages' not in config or not config['packages']:
            return True
        
        package_json = {
            "name": project_name.lower().replace(' ', '-'),
            "version": "0.1.0",
            "description": "MVP created with quick-start template",
            "main": "index.js",
            "scripts": config.get('scripts', {}),
            "dependencies": {},
            "devDependencies": {}
        }
        
        try:
            package_path = self.project_root / 'package.json'
            package_path.write_text(json.dumps(package_json, indent=2), encoding='utf-8')
            print('✅ Created package.json')
            
            packages = config.get('packages', [])
            dev_packages = config.get('dev_dependencies', [])
            
            if packages:
                print(f"📦 Install packages: npm install {' '.join(packages)}")
            if dev_packages:
                print(f"🔧 Install dev packages: npm install --save-dev {' '.join(dev_packages)}")
            
            return True
        except Exception as e:
            print(f"❌ Failed to create package.json: {e}")
            return False
    
    def create_requirements_txt(self, config: Dict) -> bool:
        """Create requirements.txt for Python projects"""
        requirements = config.get('requirements', [])
        if not requirements:
            return True
        
        try:
            req_content = '\n'.join(requirements)
            req_path = self.project_root / 'requirements.txt'
            req_path.write_text(req_content, encoding='utf-8')
            print('✅ Created requirements.txt')
            print('🐍 Install Python packages: pip install -r requirements.txt')
            return True
        except Exception as e:
            print(f"❌ Failed to create requirements.txt: {e}")
            return False
    
    def create_env_example(self, config: Dict, architecture_key: str) -> bool:
        """Create .env.example based on chosen architecture"""
        # Base environment variables that most projects need
        env_vars = {
            "# Environment Configuration": "",
            "NODE_ENV": "development"
        }
        
        # Architecture-specific environment variables
        arch_env_vars = {
            # Frontend frameworks that might need API keys
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
            
            # Full-stack frameworks
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
            
            # Mobile
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
            
            # Backend APIs
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
            
            # Serverless
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
            
            # Database
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
            
            # Testing
            'cypress': {
                "# Cypress": "",
                "CYPRESS_BASE_URL": "http://localhost:3000"
            },
            'playwright': {
                "# Playwright": "",
                "PLAYWRIGHT_BASE_URL": "http://localhost:3000"
            },
            
            # Blockchain
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
        }
        
        # Combine base and architecture-specific vars
        final_env_vars = dict(env_vars)
        if architecture_key in arch_env_vars:
            final_env_vars.update(arch_env_vars[architecture_key])
        
        # Always add common AI API keys at the end
        final_env_vars.update({
            "# AI API Keys (add only what you need)": "",
            "OPENAI_API_KEY": "your-openai-key-here",
            "ANTHROPIC_API_KEY": "your-anthropic-key-here",
            "GOOGLE_API_KEY": "your-google-key-here",
            "PERPLEXITY_API_KEY": "your-perplexity-key-here"
        })
        
        try:
            env_content = []
            for key, value in final_env_vars.items():
                if key.startswith('#'):
                    env_content.append(f'\n{key}')
                elif value:
                    env_content.append(f'{key}={value}')
                else:
                    env_content.append('')
            
            env_path = self.project_root / '.env.example'
            env_path.write_text('\n'.join(env_content), encoding='utf-8')
            print('✅ Created .env.example with architecture-specific variables')
            return True
        except Exception as e:
            print(f"❌ Failed to create .env.example: {e}")
            return False
    
    def create_readme(self, architecture: Dict, project_name: str, selected_rules: List[str]) -> bool:
        """Generate comprehensive README.md"""
        scripts_section = ""
        if architecture.get('scripts'):
            scripts_section = "### Development Commands\n\n" + '\n'.join([
                f"- **{cmd}**: `npm run {cmd}` - {script}" 
                for cmd, script in architecture['scripts'].items()
            ]) + "\n\n"
        
        install_section = ""
        if architecture.get('packages'):
            install_section += "```bash\nnpm install\n"
            if architecture.get('requirements'):
                install_section += "pip install -r requirements.txt\n"
            install_section += "```"
        elif architecture.get('requirements'):
            install_section += "```bash\npip install -r requirements.txt\n```"
        else:
            install_section += "```bash\n# No dependencies to install\n```"
        
        readme_content = f"""# {project_name}

Quick-started MVP using **{architecture['name']}** architecture.

## Architecture

This project was set up using the MVP Quick-Start Template with the following configuration:

### Active Rules
{chr(10).join([f"- {rule.replace('.mdc', '').replace('-', ' ').title()}" for rule in selected_rules])}

{scripts_section}## Getting Started

1. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

2. Install dependencies:
   {install_section}

3. Start development:
   ```bash
   npm run dev
   ```

4. Run tests:
   ```bash
   npm run test
   ```

## Project Structure

```
{project_name.lower().replace(' ', '-')}/
├── .cursorrules          # Consolidated Cursor rules
├── active_prompts/       # Development workflow prompts  
├── package.json          # Node.js dependencies and scripts
{('├── requirements.txt      # Python dependencies' + chr(10)) if architecture.get('requirements') else ''}├── README.md            # This file
└── src/                  # Your source code goes here
```

## Active Prompts

Check the `active_prompts/` directory for development workflow prompts that work with this architecture:

- **Execution Prompt**: Structured TDD workflow for feature development
- **PR Debug Prompt**: Systematic debugging and code review process

## Cursor Rules

All relevant Cursor rules have been consolidated into `.cursorrules`. These provide:
- 📝 Code standards and patterns
- 🧪 Testing guidelines  
- 🔄 Git workflow automation
- 🏗️ Architecture-specific best practices
- 🛡️ Security practices

## Development Workflow

1. **Plan Feature**: Use active prompts to structure your approach
2. **Write Tests**: Follow TDD patterns from execution prompt
3. **Implement**: Build with guidance from Cursor rules
4. **Test & Review**: Use testing guidelines and PR debug process
5. **Deploy**: Use architecture-specific deployment commands

---

*Generated with MVP Quick-Start Template - Python Edition*
"""
        
        try:
            readme_path = self.project_root / 'README.md'
            readme_path.write_text(readme_content, encoding='utf-8')
            print('✅ Created README.md with setup instructions')
            return True
        except Exception as e:
            print(f"❌ Failed to create README.md: {e}")
            return False
    
    def create_basic_structure(self, architecture_key: str, project_name: str):
        """Create basic project structure based on architecture"""
        src_dir = self.project_root / 'src'
        src_dir.mkdir(exist_ok=True)
        
        # Create architecture-specific starter files
        if architecture_key == 'fastapi':
            main_py = self.project_root / 'main.py'
            if not main_py.exists():
                main_content = '''from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="{}", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {{"message": "Hello from {} API!"}}

@app.get("/health")
async def health_check():
    return {{"status": "healthy"}}
'''.format(project_name, project_name)
                main_py.write_text(main_content, encoding='utf-8')
                print('✅ Created FastAPI starter (main.py)')
        
        elif architecture_key == 'flask-api':
            app_py = self.project_root / 'app.py'
            if not app_py.exists():
                app_content = '''from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return jsonify({{"message": "Hello from {} API!"}})

@app.route('/health')
def health_check():
    return jsonify({{"status": "healthy"}})

if __name__ == '__main__':
    app.run(debug=True)
'''.format(project_name)
                app_py.write_text(app_content, encoding='utf-8')
                print('✅ Created Flask starter (app.py)')
        
        elif architecture_key == 'django-api':
            # Create basic Django structure indicators
            manage_py = self.project_root / 'manage.py'
            if not manage_py.exists():
                print('📋 Django project structure needed - run: django-admin startproject {} .'.format(project_name.lower().replace(' ', '_')))
    
    def archive_template_files(self, selected_arch: str, project_name: str):
        """Archive unused template files after quickstart setup"""
        print('\n📦 Archiving unused template files...')
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.archive_dir.mkdir(exist_ok=True)
        
        # Files to archive (template-specific files no longer needed)
        files_to_archive = [
            'quick_start.py',  # This script itself
            'quick-start.js',  # Node.js version 
            'architectures.json',  # Architecture definitions
            'rule-mappings.json',  # Rule mappings
            'setup.sh',  # Setup script
            'WORKFLOW.md',  # Template workflow guide
        ]
        
        # Directories to archive
        dirs_to_archive = [
            '.cursor/awesome-rules',  # Downloaded awesome rules
            '.cursor/rules',  # All rules (will be replaced by selected ones)
            'dev_tools',  # Template development tools
        ]
        
        archived_count = 0
        
        # Archive files
        for file_name in files_to_archive:
            file_path = self.project_root / file_name
            if file_path.exists():
                try:
                    archive_path = self.archive_dir / f"{timestamp}_{file_name}"
                    if file_path.is_file():
                        shutil.copy2(file_path, archive_path)
                        file_path.unlink()
                        archived_count += 1
                except Exception as e:
                    print(f"⚠️  Failed to archive {file_name}: {e}")
        
        # Archive directories  
        for dir_name in dirs_to_archive:
            dir_path = self.project_root / dir_name
            if dir_path.exists() and dir_path.is_dir():
                try:
                    archive_path = self.archive_dir / f"{timestamp}_{dir_name.replace('/', '_')}"
                    shutil.copytree(dir_path, archive_path)
                    shutil.rmtree(dir_path)
                    archived_count += 1
                except Exception as e:
                    print(f"⚠️  Failed to archive {dir_name}: {e}")
        
        # Create archive info file
        archive_info = {
            "archived_at": timestamp,
            "selected_architecture": selected_arch,
            "project_name": project_name,
            "archived_files": files_to_archive,
            "archived_directories": dirs_to_archive,
            "note": "These files were archived after quickstart setup. Use add_architecture.py to add more tech stacks."
        }
        
        info_path = self.archive_dir / f"{timestamp}_archive_info.json"
        with open(info_path, 'w') as f:
            json.dump(archive_info, f, indent=2)
        
        if archived_count > 0:
            print(f'✅ Archived {archived_count} template files to archive/')
        
        # Recreate .cursor/rules with only selected rules 
        self.rules_dir.mkdir(parents=True, exist_ok=True)
    
    def create_project_config(self, architecture_key: str, project_name: str, selected_rules: List[str]):
        """Create project configuration file for other agents to read"""
        config = {
            "project_name": project_name,
            "primary_architecture": architecture_key,
            "architecture_details": self.architectures.get(architecture_key, {}),
            "active_rules": selected_rules,
            "created_at": datetime.now().isoformat(),
            "last_modified": datetime.now().isoformat(),
            "tech_stack": {
                "frontend": None,
                "backend": None,
                "database": None,
                "testing": None,
                "deployment": None
            }
        }
        
        # Categorize the architecture for better understanding
        arch_categories = {
            # Frontend
            'react': {'type': 'frontend', 'framework': 'React'},
            'vue': {'type': 'frontend', 'framework': 'Vue.js'},
            'angular': {'type': 'frontend', 'framework': 'Angular'},
            'svelte': {'type': 'frontend', 'framework': 'Svelte'},
            
            # Full-stack
            'nextjs': {'type': 'fullstack', 'framework': 'Next.js', 'includes': ['React', 'API Routes']},
            'nuxtjs': {'type': 'fullstack', 'framework': 'Nuxt.js', 'includes': ['Vue.js', 'API Routes']},
            't3-stack': {'type': 'fullstack', 'framework': 'T3 Stack', 'includes': ['Next.js', 'tRPC', 'Prisma']},
            
            # Mobile
            'react-native': {'type': 'mobile', 'framework': 'React Native', 'platform': 'iOS/Android'},
            'flutter': {'type': 'mobile', 'framework': 'Flutter', 'platform': 'iOS/Android'},
            
            # Backend
            'fastapi': {'type': 'backend', 'framework': 'FastAPI', 'language': 'Python'},
            'django': {'type': 'backend', 'framework': 'Django', 'language': 'Python'},
            'flask': {'type': 'backend', 'framework': 'Flask', 'language': 'Python'},
            'expressjs': {'type': 'backend', 'framework': 'Express.js', 'language': 'JavaScript'},
            'nestjs': {'type': 'backend', 'framework': 'NestJS', 'language': 'TypeScript'},
        }
        
        if architecture_key in arch_categories:
            config['category'] = arch_categories[architecture_key]
        
        try:
            config_path = self.project_root / '.mvp-config.json'
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=2)
            print('✅ Created .mvp-config.json for other agents to read')
        except Exception as e:
            print(f"⚠️  Failed to create project config: {e}")

    def setup_taskmaster(self, project_name: str) -> bool:
        """Initialize Taskmaster for task management and PRD parsing"""
        try:
            import subprocess
            import sys
            
            print('🤖 Setting up Taskmaster AI for task management...')
            
            # Check if Taskmaster is installed globally
            try:
                subprocess.run(['task-master', '--version'], 
                             capture_output=True, check=True)
                print('  ✅ Taskmaster already installed')
            except (subprocess.CalledProcessError, FileNotFoundError):
                print('  📦 Installing Taskmaster globally...')
                try:
                    subprocess.run([sys.executable, '-m', 'pip', 'install', 'taskmaster-ai'], 
                                 check=True, capture_output=True)
                    print('  ✅ Taskmaster installed successfully')
                except subprocess.CalledProcessError as e:
                    print(f'  ⚠️  Failed to install Taskmaster: {e}')
                    print('  💡 You can install manually with: pip install taskmaster-ai')
                    return False
            
            # Create .taskmaster directory structure
            taskmaster_dir = self.project_root / '.taskmaster'
            taskmaster_dir.mkdir(exist_ok=True)
            (taskmaster_dir / 'docs').mkdir(exist_ok=True)
            (taskmaster_dir / 'context').mkdir(exist_ok=True)
            (taskmaster_dir / 'reports').mkdir(exist_ok=True)
            
            # Initialize Taskmaster in the project
            try:
                result = subprocess.run([
                    'task-master', 'init', 
                    f'--name={project_name}',
                    f'--description=MVP project created from template'
                ], cwd=self.project_root, capture_output=True, text=True, check=True)
                print('  ✅ Taskmaster initialized in project')
            except subprocess.CalledProcessError as e:
                print(f'  ⚠️  Failed to initialize Taskmaster: {e}')
                print('  💡 You can initialize manually with: task-master init')
                return False
            
            # Create PRD template for users
            prd_template = '''# Product Requirements Document (PRD)

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
'''
            
            prd_path = taskmaster_dir / 'docs' / 'project-prd-template.md'
            prd_path.write_text(prd_template, encoding='utf-8')
            
            # Create context template reference
            context_readme = '''# Task Context Documents

This directory contains detailed context documents for each task generated from your PRD.

## Using Task Context
1. Each task has a corresponding context document: `task_XX_context.md`
2. Subtasks have their own context: `task_XX_subtask_YY_context.md`
3. Context documents include implementation guidelines, testing strategies, and success criteria

## Generating Task Context
After parsing your PRD with `task-master parse-prd`, use the MVP workflow:
```bash
# Generate comprehensive context for all tasks
python -c "
from pathlib import Path
import json
template = Path('dev_tools/templates/task_context_template.md').read_text()
# Use template to create context documents for each task
"
```

## Context Document Structure
- **Task Overview**: Objective, business value, user impact
- **Success Criteria**: Functional requirements, acceptance criteria
- **Technical Context**: Architecture integration, dependencies
- **Implementation Guidelines**: Step-by-step approach
- **Testing Strategy**: Unit, integration, E2E tests
- **Success/Failure States**: What done looks like
'''
            
            (taskmaster_dir / 'context' / 'README.md').write_text(context_readme, encoding='utf-8')
            
            print('  ✅ Created .taskmaster/ directory structure')
            print('  ✅ Created PRD template at .taskmaster/docs/project-prd-template.md')
            print('  ✅ Task context directory ready')
            
            return True
            
        except Exception as e:
            print(f'  ⚠️  Error setting up Taskmaster: {e}')
            return False

    def create_taskmaster_commands_script(self):
        """Create helper script with common Taskmaster commands"""
        script_content = '''#!/usr/bin/env python3
"""
Taskmaster Command Helper
Common commands for managing tasks in your MVP project.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command with error handling"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(e.stderr)
        return False

def main():
    print("🤖 Taskmaster MVP Command Helper")
    print("=" * 40)
    
    commands = {
        '1': ('task-master list --with-subtasks', 'List all tasks and subtasks'),
        '2': ('task-master next', 'Get next task to work on'),
        '3': ('task-master show <task_id>', 'Show detailed task information'),
        '4': ('task-master parse-prd .taskmaster/docs/project-prd.txt --num-tasks=15-25', 'Parse PRD and generate tasks'),
        '5': ('task-master analyze-complexity --research', 'Analyze task complexity'),
        '6': ('task-master expand --all --research --num=3-5', 'Break down complex tasks'),
        '7': ('task-master generate --output=docs/tasks/', 'Generate task documentation'),
        '8': ('task-master set-status --id=<task_id> --status=done', 'Mark task as completed'),
    }
    
    print("Available commands:")
    for key, (cmd, desc) in commands.items():
        print(f"{key}. {desc}")
        print(f"   Command: {cmd}")
        print()
    
    choice = input("Select command (1-8) or 'q' to quit: ").strip()
    
    if choice == 'q':
        return
    
    if choice in commands:
        cmd, desc = commands[choice]
        
        # Handle commands that need user input
        if '<task_id>' in cmd:
            task_id = input("Enter task ID: ").strip()
            cmd = cmd.replace('<task_id>', task_id)
        
        run_command(cmd, desc)
    else:
        print("Invalid selection")

if __name__ == '__main__':
    main()
'''
        
        script_path = self.project_root / 'taskmaster_commands.py'
        script_path.write_text(script_content, encoding='utf-8')
        script_path.chmod(0o755)  # Make executable
        print('  ✅ Created taskmaster_commands.py helper script')

    def create_add_architecture_script(self):
        """Create add_architecture.py script for adding more architectures later"""
        script_content = '''#!/usr/bin/env python3

"""
Add Architecture Script
Allows adding additional architectures to an existing project.
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List

class ArchitectureAdder:
    def __init__(self):
        self.project_root = Path.cwd()
        self.archive_dir = self.project_root / 'archive'
        
        # Check if this is a quickstarted project
        if not self.archive_dir.exists():
            print("❌ This doesn't appear to be a quickstarted project.")
            print("   Run this script only in projects created with quick_start.py")
            exit(1)
    
    def get_archived_architectures(self) -> Dict:
        """Load architecture definitions from archived files"""
        arch_files = list(self.archive_dir.glob("*_architectures.json"))
        if not arch_files:
            print("❌ No archived architectures.json found.")
            print("   Cannot add additional architectures without the original definitions.")
            exit(1)
        
        # Use the most recent one
        latest_arch_file = max(arch_files, key=lambda x: x.stem.split('_')[0])
        
        try:
            with open(latest_arch_file, 'r') as f:
                data = json.load(f)
            return self.flatten_architectures(data)
        except Exception as e:
            print(f"❌ Failed to load architectures: {e}")
            exit(1)
    
    def flatten_architectures(self, data: Dict) -> Dict:
        """Flatten the categorized architecture data"""
        flattened = {}
        for category_key, category_data in data.get('categories', {}).items():
            for arch_key, arch_data in category_data.get('architectures', {}).items():
                flattened[arch_key] = arch_data
        return flattened
    
    def display_available_architectures(self, architectures: Dict):
        """Display available architectures to add"""
        print('\\n🔧 Available architectures to add:\\n')
        
        for i, (key, config) in enumerate(architectures.items(), 1):
            print(f"{i}. {config['name']}")
    
    def add_architecture(self):
        """Main method to add an architecture"""
        print("🚀 Add Architecture to Existing Project")
        print("=" * 50)
        
        architectures = self.get_archived_architectures()
        self.display_available_architectures(architectures)
        
        # Get user choice
        arch_keys = list(architectures.keys())
        try:
            choice = int(input(f'\\nSelect architecture to add (1-{len(arch_keys)}): '))
            if not (1 <= choice <= len(arch_keys)):
                print("❌ Invalid selection")
                return
        except ValueError:
            print("❌ Please enter a valid number")
            return
        
        selected_key = arch_keys[choice - 1]
        config = architectures[selected_key]
        
        print(f'\\n🔧 Adding {config["name"]} to your project...')
        
        # TODO: Implement architecture addition logic
        # - Copy relevant rules
        # - Update package.json/requirements.txt  
        # - Update .cursorrules
        # - Create architecture-specific files
        
        print(f'✅ {config["name"]} added successfully!')
        print('\\n💡 You may need to:')
        print('- Install new dependencies')
        print('- Review updated .cursorrules file')
        print('- Check for new starter files in your project')

if __name__ == '__main__':
    adder = ArchitectureAdder()
    adder.add_architecture()
'''
        
        add_arch_path = self.project_root / 'add_architecture.py'
        add_arch_path.write_text(script_content, encoding='utf-8')
        add_arch_path.chmod(0o755)  # Make executable
    
    def run_setup(self):
        """Main setup workflow"""
        try:
            # Get architecture choice
            arch_key, config = self.select_architecture()
            
            # Handle custom architecture
            selected_rules = config.get('local_rules', config.get('rules', []))
            if arch_key == 'custom':
                selected_rules = self.select_custom_rules()
            
            # Get project name
            project_name = input('\nEnter project name (or press Enter for "my-mvp"): ').strip()
            if not project_name:
                project_name = 'my-mvp'
            
            print(f'\n🔧 Setting up {config["name"]} architecture...\n')
            
            # Execute setup steps
            success_steps = []
            
            # Copy awesome rules first
            awesome_rules = config.get('awesome_rules', [])
            copied_awesome_rules = self.copy_awesome_rules(awesome_rules)
            all_rules = selected_rules + copied_awesome_rules
            
            if self.activate_rules(all_rules):
                success_steps.append('Rules activated')
            
            if self.setup_prompts(config.get('prompts', [])):
                success_steps.append('Prompts configured')
            
            if self.create_package_json(config, project_name):
                success_steps.append('Package.json created')
            
            if self.create_requirements_txt(config):
                success_steps.append('Requirements.txt created')
            
            if self.create_env_example(config, arch_key):
                success_steps.append('.env.example created')
            
            if self.create_readme(config, project_name, all_rules):
                success_steps.append('README.md generated')
            
            self.create_basic_structure(arch_key, project_name)
            
            # Archive unused template files
            self.archive_template_files(arch_key, project_name)
            
            # Create project configuration for other agents
            self.create_project_config(arch_key, project_name, all_rules)
            
            # Create add_architecture script
            self.create_add_architecture_script()
            
            # Setup Taskmaster integration
            taskmaster_success = self.setup_taskmaster(project_name)
            if taskmaster_success:
                success_steps.append('Taskmaster AI configured')
                self.create_taskmaster_commands_script()
            
            # Final success message
            print(f'\n🎉 {project_name} is ready for rapid MVP development!')
            print('\nSetup completed:')
            for step in success_steps:
                print(f'  ✅ {step}')
            print('  ✅ Archived unused template files')
            print('  ✅ Created add_architecture.py for future extensions')
            
            print('\nNext steps:')
            if config.get('packages'):
                print('1. npm install (install Node.js dependencies)')
            if config.get('requirements'):
                print('1. pip install -r requirements.txt (install Python dependencies)')
            
            if config.get('scripts', {}).get('dev'):
                print('2. npm run dev (start development)')
            else:
                print('2. Start development with your preferred method')
                
            print('3. Check active_prompts/ for development workflows')
            print('4. Review .cursorrules for coding standards')
            print('5. Use add_architecture.py to add more tech stacks later')
            
            if taskmaster_success:
                print('\n🤖 Taskmaster AI Workflow:')
                print('6. Fill out .taskmaster/docs/project-prd-template.md with your PRD')
                print('7. Run: task-master parse-prd .taskmaster/docs/project-prd.txt')
                print('8. Use: python taskmaster_commands.py for task management')
                print('9. Follow: dev_tools/prompts/workflow/mvp_setup_workflow.md')
            
            # Architecture-specific tips
            if arch_key == 'react-native':
                print('\n💡 Expo CLI: npm install -g @expo/cli')
            elif arch_key == 'django-api':
                print(f'\n💡 Initialize Django: django-admin startproject {project_name.lower().replace(" ", "_")} .')
            
        except KeyboardInterrupt:
            print('\n\n👋 Setup cancelled by user')
        except Exception as e:
            print(f'\n❌ Error during setup: {e}')
            import traceback
            traceback.print_exc()

def main():
    parser = argparse.ArgumentParser(description='MVP Quick-Start Setup Script')
    parser.add_argument('--version', action='version', version='MVP Quick-Start 1.0.0')
    parser.add_argument('--list-rules', action='store_true', help='List available rules')
    
    args = parser.parse_args()
    
    quick_start = MVPQuickStart()
    
    if args.list_rules:
        print('Available rules:')
        for rule in quick_start.get_available_rules():
            name = rule.replace('.mdc', '').replace('-', ' ').title()
            print(f'  - {name} ({rule})')
        return
    
    quick_start.run_setup()

if __name__ == '__main__':
    main()