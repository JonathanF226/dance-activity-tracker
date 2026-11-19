# Requirements

Scope: Feature 1 only (Record a Dance Session). History and statistics requirements will be added when those features are started.

## Feature 1: Record a Dance Session

| ID | Requirement |
|---|---|
| REQ-001 | A session records: dance style, date, duration in minutes, and session type. |
| REQ-002 | Dance style must be one of: Cumbia, Salsa, Bachata, Merengue, Other. |
| REQ-003 | Dance style input is case-insensitive and surrounding whitespace is ignored; it is stored in standard form (e.g. "salsa" becomes "Salsa"). |
| REQ-004 | Date must be in `YYYY-MM-DD` format and be a real calendar date. |
| REQ-005 | Date must not be in the future. |
| REQ-006 | Duration must be a whole number of minutes. |
| REQ-007 | Duration minimum is 1 minute; values of 0 or less are rejected. |
| REQ-008 | Duration maximum is 480 minutes (8 hours); larger values are rejected. |
| REQ-009 | Session type must be `class` or `practice` (case-insensitive). |
| REQ-010 | A missing or empty field is rejected. |
| REQ-011 | Every rejection produces a clear error message naming the invalid field. |

## Open items (deferred)

- Definition of a "week" for weekly totals (Feature 3).
- Persistence (SQLite) decision.
