import QtQuick 2.0

Item {
    TextEdit {
        id: textEdit
        x: 294
        y: 170
        width: 80
        height: 20
        text: qsTr("Text Edit")
    }

    Rectangle {
        id: rectangle
        x: 39
        y: 18
        width: 200
        height: 200
        color: "#ffffff"
    }

}
