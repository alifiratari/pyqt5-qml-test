import People 1.0

Person {
    name: "Bob Jones"
    shoeSize: 12
}
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