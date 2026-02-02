# Dummy placeholder for test_suite_01_notifications.py
import pytest
from ecommerce.apps.windows.flows.flow_container import FlowContainer


@pytest.mark.usefixtures("class_setup_fixture")
class Test_Notifications:
    """
    E-Commerce Notifications Test Suite
    """

    @pytest.mark.smoke
    def test_open_notifications_panel(self):
        """
        Verify notifications panel opens successfully
        """
        self.fc.launch_app_and_skip_onboarding()

        self.fc.home.verify_home_page_loaded()
        self.fc.notifications.click_notifications_icon()

        assert self.fc.notifications.verify_notifications_panel_opened(), \
            "Notifications panel did not open"

    @pytest.mark.regression
    def test_mark_all_notifications_as_read(self):
        """
        Verify user can mark all notifications as read
        """
        self.fc.launch_app_and_skip_onboarding()

        self.fc.notifications.click_notifications_icon()
        self.fc.notifications.verify_notifications_panel_opened()

        self.fc.notifications.click_mark_all_as_read()

        assert self.fc.notifications.verify_no_unread_notifications(), \
            "Unread notifications still present"

    @pytest.mark.regression
    def test_clear_all_notifications(self):
        """
        Verify user can clear all notifications
        """
        self.fc.launch_app_and_skip_onboarding()

        self.fc.notifications.click_notifications_icon()
        self.fc.notifications.verify_notifications_panel_opened()

        self.fc.notifications.click_clear_all_notifications()

        assert self.fc.notifications.verify_empty_notifications_message(), \
            "Notifications were not cleared"

    @pytest.mark.regression
    def test_notification_navigation_to_orders(self):
        """
        Verify clicking order notification navigates to orders page
        """
        self.fc.launch_app_and_skip_onboarding()

        self.fc.notifications.click_notifications_icon()
        self.fc.notifications.verify_notifications_panel_opened()

        self.fc.notifications.click_order_notification()

        assert self.fc.home.verify_orders_page_loaded(), \
            "User was not navigated to Orders page"
