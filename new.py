import paramiko
from time import sleep

#可以使用环境管理器来使用模块with ··· as ···:
#years = input('Enter year:') + input('Enter quarter:')
tftp = input('Eenter your tftp_address:') or '10.27.163.35'
#如果未输入任何内容input将返回空字符串.python中空字符串是False bool(“”).运算符或返回第一个trufy值.
class MyScript:
    def __init__(self, keyword):
        self.area = keyword[0]
        self.key = keyword[1]
        self.swname = keyword[2]
        self.ip = keyword[3]
        self.user = keyword[4]
        self.passwd = keyword[5]
    def connect(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname = self.ip, username = self.user, password = self.passwd, timeout=7,look_for_keys=False)
            #look_for_keys=False(bool类型)，设置为False时用于来禁用在～/.ssh中搜索私钥文件；
        except Exception as e:
            #在try产生异常时被except捕获和处理就会继续往下执行代码主要部分，else代码块不被执行。
            print(self.ip,'error:',e)
        else:
            cmd = self.client.invoke_shell()
            if self.key == 'huawei':
                cmd.send('tftp {} put vrpcfg.zip {}/{}.zip'.format(tftp, self.area, self.swname)+'\n')
                #增加put到各自区域的文件夹中功能，使用/杠新建文件夹
                sleep(5)
                output= cmd.recv(1000)
                print(output.decode())
                self.client.close()
            elif self.key == 'cisco':
                cmd.send('copy running-config tftp\n')
                cmd.send(tftp+'\n')
                cmd.send('{}/{}.cfg'.format(self.area, self.swname)+'\n')
                sleep(5)
                output= cmd.recv(1000)
                print(output.decode())
                self.client.close()
#主程序--------------------------------
with open('d:/ip_list.txt') as f:
    for line in f:
        list1 = line.strip('\n').split(':')
        test = MyScript(list1)
        test.connect()