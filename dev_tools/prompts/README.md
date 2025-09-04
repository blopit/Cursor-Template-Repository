# Created by: claude-3.5-sonnet
# Last edited: 2024-12-19 15:30:00 UTC by claude-3.5-sonnet

# AI Prompts and Templates

## Purpose and Overview

The `prompts/` directory contains AI prompts, templates, and execution instructions for the Mantra Ultimate Assistant. These prompts define how AI agents interact with users, process queries, and execute workflows, ensuring consistent and effective AI behavior across the system.

The prompts are designed to guide AI agents in understanding user intent, maintaining context, and delivering helpful responses while following established patterns and best practices.

## File Structure

```
prompts/
├── workflow/                        # Workflow-specific prompts
│   ├── default.md                  # Comprehensive task execution workflow
│   ├── execution_prompt.md         # Test-Driven Development prompt template
│   ├── PR_debug.md                 # PR debugging and CI troubleshooting
│   ├── agent_handoff_workflow.md   # Agent handoff workflow
│   ├── debugging.md                # Debug-first methodology
│   ├── feature_scoping.md          # Feature planning requirements
│   ├── testing_strategy.md         # Testing methodology
│   ├── code_review.md              # Quality assurance checklist
│   ├── api_development.md          # API development best practices
│   ├── security_review.md          # Security guidelines
│   ├── documentation.md            # Documentation standards
│   └── README.md                   # Workflow prompts documentation
└── README.md                       # This file
```

## Key Components

### Workflow Prompts (`workflow/`)

The workflow directory contains core behavioral prompts that guide AI agents through specific workflows and development processes:

#### System Prompts Overview
System prompts define:
- AI agent behavior and instructions
- Workflow execution patterns
- Development methodologies
- Task execution frameworks

These prompts are used by AI agents to understand their role and execution patterns.
They define the core behavior and methodology for automated development tasks.

#### Test-Driven Development Prompt
A comprehensive prompt template that guides AI coding agents through Test-Driven Development (TDD) workflows:

- **Task Management Integration**: Fetches work items from Taskmaster MCP
- **Context Retrieval**: Loads task and subtask context documents
- **TDD Methodology**: Enforces RED → GREEN → REFACTOR cycles
- **Structured Reporting**: Generates detailed execution reports
- **Documentation Integration**: References project documentation when needed

## Prompt Categories

### 1. Workflow Execution Prompts
Templates for guiding AI agents through specific workflows:
- **Development Workflows**: TDD, code review, debugging processes
- **Task Management**: Work item processing and status updates
- **Quality Assurance**: Testing, validation, and verification procedures
- **Documentation**: Content generation and maintenance workflows

### 2. User Interaction Prompts
Templates for AI agent responses to user queries:
- **Query Processing**: Understanding and parsing user requests
- **Response Generation**: Crafting helpful and contextual responses
- **Error Handling**: Managing and communicating errors gracefully
- **Follow-up Actions**: Suggesting next steps and related actions

### 3. System Integration Prompts
Templates for AI agent interactions with external systems:
- **API Integration**: Calling external services and processing responses
- **Database Operations**: Data retrieval, storage, and manipulation
- **Authentication**: Secure access to user data and services
- **Monitoring**: System health checks and performance reporting

## Usage Examples

### TDD Execution Prompt Usage

The TDD execution prompt guides AI agents through a structured development process:

#### 1. Task Fetching
```
Query Taskmaster MCP for the next pending task
Within that task, select its next pending subtask
```

#### 2. Context Loading
```
Load task context: ./.taskmaster/context/task_<TaskID>_context.md
Load subtask context: ./.taskmaster/context/task_<TaskID>_subtask_<SubtaskID>_context.md
```

#### 3. Requirements Analysis
```
For each context document, produce:
- Goals (2-3 bullets)
- Constraints/Acceptance Criteria (2-3 bullets)  
- Prerequisites & Domain Knowledge (2-3 bullets)
Extract: code snippets, API endpoints, schemas, dependencies
```

