"""
locators.py
Windows UI Automation locators for OMEN Gaming Hub
"""

class OmenLocators:
    # Main application window
    OMEN_MAIN_WINDOW = "//Window[contains(@Name,'OMEN')]"

    # Dashboard loaded indicator
    DASHBOARD_PANEL = "//Pane[contains(@Name,'Dashboard')]"

    # Performance Control tab
    PERFORMANCE_CONTROL_TAB = (
        "//TabItem[contains(@Name,'Performance')]"
    )

    # System stats section
    SYSTEM_STATS_PANEL = (
        "//Pane[contains(@Name,'System') or contains(@Name,'Performance')]"
    )
