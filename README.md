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

/usr/local/src/dstat-0.7.2/dstat -lamp --mysql-qc $@


输出大概是这样子：

[root@DataHacker dstat-0.7.2]# ./run-dstat-plugin.sh 
---load-avg--- ----total-cpu-usage---- -dsk/total- -net/total- ---paging-- ---system-- ------memory-usage----- ---procs--- ------------mysql-QC-----------
 1m   5m  15m |usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw | used  buff  cach  free|run blk new|  qhit    qins    qlow    qnot 
0.06 0.06 0.06|  3   2  92   2   0   0|  77k   12k|   0     0 |   0     0 | 124   257 | 649M 78.1M  363M 1899M|  0   0 1.3|     0       0       0       3 
0.06 0.06 0.06|  3   0  97   0   0   0|   0     0 |   0     0 |   0     0 |  75   121 | 649M 78.1M  363M 1899M|  0   0   0|     0       0       0       3 ^C

