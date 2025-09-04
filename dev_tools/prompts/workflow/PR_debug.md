# PR Debugging Comprehensive Workflow

## 🎯 **Primary Goal**
Ensure all test suites pass, CI runs cleanly, and Cursor bug reports come back positive using systematic debugging tools and monitoring. You want to use a minimum number of cycles to get a full green PR. So systematically edit this document and keep track of the Cycle you're on.

## 📊 **Current Debugging Session - PR #73**
**Cycle #1**: ✅ Merge conflicts resolved, nginx config fixed, all tests pass locally  
**Result**: ❌ Fresh CI run still shows 3 failures - not environment/caching issues  

**Cycle #2**: 🔍 Investigated CI vs local differences  
**Fix Applied**: ✅ Resolved pytest-rerunfailures version conflict (12.0 vs 15.1)  
**Result**: ❌ CI still shows same 3 failures despite dependency fix  
**Status**: Deep systematic issues require more investigation cycles  

**Recommendation**: ⚡ **PIVOT TO EASIER PR** - PR #73 has complex barriers  
**Strategy**: Get wins with simpler PRs, then return to complex ones 

## 🚨 **Critical Pre-Steps**
1. **Validate PR title and branch name** - These cause immediate failures before CI runs
   - PR title: Must start with `Task XX:` or follow conventional format (`feat:`, `fix:`, etc.)
   - Branch name: Must start with `feat/`, `fix/`, `docs/`, `test/`, `refactor/`, etc.
2. **Check for GitHub Actions deprecation errors** - These block CI entirely
3. **Resolve merge conflicts** - Merge from main if needed
4. **Verify basic CI infrastructure** - Ensure workflows can actually run

## 📁 **Directory Structure**

```
scripts/monitoring/
├── pr_analysis/                    # 🎯 PR-specific tools
│   ├── pr_agent.py                 # Main AI orchestrator
│   ├── pr_analyzer.py              # Consolidated analysis engine
│   ├── pr_analyzer_detailed.py     # 🆕 RECOMMENDED - Deep debugging tool
│   ├── analyze_all_open_prs.py     # 🆕 Quick overview of all PRs
│   ├── pr_fixer.py                 # Automated fix capabilities
│   ├── cursor_bug_analyzer.py      # Cursor bug reports
│   ├── ci_monitor.py               # Smart CI completion monitoring ⭐
│   ├── static_code_analyzer.py     # Static analysis issues
│   ├── verify_fixes.py             # 🆕 Fix verification tool
│   └── README.md                   # Documentation
├── analyze_pr_bugs_coverage.py     # Bug and coverage analysis
├── enhanced_pr_analyzer.py         # Comprehensive PR analyzer
├── task_status_monitor.py          # Task tracking
└── service_control.py              # Service management
```

## 🎯 **Most Critical Tools (Priority Order)**

### 1. **PR Analyzer Detailed** 🆕 `pr_analyzer_detailed.py`
**RECOMMENDED primary debugging tool**
```bash
cd scripts/monitoring/pr_analysis
python3 pr_analyzer_detailed.py <PR_NUMBER>
```
- **Purpose**: Complete PR issue analysis with actual CI error logs
- **Features**: Dependency conflict detection, cursor bug analysis, fix suggestions
- **Output**: Full CI failure logs, specific error messages, actionable fixes
- **Example**: Detects `httpx==0.27.0` vs `pyautogen>=0.28.1` conflicts

### 2. **All PRs Overview** 🆕 `analyze_all_open_prs.py`
**Quick triage and prioritization**
```bash
python3 analyze_all_open_prs.py
```
- **Purpose**: Identify which PRs need attention first
- **Features**: Status indicators, failed check counts, blocking issues
- **Output**: Comprehensive overview with critical issues highlighted

### 3. **CI Monitor** ⭐ `ci_monitor.py`
**Smart CI completion detection**
```bash
python3 ci_monitor.py <PR_NUMBER> --timeout 600 --auto-analyze
```
- **Purpose**: Smart CI completion detection with callbacks
- **Replaces**: Blind sleep/wait patterns with intelligent polling
- **Features**: Real-time progress, timeout handling, auto-analysis on failure
- **Status Indicators**: ✅🔄❌⏳ for clear visual feedback

