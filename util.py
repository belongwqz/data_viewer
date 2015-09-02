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
            env_type varchar(50),
            info varchar(4096),
            info_type varchar(50),
            comment varchar(4096),
            PRIMARY KEY(system, env_type, info, info_type, comment)
          )
            ''')
    q.exec_('commit')


# noinspection PyCallByClass,PyTypeChecker
class ParamDlg(QtGui.QDialog):
    def __init__(self, record, systems, env_types, info_types, *args, **kwargs):
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
        self.cb_system = QtGui.QComboBox(self.layoutWidget)
        self.cb_system.setEditable(True)
        self.cb_system.setObjectName("cb_system")
        self.hl_system.addWidget(self.cb_system)
        vs_system = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_system.addItem(vs_system)
        self.vl_total.addLayout(self.hl_system)
        self.hl_env = QtGui.QHBoxLayout()
        self.hl_env.setObjectName("hl_env")
        self.lb_env = QtGui.QLabel(self.layoutWidget)
        self.lb_env.setObjectName("lb_env")
        self.hl_env.addWidget(self.lb_env)
        self.cb_env = QtGui.QComboBox(self.layoutWidget)
        self.cb_env.setEditable(True)
        self.cb_env.setObjectName("cb_env")
        self.hl_env.addWidget(self.cb_env)
        vs_env = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_env.addItem(vs_env)
        self.vl_total.addLayout(self.hl_env)
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
        self.hl_info_type = QtGui.QHBoxLayout()
        self.hl_info_type.setObjectName("hl_info_type")
        self.lb_info_type = QtGui.QLabel(self.layoutWidget)
        self.lb_info_type.setObjectName("lb_info_type")
        self.hl_info_type.addWidget(self.lb_info_type)
        self.cb_info_type = QtGui.QComboBox(self.layoutWidget)
        self.cb_info_type.setEditable(True)
        self.cb_info_type.setObjectName("cb_info_type")
        self.hl_info_type.addWidget(self.cb_info_type)
        vs_info_type = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_info_type.addItem(vs_info_type)
        self.vl_total.addLayout(self.hl_info_type)
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
        self.lb_info.setText(QtGui.QApplication.translate("dlg_param", "信息", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_info_type.setText(QtGui.QApplication.translate("dlg_param", "类型", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_comment.setText(QtGui.QApplication.translate("dlg_param", "说明", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_system.addItems(systems)
        self.cb_env.addItems(env_types)
        self.cb_info_type.addItems(info_types)
        self.buttonBox.accepted.connect(self.handle_accept)
        self.buttonBox.rejected.connect(self.reject)
        self.cb_system.setEditText(record.value('system'))
        self.cb_env.setEditText(record.value('env_type'))
        self.txt_info.setPlainText(record.value('info'))
        self.cb_info_type.setEditText(record.value('info_type'))
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
        return self.cb_system.currentText()

    def env_type(self):
        return self.cb_env.currentText()

    def info(self):
        return self.txt_info.toPlainText()

    def info_type(self):
        return self.cb_info_type.currentText()

    def comment(self):
        return self.txt_comment.toPlainText()


class Model(QSqlTableModel):
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        self.setTable("tb_sys_info")
        [self.setHeaderData(i, QtCore.Qt.Horizontal, h) for i, h in enumerate([u'系统名称', u'环境', u'信息', u'类型', u'说明'])]
        self.select()
        self.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
