import paramiko
import time
#from time import sleep

#tftp = input('Eenter your tftp_address:')

class MyScript():
    #定义构造方法（特殊方法，魔法方法）
    #先将所有属性都定义
    def __init__(self, swname, ip, user, passwd, tftp):
        self.swname = swname
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.tftp = tftp
    #
    def connet(self,)
        self.paramiko.SSHClient()
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.
        
        try:
            ssh.connect(hostname=ip, username=user, password=passwd, timeout=8)
        except Exception as e:
        #在try产生异常时被except捕获和处理就会继续往下执行代码主要部分，else代码块不被执行。
        print(ip,'node 1，连接失败:',e)
        
        finally:
            ssh.close() 
    #定义方法
    def huawei(self):
        else:
            cmd = ssh.invoke_shell()
            cmd.send('tftp {} put vrpcfg.zip {}.zip'.format(tftp, swname)+'\n')
            time.sleep(6)
            output= cmd.recv(10000)
            print(output.decode())
#----------------------------
    def cisco(self):
        else:
            cmd = ssh.invoke_shell()
            cmd.send('copy running-config tftp\n')
            cmd.send(tftp+'\n')
            cmd.send('\n')
            time.sleep(6)
            output= cmd.recv(10000)
            print(output.decode())