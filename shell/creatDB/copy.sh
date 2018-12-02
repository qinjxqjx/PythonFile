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
    
    #��Ŀ¼���ļ��������޸�Ϊ��ǰ�汾������
    find ./$cur -type d -name "*$pre" | sed -r -n "s/(.*\/)([^\/]*)$pre/mv & \1\2$cur/e";
    #ɾ��dml�ű�
    find ./$cur -type f -name "dml*.sql" -exec rm {} \;
    #ɾ���ļ���ִ��dml����
    find ./$cur -name "*.sql" | xargs sed -i -r "/dml/d";
    #���ļ��а汾�޸�Ϊ��ǰ�汾
    find ./$cur -name "*.sql" | xargs sed -i -r "s/$pre/$cur/g";
else
    echo "flag = $flag, end to excute the remain process"
fi

