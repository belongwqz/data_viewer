# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\project\py\SysInfo\main.ui'
#
# Created: Thu Aug 27 10:01:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtSql import *


# noinspection PyCallByClass,PyTypeChecker
def init_db():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('d:\\sys-info.db')
    db.open()
    q = QSqlQuery()
    q.exec_('''
          create table if not exists tb_sys_info (
            system varchar(100),
            env varchar(50),
            info varchar(4096),
            comment varchar(4096),
            PRIMARY KEY(system, env, info, comment)
          )
            ''')
    q.exec_('commit')


# noinspection PyCallByClass,PyTypeChecker
class ParamDlg(QtGui.QDialog):
    def __init__(self, record, *args, **kwargs):
        super(ParamDlg, self).__init__(*args, **kwargs)
        self.setObjectName("dlg_param")
        self.resize(531, 392)
        self.setSizeGripEnabled(True)
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 12, 511, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vl_total = QtGui.QVBoxLayout(self.layoutWidget)
        self.vl_total.setContentsMargins(0, 0, 0, 0)
        self.vl_total.setObjectName("vl_total")
        self.hl_system = QtGui.QHBoxLayout()
        self.hl_system.setObjectName("hl_system")
        self.lb_system = QtGui.QLabel(self.layoutWidget)
        self.lb_system.setObjectName("lb_system")
        self.hl_system.addWidget(self.lb_system)
        self.txt_system = QtGui.QLineEdit(self.layoutWidget)
        self.txt_system.setObjectName("txt_system")
        self.hl_system.addWidget(self.txt_system)
        self.vl_total.addLayout(self.hl_system)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_env = QtGui.QLabel(self.layoutWidget)
        self.lb_env.setObjectName("lb_env")
        self.horizontalLayout.addWidget(self.lb_env)
        self.txt_env = QtGui.QLineEdit(self.layoutWidget)
        self.txt_env.setObjectName("txt_env")
        self.horizontalLayout.addWidget(self.txt_env)
        self.vl_total.addLayout(self.horizontalLayout)
        self.hl_info = QtGui.QHBoxLayout()
        self.hl_info.setObjectName("hl_info")
        self.vl_info = QtGui.QVBoxLayout()
        self.vl_info.setObjectName("vl_info")
        self.lb_info = QtGui.QLabel(self.layoutWidget)
        self.lb_info.setObjectName("lb_info")
        self.vl_info.addWidget(self.lb_info)
        vs_info = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_info.addItem(vs_info)
        self.hl_info.addLayout(self.vl_info)
        self.txt_info = QtGui.QPlainTextEdit(self.layoutWidget)
        self.txt_info.setTabChangesFocus(True)
        self.txt_info.setObjectName("txt_info")
        self.hl_info.addWidget(self.txt_info)
        self.vl_total.addLayout(self.hl_info)
        self.hl_comment = QtGui.QHBoxLayout()
        self.hl_comment.setObjectName("hl_comment")
        self.vl_comment = QtGui.QVBoxLayout()
        self.vl_comment.setObjectName("vl_comment")
        self.lb_comment = QtGui.QLabel(self.layoutWidget)
        self.lb_comment.setObjectName("lb_comment")
        self.vl_comment.addWidget(self.lb_comment)
        vs_comment = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_comment.addItem(vs_comment)
        self.hl_comment.addLayout(self.vl_comment)
        self.txt_comment = QtGui.QPlainTextEdit(self.layoutWidget)
        self.txt_comment.setTabChangesFocus(True)
        self.txt_comment.setObjectName("txt_comment")
        self.hl_comment.addWidget(self.txt_comment)
        self.vl_total.addLayout(self.hl_comment)
        self.hl_action = QtGui.QHBoxLayout()
        self.hl_action.setObjectName("hl_action")
        hs_action_left = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_action.addItem(hs_action_left)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.hl_action.addWidget(self.buttonBox)
        hs_action_right = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_action.addItem(hs_action_right)
        self.vl_total.addLayout(self.hl_action)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setWindowTitle(QtGui.QApplication.translate("dlg_param", "参数", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_system.setText(QtGui.QApplication.translate("dlg_param", "系统名称", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_env.setText(QtGui.QApplication.translate("dlg_param", "环境类型", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_info.setText(QtGui.QApplication.translate("dlg_param", "系统信息", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_comment.setText(QtGui.QApplication.translate("dlg_param", "补充说明", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox.accepted.connect(self.handle_accept)
        self.buttonBox.rejected.connect(self.reject)
        self.txt_system.setText(record.value('system'))
        self.txt_env.setText(record.value('env'))
        self.txt_info.setPlainText(record.value('info'))
        self.txt_comment.setPlainText(record.value('comment'))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('app.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def handle_accept(self):
        if self.system().strip() == '' or self.info().strip() == '':
            QtGui.QMessageBox.warning(self, u'警告', u'系统或信息不能为空！', QtGui.QMessageBox.Warning)
            return
        self.accept()

    def system(self):
        return self.txt_system.text()

    def env(self):
        return self.txt_env.text()

    def info(self):
        return self.txt_info.toPlainText()

    def comment(self):
        return self.txt_comment.toPlainText()


class Model(QSqlTableModel):
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        self.setTable("tb_sys_info")
        [self.setHeaderData(i, QtCore.Qt.Horizontal, h) for i, h in enumerate([u'系统名称', u'环境类型', u'系统信息', u'补充说明'])]
        self.select()
        self.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
