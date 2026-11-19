# Test Plan

Scope: Feature 1 only (Record a Dance Session). Covers REQ-001 to REQ-011 in [requirements.md](requirements.md).

## Objectives
- Verify a valid session can be recorded.
- Verify every invalid input is rejected with a clear error naming the field.
- Verify values at the limits of each rule behave correctly.

## Test types
| Type | Applies to |
|---|---|
| Functional | Recording valid sessions (REQ-001, REQ-002, REQ-003, REQ-009) |
| Input validation | Bad, missing or wrongly typed input (REQ-004, REQ-006, REQ-010, REQ-011) |
| Boundary | Duration 0/1/480/481; date today/tomorrow (REQ-005, REQ-007, REQ-008) |
| Regression | Full suite is rerun after every defect fix |

## Approach
- Test cases are defined in [test-cases.md](test-cases.md), each traced to a requirement.
- Automated with pytest: `tests/test_dance_session.py` (valid sessions) and `tests/test_validation.py` (rejections and boundaries).
- Run with `pytest --cov=src`.
- Failures are logged in `defect-reports.md` with ID, description, steps, expected, actual, severity and status (Open / Fixed / Verified).

## Entry / exit criteria
- Entry: requirements reviewed; `dance_session.py` implemented.
- Exit: all Feature 1 test cases executed; no Open defects of High severity; fixed defects verified and the full suite rerun.

## Out of scope (for now)
History (Feature 2), statistics (Feature 3), persistence, CLI, CI.
