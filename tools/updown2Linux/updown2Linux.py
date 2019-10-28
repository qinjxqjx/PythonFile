#!/usr/bin/python
# coding=utf-8
import paramiko
import os
from multiprocessing import Pool
import multiprocessing


def sftp_upload(host, port, username, password, local, remote):
    sf = paramiko.Transport((host, port))
    sf.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(sf)

    try:
        if (os.path.isdir(local)): # 判断本地参数是目录还是文件
            for f in os.listdir(local): # 遍历本地目录
                sftp.put(os.path.join(local + f), os.path.join(remote + f))  # 上传目录中的文件
        else:
            file = os.path.basename(local)
            sftp.put(local, os.path.join(remote, file))  # 上传文件
    except Exception as e:
        print('upload file exception:', e)

    sf.close()


def sftp_download(host, port, username, password, local, remote):
    sf = paramiko.Transport((host, port))
    sf.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(sf)

    try:
        if os.path.isdir(local):  # 判断本地参数是目录还是文件
            for f in sftp.listdir(remote):  # 遍历远程目录
                sftp.get(os.path.join(remote + f), os.path.join(local + f))  # 下载目录中文件
        else:
            sftp.get(remote, local)  # 下载文件
    except Exception as e:
        print(e)

    sf.close()
    


if __name__ == '__main__':
    hosts = '10.18.190.166,10.18.190.177,10.18.190.168' # 主机
    port = 22  # 端口
    username = 'mj'  # 用户名
    password = 'acebdf'  # 密码
    local = 'C:\\Users\\Administrator\\Desktop\\zookeeper\\zookeeper-3.4.10.tar.gz'  # 本地文件或目录，与远程一致，当前为windows目录格式，window目录中间需要使用双斜线
    remote = '/home/mj/installpackage/'  # 远程文件或目录，与本地一致，当前为linux目录格式
    # sftp_upload(host,port,username,password,local,remote)#上传
    # sftp_download(host,port,username,password,local,remote)#下载

    #单线程
    # for host in hosts.split(','):
    #     print(host.strip())
    #     sftp_upload(host.strip(), port, username, password, local, remote)


    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=3)

    for host in hosts.split(','):
        pool.apply_async(sftp_upload, (host.strip(), port, username, password, local, remote))

    print("Starting tasks...")
    pool.close()
    pool.join()

    print("Sub-process(es) done.")