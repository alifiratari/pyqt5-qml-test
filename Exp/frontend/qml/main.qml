import QtQuick 2.4
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQuick.Extras 1.4

Rectangle {
    width: 800
    height: 600
    color: "#2c2a2a"
    opacity: 1
    border.color: "#000000"
    id: screen
    objectName: "Screen"

    signal messageRequired;

        function updateMessage(text) {
            statusbar_text.text = text
        }

    signal messageRequired1;
        function refreshMessage() {
            statusbar_text.text = textField.text
        }

    Rectangle {
        id: mainbar
        x: 0
        y: 30
        width: 800
        height: 553
        color: "#2b2b2b"
        objectName: "Mainbar"

        TextField {
            id: textField
            x: 56
            y: 55
            text: qsTr("Text Field")
            font.pointSize: 9
            objectName: "Textfield"
            onTextChanged: messageRequired1()
        }

        Button {
            id: button
            x: 458
            y: 55
            text: qsTr("Zamanı Göster")
            onClicked: messageRequired()
        }
    }

    Rectangle {
        id: titlebar
        objectName: "Titlebar"
        height: 24
        width: parent.width
        color: "#151515"
        opacity: 0.9

        Button {
            id: exitButton
            x: 752
            y: 0
            width: 48
            height: 23
            text: qsTr("Exit")
            highlighted: true
            objectName: "exitButton"
        }
    }


    Rectangle {
        id: statusbar
        objectName: "Statusbar"
        color: "#151515"
        height: 24
        width: parent.width
        anchors { horizontalCenter: parent.horizontalCenter; bottom: parent.bottom }
        property int padding
        padding: 4

        Text {
            id: statusbar_text
            anchors {fill: parent; leftMargin: parent.padding; topMargin: parent.padding}
            objectName: "testText"
            text: "trst"
            font.pointSize: 10
            textFormat: Text.StyledText
            color: "#496DA5"
        }

    }

}

