# Agent Handoff & Context Transfer Prompt

<!-- Created by: claude-3-5-sonnet-20241022 -->
<!-- Last edited: 2025-08-02 20:48:52 UTC by claude-3-5-sonnet-20241022 -->

## Purpose

This prompt guides AI agents in effectively transferring complete context and state information when handing off work to another agent, ensuring seamless continuity and preventing loss of critical information.

## Handoff Protocol

### 1. Context Assessment & Preparation

Before initiating a handoff, gather and organize the following information:

#### **Current State Analysis**

- [ ] **Active Task Context**: Current task/subtask being worked on
- [ ] **Implementation Status**: What has been completed vs. what remains
- [ ] **Code Changes**: Files modified, created, or deleted in this session
- [ ] **Dependencies**: External services, APIs, or systems involved
- [ ] **Environment State**: Running services, active connections, or temporary states

#### **Decision History**

- [ ] **Key Decisions Made**: Technical choices and their reasoning
- [ ] **Alternatives Considered**: Options evaluated but not chosen
- [ ] **Trade-offs Identified**: Known compromises or limitations
- [ ] **User Preferences**: Explicit user choices or requirements gathered

#### **Technical Context**

- [ ] **Architecture Patterns**: Design patterns or frameworks being used
- [ ] **Data Flow**: How information moves through the system
- [ ] **Integration Points**: External APIs, databases, or services
- [ ] **Performance Considerations**: Optimization requirements or constraints

### 2. Handoff Documentation Structure

Use this standardized format for context transfer:

```markdown
# Agent Handoff Report

**Transfer Date**: [ISO DateTime]
**Transferring Agent**: [Agent Identifier]
**Session Duration**: [Duration]
**Handoff Reason**: [Brief explanation]

## Current Objective

[Clear statement of what the receiving agent should accomplish]

## Work Completed This Session

### Code Changes

- **Files Modified**: [List with brief description of changes]
- **Files Created**: [List with purpose]
- **Files Deleted**: [List with reason]

### Tasks Completed

- [List of completed subtasks with IDs]
- [Key milestones reached]

### Decisions Made

- **Technical Decisions**: [List with rationale]
- **User Preferences**: [Captured requirements]
- **Architecture Choices**: [Design decisions]

## Current State

### Active Context

- **Current Task**: [Task ID and description]
- **Current Subtask**: [Subtask ID and specific focus]
- **Implementation Phase**: [Planning/Development/Testing/Review]

### Environment Status

- **Running Services**: [List any active processes]
- **Open Connections**: [Database, API, or external connections]
- **Temporary States**: [Any temporary configurations or data]

### Code Base Status

- **Branch**: [Current git branch]
- **Uncommitted Changes**: [List any unstaged/uncommitted work]
- **Build Status**: [Last known build/test status]

## Next Steps & Priorities

### Immediate Actions Needed

1. [Highest priority next step]
2. [Second priority]
3. [Third priority]

### Known Blockers

- [List any identified obstacles]
- [Dependencies waiting for resolution]
- [Information needed from user]

### Implementation Notes

- **Patterns to Follow**: [Established patterns in the codebase]
- **Testing Strategy**: [How to verify the implementation]
- **Integration Points**: [What needs to connect with what]

## Context Files & Resources

### Task Context

- **Primary Task Context**: `./.taskmaster/context/task_[ID]_context.md`
- **Subtask Context**: `./.taskmaster/context/task_[ID]_subtask_[ID]_context.md`

### Code References

- **Key Files**: [List of important files to understand]
- **Documentation**: [Relevant docs or comments]
- **Test Files**: [Related test files]

### External References

- **APIs/Services**: [Links to documentation]
- **Libraries/Frameworks**: [Version info and docs]
- **Standards/Conventions**: [Project-specific guidelines]

## Risks & Considerations

### Technical Risks

- [Known technical challenges or risks]
- [Potential breaking changes]
- [Performance implications]

### Business Risks

- [Impact on user experience]
- [Timeline considerations]
- [Scope creep potential]

## Validation Criteria

### Success Metrics

- [How to know the work is complete]
- [Quality standards to meet]
- [Performance benchmarks]

### Testing Requirements

- [Unit tests needed]
- [Integration tests required]
- [Manual testing steps]

## Communication Log

### User Interactions

- [Key user feedback or requests]
- [Clarifications received]
- [Preferences expressed]

### Assumptions Made

- [List any assumptions that should be validated]
- [Areas where clarification might be needed]
```

