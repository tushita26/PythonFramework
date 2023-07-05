from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser.............")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser........")
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):  # This will get from CLI hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return Browser value to setup method
    return request.config.getoption("--browser")


############### PyTest HTML Reports #################

# It is hook for adding env info to HTML Reports
def pytest_configure(config):
    config._metadata = {
        'Project Name': 'nop Commerce',
        'Module Name': 'Customers',
        'Tester': 'Tushita'
    }


# It is hook or delete/modify env to info HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
