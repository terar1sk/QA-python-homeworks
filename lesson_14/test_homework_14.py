import logging
import pytest

from lesson_14.homework_14 import log_event


def test_success_logs_info(caplog):
    with caplog.at_level(logging.INFO):
        log_event("user1", "success")
    assert "Username: user1" in caplog.text
    assert "Status: success" in caplog.text
    assert caplog.records[0].levelname == "INFO"


def test_expired_logs_warning(caplog):
    with caplog.at_level(logging.WARNING):
        log_event("user2", "expired")
    assert "Status: expired" in caplog.text
    assert caplog.records[0].levelname == "WARNING"


def test_failed_logs_error(caplog):
    with caplog.at_level(logging.ERROR):
        log_event("user3", "failed")
    assert "Status: failed" in caplog.text
    assert caplog.records[0].levelname == "ERROR"


def test_unknown_status_logs_error(caplog):
    with caplog.at_level(logging.ERROR):
        log_event("user4", "unknown")
    assert "Status: unknown" in caplog.text
    assert caplog.records[0].levelname == "ERROR"


def test_message_format(caplog):
    with caplog.at_level(logging.INFO):
        log_event("admin", "success")
    assert "Login event" in caplog.text