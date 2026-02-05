import pytest
import time

from methods.omen_methods import OmenMethods


@pytest.fixture(scope="session")
def omen_session():
    """
    Session-level fixture
    - Starts OMEN Gaming Hub once
    - Closes OMEN after all tests complete
    """

    omen = OmenMethods()

    # -------------------------
    # SETUP (Session Start)
    # -------------------------
    omen.launch_omen_app()
    omen.verify_omen_launched()
    omen.wait_for_app_to_load()

    yield omen

    # -------------------------
    # TEARDOWN (Session End)
    # -------------------------
    omen.close_omen_app()


@pytest.fixture(scope="function")
def omen_test_setup(omen_session):
    """
    Function-level fixture
    - Ensures clean state before each test
    - Returns to dashboard
    """

    # -------------------------
    # PRE-CONDITION
    # -------------------------
    omen_session.verify_omen_launched()
    omen_session.verify_dashboard_loaded()

    yield omen_session

    # -------------------------
    # POST-CONDITION
    # -------------------------
    # Small delay to stabilize UI before next test
    time.sleep(2)
