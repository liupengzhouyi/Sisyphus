#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.config.v1.load_config import LoadConfig
from frame.log.log4py import print_log
from frame.soft_cat.check_version.v1.check_version import has_install
from frame.soft_cat.install.v1.install_soft import apt_get_update, install_soft
from frame.soft_cat.uninstall.v1.uninstall_soft import uninstall_soft
from model.soft.v1.soft_factory import create_soft_by_dict
from tools.file_box.v1.file_box import FileBox
from tools.json_box.v1.json_box import JsonBox


def do_install(install_softs: dict):
    
    apt_get_update()
    for item in install_softs.keys():
        soft = install_softs.get(item)
        a = create_soft_by_dict(soft=soft)
        a.show()
        if not has_install(soft=a):
            install_soft(soft=a)
            uninstall_soft(soft=a)
            pass
        

def start():

    print_log(log="开始执行", level="DEBUG")
    print_log(log="开始加载配置文件", level="DEBUG")
    config_path = "./config/config.json"
    load_config = LoadConfig.load(config_path=config_path)
    print_log(log="开始读取策略文件", level="DEBUG")
    file_path = './template.json'
    info = FileBox.read(file_path=file_path)
    json_box = JsonBox(json_string=info)

    softs = json_box.get_value("soft")
    install_softs = softs.get("install")
    do_install(install_softs=install_softs)
        
    print_log(log="开始探测环境", level="DEBUG")
    
    print_log(log="检测包管理软件是否安装？", level="DEBUG")
    
    print_log(log="检测包管理软件是否需要升级？", level="DEBUG")
    
    print_log(log="开始安装软件", level="DEBUG")
    
    print_log(log="开始安装python包", level="DEBUG")
    
    print_log(log="开始使用pip安装python包", level="DEBUG")
    
    print_log(log="开始设置文件夹目录", level="DEBUG")
    
    print_log(log="开始恢复文件", level="DEBUG")
    
    
if __name__ == "__main__":
    
    start()
