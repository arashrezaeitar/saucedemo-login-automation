import utils.config as config
from pages.login_page import LoginPage

def test_login_with_invalid_password(driver):
    page = LoginPage(driver)
    page.open(config.BASE_URL)
    page.login(config.USERNAME, "wrong_password")

    typed = page.current_username_value()
    assert typed == config.USERNAME, f"Unexpected username value: {typed!r}"

    error_text = page.get_error_text()
    assert "Epic sadface" in error_text or "Username and password do not match" in error_text, \
        f"Unexpected error message: {error_text}"

   