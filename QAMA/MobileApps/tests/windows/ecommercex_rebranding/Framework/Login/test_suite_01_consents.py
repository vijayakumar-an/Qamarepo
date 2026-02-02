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
