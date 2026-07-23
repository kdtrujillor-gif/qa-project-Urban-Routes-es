from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class UrbanRoutesPage:
    #1- Configurar la dirección
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    #2- eleccionar la tarifa Comfort
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tariff-cards .tcard.active .tcard-title')
    #3- Rellenar el número de teléfono
    phone_number_button = (By.XPATH, '//div[@class="np-text" and text()="Número de teléfono"]')
    phone_number_button_assert= (By.CSS_SELECTOR, '.from .np-button .np-text')
    phone_number_field = (By.ID, 'phone')
    submit_phone_button = (By.CSS_SELECTOR, '.button.full')
    sms_code_field = (By.ID, 'code')
    confirm_sms_button = (By.XPATH, '//button[contains(text(), "Confirmar")]')
    #4- Agregar una tarjeta de crédito
    payment_method_button = (By.XPATH, '//div[@class="pp-text" and text()="Método de pago"]')
    payment_method_button_assert = (By.CSS_SELECTOR, '.from .pp-button .pp-text')
    add_card_icon = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    add_card_icon_assert = (By.CSS_SELECTOR, '.pp-selector .pp-row.disabled .pp-title')
    card_number_field = (By.ID, 'number')
    card_cvv_field = (By.CSS_SELECTOR, '.card-code-input input.card-input')
    submit_card_button = (By.CSS_SELECTOR, '.pp-buttons .button.full')
    close_button = (By.CSS_SELECTOR, '.payment-picker .close-button')
    #5- Escribir un mensaje para el conductor
    comment_box = (By.ID, 'comment')
    #6- Pedir una manta y pañuelos
    switch_blanket_and_tissue = (By.CSS_SELECTOR, '.reqs.open .r-sw-container .switch')
    #7- Pedir 2 helados
    counter_ice_cream = (By.CSS_SELECTOR, '.r-group-items .r-counter .counter-plus')
    #8- Aparece el modal para buscar un taxi
    request_blue_button = (By.CSS_SELECTOR, '.smart-button')
    order_modal = (By.CSS_SELECTOR, 'div.order')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
#1- Configurar la dirección con def
    def set_from(self, from_address):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

# 2- eleccionar la tarifa Comfort con def
    def get_request_taxi_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(self.comfort_icon_assert)
        )

# 3- Rellenar el número de teléfono con def
    def get_phone_number_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_button_assert(self):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(self.phone_number_button_assert)
        )

    def set_phone_number_button(self, phone_number):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.phone_number_field)
        ).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def get_submit_phone_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.submit_phone_button)
        )

    def click_submit_phone_button(self):
        self.get_submit_phone_button().click()


    def set_sms_code(self, code):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.sms_code_field)
        ).send_keys(code)

    def get_sms_code(self):
        return self.driver.find_element(*self.sms_code_field).get_property('value')

    def get_confirm_sms_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.confirm_sms_button)
        )

    def click_confirm_sms_button(self):
        self.get_confirm_sms_button().click()
#4- Agregar una tarjeta de crédito con def
    def get_payment_method_button(self ):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.payment_method_button)
        )
    def click_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_payment_method_button_assert(self):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(self.payment_method_button_assert)
        )

    def get_add_card_icon(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.add_card_icon)
        )

    def click_add_card_icon(self):
        self.get_add_card_icon().click()

    def get_add_card_icon_assert(self):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(self.add_card_icon_assert)
        )

    def set_card_number(self, number_card):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.card_number_field)
        ).send_keys(number_card)

    def set_card_cvv(self, code_card):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.card_cvv_field)
        ).send_keys(code_card, Keys.TAB)

    def get_card_number_field(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_card_cvv_field(self):
        return self.driver.find_element(*self.card_cvv_field).get_property('value')

    def set_add_credit_card(self, number_card, code_card):
        self.set_card_number(number_card)
        self.set_card_cvv(code_card)

    def get_submit_card_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.submit_card_button)
        )

    def click_submit_card_button(self):
        self.get_submit_card_button().click()

    def get_close_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.close_button)
        )
    def click_close_button(self):
        self.get_close_button().click()
# 5- Escribir un mensaje para el conductor
    def set_comment_box(self, message_for_driver):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.comment_box)
        ).send_keys(message_for_driver)

    def get_comment_box(self):
        return self.driver.find_element(*self.comment_box).get_property('value')
#6- Pedir una manta y pañuelos def
    def get_switch_blanket_and_tissue(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.switch_blanket_and_tissue)
        )

    def click_switch_blanket_and_tissue(self):
        self.get_switch_blanket_and_tissue().click()
#7- Pedir 2 helados def
    def get_counter_ice_cream(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.counter_ice_cream)
        )

    def click_counter_ice_cream(self, times=2):
        for _ in range(times):
            self.get_counter_ice_cream().click()

#8- Aparece el modal para buscar un taxi
    def get_request_blue_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.request_blue_button)
        )

    def click_request_blue_button(self):
        self.get_request_blue_button().click()

    def get_order_modal(self):
        return self.wait.until(
            expected_conditions.presence_of_element_located(self.order_modal)
        )

    def is_order_modal_shown(self):
        modal = self.get_order_modal()
        classes = modal.get_attribute('class')
        return 'shown' in classes.split()