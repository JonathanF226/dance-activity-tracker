"""Input validation and boundary tests (TC-010 to TC-038)."""

from datetime import date, timedelta

import pytest

from src.dance_session import DanceSession, ValidationError

GOOD = dict(style="Salsa", date="2025-01-15", duration=60, session_type="class")


def make(**overrides):
    return DanceSession.create(**{**GOOD, **overrides})


# (test case, field kwarg, bad value, field name expected in the error)
REJECTED = [
    ("TC-010", "style", "Tango", "style"),
    ("TC-011", "style", "", "style"),
    ("TC-012", "style", None, "style"),
    ("TC-013", "date", "2025/01/15", "date"),
    ("TC-014", "date", "15-01-2025", "date"),
    ("TC-015", "date", "2025-02-30", "date"),
    ("TC-016", "date", "", "date"),
    ("TC-017", "duration", "abc", "duration"),
    ("TC-018", "duration", "30.5", "duration"),
    ("TC-019", "duration", "-5", "duration"),
    ("TC-020", "duration", "", "duration"),
    ("TC-021", "session_type", "lesson", "session type"),
    ("TC-022", "session_type", "", "session type"),
    ("TC-030", "duration", 0, "duration"),
    ("TC-033", "duration", 481, "duration"),
    ("TC-038", "date", "2025-02-29", "date"),
]


@pytest.mark.parametrize("tc,field,value,named", REJECTED, ids=[r[0] for r in REJECTED])
def test_rejected_input_names_the_field(tc, field, value, named):
    # Covers TC-023 (REQ-011): the error message names the invalid field.
    with pytest.raises(ValidationError) as exc:
        make(**{field: value})
    assert exc.value.field == named
    assert named in str(exc.value)


def test_tc018_float_duration_rejected():
    with pytest.raises(ValidationError):
        make(duration=30.5)


def test_tc031_minimum_duration_accepted():
    assert make(duration=1).duration == 1


def test_tc032_maximum_duration_accepted():
    assert make(duration=480).duration == 480


def test_tc034_today_accepted():
    assert make(date=date.today().isoformat()).date == date.today()


def test_tc035_tomorrow_rejected():
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    with pytest.raises(ValidationError) as exc:
        make(date=tomorrow)
    assert exc.value.field == "date"


def test_tc036_yesterday_accepted():
    yesterday = date.today() - timedelta(days=1)
    assert make(date=yesterday.isoformat()).date == yesterday


def test_tc037_leap_day_accepted():
    assert make(date="2024-02-29").date == date(2024, 2, 29)


# --- Defects found during exploratory testing (see docs/defect-reports.md) ---


def test_def001_underscore_in_duration_rejected():
    with pytest.raises(ValidationError) as exc:
        make(duration="6_0")
    assert exc.value.field == "duration"


def test_def002_non_ascii_digits_in_duration_rejected():
    with pytest.raises(ValidationError) as exc:
        make(duration="１２０")  # full-width digits
    assert exc.value.field == "duration"


def test_def003_huge_duration_reports_maximum():
    with pytest.raises(ValidationError) as exc:
        make(duration="9" * 5000)
    assert "at most 480" in str(exc.value)
