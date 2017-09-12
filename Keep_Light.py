# coding=utf-8
import win32api
import win32con
import pythoncom  
import pyHook 
import time
import thread
import sys

'''
FLAG = 0
# 按键响应函数
def onKeyboardEvent(event):
	# F10的键码为121
	if event.KeyID == 121:
		global FLAG
		FLAG = 1
	return True  

# 监听键盘输入的线程
def watchKeyboard():
	# 创建一个“钩子”管理对象     
	hm = pyHook.HookManager()
	# 监听所有键盘事件     
	hm.KeyDown = onKeyboardEvent
	# 设置键盘“钩子”     
	hm.HookKeyboard()
	# 循环监听
	pythoncom.PumpMessages()
	return
'''
# 模拟按键输入的线程
def keyPress():
	# 最多执行40分钟
	for i in range(1,10):
		win32api.keybd_event(20,0,0,0) #CapsLock键码:20 
		win32api.keybd_event(20,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
		time.sleep(250)
	return

 
str = "已开启常亮模式，默认持续时间40分钟，关闭窗口可终止"
# 解决控制台输出中文乱码问题
print str.decode('UTF-8')
keyPress()
