#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # 检查当前脚本是否作为主程序执行

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secure_system.settings")
    # 设置 Django 项目的默认设置模块

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # 尝试导入 Django 的 execute_from_command_line 函数
        try:
            import django
        except ImportError:
            # 如果导入 Django 失败，抛出 ImportError 异常
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    execute_from_command_line(sys.argv)
    # 使用命令行参数执行 Django 管理命令
