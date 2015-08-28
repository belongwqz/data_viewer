# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\project\py\SysInfo\main.ui'
#
# Created: Thu Aug 27 10:01:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from util import *


# noinspection PyAttributeOutsideInit,PyPep8Naming,PyUnresolvedReferences
class Wnd(object):
    # noinspection PyShadowingNames,PyPep8Naming
    def setupUi(self, mainWnd):
        mainWnd.setObjectName("mainWnd")
        mainWnd.setMinimumSize(QtCore.QSize(621, 471))
        mainWnd.setMaximumSize(QtCore.QSize(621, 471))
        self.centralWidget = QtGui.QWidget(mainWnd)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vl_total = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vl_total.setContentsMargins(0, 0, 0, 0)
        self.vl_total.setObjectName("vl_total")
        self.hl_search = QtGui.QHBoxLayout()
        self.hl_search.setObjectName("hl_search")
        self.lb_search = QtGui.QLabel(self.verticalLayoutWidget)
        self.lb_search.setObjectName("lb_search")
        self.hl_search.addWidget(self.lb_search)
        self.txt_search = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txt_search.setObjectName("txt_search")
        self.hl_search.addWidget(self.txt_search)
        self.cb_search = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cb_search.setObjectName("cb_search")
        self.hl_search.addWidget(self.cb_search)
        self.btn_setting = QtGui.QToolButton(self.verticalLayoutWidget)
        self.btn_setting.setObjectName("btn_setting")
        self.hl_search.addWidget(self.btn_setting)
        self.vl_total.addLayout(self.hl_search)
        self.tb_data = QtGui.QTableView(self.verticalLayoutWidget)
        self.tb_data.setObjectName("tb_data")
        self.vl_total.addWidget(self.tb_data)
        self.hl_action = QtGui.QHBoxLayout()
        self.hl_action.setObjectName("hl_action")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_action.addItem(spacerItem)
        self.btn_add = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_add.setObjectName("btn_add")
        self.hl_action.addWidget(self.btn_add)
        self.btn_del = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_del.setObjectName("btn_del")
        self.hl_action.addWidget(self.btn_del)
        self.btn_mod = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_mod.setObjectName("btn_mod")
        self.hl_action.addWidget(self.btn_mod)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_action.addItem(spacerItem1)
        self.vl_total.addLayout(self.hl_action)
        mainWnd.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainWnd)
        QtCore.QMetaObject.connectSlotsByName(mainWnd)
        self.wnd = mainWnd
        self.setup()

    def set_icon(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('app.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wnd.setWindowIcon(icon)

    def setup(self):
        self.set_icon()
        self.view = self.tb_data
        self.view.verticalHeader().setVisible(False)
        self.view.setAlternatingRowColors(True)
        self.view.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)  # 不允许编辑
        # self.view.setSelectionBehavior(QtGui.QTableWidget.SelectRows)  #行选中
        self.view.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        # self.view.setItemDelegate(QSqlRelationalDelegate(self.view));
        self.model = Model(self.view)
        self.proxy = QtGui.QSortFilterProxyModel(self.wnd)
        self.proxy.setSourceModel(self.model)
        self.view.setModel(self.proxy)
        self.cb_search.addItems(
            [self.model.headerData(i, QtCore.Qt.Horizontal) for i in range(self.model.columnCount())])
        self.txt_search.textChanged.connect(self.on_txt_search_text_changed)
        self.cb_search.currentIndexChanged.connect(self.on_cb_search_currentIndexChanged)
        self.horizontalHeader = self.view.horizontalHeader()
        self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)
        self.view.doubleClicked.connect(self.on_view_doubleClicked)
        self.btn_add.clicked.connect(self.add_record)
        self.btn_del.clicked.connect(self.del_record)
        self.btn_mod.clicked.connect(self.mod_record)
        self.view.clicked.connect(self.table_clicked)
        self.btn_mod.setEnabled(False)
        self.btn_del.setEnabled(False)

    def table_clicked(self, index):
        self.btn_mod.setEnabled(index.row() != -1)
        self.btn_del.setEnabled(index.row() != -1)

    def msg(self, msg):
        QtGui.QMessageBox.warning(self.wnd, u'警告', msg, QtGui.QMessageBox.Warning)

    def exist(self, record):
        return record in [self.model.record(i) for i in range(self.model.rowCount())]

    def can_action(self):
        return self.view.currentIndex().row() != -1

    def mod_record(self):
        if self.can_action():
            rowIndex = self.view.currentIndex().row()
            record = self.model.record(rowIndex)
            dlg = ParamDlg(record)
            if QtGui.QDialog.Accepted == dlg.exec_():
                record.setValue('system', dlg.system())
                record.setValue('env', dlg.env())
                record.setValue('info', dlg.info())
                record.setValue('comment', dlg.comment())
                if self.exist(record):
                    self.msg(u'记录重复，修改失败！')
                else:
                    self.model.setRecord(rowIndex, record)
                    if not self.model.submitAll():
                        self.msg(u'提交失败！')

    def del_record(self):
        if self.can_action() and QtGui.QMessageBox.Yes == QtGui.QMessageBox.information(
                self.wnd, u'提示', u'确认删除？', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No):
            self.model.removeRow(self.view.currentIndex().row())

    def add_record(self):
        record = self.model.record()
        dlg = ParamDlg(record)
        if QtGui.QDialog.Accepted == dlg.exec_():
            record = self.model.record()
            record.setValue("system", dlg.system())
            record.setValue("env", dlg.env())
            record.setValue("info", dlg.info())
            record.setValue("comment", dlg.comment())
            if self.exist(record):
                self.msg(u'记录重复，修改失败！')
            else:
                self.model.insertRecord(self.model.rowCount(), record)
                if not self.model.submitAll():
                    self.msg(u'提交失败！')

    # noinspection PyMethodMayBeStatic,PyArgumentList
    def on_view_doubleClicked(self, info):
        QtGui.QApplication.clipboard().setText(info.data())

    def on_txt_search_text_changed(self, text):
        search = QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self.proxy.setFilterRegExp(search)

    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        self.logicalIndex = logicalIndex
        self.cb_search.blockSignals(True)
        self.cb_search.setCurrentIndex(self.logicalIndex)
        self.cb_search.blockSignals(False)
        self.menuValues = QtGui.QMenu(self.wnd)
        self.signalMapper = QtCore.QSignalMapper(self.wnd)
        valuesUnique = [self.model.record(row).value(self.logicalIndex) for row in range(self.model.rowCount())]
        actionAll = QtGui.QAction(u'所有', self.wnd)
        actionAll.triggered.connect(self.on_actionAll_triggered)
        self.menuValues.addAction(actionAll)
        self.menuValues.addSeparator()

        for actionNumber, actionName in enumerate(sorted(list(set(valuesUnique)))):
            action = QtGui.QAction(actionName, self.wnd)
            self.signalMapper.setMapping(action, actionNumber)
            action.triggered.connect(self.signalMapper.map)
            self.menuValues.addAction(action)

        self.signalMapper.mapped.connect(self.on_signalMapper_mapped)
        headerPos = self.view.mapToGlobal(self.horizontalHeader.pos())
        posY = headerPos.y() + self.horizontalHeader.height()
        posX = headerPos.x() + self.horizontalHeader.sectionPosition(self.logicalIndex)
        self.menuValues.exec_(QtCore.QPoint(posX, posY))

    def on_actionAll_triggered(self):
        filterColumn = self.logicalIndex
        filterString = QtCore.QRegExp("", QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    def on_signalMapper_mapped(self, i):
        stringAction = self.signalMapper.mapping(i).text()
        filterColumn = self.logicalIndex
        filterString = QtCore.QRegExp(stringAction, QtCore.Qt.CaseSensitive, QtCore.QRegExp.FixedString)
        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    def on_cb_search_currentIndexChanged(self, index):
        self.proxy.setFilterKeyColumn(index)

    # noinspection PyCallByClass,PyShadowingNames,PyTypeChecker,PyPep8Naming
    def retranslateUi(self, mainWnd):
        mainWnd.setWindowTitle(QtGui.QApplication.translate('mainWnd', "系统信息查询", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_search.setText(QtGui.QApplication.translate('mainWnd', "搜索", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_setting.setText(QtGui.QApplication.translate('mainWnd', "设置", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add.setText(QtGui.QApplication.translate('mainWnd', "新增", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_del.setText(QtGui.QApplication.translate('mainWnd', "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_mod.setText(QtGui.QApplication.translate('mainWnd', "修改", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    init_db()
    mainWnd = QtGui.QMainWindow()
    tran = QtCore.QTranslator()
    tran.load("zh_CN.qm")
    app.installTranslator(tran)
    ui = Wnd()
    ui.setupUi(mainWnd)
    mainWnd.show()
    sys.exit(app.exec_())
