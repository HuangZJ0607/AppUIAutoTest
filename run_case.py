import os
import pytest

if __name__ == '__main__':
    # 当前路径(使用 abspath 方法可通过dos窗口执行)
    current_path = os.path.dirname(os.path.abspath(__file__))
    # 执行pytest下的用例并生成json文件
    pytest.main(['-s', '-v'])
