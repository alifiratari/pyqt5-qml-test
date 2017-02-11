from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *
from PyQt5 import QtQuick
import sys

class DataObject(QObject):

    signal = pyqtSignal()

    @pyqtProperty(str, notify=signal)
    def text(self):
        print(self._text)
        return self._text


    @text.setter
    def text(self, text):
        if self._text != text:
            self._text = text
            print(text)
            self.signal.emit("te")


    def __init__(self, text='', parent=None):
        super(DataObject, self).__init__(parent)

        self._text = text

        print(self._text)
        print(text)

class Now(QObject):

    signal = pyqtSignal(str)

    def emit_now(self):
        formatted_date = QDateTime.currentDateTime().toString()
        self.signal.emit(formatted_date)

class Refresh(QObject):

    signal = pyqtSignal()

    def emit_refresh(self):
        self.signal.emit()

class App(object):
    def __init__(self):

        # view olarak kısaltıyoruz rahat yazabilmek için
        self.view = QQuickView()
        # Obje ismi atıyoruz
        self.view.setObjectName("View")
        # Çercevesiz pencere oluşturmak için
        self.view.setFlags(Qt.FramelessWindowHint)
        # Qml Kaynağı ile render alıcak.
        self.view.setSource(QUrl("frontend/qml/main.qml"))
        self.view.setResizeMode(QQuickView.SizeRootObjectToView)
        ## Pencere boyutunu değiştirmek için
        #self.view.resize( 854, 480 )

        # Root objeyi ve altındakilerden bazılarını kısalttık
        self.Screen = self.view.rootObject()
        print("Screen(Root) = " + str(self.Screen))
        self.Mainbar = self.Screen.findChild(QObject, "Mainbar")
        print("Mainbar = " + str(self.Mainbar))
        self.Titlebar = self.Screen.findChild(QObject, "Titlebar")
        print("Titlebar = " + str(self.Titlebar))
        self.Statusbar = self.Screen.findChild(QObject, "Statusbar")
        print("Statusbar = " + str(self.Statusbar))
        self.Textfield = self.Screen.findChild(QObject, "Textfield")
        print("Textfield = " + str(self.Textfield))

        ## ButtonExit'a tıklandığında kapanma emri verdik.
        self.Screen.findChild( QObject, "exitButton" ).clicked.connect( exit )

        ## Statusbara yazı yazdırma
        self.Screen.updateMessage( "Click to get the current date and time" )

        ## Butona tıklandığında saati statusbara yazması için.
        self.now = Now()
        self.Screen.messageRequired.connect(self.now.emit_now)
        self.now.signal.connect(self.Screen.updateMessage)


        ## Text değiştirildiğinde değiştirilen texti statusbara yazması için.
        self.refresh = Refresh()
        self.Screen.messageRequired1.connect(self.refresh.emit_refresh)
        self.refresh.signal.connect(self.Screen.refreshMessage)

        ## Test
        DataObject("test")
        #// Configuration Defines

        if fullscreen:
            self.view.showFullScreen( )
        else:
            self.view.show( )
        ##

fullscreen = False
app = QApplication(sys.argv)
test = App()
sys.exit(app.exec_())



