from Basic.Log import Logger
from appium import webdriver
import Setting
import os

log = Logger().get_logger()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class GetDevices:
    """获取设备信息"""

    def __init__(self):
        self.option = {}
        self.option.update(Setting.devices_setting)

    def _deviceName(self, device=str()):
        if device:
            self.option.update({"deviceName": device})
        else:
            device = os.popen("adb devices")
            result = [i for i in device.read().split("\n") if i != ""]
            log.info('检索当前电脑所链接的设备中，请稍等~')
            if len(result) > 1:
                if len(result) > 2:
                    log.info(f'\033[31m请检查是否同时链接着两台设备，如若链接着两台设备请在任意adb命令中指定设备名：---> -s\033[0m')
                else:
                    for n in result:
                        if '\tdevice' in n:
                            _device = str(n).split('\tdevice')[0].strip()
                            self.option.update({"deviceName": _device})
            else:
                raise ValueError('请检查设备连接情况')
        return self

    def _platform(self, platformName=str(), platformVersion=str()):
        if platformName:
            self.option.update({"platformName": platformName})
        else:
            result = os.popen("adb shell getprop ro.product.brand").read().strip()
            if result != 'iphone':
                result = 'Android'
            self.option.update({"platformName": result})
        if platformVersion:
            self.option.update({"platformVersion": platformVersion})
        else:
            result = os.popen("adb shell getprop ro.build.version.release").read().strip()
            self.option.update({"platformVersion": result})
        return self

    def options(self, **kwargs):
        self.option.update(**kwargs)
        deviceName = kwargs.get("deviceName", "")
        platformName = kwargs.get("platformName", "")
        platformVersion = kwargs.get("platformVersion", "")
        self._deviceName(deviceName)
        self._platform(platformName, platformVersion)
        log.debug(f'当前链接设备信息：{self.option}')
        return self.option


class Driver(GetDevices):
    def __init__(self):
        super(Driver, self).__init__()
        self.ip = Setting.appium_server["ip"]
        self.port = Setting.appium_server["port"]
        self.project = Setting.test_project
        self.pk_name = Setting.project[self.project]["pk_name"]
        self.option.update({"appPackage": self.pk_name})

    def ConnectDevice(self, **kwargs):
        try:
            driver = webdriver.Remote(f'http://{self.ip}:{self.port}/wd/hub', self.options(**kwargs))
            log.info(f'链接{self.option["deviceName"]}设备成功，启动{self.project}~')
            return driver
        except Exception as e:
            raise e


if __name__ == "__main__":
    dev = {}
    driver = Driver().ConnectDevice(**dev)
