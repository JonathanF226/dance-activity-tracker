# Defect Reports

Found by exploratory testing of Feature 1 after all planned test cases (TC-001 to TC-038) passed.
Regression tests for each defect are in `tests/test_validation.py`.

## DEF-001: Underscore accepted in duration

| | |
|---|---|
| Requirement | REQ-006 (duration must be a whole number) |
| Severity | Low |
| Status | Verified |

**Description:** Python's `int()` treats underscores as digit separators, so `"6_0"` is accepted as 60.

**Steps to reproduce:**
1. Call `DanceSession.create("Salsa", "2025-01-15", "6_0", "class")`.

**Expected:** Rejected with an error naming `duration`.
**Actual:** Accepted; duration stored as 60.

**Fix:** Duration text must match `[+-]?[0-9]+` before conversion.
**Verification:** `test_def001_underscore_in_duration_rejected` fails before the fix and passes after; full suite rerun.

## DEF-002: Non-ASCII digits accepted in duration

| | |
|---|---|
| Requirement | REQ-006 |
| Severity | Low |
| Status | Verified |

**Description:** `int()` accepts any Unicode decimal digit, so full-width `"１２０"` is accepted as 120.

**Steps to reproduce:**
1. Call `DanceSession.create("Salsa", "2025-01-15", "１２０", "class")`.

**Expected:** Rejected with an error naming `duration`.
**Actual:** Accepted; duration stored as 120.

**Fix:** Same ASCII-only pattern as DEF-001.
**Verification:** `test_def002_non_ascii_digits_in_duration_rejected` fails before, passes after; full suite rerun.

## DEF-003: Very large duration gives a misleading error

| | |
|---|---|
| Requirement | REQ-008, REQ-011 (clear message) |
| Severity | Low |
| Status | Verified |

**Description:** A duration string of thousands of digits exceeds Python's integer-conversion limit, so the code reports "must be a whole number of minutes" instead of the maximum-duration message.

**Steps to reproduce:**
1. Call `DanceSession.create("Salsa", "2025-01-15", "9" * 5000, "class")`.

**Expected:** Rejected with the message that duration must be at most 480 minutes.
**Actual:** Rejected, but the message says it must be a whole number (it is one).

**Fix:** A digit string that is too long to convert is reported as exceeding the maximum.
**Verification:** `test_def003_huge_duration_reports_maximum` fails before, passes after; full suite rerun.

## Observations (not logged as defects)

- `"+60"` is accepted as 60. The requirements don't forbid a leading plus; left as is.
- Dates with surrounding whitespace (`" 2025-01-15 "`) are accepted. REQ-003 only promises whitespace handling for style; left as is.
