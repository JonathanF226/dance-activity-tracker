# Test Cases: Feature 1 (Record a Dance Session)

Executed 2026-11-18 with `pytest` (automated). All 29 planned cases pass. Three further defects were found by exploratory testing; see [defect-reports.md](defect-reports.md).

## Functional (valid input)

| ID | Req | Input (style, date, duration, type) | Expected | Result |
|---|---|---|---|---|
| TC-001 | 001, 002 | Cumbia, 2025-01-15, 60, class | Session recorded with those values | Pass |
| TC-002 | 002 | Each of Salsa, Bachata, Merengue, Other | Each accepted | Pass |
| TC-003 | 003 | `salsa` | Stored as `Salsa` | Pass |
| TC-004 | 003 | `  BACHATA  ` | Stored as `Bachata` | Pass |
| TC-005 | 009 | type `practice` | Accepted | Pass |
| TC-006 | 009 | type `CLASS` | Accepted, stored as `class` | Pass |

## Input validation (invalid input)

| ID | Req | Field | Input | Expected | Result |
|---|---|---|---|---|---|
| TC-010 | 002 | style | `Tango` | Rejected, error names style | Pass |
| TC-011 | 010 | style | `` (empty) | Rejected, error names style | Pass |
| TC-012 | 010 | style | `None` / missing | Rejected, error names style | Pass |
| TC-013 | 004 | date | `2025/01/15` | Rejected, error names date | Pass |
| TC-014 | 004 | date | `15-01-2025` | Rejected, error names date | Pass |
| TC-015 | 004 | date | `2025-02-30` (not a real date) | Rejected, error names date | Pass |
| TC-016 | 010 | date | `` (empty) | Rejected, error names date | Pass |
| TC-017 | 006 | duration | `abc` | Rejected, error names duration | Pass |
| TC-018 | 006 | duration | `30.5` | Rejected, error names duration | Pass |
| TC-019 | 007 | duration | `-5` | Rejected, error names duration | Pass |
| TC-020 | 010 | duration | `` (empty) | Rejected, error names duration | Pass |
| TC-021 | 009 | type | `lesson` | Rejected, error names session type | Pass |
| TC-022 | 010 | type | `` (empty) | Rejected, error names session type | Pass |
| TC-023 | 011 | any | Any rejection above | Message is clear and names the invalid field | Pass |

## Boundary

| ID | Req | Field | Input | Expected | Result |
|---|---|---|---|---|---|
| TC-030 | 007 | duration | `0` | Rejected | Pass |
| TC-031 | 007 | duration | `1` | Accepted (minimum) | Pass |
| TC-032 | 008 | duration | `480` | Accepted (maximum) | Pass |
| TC-033 | 008 | duration | `481` | Rejected | Pass |
| TC-034 | 005 | date | today | Accepted | Pass |
| TC-035 | 005 | date | tomorrow | Rejected | Pass |
| TC-036 | 005 | date | yesterday | Accepted | Pass |
| TC-037 | 004 | date | `2024-02-29` (leap day) | Accepted | Pass |
| TC-038 | 004 | date | `2025-02-29` (not a leap year) | Rejected | Pass |

## Traceability

| Requirement | Test cases |
|---|---|
| REQ-001 | TC-001 |
| REQ-002 | TC-001, TC-002, TC-010 |
| REQ-003 | TC-003, TC-004 |
| REQ-004 | TC-013, TC-014, TC-015, TC-037, TC-038 |
| REQ-005 | TC-034, TC-035, TC-036 |
| REQ-006 | TC-017, TC-018 |
| REQ-007 | TC-019, TC-030, TC-031 |
| REQ-008 | TC-032, TC-033 |
| REQ-009 | TC-005, TC-006, TC-021 |
| REQ-010 | TC-011, TC-012, TC-016, TC-020, TC-022 |
| REQ-011 | TC-023 (and the error checks in every rejection case) |
