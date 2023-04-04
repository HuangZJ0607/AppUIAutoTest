import pytest
from Basic.Driver import GetDevices, Driver


@pytest.fixture(autouse=True, scope="session")
def start_app():
    dev = {}
    driver = Driver().ConnectDevice(**dev)




@pytest.fixture(autouse=True, scope="session")
def close_app():
    yield
    driver.stop_client()


if __name__ == '__main__':
    pytest.main(['-s'])
