from PyQt5 import QtWidgets, QtCore
import sys
#获取窗口
app = QtWidgets.QApplication(sys.argv)
#设置窗口大小
widget = QtWidgets.QWidget()
widget.resize(500, 200)
#设置窗口名称
widget.setWindowTitle("PyQt 窗口")
#显示窗口
widget.show()
#定住窗口,点窗口右上角的关闭按键才退出
exit(app.exec_())