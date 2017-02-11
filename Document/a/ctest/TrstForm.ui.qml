import QtQuick 2.4

Item {
    width: 400
    height: 400

    Rectangle {
        id: rectangle
        color: "#ffffff"
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        anchors.fill: parent

        TextEdit {
            id: textEdit
            x: 37
            y: 28
            width: 80
            height: 20
            text: qsTr("Text Edit")
            font.pixelSize: 12
        }
    }

    Connections {
        id: connects1
        target: textEdit
        onContentSizeChanged: textEdit.text = value
    }
}
