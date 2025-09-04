# Created by: claude-3.5-sonnet
# Last edited: 2024-12-19 15:30:00 UTC by claude-3.5-sonnet

# Default Task Execution Workflow

<!-- Created by: claude-3-5-sonnet-20241022 -->
<!-- Last edited: 2025-08-13 18:45:00 UTC by gpt-5 -->
<!-- Updated: Aligned workflow with master tag context and UserProxy architecture (Supabase + Pinecone + Multi-Agent Council) -->

## Overview

This is the standard workflow for AI agents to pick up and execute development tasks efficiently. It provides a streamlined approach for task-driven development while ensuring proper documentation and quality control.

**🚨 CRITICAL COMPLETION REQUIREMENT**: **EVERY TASK MUST** achieve full green CI status before being marked complete. Use systematic CI monitoring tools immediately after PR creation and continue until all checks pass.

**MVP FOCUS:** This workflow operates in the **MVP tag context** by default, focusing on core UserProxy MVP architecture: Gmail/Calendar → Supabase/Pinecone → AutoGen Council → Action Tiles for intelligent assistance. Prioritizes MVP feature delivery as defined in userproxy-mvp-prd.txt.

**Strategic Context:** For broader project vision, timeline, and feature priorities, refer to the [MASTER_ROADMAP.md](../../MASTER_ROADMAP.md) which outlines the complete UserProxy development journey from MVP through Post-Launch phases.

## Core Workflow Steps

### 1. Task Acquisition

- **Get Next Task**: Use Taskmaster MCP to fetch the next pending task from MVP context
  - Call `next_task` to get the highest priority available task (operates in MVP tag by default)
  - If a specific task is assigned, use `get_task` to retrieve details
  - **Strategic Focus**: Prioritize tasks that advance core UserProxy architecture and user value
- **Understand Context**: Review task description, dependencies, and acceptance criteria
- **Validate Prerequisites**: Ensure all dependency tasks are completed
- **Scope Alignment**: Verify task aligns with current development phase goals from MASTER_ROADMAP.md

### 2. Environment Setup

- **Branch Management**: Create a new feature branch from fresh main
  - Use descriptive branch names: `feature/task-<id>-<brief-description>`
  - Ensure local main is up to date before branching. Run:
    ```bash
    git checkout main
    git pull --rebase origin main
    git fetch --prune --tags
    ```
- **Context Loading**: Read task and subtask context documents
  - Load `./.taskmaster/context/task_<TaskID>_context.md`
  - Load `./.taskmaster/context/task_<TaskID>_subtask_<SubtaskID>_context.md`

### 2.5. Execution Flow Analysis (Recommended)

- Use the TDD Execution Flow tool to analyze parallelization opportunities and blockers from `./.taskmaster/tasks/tasks.json`:
  ```bash
  python3 scripts/tdd_task_execution_flow.py --analyze
  python3 scripts/tdd_task_execution_flow.py --plan --json > .taskmaster/reports/tdd_execution_plan.json
  ```
  - If a wrapper exists, you may use: `python3 execution-flow-optimizer.py .taskmaster/tasks/tasks.json`
  - Use the plan output to prioritize high-impact tasks and surface infra gaps early

### 3. Implementation Planning

- **Reference Methodology**: Read `@execution_prompt.md` for detailed TDD guidance
- **UserProxy Architecture Principles**: Focus on robust foundation and intelligent features
  - Multi-agent council system with orchestrator and specialist agents
  - Supabase + Pinecone for data storage and semantic memory
  - Web interface first (mobile optimization in later phases)
  - Direct API integrations (Gmail, Calendar) with intelligent processing
- **Strategic Alignment**: Check [MASTER_ROADMAP.md](../../MASTER_ROADMAP.md) to ensure task aligns with current phase priorities
- **Analyze Requirements**: Extract specific implementation requirements, **balancing quality with development velocity**
- **Plan Architecture**: Determine files to modify/create and integration points
- **Set Status**: Update task status to `in-progress` using `set_task_status`

### 4. Development Execution

- **Follow TDD Cycles**: Implement using RED → GREEN → REFACTOR methodology
- **UserProxy Development Approach**: Current focus is on foundational architecture:
  - **Core Infrastructure**: Gmail/Calendar data ingestion → Supabase storage → Pinecone semantic memory → Multi-agent council → Web tiles
  - **Quality Over Speed**: Build robust, scalable solutions that support long-term vision
  - **User Value Focus**: Demonstrate intelligent assistance that learns and adapts to user patterns
  - **Strategic Implementation**: Build council system, semantic memory, and personalization features progressively
