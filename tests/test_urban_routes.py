from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from helpers.retrieve_code import retrieve_phone_code
from pages.urban_routes_page import UrbanRoutesPage



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)


    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_comfort_tariff_selection(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        assert_text = self.routes_page.get_comfort_icon_assert().text
        assert assert_text == "Comfort"

    def test_fill_phone_number(self):
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number_button(data.phone_number)
        self.routes_page.click_submit_phone_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(code)
        self.routes_page.click_confirm_sms_button()
        assert self.routes_page.get_phone_number() == data.phone_number
        assert self.routes_page.get_sms_code() == code

    def test_add_credit_card(self):
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_icon()
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_add_credit_card(card_number, card_code)
        self.routes_page.click_submit_card_button()
        self.routes_page.click_close_button()
        assert self.routes_page.get_card_cvv_field() == card_code
        assert self.routes_page.get_card_number_field() == card_number

    def test_comment_to_the_driver(self):
        message_for_driver = data.message_for_driver
        self.routes_page.set_comment_box(message_for_driver)
        assert self.routes_page.get_comment_box() == message_for_driver

    def test_blanket_and_tissue_selection(self):
        self.routes_page.click_switch_blanket_and_tissue()

    def test_order_two_ice_cream(self):
        self.routes_page.click_counter_ice_cream()

    def test_taxi_search_modal_appears(self):
        assert not self.routes_page.is_order_modal_shown()
        self.routes_page.click_request_blue_button()
        assert self.routes_page.is_order_modal_shown()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()