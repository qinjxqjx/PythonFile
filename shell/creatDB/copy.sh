#!/bin/bash

. ./config
#echo $pre

if [ ! -d $cur ] && [ -d $pre ]
then    
    cp -r $pre $cur
    echo "creat $cur successfully"
    flag=0
else
    echo "$pre not a directory or $cur already exited"
    #exit 1
    flag=1
fi


if [ $flag -ne 0 ]; then
    echo "begin to find directories or files with name contains $pre "
    
    #将目录下文件夹名称修改为当前版本号名称
    find ./$cur -type d -name "*$pre" | sed -r -n "s/(.*\/)([^\/]*)$pre/mv & \1\2$cur/e";
    #删除dml脚本
    find ./$cur -type f -name "dml*.sql" -exec rm {} \;
    #删除文件中执行dml的行
    find ./$cur -name "*.sql" | xargs sed -i -r "/dml/d";
    #将文件中版本修改为当前版本
    find ./$cur -name "*.sql" | xargs sed -i -r "s/$pre/$cur/g";
else
    echo "flag = $flag, end to excute the remain process"
fi

