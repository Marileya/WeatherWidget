from PySide6.QtCore import (QCoreApplication,
                            QMetaObject,
                            QSize)
from PySide6.QtGui import (QIcon,
                           QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QLayout, QLineEdit, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)
import res_rc


class Ui_WeatherAPI(object):
    def setupUi(self, WeatherAPI):
        if not WeatherAPI.objectName():
            WeatherAPI.setObjectName(u"WeatherAPI")
        WeatherAPI.resize(400, 300)
        WeatherAPI.setMaximumSize(QSize(400, 300))
        WeatherAPI.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0903955 rgba(31, 137, 204, 255), stop:0.386364 rgba(255, 255, 255, 255), stop:0.761364 rgba(14, 207, 216, 255));\n"
                                 "font: 12pt \"Tw Cen MT\";")
        self.centralwidget = QWidget(WeatherAPI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
# блок с выводом погодных данных
        self.temp = QFrame(self.centralwidget)
        self.temp.setObjectName(u"temp")
        self.temp.setMaximumSize(QSize(16777215, 16777215))
        self.temp.setStyleSheet(u"background-color: rgba(255,255,255,45);\n"
                                "border-radius: 7px;")
        self.horizontalLayout_2 = QHBoxLayout(self.temp)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
    # температура фактическая
        self.text1 = QLabel(self.temp)
        self.text1.setObjectName(u"text1")
        self.text1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(14, 23, 216, 35), stop:1 rgba(39, 202, 32, 35));\n"
                                 "border-color: none;")

        self.verticalLayout.addWidget(self.text1)
    # температура по-ощущениям
        self.text2 = QLabel(self.temp)
        self.text2.setObjectName(u"text2")
        self.text2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(14, 23, 216, 35), stop:1 rgba(39, 202, 32, 35));\n"
                                 "border-color: none;")

        self.verticalLayout.addWidget(self.text2)
    # скорость ветра
        self.text3 = QLabel(self.temp)
        self.text3.setObjectName(u"text3")
        self.text3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(14, 23, 216, 35), stop:1 rgba(39, 202, 32, 35));\n"
                                 "border-color: none;")

        self.verticalLayout.addWidget(self.text3)
    # давление (переведенное)
        self.text4 = QLabel(self.temp)
        self.text4.setObjectName(u"text4")
        self.text4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(14, 23, 216, 35), stop:1 rgba(39, 202, 32, 35));\n"
                                 "border-color: none;")

        self.verticalLayout.addWidget(self.text4)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.picture = QLabel(self.temp)
        self.picture.setObjectName(u"picture")
        self.picture.setEnabled(True)
        self.picture.setMaximumSize(QSize(100, 100))
        self.picture.setStyleSheet(u"background-color: none;\n"
                                   "border-color: none;")
        self.picture.setPixmap(
            QPixmap(u"icons/wb_sunny_48dp_FILL0_wght400_GRAD0_opsz48.png"))
        self.picture.setScaledContents(True)
        self.picture.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.picture)

        self.verticalLayout_2.addWidget(self.temp)

        self.City = QFrame(self.centralwidget)
        self.City.setObjectName(u"City")
        self.City.setEnabled(True)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.City.sizePolicy().hasHeightForWidth())
        self.City.setSizePolicy(sizePolicy)
        self.City.setMinimumSize(QSize(380, 50))
        self.City.setMaximumSize(QSize(400, 50))
        self.City.setStyleSheet(u"background-color: none;\n"
                                "border-radius: 7px;\n"
                                "")
        self.horizontalLayout = QHBoxLayout(self.City)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetFixedSize)
        self.lineEdit = QLineEdit(self.City)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(270, 0))
        self.lineEdit.setStyleSheet(u"background-color: none;\n"
                                    "border-color: none;")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.City)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0903955 rgba(31, 137, 204, 255), stop:0.386364 rgba(255, 255, 255, 255), stop:0.761364 rgba(14, 207, 216, 255));\n"
                                      "border: 1px solid rgb(0, 0, 0);\n"
                                      "border-radius: 7px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgba(31, 137, 204, 50);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: rgba(31, 137, 204, 100)\n"
                                      "}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/search_FILL0_wght400_GRAD0_opsz24.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout_2.addWidget(self.City)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        WeatherAPI.setCentralWidget(self.centralwidget)

        self.retranslateUi(WeatherAPI)

        QMetaObject.connectSlotsByName(WeatherAPI)

    def retranslateUi(self, WeatherAPI):
        WeatherAPI.setWindowTitle(QCoreApplication.translate(
            "WeatherAPI", u"Weather API", None))
        self.text1.setText(QCoreApplication.translate(
            "WeatherAPI", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 = 15\u0421", None))
        self.text2.setText(QCoreApplication.translate(
            "WeatherAPI", u"\u041f\u043e \u043e\u0449\u0443\u0449\u0435\u043d\u0438\u044e 13 \u0421", None))
        self.text3.setText(QCoreApplication.translate(
            "WeatherAPI", u"\u0412\u0435\u0442\u0435\u0440 2 \u043c/\u0441", None))
        self.text4.setText(QCoreApplication.translate(
            "WeatherAPI", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435 748 \u043c\u043c.\u0440\u0442.\u0441\u0442.", None))
        self.picture.setText("")
        self.lineEdit.setText(QCoreApplication.translate(
            "WeatherAPI", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0433\u043e\u0440\u043e\u0434", None))
        self.pushButton.setText(QCoreApplication.translate(
            "WeatherAPI", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
