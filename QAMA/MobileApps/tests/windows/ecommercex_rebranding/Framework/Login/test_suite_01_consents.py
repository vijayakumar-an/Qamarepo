# Dummy placeholder for test_suite_01_consents.py
import pytest
from ecommerce.apps.windows.flows.flow_container import FlowContainer


@pytest.mark.usefixtures("class_setup_fixture")
class Test_Login:
    """
    E-Commerce Login Test Suite
    """

    @pytest.mark.smoke
    def test_login_with_valid_credentials(self):
        """
        Verify user can log in with valid credentials
        """
        self.fc.launch_app_and_skip_onboarding()

        self.fc.home.verify_home_page_loaded()
        self.fc.profile.click_login_register_btn()

        self.fc.login.verify_login_page_loaded()
        self.fc.login.enter_email("user@test.com")
        self.fc.login.enter_password("Password123")
        self.fc.login.click_login()

        assert self.fc.home.verify_user_logged_in(), "User login failed"

    @pytest.mark.regression
    def test_login_with_invalid_password(self):
        """
        Verify error message is shown for invalid password
        """
        self.fc.launch_app_and_skip_onboarding()

        self.fc.profile.click_login_register_btn()
        self.fc.login.verify_login_page_loaded()

        self.fc.login.enter_email("user@test.com")
        self.fc.login.enter_password("WrongPassword")
        self.fc.login.click_login()

        assert self.fc.login.verify_login_error_message(), \
            "Error message not displayed"

    @pytest.mark.regression
    def test_navigate_to_create_account_from_login(self):
        """
        Verify navigation to create account from login screen
        """
        self.fc.launch_app_and_skip_onboarding()

        self.fc.profile.click_login_register_btn()
        self.fc.login.verify_login_page_loaded()

        self.fc.login.click_create_account_link()
        assert self.fc.login.verify_create_account_page(), \
            "Create account page not displayed"
