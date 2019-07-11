# !/usr/bin/python3
#you-get快速调用脚本
import os
links=input('请输入网页链接： ')
os.chdir(os.environ["HOMEPATH"]+"\\Downloads")
cmdstr="you-get  "+links
os.system(cmdstr)
input('按下ENTER关闭本窗口')
exit()
