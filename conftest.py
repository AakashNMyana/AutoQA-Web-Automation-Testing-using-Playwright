import pytest
from playwright.sync_api import sync_playwright
from config.config import BROWSER, HEADLESS
from utils.screenshot import take_screenshot

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = getattr(p, BROWSER).launch(headless=HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()
    yield page

    if request.node.rep_call.failed:
        take_screenshot(page, request.node.name)

    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# ---- Advanced pytest-html customization ----

def pytest_html_report_title(report):
    report.title = "AutoQA Automation Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<h2>Execution Summary</h2>",
        "<p><strong>Framework:</strong> Playwright + Pytest</p>",
        "<p><strong>Project:</strong> AutoQA Automation Suite</p>",
        "<p><strong>Scope:</strong> Login, Sorting, Cart, Logout, API Validation</p>"
    ])


def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')


def pytest_html_results_table_row(report, cells):
    test_name = report.nodeid.split("::")[-1]

    descriptions = {
        "test_login": "Validates successful login",
        "test_sort_products": "Validates product price sorting",
        "test_cart_price_validation": "Validates cart pricing logic",
        "test_logout": "Validates user logout flow",
        "test_ui_api_product_validation": "Validates UI vs API product consistency"
    }

    desc = descriptions.get(test_name, "Test execution")
    cells.insert(2, f'<td>{desc}</td>')