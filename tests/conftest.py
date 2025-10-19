# tests/conftest.py
import tempfile, shutil, pytest
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):
    """Create a fresh Chrome profile and WebDriver for each test."""
    tmp_profile = tempfile.mkdtemp(prefix="chrome-swag-")

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--incognito")
    options.add_argument(f"--user-data-dir={tmp_profile}")

    driver = webdriver.Chrome(options=options)

    
    request.node.driver = driver

    yield driver

    driver.quit()
    shutil.rmtree(tmp_profile, ignore_errors=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    outcome = yield
    rep = outcome.get_result()
    if rep.when != "call":
        return

    driver = getattr(item, "driver", None)
    if not driver:
        return

    
    project_root = Path(__file__).resolve().parents[1]
    screenshots_dir = project_root / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    status = "PASS" if rep.passed else "FAIL"
    filename = f"{item.name}_{status}_{ts}.png"

    driver.save_screenshot(str(screenshots_dir / filename))
