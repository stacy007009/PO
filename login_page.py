from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Minimal page object for a login page.
    Defaults use common locators but can be overridden if your page uses different attributes.
    """

    def __init__(
        self,
        driver: WebDriver,
        username_locator: Tuple[str, str] = (By.NAME, "username"),
        password_locator: Tuple[str, str] = (By.NAME, "password"),
        submit_locator: Tuple[str, str] = (By.CSS_SELECTOR, "button[type='submit']"),
        timeout: int = 10,
    ):
        self.driver = driver
        self.username_locator = username_locator
        self.password_locator = password_locator
        self.submit_locator = submit_locator
        self.wait = WebDriverWait(driver, timeout)

    def _find(self, locator: Tuple[str, str]):
        by, value = locator
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def enter_username(self, username: str) -> None:
        el = self._find(self.username_locator)
        el.clear()
        el.send_keys(username)

    def enter_password(self, password: str) -> None:
        el = self._find(self.password_locator)
        el.clear()
        el.send_keys(password)

    def click_login(self) -> None:
        btn = self._find(self.submit_locator)
        try:
            btn.click()
        except Exception:
            # Fallback: try submitting containing form if click fails
            try:
                form = btn.find_element(By.XPATH, "./ancestor::form")
                form.submit()
            except Exception:
                raise