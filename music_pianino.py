import sys
import os
from PyQt6 import uic
from PyQt6 import QtCore, QtMultimedia
from PyQt6.QtWidgets import QApplication, QMainWindow


lst = os.listdir('melody')
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('melodyi.ui', self)
        self.setWindowTitle('Music')
        self.setFixedSize(578, 689)
        self.lst_btn = [self.pushButton, self.pushButton2, self.pushButton3,self.pushButton4,
                        self.pushButton5, self.pushButton6, self.pushButton7, self.pushButton8,
                        self.pushButton9, self.pushButton10, self.pushButton11, self.pushButton12,
                        self.pushButton13, self.pushButton14, self.pushButton15, self.pushButton16,
                        self.pushButton17, self.pushButton18, self.pushButton19, self.pushButton20,
                        self.pushButton21, self.pushButton22, self.pushButton23, self.pushButton24,
                        self.pushButton25, self.pushButton26, self.pushButton27, self.pushButton28,
                        self.pushButton29, self.pushButton30, self.pushButton31, self.pushButton32,
                        self.pushButton33, self.pushButton34, self.pushButton35, self.pushButton36,
                        self.pushButton37, self.pushButton38, self.pushButton39, self.pushButton40,
                        self.pushButton41, self.pushButton42, self.pushButton43, self.pushButton44,
                        self.pushButton45, self.pushButton46, self.pushButton47, self.pushButton48,
                        self.pushButton49, self.pushButton50, self.pushButton51, self.pushButton52,
                        self.pushButton53, self.pushButton54, self.pushButton55, self.pushButton56,
                        self.pushButton57, self.pushButton58, self.pushButton59, self.pushButton60,
                        self.pushButton61, self.pushButton62, self.pushButton63, self.pushButton64,
                        self.pushButton65, self.pushButton66, self.pushButton67, self.pushButton68,
                        self.pushButton69, self.pushButton70, self.pushButton71, self.pushButton72,
                        self.pushButton73, self.pushButton74, self.pushButton75, self.pushButton76,
                        self.pushButton77, self.pushButton78, self.pushButton79, self.pushButton80,
                        self.pushButton81, self.pushButton82, self.pushButton83, self.pushButton84,
                        self.pushButton85, self.pushButton86, self.pushButton87, self.pushButton88]
        for i in self.lst_btn:
            i.clicked.connect(self.run)
        
    def run(self):
        for i in self.lst_btn:
            if self.sender().objectName() in i.objectName():
                self.load_mp3(f'{lst[self.lst_btn.index(i)]}')
                # print(lst[self.lst_btn.index(i)])
                self._player.play()


    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        self._audio_output = QtMultimedia.QAudioOutput()
        self._player = QtMultimedia.QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(50)
        self._player.setSource(media)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())