- **Success Metrics**: Aim for intelligent, contextual assistance that saves users significant time daily
- **Maintain Documentation**: Update context documents with findings and decisions
- **Code Quality**: Follow established coding standards and patterns
- **Progressive Testing**: Ensure tests pass at each stage

### 5. Progress Tracking

- **Log Progress**: Use `update_subtask` to document implementation progress
- **Update Context**: Add findings, decisions, and technical notes to context files
- **Status Updates**: Mark subtasks as complete when finished
- **Commit Frequently**: Make atomic commits with descriptive messages

### 6. Completion & Integration

- **Final Validation**: Ensure all acceptance criteria are met
- **Code Review**: Self-review against established quality standards
- **Update Status**: Mark task/subtask as `done` using `set_task_status`
- **Git Operations**:
  - Final commit with comprehensive message
  - Push branch to remote repository

### 7. Pull Request Creation & Comprehensive CI Debugging

- **Pre-PR Validation**: Ensure PR meets requirements BEFORE creation
  - **PR Title Format**: Must use `Task XX:` or conventional format (`feat:`, `fix:`, etc.)
  - **Branch Name**: Must start with `feat/`, `fix/`, `docs/`, `test/`, `refactor/`
  - **Merge Conflicts**: Resolve any conflicts with main branch
- **Create PR**: When entire subtask is complete, create pull request
  - **PR Description**: Include task context, changes made, and testing notes
  - **Link Tasks**: Reference related task/subtask IDs in PR description
  - **Request Review**: Assign appropriate reviewers based on code changes

### 8. **MANDATORY** Comprehensive CI Monitoring & Debugging 

**🎯 CRITICAL REQUIREMENT:** **EVERY PR MUST** use systematic CI monitoring to achieve full green status. **DO NOT** consider a task complete until CI is fully green. Follow PR_debug.md methodology with smart monitoring.

**🚨 STRICT INTEGRITY REQUIREMENTS:**
- **NEVER** modify tests to bypass failures - fix the underlying issues
- **NEVER** disable CI checks, ESLint rules, or TypeScript errors
- **NEVER** skip tests or remove test coverage 
- **NEVER** commit temporary workarounds that bypass quality gates
- **ALWAYS** fix legitimate issues rather than circumventing checks

**COMPLETE THE FULL CI DEBUGGING PROCESS:**
1. **Monitor** CI failures systematically
2. **Analyze** specific error logs and failure patterns  
3. **Fix** each category of errors: ESLint, TypeScript, Prettier, tests
4. **Commit** fixes with descriptive messages
5. **Push** changes to trigger new CI run
6. **Repeat** until achieving **10✅ 0❌ 0🔄 0⏳** status

#### **Critical Pre-Steps** 🚨
1. **Validate PR title and branch name** - These cause immediate failures before CI runs
   - PR title: Must start with `Task XX:` or follow conventional format (`feat:`, `fix:`, etc.)
   - Branch name: Must start with `feat/`, `fix/`, `docs/`, `test/`, `refactor/`, etc.
2. **Check for GitHub Actions deprecation errors** - These block CI entirely
3. **Resolve merge conflicts** - Merge from main if needed
4. **Verify basic CI infrastructure** - Ensure workflows can actually run

#### **Phase 1: Smart CI Monitoring** ⭐ **[IMMEDIATE REQUIREMENT]**
```bash
# IMMEDIATE: Start smart CI monitoring (replaces blind waiting)
cd scripts/monitoring/pr_analysis
python3 ci_monitor.py <PR_NUMBER> --timeout 600 --auto-analyze
```
- **MANDATORY**: Must be executed immediately after PR creation
- **No More Sleep Commands**: Smart polling with exponential backoff
- **Real-time Progress**: ✅🔄❌⏳ status indicators
- **Auto-analysis**: Triggers detailed analysis on CI failure
- **Completion Callbacks**: Execute actions when CI completes

