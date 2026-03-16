import logging
import pytest
import allure

from lesson_14.homework_14 import log_event


@allure.feature("Login Event Logging")
class TestLogEvent:

    @allure.title("Success status logs at INFO level")
    def test_success_logs_info(self, caplog):
        with allure.step("Call log_event with status='success'"):
            with caplog.at_level(logging.INFO):
                log_event("user1", "success")
        with allure.step("Check log contains username"):
            assert "Username: user1" in caplog.text
        with allure.step("Check log contains status"):
            assert "Status: success" in caplog.text
        with allure.step("Check log level is INFO"):
            assert caplog.records[0].levelname == "INFO"

    @allure.title("Expired status logs at WARNING level")
    def test_expired_logs_warning(self, caplog):
        with allure.step("Call log_event with status='expired'"):
            with caplog.at_level(logging.WARNING):
                log_event("user2", "expired")
        with allure.step("Check log contains status"):
            assert "Status: expired" in caplog.text
        with allure.step("Check log level is WARNING"):
            assert caplog.records[0].levelname == "WARNING"

    @allure.title("Failed status logs at ERROR level")
    def test_failed_logs_error(self, caplog):
        with allure.step("Call log_event with status='failed'"):
            with caplog.at_level(logging.ERROR):
                log_event("user3", "failed")
        with allure.step("Check log contains status"):
            assert "Status: failed" in caplog.text
        with allure.step("Check log level is ERROR"):
            assert caplog.records[0].levelname == "ERROR"

    @allure.title("Unknown status logs at ERROR level")
    def test_unknown_status_logs_error(self, caplog):
        with allure.step("Call log_event with status='unknown'"):
            with caplog.at_level(logging.ERROR):
                log_event("user4", "unknown")
        with allure.step("Check log contains status"):
            assert "Status: unknown" in caplog.text
        with allure.step("Check log level is ERROR"):
            assert caplog.records[0].levelname == "ERROR"

    @allure.title("Log message contains 'Login event' prefix")
    def test_message_format(self, caplog):
        with allure.step("Call log_event with user 'admin'"):
            with caplog.at_level(logging.INFO):
                log_event("admin", "success")
        with allure.step("Check log contains 'Login event'"):
            assert "Login event" in caplog.text