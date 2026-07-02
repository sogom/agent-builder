# Skill Name

## Purpose

한 문장으로 작성한다.

## Called When

- 

## Not Called When

- 

## Required Inputs

```yaml
required:
  - 
```

## Optional Inputs

```yaml
optional:
  - 
```

## Outputs

```yaml
output:
  status:
  result:
  limitations:
  assumptions:
```

## Preconditions

- 

## Procedure

1. 
2. 
3. 

## Tools

- 

## Permissions

### Allowed

- 

### Approval Required

- 

### Prohibited

- 

## Applicable Rules

- 전달받은 `Applicable Rule Set`을 따른다.
- 프로젝트 전용 규칙을 스킬 내부에 하드코딩하지 않는다.

## Dependencies

### Required

- 

### Optional

- 

### Conditional

- 

## Success Conditions

- 

## Failure States

- `PARTIAL`
- `NEEDS_CLARIFICATION`
- `NEEDS_APPROVAL`
- `FAILED`

## Failure Handling

- 

## Result Schema

```yaml
status: SUCCESS | PARTIAL | NEEDS_CLARIFICATION | NEEDS_APPROVAL | FAILED
result:
limitations: []
assumptions: []
unresolved: []
suggested_question:
requested_action:
```

## Validation Scenarios

### Normal

- Input:
- Expected:

### Missing Required Input

- Input:
- Expected:

### Tool Failure

- Input:
- Expected:

### Permission Required

- Input:
- Expected:
