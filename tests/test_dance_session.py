"""Functional tests: valid sessions (TC-001 to TC-006)."""

from datetime import date

import pytest

from src.dance_session import DanceSession


def test_tc001_record_cumbia_session():
    s = DanceSession.create("Cumbia", "2025-01-15", 60, "class")
    assert s.style == "Cumbia"
    assert s.date == date(2025, 1, 15)
    assert s.duration == 60
    assert s.session_type == "class"


@pytest.mark.parametrize("style", ["Salsa", "Bachata", "Merengue", "Other"])
def test_tc002_all_styles_accepted(style):
    assert DanceSession.create(style, "2025-01-15", 30, "class").style == style


def test_tc003_style_case_insensitive():
    assert DanceSession.create("salsa", "2025-01-15", 30, "class").style == "Salsa"


def test_tc004_style_whitespace_ignored():
    assert DanceSession.create("  BACHATA  ", "2025-01-15", 30, "class").style == "Bachata"


def test_tc005_practice_type_accepted():
    assert DanceSession.create("Salsa", "2025-01-15", 30, "practice").session_type == "practice"


def test_tc006_type_case_insensitive():
    assert DanceSession.create("Salsa", "2025-01-15", 30, "CLASS").session_type == "class"
