# Dummy placeholder for flow_container.py
"""
Flow Container for E-Commerce Windows Application
Acts as a centralized registry for all application flows
"""

# Core / Navigation
from ecommerce.apps.windows.flows.navigation.header import Header
from ecommerce.apps.windows.flows.navigation.sidebar import Sidebar
from ecommerce.apps.windows.flows.home.home import Home

# Authentication & Account
from ecommerce.apps.windows.flows.auth.login import Login
from ecommerce.apps.windows.flows.auth.registration import Registration
from ecommerce.apps.windows.flows.account.profile import Profile
from ecommerce.apps.windows.flows.account.settings import AccountSettings

# Onboarding & Consent
from ecommerce.apps.windows.flows.onboarding.privacy_consent_flow import PrivacyConsentFlow
from ecommerce.apps.windows.flows.onboarding.terms_and_conditions import TermsAndConditions

# Shopping
from ecommerce.apps.windows.flows.catalog.product_listing import ProductListing
from ecommerce.apps.windows.flows.catalog.product_details import ProductDetails
from ecommerce.apps.windows.flows.cart.cart import Cart
from ecommerce.apps.windows.flows.checkout.checkout import Checkout

# Orders & Payments
from ecommerce.apps.windows.flows.orders.order_history import OrderHistory
from ecommerce.apps.windows.flows.payments.payment_methods import PaymentMethods
from ecommerce.apps.windows.flows.payments.refunds import Refunds

# Support
from ecommerce.apps.windows.flows.support.support_home import SupportHome
from ecommerce.apps.windows.flows.support.contact_support import ContactSupport
from ecommerce.apps.windows.flows.support.faq import FAQ

# Utilities
from ecommerce.apps.windows.flows.utils.api_utility import APIUtility
from ecommerce.apps.windows.flows.utils.config_utility import ConfigUtility


class FlowContainer:
    """
    Central access point for all E-Commerce flows
    """

    def __init__(self, driver):
        self.driver = driver

        # Core
        self.home = Home(driver)
        self.header = Header(driver)
        self.sidebar = Sidebar(driver)

        # Auth & Account
        self.login = Login(driver)
        self.registration = Registration(driver)
        self.profile = Profile(driver)
        self.account_settings = AccountSettings(driver)

        # Onboarding
        self.privacy_consent = PrivacyConsentFlow(driver)
        self.terms = TermsAndConditions(driver)

        # Shopping
        self.product_listing = ProductListing(driver)
        self.product_details = ProductDetails(driver)
        self.cart = Cart(driver)
        self.checkout = Checkout(driver)

        # Orders & Payments
        self.order_history = OrderHistory(driver)
        self.payment_methods = PaymentMethods(driver)
        self.refunds = Refunds(driver)

        # Support
        self.support_home = SupportHome(driver)
        self.contact_support = ContactSupport(driver)
        self.faq = FAQ(driver)

        # Utilities
        self.api_utility = APIUtility()
        self.config_utility = ConfigUtility()
