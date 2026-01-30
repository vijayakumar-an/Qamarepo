import pytest
from ecommerce.apps.windows.flows.flow_container import FlowContainer


# -----------------------------
# Pytest CLI options
# -----------------------------

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against (qa / staging / prod)"
    )

    parser.addoption(
        "--browser",
        action="store",
        default="windows",
        help="Platform or browser (windows / web)"
    )


# -----------------------------
# Session-level fixtures
# -----------------------------

@pytest.fixture(scope="session")
def test_environment(request):
    """
    Returns the test environment (qa/staging/prod)
    """
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def platform(request):
    """
    Returns platform or browser type
    """
    return request.config.getoption("--browser")


# -----------------------------
# Driver fixture (Dummy)
# -----------------------------

@pytest.fixture(scope="class")
def windows_test_setup(request, platform):
    """
    Initialize and teardown Windows application driver
    Dummy implementation
    """
    driver = None

    if platform == "windows":
        # Initialize WinAppDriver / Desktop driver here
        # driver = WindowsDriver(...)
        driver = "DUMMY_WINDOWS_DRIVER"

    yield driver

    # Teardown
    if driver:
        # driver.quit()
        pass


# -----------------------------
# FlowContainer fixture
# -----------------------------

@pytest.fixture(scope="class")
def flow_container(windows_test_setup):
    """
    Provides FlowContainer instance
    """
    return FlowContainer(windows_test_setup)


# -----------------------------
# Common class-level fixture
# -----------------------------

@pytest.fixture(scope="class")
def class_setup_fixture(request, windows_test_setup):
    """
    Common setup fixture used across test suites
    """
    request.cls.driver = windows_test_setup
    request.cls.fc = FlowContainer(windows_test_setup)

    yield

    # Global teardown
    if windows_test_setup:
        request.cls.fc.close_application()


# -----------------------------
# Function-level cleanup
# -----------------------------

@pytest.fixture(scope="function", autouse=True)
def function_cleanup():
    """
    Runs after every test function
    """
    yield
    # Add cleanup steps if needed (logout, reset state, etc.)