#### **Phase 2: Detection & Triage** 🆕
```bash
# Quick overview of all PRs to identify priority issues
python3 analyze_all_open_prs.py

# Deep analysis of specific failing PR with ACTUAL CI logs
python3 pr_analyzer_detailed.py <PR_NUMBER>
```
- **Comprehensive Analysis**: Fetches actual CI error logs (not just failure status)
- **Dependency Conflict Detection**: Specific package version conflicts (e.g., httpx vs pyautogen)
- **Cursor Bug Analysis**: By severity level with commit references
- **Fix Suggestions**: Actionable recommendations for each issue type

#### **Phase 3: Systematic Fixing (Priority Order)**
1. **GitHub Actions deprecation** → Immediate CI blocking (actions/checkout@v3 → @v4)
2. **Missing infrastructure** → Workflow files, scripts, functions
3. **Dependency conflicts** → Version compatibility issues (httpx==0.27.0 vs pyautogen>=0.28.1)
4. **Test configuration** → Expected vs actual structure mismatches
5. **Code-level issues** → Logic bugs, attribute errors

```bash
# Apply automated fixes based on analysis
python3 pr_fixer.py <PR_NUMBER> --auto-fix

# OR use AI agent for complex fixes
python3 pr_agent.py <PR_NUMBER> --fix-all

# MANUAL FIXING PROCESS (when automated tools don't resolve all issues):
# 🚨 CRITICAL: Fix actual issues, NEVER bypass or disable checks
cd app
npm run lint                    # Fix ESLint errors (NEVER disable rules)
npm run type-check             # Fix TypeScript errors (NEVER use @ts-ignore)
npm run format                # Fix Prettier formatting (NEVER disable format checks)
npm test                      # Ensure tests pass (NEVER skip/disable failing tests)
git add . && git commit -m "fix(ci): [specific fix description]"
git push origin <branch>
```

#### **Phase 4: Verification Cycle**
```bash
# MANDATORY: Use proper commit message format
git add . && git commit -m "fix(component): specific issue description"
# Examples:
# git commit -m "fix(autogen): resolve import path conflicts"
# git commit -m "feat(monitoring): add CI completion callbacks"
# git commit -m "Task 16: implement enhanced monitoring system"

git push origin <branch>

# Monitor with smart callbacks until completely green
python3 ci_monitor.py <PR_NUMBER> --timeout 600 --auto-analyze

# Verify fixes worked
python3 verify_fixes.py <PR_NUMBER>
```

#### **Phase 5: Success Validation** **[TASK COMPLETION REQUIREMENT]**
**Target State**: Continue cycles until achieving:
- ✅ All CI checks passing (4✅ 0❌ 0🔄 0⏳)
- ✅ Zero test failures
- ✅ Zero active Cursor bugs
- ✅ Vercel deployment status confirmed (failure acceptable)
- ✅ CI duration under 5 minutes

**🚨 CRITICAL**: **TASK IS NOT COMPLETE** until this target state is achieved.

**Success Metrics**:
- **Monitor reduction**: 15 failures → 2 failures → 1 failure → 0 failures
- **Infrastructure health**: No hanging, timeout, or deprecation issues
- **Bug resolution**: Active bugs resolved with commit references
- **Debugging efficiency**: Hours → minutes with detailed analyzer
- **Smart monitoring**: No more blind waiting with sleep commands

## Quality Checkpoints

### Before Starting Implementation

- [ ] Task context is clearly understood
- [ ] All dependencies are satisfied
- [ ] Current development phase is identified from [MASTER_ROADMAP.md](../../MASTER_ROADMAP.md)
- [ ] Implementation approach aligns with phase-specific priorities
- [ ] Branch is created from latest main
- [ ] Development environment is set up

### During Implementation

- [ ] Following TDD methodology
- [ ] Tests are passing
- [ ] Code follows project standards
- [ ] Progress is documented in context files

### Before Task Completion

- [ ] All acceptance criteria met
- [ ] Code is properly tested
- [ ] Documentation is updated
- [ ] Task status is updated in Taskmaster

### Before PR Creation

- [ ] Final testing completed
- [ ] Code review completed
- [ ] All commits are properly formatted
- [ ] Branch is pushed to remote

### After PR Creation & CI Debugging **[MANDATORY FOR TASK COMPLETION]**

