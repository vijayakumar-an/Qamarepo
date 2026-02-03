"""
conftest.py
PyTest configuration for Windows OMEN automation
"""

import pytest
from appium import webdriver


@pytest.fixture(scope="session")
def windows_driver():
    desired_caps = {
        "platformName": "Windows",
        "deviceName": "WindowsPC",
        "app": "Root"  # Attaches to desktop session
    }

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        desired_capabilities=desired_caps
    )

    yield driver

    driver.quit()
