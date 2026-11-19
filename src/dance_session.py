"""Feature 1: Record a Dance Session (REQ-001 to REQ-011)."""

import re
from dataclasses import dataclass
from datetime import date, datetime

VALID_STYLES = ("Cumbia", "Salsa", "Bachata", "Merengue", "Other")
VALID_TYPES = ("class", "practice")
MIN_DURATION = 1
MAX_DURATION = 480


class ValidationError(ValueError):
    """Raised when a session field is invalid. `field` names the field (REQ-011)."""

    def __init__(self, field, message):
        self.field = field
        super().__init__(f"Invalid {field}: {message}")


def _require_text(field, value):
    """Return stripped text, rejecting missing/empty/non-text input (REQ-010)."""
    if value is None or not isinstance(value, str) or not value.strip():
        raise ValidationError(field, "a value is required")
    return value.strip()


def validate_style(value):
    text = _require_text("style", value)
    for style in VALID_STYLES:
        if style.lower() == text.lower():
            return style
    raise ValidationError("style", f"must be one of: {', '.join(VALID_STYLES)}")


def validate_date(value, today=None):
    text = _require_text("date", value)
    try:
        parsed = datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError("date", "must be a real date in YYYY-MM-DD format")
    # strptime accepts e.g. "2025-1-5"; require the exact zero-padded form.
    if parsed.isoformat() != text:
        raise ValidationError("date", "must be a real date in YYYY-MM-DD format")
    if parsed > (today or date.today()):
        raise ValidationError("date", "must not be in the future")
    return parsed


def validate_duration(value):
    if value is None or isinstance(value, bool) or isinstance(value, float):
        raise ValidationError("duration", "must be a whole number of minutes")
    if isinstance(value, str):
        text = _require_text("duration", value)
        # ASCII digits only: int() alone also accepts "6_0" and full-width digits.
        if not re.fullmatch(r"[+-]?[0-9]+", text):
            raise ValidationError("duration", "must be a whole number of minutes")
        try:
            minutes = int(text)
        except ValueError:  # digit string too long for Python to convert
            if text.startswith("-"):
                raise ValidationError("duration", f"must be at least {MIN_DURATION} minute")
            raise ValidationError("duration", f"must be at most {MAX_DURATION} minutes")
    elif isinstance(value, int):
        minutes = value
    else:
        raise ValidationError("duration", "must be a whole number of minutes")
    if minutes < MIN_DURATION:
        raise ValidationError("duration", f"must be at least {MIN_DURATION} minute")
    if minutes > MAX_DURATION:
        raise ValidationError("duration", f"must be at most {MAX_DURATION} minutes")
    return minutes


def validate_session_type(value):
    text = _require_text("session type", value).lower()
    if text not in VALID_TYPES:
        raise ValidationError("session type", "must be 'class' or 'practice'")
    return text


@dataclass(frozen=True)
class DanceSession:
    style: str
    date: date
    duration: int
    session_type: str

    @classmethod
    def create(cls, style, date, duration, session_type, today=None):
        """Validate raw input and build a session. Raises ValidationError."""
        return cls(
            style=validate_style(style),
            date=validate_date(date, today=today),
            duration=validate_duration(duration),
            session_type=validate_session_type(session_type),
        )