#### 4. TDD Planning
```
1. Storyboard the Workflow
2. Define Test Matrix
3. Create Action Items with:
   - Tests to create (filename & purpose)
   - Implementation files/modules affected
   - Tools/commands required
   - Dependencies & blockers
   - Estimated effort/complexity
```

#### 5. Implementation Cycles
```
RED Phase: Write failing tests first
GREEN Phase: Implement code to pass tests
REFACTOR Phase: Improve code without changing behavior
```

### Custom Prompt Development

#### Prompt Template Structure
```markdown
### **Prompt: [Prompt Name] – [Purpose Edition]**

[Brief description of the prompt's purpose and scope]

---

#### **1. [Step Name]**
* [Specific instruction or action]
* [Additional details or constraints]

#### **2. [Next Step Name]**
* [Instruction with parameters]
* [Expected outcomes or validation criteria]

[Continue with numbered steps...]

#### **[Final Step]. [Completion Action]**
Output a **[format]** containing:
* [Required output element 1]
* [Required output element 2]
* [Additional metadata or context]

---

**[Final instruction or reminder]**
```

#### Example Custom Prompt
```markdown
### **Prompt: Email Processing Agent – User Query Edition**

You are an email processing specialist that helps users manage their inbox efficiently and intelligently.

---

#### **1. Analyze User Query**
* Parse the user's email-related request
* Identify specific actions requested (read, send, organize, etc.)
* Extract relevant parameters (sender, timeframe, keywords)

#### **2. Retrieve Email Data**
* Connect to user's Gmail account via authenticated API
* Fetch relevant emails based on query parameters
* Apply intelligent filtering and prioritization

#### **3. Process and Analyze**
* Categorize emails by importance and urgency
* Identify actionable items and follow-ups
* Generate summary insights and recommendations

#### **4. Generate Response**
Output a **structured response** containing:
* Summary of emails found
* Prioritized action items
* Suggested responses or next steps
* Relevant email metadata and context

---

**Always maintain user privacy and follow data handling best practices.**
```

## Prompt Engineering Best Practices

### 1. Clarity and Specificity
- Use clear, unambiguous language
- Provide specific instructions and expected outcomes
- Include examples when helpful
- Define technical terms and acronyms

### 2. Structure and Organization
- Use numbered steps for sequential processes
- Employ bullet points for lists and options
- Include section headers for different phases
- Maintain consistent formatting throughout

### 3. Context and Constraints
- Specify the AI agent's role and capabilities
- Define scope and limitations clearly
- Include relevant background information
- Set expectations for output format and quality

### 4. Error Handling and Edge Cases
- Include instructions for handling errors
- Address common edge cases and exceptions
- Provide fallback strategies and alternatives
- Specify when to ask for clarification

### 5. Integration and Dependencies
- Reference external systems and APIs clearly
- Specify required permissions and credentials
- Include dependency checks and validations
- Define integration points and data flows

## Prompt Validation and Testing

### Testing Prompt Effectiveness
```python
class PromptTester:
    """Test framework for validating prompt effectiveness"""
    
    def test_prompt_clarity(self, prompt_text):
        """Test if prompt instructions are clear and unambiguous"""
        # Analyze prompt for clarity metrics
        pass
    
    def test_prompt_completeness(self, prompt_text):
        """Test if prompt covers all necessary steps"""
        # Check for missing components
        pass
    
    def test_prompt_consistency(self, prompt_text):
        """Test if prompt follows established patterns"""
        # Validate against style guidelines
        pass
    
    def test_prompt_execution(self, prompt_text, test_scenarios):
        """Test prompt with various input scenarios"""
        # Execute prompt with different inputs
        pass
```

### Prompt Metrics and Analytics
- **Execution Success Rate**: Percentage of successful prompt executions
- **Response Quality**: Evaluation of generated responses
- **User Satisfaction**: Feedback on prompt-generated interactions
- **Performance Metrics**: Execution time and resource usage
- **Error Rates**: Frequency and types of execution errors