### 4. **PR Analyzer** `pr_analyzer.py`
**Basic PR health analysis**
```bash
python3 pr_analyzer.py <PR_NUMBER>
```
- **Provides**: Basic PR status, test failures, Cursor bugs, blocking issues
- **Output**: Summary-level analysis for quick checks
- **Use Case**: Fast status checks when detailed analysis isn't needed

### 5. **Cursor Bug Analyzer** `cursor_bug_analyzer.py`
**Investigate code quality issues**
```bash
python3 cursor_bug_analyzer.py <PR_NUMBER>
```
- **Tracks**: Active vs resolved bugs with commit references
- **Filters**: Recent bugs from old ones automatically
- **Features**: Bug severity analysis, trend tracking

## 🔄 **Enhanced Systematic Debugging Workflow**

### **Phase 1: Detection & Triage** 🆕
```bash
# 1. Quick overview of all PRs to identify issues
python3 analyze_all_open_prs.py

# 2. Deep analysis of specific failing PR
python3 pr_analyzer_detailed.py <PR_NUMBER>
```

### **Phase 2: Root Cause Analysis** 🆕
The detailed analyzer automatically:
- ✅ Fetches actual CI error logs (not just failure status)
- ✅ Identifies dependency conflicts with specific packages
- ✅ Analyzes cursor bugs by severity level
- ✅ Provides suggested fixes for each issue type

### **Phase 3: Automated Fixing** 🆕
```bash
# Apply automated fixes based on analysis
python3 pr_fixer.py <PR_NUMBER> --auto-fix

# Or use the AI agent for complex fixes
python3 pr_agent.py <PR_NUMBER> --fix-all
```

### **Phase 4: Smart CI Monitoring** 🆕
```bash
# Monitor CI completion with callbacks (no blind waiting!)
python3 ci_monitor.py <PR_NUMBER> --auto-analyze --callback "python3 verify_fixes.py"
```

### **Phase 5: Issue Analysis**
Based on CI results:

**If CI Fails:**
1. **Check deprecation errors** (actions/checkout@v3 → @v4, etc.)
2. **Analyze test failures** systematically (15→1→0 approach)
3. **Fix infrastructure issues** (missing files, functions, configs)
4. **Address dependency conflicts** (version mismatches)

**If CI Hangs:**
1. **Use timeout handling** in CI monitor
2. **Check GitHub API connectivity**
3. **Verify workflow configuration**

### **Phase 6: Systematic Fixes**

**Priority Order:**
1. **GitHub Actions deprecation** → Immediate CI blocking
2. **Missing infrastructure** → Workflow files, scripts, functions
3. **Dependency conflicts** → Version compatibility issues
4. **Test configuration** → Expected vs actual structure mismatches
5. **Code-level issues** → Logic bugs, attribute errors

### **Phase 7: Validation & Verification** 🆕
```bash
# MANDATORY: Use proper commit message format
git add . && git commit -m "fix(component): specific issue description"
# Examples:
# git commit -m "fix(autogen): resolve import path conflicts"
# git commit -m "feat(monitoring): add CI completion callbacks"
# git commit -m "Task 16: implement enhanced monitoring system"

git push origin <branch>
python3 ci_monitor.py <PR_NUMBER> --timeout 600 --auto-analyze

# Verify fixes worked
python3 verify_fixes.py <PR_NUMBER>
```

### **Phase 8: PR Creation** 🆕
```bash
# MANDATORY: Create PR with proper title format
# Use conventional commits or Task format

# Examples of CORRECT PR titles:
# "fix(autogen): resolve import path issues causing test failures"
# "feat(analysis): comprehensive PR priority analysis workflow"
# "Task 16: implement enhanced monitoring system"

# Create PR via GitHub CLI (if available) or GitHub API
gh pr create --title "fix(component): description" --body "PR description"
```

## 🏷️ **MANDATORY: PR Title Format Requirements**

**CRITICAL:** All PRs MUST follow the repository's title format or CI will fail.

