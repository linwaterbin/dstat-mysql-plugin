dstat-mysql-plugin
==================

dstat二次开发

Hi,all：

这是一个dstat-mysql插件开发的资料仓库，欢迎fork并push，感谢 :-)


使用方法：


#!/bin/bash

export DSTAT_MYSQL_USER="root"
export DSTAT_MYSQL_PWD="oracle"
export DSTAT_MYSQL_HOST="127.0.0.1"

/usr/local/src/dstat-0.7.2/dstat --mysql-qc $@