## Prompt Versioning and Management

### Version Control
```
prompts/
├── execution/
│   ├── v1.0/
│   │   └── tdd_prompt.md
│   ├── v1.1/
│   │   └── tdd_prompt.md
│   └── current/
│       └── tdd_prompt.md -> ../v1.1/tdd_prompt.md
```

### Prompt Metadata
```yaml
# prompt_metadata.yml
prompt_name: "TDD Execution Prompt"
version: "1.1"
created_date: "2024-01-15"
last_modified: "2024-01-20"
author: "Development Team"
purpose: "Guide AI agents through Test-Driven Development workflows"
target_agents: ["coding_agent", "development_assistant"]
dependencies: ["taskmaster_mcp", "project_context"]
validation_status: "tested"
performance_metrics:
  success_rate: 0.95
  avg_execution_time: "45s"
  user_satisfaction: 4.2
```

### Prompt Deployment
```python
class PromptManager:
    """Manage prompt deployment and updates"""
    
    def deploy_prompt(self, prompt_name, version):
        """Deploy a specific prompt version"""
        pass
    
    def rollback_prompt(self, prompt_name, previous_version):
        """Rollback to previous prompt version"""
        pass
    
    def validate_prompt(self, prompt_content):
        """Validate prompt before deployment"""
        pass
    
    def monitor_prompt_performance(self, prompt_name):
        """Monitor prompt execution metrics"""
        pass
```

## Integration with AI Agents

### Agent Prompt Loading
```python
from mantra.backend.agents.prompt_manager import PromptManager

class AIAgent:
    def __init__(self):
        self.prompt_manager = PromptManager()
    
    async def load_execution_prompt(self, workflow_type):
        """Load appropriate execution prompt for workflow"""
        prompt = await self.prompt_manager.get_prompt(
            category="execution",
            workflow=workflow_type,
            version="current"
        )
        return prompt
    
    async def execute_with_prompt(self, prompt, context):
        """Execute workflow using loaded prompt"""
        # Process prompt with context
        # Execute workflow steps
        # Return structured results
        pass
```

### Dynamic Prompt Customization
```python
class PromptCustomizer:
    """Customize prompts based on context and user preferences"""
    
    def customize_prompt(self, base_prompt, user_context):
        """Customize prompt for specific user and context"""
        # Inject user preferences
        # Adapt to user's skill level
        # Include relevant context
        # Return customized prompt
        pass
    
    def personalize_instructions(self, prompt, user_history):
        """Personalize prompt based on user interaction history"""
        # Analyze user patterns
        # Adjust instruction style
        # Include learned preferences
        pass
```

## Future Enhancements

### Planned Improvements
1. **Multi-Modal Prompts**: Support for image and audio prompt components
2. **Interactive Prompts**: Dynamic prompts that adapt based on intermediate results
3. **Collaborative Prompts**: Multi-agent coordination prompts
4. **Learning Prompts**: Self-improving prompts based on execution feedback
5. **Domain-Specific Prompts**: Specialized prompts for different user domains

### Advanced Features
1. **Prompt Chaining**: Sequential execution of related prompts
2. **Conditional Logic**: Branching prompt execution based on conditions
3. **Prompt Templates**: Reusable prompt components and patterns
4. **Natural Language Prompts**: User-generated prompts in natural language
5. **Prompt Analytics**: Advanced analytics and optimization tools

## Related Documentation

- [`../docs/agent_architecture.md`](../docs/agent_architecture.md) - AI agent system architecture
- [`../mantra/backend/agents/README.md`](../mantra/backend/agents/README.md) - Agent implementation details
- [`../tests/ai_agent/README.md`](../tests/ai_agent/README.md) - AI agent testing procedures
- [`../docs/project_requirements.md`](../docs/project_requirements.md) - Project specifications and requirements
