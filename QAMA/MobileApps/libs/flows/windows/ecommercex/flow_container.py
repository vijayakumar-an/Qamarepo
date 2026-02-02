# flow_container.py

from QAMA.MobileApps.libs.flows.windows.ecommercex.first_use_flow.ecommerce_privacy_CN_setting import EcommerceGenericActionFlow
from ecommerce.apps.windows.flows.generic.ecommerce_generic_action_flow 
import EcommerceGenericActionFlow


class FlowContainer:
    """
    Central access point for E-Commerce flows
    (Based strictly on current test coverage)
    """

    def __init__(self, driver):
        self.driver = driver

        # Generic flow backing all current test cases
        self.generic_action = EcommerceGenericActionFlow(driver)