- [ ] **Critical Pre-Steps Validated**: PR title/branch format, no deprecation errors, merge conflicts resolved
- [ ] **Phase 1 - Smart CI Monitoring**: `ci_monitor.py` with auto-analyze initiated (no blind waiting) **[IMMEDIATE REQUIREMENT]**
- [ ] **Phase 2 - Detection & Triage**: All PR overview and detailed analysis completed if CI fails
- [ ] **Phase 3 - Systematic Fixing**: Applied in priority order (deprecation → infrastructure → dependencies → tests → code)
- [ ] **Phase 4 - Verification Cycle**: Proper commit format, push, re-monitor, verify fixes
- [ ] **Phase 5 - Success Validation**: Target state achieved **[TASK NOT COMPLETE WITHOUT THIS]**:
  - [ ] All CI checks passing (4✅ 0❌ 0🔄 0⏳)
  - [ ] Zero test failures
  - [ ] Zero active Cursor bugs
  - [ ] Vercel deployment status confirmed (failure acceptable)
  - [ ] CI duration under 5 minutes
  - [ ] Success metrics: 15→2→1→0 failure progression, no infrastructure issues, smart monitoring used
  - [ ] **INTEGRITY VERIFIED**: No bypassed checks, disabled rules, or circumvented quality gates

**🚨 CRITICAL REMINDER**: A task is **NOT COMPLETE** until all CI checks are green. Do not mark task as done or move to next task until full CI success is achieved.

**🛡️ QUALITY ASSURANCE**: All green status must be achieved through legitimate fixes, not bypasses or workarounds.

## ⛔ PROHIBITED PRACTICES

**NEVER attempt to bypass CI quality gates through:**

### Code Quality Bypasses (FORBIDDEN)
- ❌ Adding `// eslint-disable` comments to silence errors
- ❌ Using `@ts-ignore` or `@ts-expect-error` to hide TypeScript issues  
- ❌ Modifying `.eslintrc` or `tsconfig.json` to lower standards
- ❌ Disabling Prettier checks or formatting rules
- ❌ Adding `prettier-ignore` comments to avoid formatting

### Test Integrity Violations (FORBIDDEN)
- ❌ Skipping tests with `.skip()` or `xit()` to avoid failures
- ❌ Commenting out failing test cases
- ❌ Modifying test expectations to match broken behavior
- ❌ Reducing test coverage requirements
- ❌ Mocking away functionality to hide real issues

### CI Configuration Bypasses (FORBIDDEN)
- ❌ Modifying GitHub Actions workflows to skip checks
- ❌ Removing required CI status checks from branch protection
- ❌ Using `--force` push to bypass review requirements
- ❌ Creating empty commits to trigger false green status
- ❌ Disabling security scanning or dependency checks

### Build Process Circumvention (FORBIDDEN)
- ❌ Commenting out failing build steps
- ❌ Adding temporary environment variables to hide errors
- ❌ Modifying package.json scripts to skip quality checks
- ❌ Using `|| true` to make failing commands appear successful

**✅ CORRECT APPROACH**: Always identify and fix the root cause of any CI failure through legitimate code changes, proper error handling, and quality improvements.

## Integration Points

### Taskmaster Integration

- Use MCP tools for all task management operations
- Update task status at key milestones
- Document progress in subtask details
- Reference task IDs in all related artifacts

### Git Integration

- Follow consistent branching strategy
- Use conventional commit message format
- Link commits to specific tasks/subtasks
- Maintain clean commit history

### Documentation Integration

- Update context documents with implementation notes
- Reference relevant documentation in code
- Create/update technical documentation as needed
- Link to external resources and standards

### Roadmap Integration

- **Phase Awareness**: Always consider current development phase when making implementation decisions
- **Feature Prioritization**: Refer to [MASTER_ROADMAP.md](../../MASTER_ROADMAP.md) for feature priorities specific to current phase
- **Timeline Alignment**: Ensure task completion aligns with phase timelines and milestones
- **Success Metrics**: Consider phase-specific success metrics when validating implementation

## Error Handling

### Task Blockers

- Document blocker in task context
- Update task status to `blocked`
- Identify resolution steps or dependencies
- Communicate with stakeholders if needed

### Implementation Issues

- Use debugging methodology from `@debugging.md`
- Document troubleshooting steps in context
- Seek guidance through appropriate channels
- Update task context with resolution

### Quality Issues

- Address code quality problems before completion
- Use code review checklist from `@code_review.md`
- Ensure security considerations from `@security_review.md`
- Validate testing strategy from `@testing_strategy.md`