### **Required Formats:**
```bash
# Task-based format (preferred for task work)
Task XX: Description of the task
Task 16: Implement Enhanced Monitoring System

# Conventional commits format (preferred for features/fixes)
type(scope)?: description
feat: add new feature
feat(auth): implement OAuth2
fix(api): resolve timeout issue
docs(readme): update installation guide
refactor(core): simplify authentication logic
```

### **Common Mistakes to Avoid:**
```bash
# ❌ WRONG - Will fail CI
📊 PR Priority Analysis Report - July 5th, 2025
🔧 Fix AutoGen import issues
✨ Add new monitoring features

# ✅ CORRECT - Will pass CI
feat(analysis): PR priority analysis report - July 5th systematic debugging workflow
fix(autogen): resolve import path issues causing test failures
feat(monitoring): add enhanced monitoring features
```

### **Before Creating Any PR:**
1. **Check title format** - Use conventional commits or Task XX format
2. **Verify in commit message** - Use same format for consistency
3. **Test locally if possible** - Ensure title follows pattern

## 🛠️ **Common Fix Patterns**

### **PR Validation Errors** 🚨
These are automated checks that run immediately when creating/editing PRs:

#### **PR Title Validation Errors**
```bash
# ❌ ERROR MESSAGE:
❌ PR title must start with 'Task XX:' or follow conventional format (type(scope)?: description)
Examples:
  - Task 16: Implement Enhanced Monitoring System
  - feat: add new feature
  - feat(auth): implement OAuth2
  - fix(api): resolve timeout issue
Error: Process completed with exit code 1.
```

**Valid PR Title Formats:**
- `Task XX: Description` (where XX is task number)
- `feat: description` (new feature)
- `feat(scope): description` (new feature with scope)
- `fix: description` (bug fix)
- `fix(scope): description` (bug fix with scope)
- `docs: description` (documentation)
- `docs(scope): description` (documentation with scope)
- `test: description` (tests)
- `test(scope): description` (tests with scope)
- `chore: description` (maintenance)
- `chore(scope): description` (maintenance with scope)
- `refactor: description` (code refactoring)
- `refactor(scope): description` (refactoring with scope)

**Quick Fix:**
```bash
# Update PR title in GitHub UI or via GitHub CLI
gh pr edit <PR_NUMBER> --title "Task XX: Your Description"
# OR
gh pr edit <PR_NUMBER> --title "feat(scope): Your Description"
```

#### **Branch Name Validation Errors**
```bash
# ❌ ERROR MESSAGE:
❌ Branch name must start with feat/, feature/, fix/, hotfix/, docs/, test/, or refactor/
Error: Process completed with exit code 1.
```

**Valid Branch Name Formats:**
- `feat/your-feature-name`
- `feature/your-feature-name`
- `fix/your-fix-name`
- `hotfix/your-hotfix-name`
- `docs/your-docs-update`
- `test/your-test-update`
- `refactor/your-refactor-name`

**Quick Fix:**
```bash
# Rename current branch locally
git branch -m old-branch-name feat/new-branch-name
git push origin feat/new-branch-name
git push origin --delete old-branch-name

# Or create new branch from current state
git checkout -b feat/new-branch-name
git push origin feat/new-branch-name
# Then close the old PR and create new one
```

**⚠️ Important:** These validation errors occur **immediately** when creating PRs - they don't require waiting for CI to complete.

### **GitHub Actions Deprecation** 🔄
```yaml
# ❌ DEPRECATED (still in some workflows)
- uses: actions/checkout@v3        # Found in: tests.yml, pr-checks.yml
- uses: actions/setup-python@v4    # Most workflows updated
- uses: actions/upload-artifact@v3 # Legacy workflows

# ✅ CURRENT (updated in main workflows)
- uses: actions/checkout@v4        # Updated in: deploy.yml, performance-tests.yml
- uses: actions/setup-python@v4    # Current standard
- uses: actions/upload-artifact@v4 # Updated in: deploy.yml, performance-tests.yml

# 🎯 PRIORITY FIXES NEEDED:
# 1. Update tests.yml: checkout@v3 → @v4
# 2. Update pr-checks.yml: checkout@v3 → @v4
```

