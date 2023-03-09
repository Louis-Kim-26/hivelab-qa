from selenium.webdriver.common.by import By

# Login Page
class DevLoginPageLocators(object):
    ID_INPUT = (By.NAME, "user_id")
    PW_INPUT = (By.NAME, "user_pw")
    LOGIN_BTN = (By.CLASS_NAME, "btn")
    
class P6LoginPageLocators(object):
    ID_INPUT = (By.NAME, "j_username")
    PW_INPUT = (By.NAME, "j_password")
    LOGIN_BTN = (By.CLASS_NAME, "coral3-Button")

# Highlights Page
class HighlightsPageLocators(object):
    # KV
    KV_SECTION = (By.CLASS_NAME, "highlights-kv__wrap")
    OVERVIEW_SECTION = (By.ID, "overview")

    # Feature: Design
    DESIGN_SECTION = (By.ID, "design")
    COLORS_SECTION = (By.ID, "colors")
    ONLINEEXCLUSIVECOLORS_SECTION = (By.ID, "online-exclusive-color")
    MATERIALS_SECTION = (By.ID, "materials")
    SPEN_SECTION = (By.ID, "s-pen")

    # Feature: Camera
    CAMERA_SECTION = (By.ID, "camera")
    CAMERASPEC_SECTION = (By.ID, "camera-spec")
    NIGHTOGRAPHYCAMERA_SECTION = (By.ID, "nightography-camera")
    HIGHRESOLUTION_SECTION = (By.ID, "high-resolution")
    EXPERTRAW_SECTION = (By.ID, "expert-raw")

    # Feature: Performance
    PERFORMANCE_SECTION = (By.ID, "performance")
    BATTERY_SECTION = (By.ID, "battery")
    DISPLAY_SECTION = (By.ID, "display")
    
    # S pen more
    PRODUCTIVITYWITHSPEN_SECTION = (By.ID, "productivity-with-s-pen")
    
    # Smart-switch
    SMARTSWITCH_SECTION = (By.ID, "smart-switch")

    # PC Continuity
    PCCONTINUITY_SECTION = (By.ID, "pc-continuity")

    # ONE UI
    ONEUI_SECTION = (By.ID, "one-ui")

    # Wallet & Health
    SAMSUNGWALLET_SECTION = (By.ID, "samsung-wallet")
    SAMSUNGHEALTH_SECTION = (By.ID, "samsung-health")

    # Accessories
    ACCESSORIES_SECTION = (By.ID, "accessories")

    # FAQ
    FAQ_SECTION = (By.ID, "faq")
    

    # Etc.
    COLORCHIP = (By.CLASS_NAME, "highlights-colors__tab-item")

# Compare Page
class ComparePageLocators(object):
    COLUMN = (By.CLASS_NAME, "compare-section__list-item")
    SELECT_DEVICE_BTN = (By.CLASS_NAME, "select-device")
    # DEVICE = (By.CLASS_NAME, "compare-sticky__name-dropdown-item")
    DEVICE = (By.TAG_NAME, "a")

    COLORCHIP = (By.CLASS_NAME, "compare-device__colorchip-item")
    COLORCHIP_IMAGE = (By.TAG_NAME, "img")
    COLORCHIP_LABEL = (By.TAG_NAME, "label")

# Common
class CommonLocators(object):
    DISCLAIMER_NUMBERS_IN_MAINTEXT = (By. CLASS_NAME, "click_sup")
    BOTTOM_DISCLAIMER_SECTION = (By.TAG_NAME, "ol")
    EACH_BOTTOM_DISCLAIMER_ELEMENT = (By.CLASS_NAME, "common-bottom-disclaimer__list-item")

