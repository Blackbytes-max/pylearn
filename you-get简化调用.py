# !/usr/bin/python3
#you-get快速调用脚本
import os
links=input('请输入网页链接： ')
save_path=os.environ["HOMEDRIVE"]+os.environ["HOMEPATH"]+"\Downloads"
if os.access(save_path, os.F_OK|os.R_OK|os.W_OK) :  #判断目录是否存在且可读写
    os.chdir(save_path)
else :
    print(save_path,'不存在')
    del save_path
cmdstr="you-get  "+links
os.system(cmdstr)
input('按下ENTER关闭本窗口')
exit()
