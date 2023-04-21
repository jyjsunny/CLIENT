import logging
from ftplib import FTP
 

class MyFtp():
    def __init__(self):
        self.ftp_client = FTP()

    # ftp 连接+登录
    def ftp_login(self,host_ip,username,password):
        try:
            self.ftp_client.connect(host_ip,port=2200,timeout=10)
        except :
            logging.warning('network connect time out')
            return 0
        try:
            self.ftp_client.login(user=username, passwd=password)
        except:
            logging.warning('username or password error')
            return -1
        return 1

    # 执行ftp命令
    def execute_some_command(self):
        # 通运sendcmd方法形式执行pwd命令，为使用形式统一起见不推荐使用此种形式，而且其实大多数命令都是支持这种形式的
        command_result = self.ftp_client.sendcmd('pwd')
        print('command_result:%s'% command_result)
        # 通过直接使用pwd方法执行pwd命令，推荐统一使用此种形式
        command_result = self.ftp_client.pwd()
        print('command_result:%s' % command_result)
        # 上传文件；'stor ftp_client.py'告诉服务端将上传的文件保存为ftp_client.py，open()是以二进制读方式打开本地要上传的文件
        command_result = self.ftp_client.storbinary('stor 111.py',open("111.py",'rb'))
        print('command_result:%s' % command_result)
        # # 下载文件；'retr .bash_profile'告诉服务端要下载服务端当前目录下的.bash_profile文件，open()是以二进制写方式打开本地要存成的文件
        # command_result = self.ftp_client.retrbinary('retr .bash_profile', open('local_bash_profile', 'wb').write)
        # logging.warning('command_result:%s' % command_result)
        
        command_result = self.ftp_client.sendcmd('LIST')
        print('command_result:%s'% command_result)
        # command_result = self.ftp_client.mkd(self,'ss')
        # print('command_result:%s'% command_result)


    # 此函数实现退出ftp会话
    def ftp_logout(self):
        print('now will disconnect with server')
        self.ftp_client.close()

if __name__ == '__main__':
    host_ip = '127.0.0.1'
    username = 'sunny'
    password = '123456'
    # 实例化
    my_ftp = MyFtp()
    # 如果登录成功则执行命令，然后退出
    if my_ftp.ftp_login(host_ip,username,password) == 1:
        print('login success , now will execute some command')
        my_ftp.execute_some_command()
        my_ftp.ftp_logout()
        print('logout!')
