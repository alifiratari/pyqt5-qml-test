
import sys
import os.path

from PyQt5.QtCore import QObject,  Qt
from PyQt5.QtCore import QUrl, pyqtSignal, pyqtProperty
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView, QQuickItem

app = QGuiApplication(sys.argv)


qmlFile = 'Trst.qml'

#qmlFile = "qrc:data/"


view = QQuickView()
view.setResizeMode(QQuickView.SizeRootObjectToView)
view.engine().quit.connect(app.quit)

engine = view.engine()
view.setSource(QUrl(qmlFile)) # putting at the end didn't solve referenceError 'This is supposed to solve all referenceErrors

qmlRoot = view.rootObject()

onContentSizeChanged = pyqtSignal(str)

value = pyqtProperty(int, fget=Test.getReadyString, notify=onContentSizeChanged)
print(value)
print(Test.getReadyString)
print(onContentSizeChanged)
view.show()
sys.exit(app.exec_())