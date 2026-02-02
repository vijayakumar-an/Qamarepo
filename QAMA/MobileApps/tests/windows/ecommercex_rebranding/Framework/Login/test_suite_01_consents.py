<<<<<<< HEAD
# test_suite_generic_actions.py

import pytest
from ecommerce.apps.windows.flows.flow_container import FlowContainer


@pytest.mark.usefixtures("class_setup_fixture")
class Test_Generic_Ecommerce_Actions:
    """
    E-Commerce Generic Test Suite
    (Derived strictly from provided test cases)
    """

    @pytest.mark.smoke
    def test_tc_2801(self):
        """
        Test Case 2801:
        1. Open app
        2. Perform action 1
        3. Verify response
        """
        self.fc.generic_action.open_application()
        self.fc.generic_action.perform_action(1)

        assert self.fc.generic_action.verify_response_displayed(), \
            "Response not displayed for action 1"

    @pytest.mark.regression
    def test_tc_2802(self):
        """
        Test Case 2802:
        1. Open app
        2. Perform action 2
        3. Verify response
        """
        self.fc.generic_action.open_application()
        self.fc.generic_action.perform_action(2)

        assert self.fc.generic_action.verify_response_displayed(), \
            "Response not displayed for action 2"

    @pytest.mark.regression
    def test_tc_2803(self):
        """
        Test Case 2803:
        1. Open app
        2. Perform action 3
        3. Verify response
        """
        self.fc.generic_action.open_application()
        self.fc.generic_action.perform_action(3)

        assert self.fc.generic_action.verify_response_displayed(), \
            "Response not displayed for action 3"
=======
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
>>>>>>> 280f6387fc1f52fd5800e97681be3e1d528d1965
