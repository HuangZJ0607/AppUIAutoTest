from Basic.Base import BasePage
from Basic.Common import PackageSetting


class LoginPage(BasePage):
    def __int__(self, driver):
        self.driver = driver

    # pk_name = pro["pk_name"]
    # project_name = pro["project_name"]
    # account = pro["account"]
    # code = pro["code"]
    #
    # # 个人信息保护指引
    # msg_protect = {"resourceId": f"{pk_name}:id/tv_title", "text": "个人信息保护指引"}
    # msg_pattern = r"感谢您使用[\s\S]*{}[\s\S]*".format(project_name)
    # msg_protect_content = {"textMatches": msg_pattern}
    # msg_protect_confirm_btn = {"resourceId": f"{pk_name}:id/btn_confirm"}
    # permission_allow_btn = "com.android.packageinstaller:id/permission_allow_button"
    # # 检查帮助与反馈页
    # help_lk = {'text': "遇到问题?"}
    # help_title = {"resourceId": f"{pk_name}:id/title", "text": "帮助与反馈"}
    # back_btn = {"resourceId": f"{pk_name}:id/back"}
    # # 检查用户服务协议
    # user_lk = {"text": "用户服务协议"}
    # user_title = {"resourceId": f"{pk_name}:id/title", "text": "用户服务协议"}
    # user_pattern = r"用户服务协议 .*{}.*".format(project_name)
    # user_content = {"textMatches": user_pattern}
    # # 检查隐私政策
    # secret_lk = {"text": "隐私政策"}
    # secret_title = {"resourceId": f"{pk_name}:id/title", "text": "隐私政策"}
    # secret_pattern = r"本《隐私政策》.*{}.*".format(project_name)
    # secret_content = {"textMatches": secret_pattern}
    # # 使用手机号登录
    # other_login_title = {"text": "点击下方头像登录"}
    # change_login_way_lk = {"text": "换个账号登录"}
    # phone_login_btn = {"text": "手机号码登录"}
    # account_input_box = {"resourceId": f"{pk_name}:id/edit_phone_login_phone_num"}
    # code_input_box = {"resourceId": f"{pk_name}:id/edit_phone_login_verify_code"}
    # login_btn = {"resourceId": f"{pk_name}:id/btn_phone_login"}
    # # 同意协议
    # agree = {"text": "同意"}
    #
    # # 通用返回按钮
    # def back_btn_click(self):
    #     """
    #         点击返回按钮
    #     """
    #     self.click(**self.back_btn)
    #
    # # todo，未知按钮功能，初步估计是系统设置按钮
    # def permission_allow_btn_exists(self):
    #     exists_permission_allow_btn = self.exists(self.permission_allow_btn)
    #     return exists_permission_allow_btn
    #
    # def permission_allow_btn_click(self):
    #     self.click(self.permission_allow_btn)
    #
    # # 个人信息保护指引弹窗
    # def msg_protect_exists(self):
    #     """
    #         判断个人信息保护指引弹窗是否存在
    #     """
    #     exists_msg_protect = self.exists(**self.msg_protect)
    #     return exists_msg_protect
    #
    # def msg_protect_content_assert(self):
    #     """
    #         检查个人信息保护指引弹窗的文本
    #     """
    #     try:
    #         exist_msg_protect_content = self.exists(**self.msg_protect_content)
    #         assert_equal(exist_msg_protect_content, True, "个人信息保护指引内容正确")
    #     except AssertionError as e:
    #         log("个人信息保护指引内容断言失败")
    #
    # def msg_protect_confirm_btn_click(self):
    #     """
    #         个人信息保护指引弹窗，点击确认按钮
    #     """
    #     self.click(**self.msg_protect_confirm_btn)
    #
    # # 帮助与反馈
    # def help_lk_click(self):
    #     """
    #         点击"遇到问题"，进入帮助与反馈页面
    #     """
    #     self.click(**self.help_lk)
    #
    # def help_title_assert(self):
    #     """
    #         检查帮助与反馈页面是否进入成功
    #     """
    #     try:
    #         help_title_exist = self.exists(**self.help_title)
    #         assert_equal(help_title_exist, True, "帮助与反馈存在")
    #     except AssertionError as e:
    #         log("帮助与反馈断言失败")
    #
    # # 用户服务协议
    # def user_lk_click(self):
    #     """
    #         点击用户服务协议
    #     """
    #     self.click(**self.user_lk)
    #
    # def user_content_assert(self):
    #     """
    #         检查用户服务协议内容
    #     """
    #     try:
    #         user_title_exist = self.exists(**self.user_title)
    #         user_content_exist = self.exists(**self.user_content)
    #         assert_equal(user_title_exist, True, "用户服务协议存在")
    #         assert_equal(user_content_exist, True, "用户服务协议内容正确")
    #     except AssertionError as e:
    #         log("用户服务协议断言失败")
    #
    # # 隐私政策
    # def secret_lk_click(self):
    #     """
    #         点击隐私政策
    #     """
    #     self.click(**self.secret_lk)
    #
    # def secret_content_assert(self):
    #     """检查隐私政策内容"""
    #     try:
    #         secret_title_exist = self.exists(**self.secret_title)
    #         secret_content_exist = self.exists(**self.secret_content)
    #         assert_equal(secret_title_exist, True, "隐私政策存在")
    #         assert_equal(secret_content_exist, True, "隐私政策内容正确")
    #     except AssertionError as e:
    #         log("隐私政策断言失败")
    #
    # # 登录
    # def other_login_title_exists(self):
    #     """判断该设备之前是否登录过账号"""
    #     other_login_exists = self.exists(**self.other_login_title)
    #     return other_login_exists
    #
    # def change_login_way_lk_click(self):
    #     """点击【换个账号登录】按钮，进入到手机号登录页"""
    #     self.click(**self.change_login_way_lk)
    #
    # def phone_login_btn_click(self):
    #     """点击【手机号码登录】按钮，拉起协议弹窗"""
    #     self.click(**self.phone_login_btn)
    #     if self.exists(**self.agree):
    #         self.login_agree()
    #         if self.exists(**self.phone_login_btn):
    #             self.phone_login_btn_click()
    #
    # def login_agree(self):
    #     """点击协议弹窗【同意】按钮"""
    #     self.click(**self.agree)
    #
    # def account_input(self):
    #     """手机号输入"""
    #     self.find_element(**self.account_input_box).set_text(self.account)
    #
    # def code_input(self):
    #     """密码输入"""
    #     self.find_element(**self.code_input_box).set_text(self.code)
    #
    # def login_btn_click(self):
    #     """点击【登录】按钮"""
    #     self.click(**self.login_btn)
    #
    # def login_with_account(self):
    #     if self.other_login_title_exists():
    #         self.change_login_way_lk_click()
    #     self.phone_login_btn_click()
    #     self.account_input()
    #     self.code_input()
    #     self.login_btn_click()
    #     sleep(5)


if __name__ == '__main__':
    LoginPage().ddd()