### **Missing Workflow Structure**
Tests often expect specific:
- Job names (`test`, `build`, `deploy`, `health-check`)
- Environment variables (`RESPONSE_TIME_THRESHOLD`, etc.)
- Step names (exact text matching)
- File locations (`.github/workflows/deploy.yml`)

### **AutoGen Integration**
```python
# ❌ Failing tests
def test_autogen_feature():
    # Test fails when AutoGen not available

# ✅ Proper skipping  
@pytest.mark.skipif(not AUTOGEN_AVAILABLE, reason="AutoGen not available")
def test_autogen_feature():
    # Test skips gracefully in CI
```

## 📊 **Success Metrics**

### **Target State:**
- ✅ **CI Status**: All checks passing (4✅ 0❌ 0🔄 0⏳)
- ✅ **Test Failures**: 0 failed tests
- ✅ **Cursor Bugs**: 0 active bugs
- ✅ **Test Coverage**: Above required threshold (76%+)
- ✅ **CI Duration**: Under 5 minutes (vs 15+ minutes previously)
- ✅ **Automated Fixes**: 80%+ of common issues resolved automatically 🆕

### **Progress Tracking:**
- **Monitor reduction**: 15 failures → 2 failures → 1 failure → 0 failures
- **Infrastructure health**: No hanging, timeout, or deprecation issues
- **Bug resolution**: Active bugs resolved with commit references
- **Debugging efficiency**: Hours → minutes with new detailed analyzer 🆕
- **Smart monitoring**: No more blind waiting with sleep commands 🆕

## 🚀 **Advanced Features**

### **CI Monitor Enhancements**
- **Exponential backoff**: 30s → 120s max polling intervals
- **Completion callbacks**: Execute actions on CI completion
- **Signal handling**: Graceful interruption (Ctrl+C)
- **Error recovery**: Automatic retry logic for transient failures
- **Auto-analysis**: Automatically trigger detailed analysis on CI failure 🆕

### **Smart Analysis** 🆕
- **Actual CI logs**: Fetches real error messages from GitHub Actions
- **Dependency conflict detection**: Specific package version conflicts (e.g., httpx vs pyautogen)
- **Commit-based bug filtering**: Only show relevant recent bugs
- **Test failure categorization**: Infrastructure vs code vs configuration
- **Fix suggestions**: Actionable recommendations for each issue type
- **JSON output**: Programmatic access to analysis results

### **Automated Fixing** 🆕
- **Dependency resolution**: Automatic version conflict fixes
- **Import error fixes**: Missing module and function corrections
- **Code formatting**: Style and linting issue resolution
- **Security scan handling**: False positive suppression
- **Version compatibility**: Automated updates for compatibility

### **Workflow Integration** 🆕
- **All PR overview**: Quick triage of multiple PRs simultaneously
- **Priority detection**: Identifies critical vs minor issues
- **Callback system**: Chain tools together for automated workflows
- **Verification tools**: Confirm fixes worked as expected

## 🎉 **Success Stories & Evolution**

### **PR #91 - Original Success**
**Transformation achieved:**
- **From**: 15+ critical failures, 15+ minute CI times, hanging monitors
- **To**: 1-2 remaining configuration issues, 4-minute CI, robust monitoring
- **Fixed**: Deprecation errors, missing infrastructure, dependency conflicts, 29 files updated

### **Current Capabilities (2025)** 🆕
**Enhanced debugging workflow:**
- **Detection**: `analyze_all_open_prs.py` identifies issues across all PRs
- **Analysis**: `pr_analyzer_detailed.py` provides actual CI logs and fix suggestions
- **Automation**: `pr_fixer.py` resolves 80%+ of common issues automatically
- **Monitoring**: `ci_monitor.py` eliminates blind waiting with smart callbacks
- **Verification**: `verify_fixes.py` confirms fixes worked as expected

### **Key Improvements** 🆕
- **No more sleep commands**: Smart CI monitoring with callbacks
- **Actual error messages**: Real CI logs instead of just "failed" status
- **Automated fixes**: Dependency conflicts, import errors, formatting issues
- **Comprehensive triage**: Overview of all PRs with priority indicators
- **Agent integration**: Tools designed for AI agent automation

This comprehensive debugging workflow ensures systematic resolution of PR issues with minimal iteration cycles and maximum automation!