## Best Practices

### Communication

- Keep task context updated with latest findings
- Use clear, descriptive commit messages
- Document decisions and trade-offs made
- Reference related tasks and dependencies

### Code Quality

- Follow established coding standards
- Write meaningful tests
- Use consistent naming conventions
- Maintain readable code structure

### Process Adherence

- Don't skip quality checkpoints
- Update task status promptly
- Create atomic, focused commits
- Complete full workflow for each task

## Quick Reference Commands

```bash
# Get next task (from MVP context)
mcp_taskmaster-ai_next_task(projectRoot="/Users/shrenilpatel/Github/UserProxy", tag="MVP")

# Update task status (MVP context)
mcp_taskmaster-ai_set_task_status(id="<task_id>", status="in-progress", projectRoot="/Users/shrenilpatel/Github/UserProxy", tag="MVP")

# Log progress (MVP context)
mcp_taskmaster-ai_update_subtask(id="<subtask_id>", prompt="Implementation progress...", projectRoot="/Users/shrenilpatel/Github/UserProxy", tag="MVP")

# View current MVP tasks
mcp_taskmaster-ai_get_tasks(projectRoot="/Users/shrenilpatel/Github/UserProxy", withSubtasks=true, tag="MVP")

# Create branch (proper format required)
git checkout -b feat/task-<id>-<description>

# Commit changes (proper format required)
git add . && git commit -m "feat(task-<id>): <description>"

# Push and create PR
git push origin feat/task-<id>-<description>

# Create PR with proper title format
gh pr create --title "Task <id>: <description>" --body "<PR description>"
# OR conventional format:
gh pr create --title "feat(scope): <description>" --body "<PR description>"

# === CRITICAL: CI DEBUGGING WORKFLOW (Follow PR_debug.md) ===
# ALWAYS navigate to monitoring tools first
cd scripts/monitoring/pr_analysis

# 🚨 CRITICAL PRE-STEPS (immediate failures if missed):
# 1. Validate PR title: "Task XX:" or "feat(scope):" format
# 2. Validate branch name: "feat/", "fix/", "docs/", etc.
# 3. Check for deprecation errors: actions/checkout@v3 → @v4
# 4. Resolve merge conflicts

# Phase 1: IMMEDIATE Smart CI Monitoring ⭐ **[MANDATORY]** (no blind waiting)
python3 ci_monitor.py <PR_NUMBER> --timeout 600 --auto-analyze

# Phase 2: Detection & Triage 🆕 (if CI fails)
python3 analyze_all_open_prs.py                    # Quick overview
python3 pr_analyzer_detailed.py <PR_NUMBER>        # ACTUAL CI logs + fix suggestions

# Phase 3: Automated Fixing (priority order)
python3 pr_fixer.py <PR_NUMBER> --auto-fix         # Automated fixes
python3 pr_agent.py <PR_NUMBER> --fix-all          # AI agent for complex issues

# Phase 3 Manual Fixing (when automated tools insufficient):
# 🚨 NEVER bypass checks - fix actual issues only
cd app && npm run lint && npm run type-check && npm run format && npm test
git add . && git commit -m "fix(ci): [specific description]" && git push origin <branch>

# Phase 4: Verification Cycle (repeat until green)
git add . && git commit -m "fix(component): specific issue description"
git push origin <branch>
python3 ci_monitor.py <PR_NUMBER> --timeout 600 --auto-analyze
python3 verify_fixes.py <PR_NUMBER>

# TARGET: 15 failures → 2 failures → 1 failure → 0 failures ✅
# SUCCESS: 4✅ 0❌ 0🔄 0⏳, zero bugs, <5min CI duration

# Legacy commands (use only if new tools unavailable)
gh pr checks <pr_number>
gh pr view <pr_number>

# Optional: Check Vercel (failure acceptable)
vercel ls
vercel inspect <deployment-url>
```

```bash
# Execution Flow Analysis (TDD) — analyze and generate plan
python3 scripts/tdd_task_execution_flow.py --analyze
python3 scripts/tdd_task_execution_flow.py --plan --json > .taskmaster/reports/tdd_execution_plan.json
# Optional wrapper (if present)
python3 execution-flow-optimizer.py .taskmaster/tasks/tasks.json
```

This workflow ensures consistent, high-quality task execution while maintaining proper documentation and integration with project management systems.
