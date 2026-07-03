# Project Rules

## Rule Priority

```text
Safety, security, and legal constraints
> Current user request
> Task-specific rules
> Project rules
> Organization rules
> Agent defaults
> Skill defaults
```

## Coding Rules

-

## Architecture Rules

-

## Testing Rules

-

## Documentation Rules

-

## Security Rules

- Do not print or persist secrets.
- Do not make production changes without explicit approval.

## Approval Required

- Package installation or removal
- Lock file generation or large regeneration
- Database schema changes
- Authentication, authorization, or deployment changes
- CI/CD changes
- Public API breaking changes

## Prohibited By Default

- Production deployment
- Storing real secret values
- External write operations
- Large restructuring without user approval

## Rule Sources

-

## Conflict Handling

- If rules conflict and the result materially changes architecture, permissions, or safety, return `NEEDS_CLARIFICATION`.
