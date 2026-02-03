class OmenXPaths:

    # ===============================
    # Application / Window
    # ===============================
    OMEN_MAIN_WINDOW = "//Window[@Name='OMEN Gaming Hub']"
    OMEN_LOADING_SPINNER = "//ProgressBar[@AutomationId='LoadingSpinner']"

    # ===============================
    # Dashboard
    # ===============================
    DASHBOARD_VIEW = "//Pane[@AutomationId='DashboardView']"
    DASHBOARD_WIDGET = "//Pane[contains(@AutomationId,'DashboardWidget')]"

    # ===============================
    # Navigation Tabs
    # ===============================
    TAB_PERFORMANCE_CONTROL = "//TabItem[@Name='Performance Control']"
    TAB_MY_GAMES = "//TabItem[@Name='My Games']"
    TAB_LIGHTING = "//TabItem[@Name='Lighting']"
    TAB_SETTINGS = "//TabItem[@Name='Settings']"

    # ===============================
    # Performance Control
    # ===============================
    PERFORMANCE_VIEW = "//Pane[@AutomationId='PerformanceView']"

    CPU_USAGE_VALUE = "//Text[@AutomationId='CpuUsageValue']"
    GPU_USAGE_VALUE = "//Text[@AutomationId='GpuUsageValue']"
    MEMORY_USAGE_VALUE = "//Text[@AutomationId='MemoryUsageValue']"
    TEMPERATURE_VALUE = "//Text[@AutomationId='TemperatureValue']"

    PERFORMANCE_MODE_DROPDOWN = "//ComboBox[@AutomationId='PerformanceModeDropdown']"
    PERFORMANCE_MODE_BALANCED = "//ListItem[@Name='Balanced']"
    PERFORMANCE_MODE_PERFORMANCE = "//ListItem[@Name='Performance']"
    PERFORMANCE_MODE_ECO = "//ListItem[@Name='Eco']"

    # ===============================
    # Games
    # ===============================
    GAME_LIBRARY_VIEW = "//Pane[@AutomationId='GameLibraryView']"
    GAME_TILE = "//ListItem[contains(@AutomationId,'GameTile')]"
    GAME_PLAY_BUTTON = ".//Button[@Name='Play']"
    GAME_RUNNING_STATUS = "//Text[@AutomationId='GameRunningStatus']"

    # ===============================
    # Lighting
    # ===============================
    LIGHTING_VIEW = "//Pane[@AutomationId='LightingView']"
    KEYBOARD_DEVICE = "//ListItem[@Name='Keyboard']"
    COLOR_PICKER = "//Button[@AutomationId='ColorPicker']"
    APPLY_LIGHTING_BUTTON = "//Button[@Name='Apply']"

    # ===============================
    # Settings
    # ===============================
    SETTINGS_VIEW = "//Pane[@AutomationId='SettingsView']"

    THEME_DROPDOWN = "//ComboBox[@AutomationId='ThemeDropdown']"
    THEME_DARK = "//ListItem[@Name='Dark']"
    THEME_LIGHT = "//ListItem[@Name='Light']"

    NOTIFICATION_TOGGLE = "//ToggleSwitch[@AutomationId='NotificationToggle']"
    STARTUP_TOGGLE = "//ToggleSwitch[@AutomationId='StartupLaunchToggle']"

    # ===============================
    # Update
    # ===============================
    UPDATE_BANNER = "//Pane[@AutomationId='UpdateBanner']"
    UPDATE_BUTTON = "//Button[@Name='Update']"

    # ===============================
    # Offline / Warnings
    # ===============================
    OFFLINE_WARNING = "//Text[contains(@Name,'offline')]"
