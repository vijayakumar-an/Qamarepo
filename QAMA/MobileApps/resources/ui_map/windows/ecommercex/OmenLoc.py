class OmenLocators:

    # =========================
    # Application / Window
    # =========================
    OMEN_MAIN_WINDOW = "//Window[@Name='OMEN Gaming Hub']"
    LOADING_SPINNER = "//ProgressBar[contains(@AutomationId,'Loading')]"

    # =========================
    # Dashboard
    # =========================
    DASHBOARD_VIEW = "//Pane[@AutomationId='DashboardView']"
    DASHBOARD_WIDGETS = "//Pane[contains(@AutomationId,'DashboardWidget')]"

    # =========================
    # Navigation Tabs
    # =========================
    TAB_PERFORMANCE = "//TabItem[@Name='Performance Control']"
    TAB_GAMES = "//TabItem[@Name='My Games']"
    TAB_LIGHTING = "//TabItem[@Name='Lighting']"
    TAB_SETTINGS = "//TabItem[@Name='Settings']"

    # =========================
    # Performance Control
    # =========================
    PERFORMANCE_VIEW = "//Pane[@AutomationId='PerformanceView']"

    CPU_METRIC = "//Text[@AutomationId='CpuUsageValue']"
    GPU_METRIC = "//Text[@AutomationId='GpuUsageValue']"
    MEMORY_METRIC = "//Text[@AutomationId='MemoryUsageValue']"
    TEMPERATURE_METRIC = "//Text[@AutomationId='TemperatureValue']"

    PERFORMANCE_MODE_DROPDOWN = "//ComboBox[@AutomationId='PerformanceModeDropdown']"
    MODE_BALANCED = "//ListItem[@Name='Balanced']"
    MODE_PERFORMANCE = "//ListItem[@Name='Performance']"
    MODE_ECO = "//ListItem[@Name='Eco']"

    # =========================
    # Games
    # =========================
    GAMES_LIBRARY_VIEW = "//Pane[@AutomationId='GameLibraryView']"
    GAME_TILE = "//ListItem[contains(@AutomationId,'GameTile')]"
    GAME_PLAY_BUTTON = ".//Button[@Name='Play']"
    GAME_STATUS_RUNNING = "//Text[contains(@Name,'Running')]"
    EMPTY_LIBRARY_MESSAGE = "//Text[contains(@Name,'No games')]"

    # =========================
    # Lighting
    # =========================
    LIGHTING_VIEW = "//Pane[@AutomationId='LightingView']"
    DEVICE_KEYBOARD = "//ListItem[contains(@Name,'Keyboard')]"
    COLOR_PICKER_BUTTON = "//Button[@AutomationId='ColorPicker']"
    APPLY_LIGHTING_BUTTON = "//Button[@Name='Apply']"

    # =========================
    # Settings
    # =========================
    SETTINGS_VIEW = "//Pane[@AutomationId='SettingsView']"

    THEME_DROPDOWN = "//ComboBox[@AutomationId='ThemeDropdown']"
    THEME_DARK = "//ListItem[@Name='Dark']"
    THEME_LIGHT = "//ListItem[@Name='Light']"

    NOTIFICATION_TOGGLE = "//ToggleSwitch[@AutomationId='NotificationToggle']"
    STARTUP_TOGGLE = "//ToggleSwitch[@AutomationId='StartupLaunchToggle']"

    # =========================
    # Update
    # =========================
    UPDATE_BANNER = "//Pane[contains(@AutomationId,'UpdateBanner')]"
    UPDATE_BUTTON = "//Button[@Name='Update']"

    # =========================
    # Network / Offline
    # =========================
    OFFLINE_WARNING = "//Text[contains(@Name,'offline')]"
    NETWORK_WARNING = "//Text[contains(@Name,'network')]"