### 3. Handoff Execution Steps

#### **Pre-Handoff Checklist**

1. [ ] Complete current atomic work unit (don't leave broken state)
2. [ ] Update task/subtask status in Taskmaster
3. [ ] Commit or stash any code changes with descriptive messages
4. [ ] Document any temporary workarounds or incomplete implementations
5. [ ] Test current implementation state

#### **Context Transfer Process**

1. **Generate Handoff Report**: Use the template above
2. **Validate Completeness**: Ensure all critical information is captured
3. **Create Transition Artifacts**:
   - Update task context files with latest findings
   - Create summary comments in code if needed
   - Document any temporary states or configurations

#### **Receiving Agent Onboarding**

When receiving a handoff:

1. [ ] **Read Handoff Report**: Thoroughly review all sections
2. [ ] **Verify Environment**: Confirm system state matches documentation
3. [ ] **Review Code Changes**: Understand modifications made
4. [ ] **Validate Context**: Ensure task/subtask context is current
5. [ ] **Confirm Next Steps**: Verify understanding of immediate priorities
6. [ ] **Test Current State**: Run tests to confirm starting point
7. [ ] **Ask Clarifying Questions**: If any context is unclear

### 4. Best Practices

#### **Information Capture**

- **Be Comprehensive**: Include more context rather than less
- **Be Specific**: Use exact file paths, function names, and line numbers
- **Be Current**: Ensure all information reflects the latest state
- **Be Actionable**: Provide clear next steps, not just status updates

#### **Communication**

- **Use Standard Terminology**: Follow project conventions and naming
- **Provide Rationale**: Explain the "why" behind decisions
- **Flag Uncertainties**: Clearly mark assumptions or areas needing validation
- **Include Examples**: Code snippets, commands, or configuration examples

#### **State Management**

- **Clean Handoff**: Don't transfer broken or inconsistent states
- **Document Workarounds**: Explain any temporary solutions
- **Preserve Options**: Don't close off alternative approaches unnecessarily
- **Maintain Traceability**: Link back to original requirements and decisions

## Emergency Handoff Protocol

For urgent or unexpected handoffs:

### **Minimal Context Transfer**

1. **Current Focus**: What were you working on right now?
2. **Immediate Blocker**: What's preventing progress?
3. **Critical State**: Any running processes or temporary configurations?
4. **Next Action**: What's the single most important next step?
5. **Risk Warning**: Any critical risks or breaking changes in progress?

### **Quick Reference Format**

```
URGENT HANDOFF
Focus: [One-line description]
Blocker: [Primary obstacle]
State: [Critical system state info]
Next: [Immediate action needed]
Risk: [Any critical warnings]
Files: [Key files to examine]
```

## Integration with Project Workflows

### **Taskmaster Integration**

- Always update task/subtask status before handoff
- Use `update_subtask` to log handoff information
- Reference task context documents in handoff report

### **Git Integration**

- Commit work with descriptive messages before handoff
- Use branch names that reflect the work context
- Tag handoff points for easy reference

### **Documentation Integration**

- Update relevant documentation with findings
- Create or update context files as needed
- Link to external resources discovered during work

## Common Handoff Scenarios

### **Planned Session End**

- Complete current work unit
- Update all tracking systems
- Prepare comprehensive handoff report
- Test final state

### **Expertise Transfer**

- Focus on domain knowledge transfer
- Provide background on technical decisions
- Share relevant learning resources
- Establish communication channel for questions

### **Workflow Transition**

- Explain workflow stage transition
- Provide next-stage requirements
- Transfer relevant artifacts
- Update process tracking

### **Emergency Handoff**

- Prioritize safety and stability
- Document critical risks
- Provide minimal viable context
- Establish urgent communication channel

This handoff protocol ensures that critical context, decisions, and state information are preserved across agent transitions, maintaining productivity and preventing rework or missed requirements.
