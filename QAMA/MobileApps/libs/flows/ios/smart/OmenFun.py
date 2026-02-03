"""
methods.py
Action methods for OMEN Gaming Hub
"""

from locators import OmenLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OmenMethods:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def launch_omen_app(self):
        """
        Step: Launch OMEN Gaming Hub
        """
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, OmenLocators.OMEN_MAIN_WINDOW)
            )
        )

    def wait_for_dashboard(self):
        """
        Step: Wait for dashboard to load
        """
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, OmenLocators.DASHBOARD_PANEL)
            )
        )

    def open_performance_control(self):
        """
        Step: Click on Performance Control tab
        """
        tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, OmenLocators.PERFORMANCE_CONTROL_TAB)
            )
        )
        tab.click()

    def verify_system_stats_displayed(self):
        """
        Step: Verify system stats are displayed
        """
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, OmenLocators.SYSTEM_STATS_PANEL)
            )
        )
