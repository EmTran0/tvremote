from PyQt5.QtWidgets import *
from view_remote import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Television(QMainWindow, Ui_MainWindow):
    """
    A class representing details for a television object
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    SLIDER_VALUE = 0

    def __init__(self, *args, **kwargs) -> None:
        """
        Function to set up object.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.power_button.clicked.connect(lambda: self.power())
        self.mute_button.clicked.connect(lambda: self.mute())
        self.volume_up_button.clicked.connect(lambda: self.volume_up())
        self.volume_down_button.clicked.connect(lambda: self.volume_down())
        self.channel_up_button.clicked.connect(lambda: self.channel_up())
        self.channel_down_button.clicked.connect(lambda: self.channel_down())
        self.tv_screen.setText('_______________\n'
                                   '| /~~~~~~~~\ ||||\n'
                                   '||      x     x        |...|\n'
                                   '||          o          |   |\n'
                                   '| \__________/  O |\n'
                                   '~~~~~~~~~~\n'
                                   )

    def power(self) -> None:
        """
        Method to turn the television off and on.
        """
        self.__status = not self.__status
        if not self.__status:
            self.tv_screen.setText('_______________\n'
                                   '| /~~~~~~~~\ ||||\n'
                                   '||      x     x        |...|\n'
                                   '||          o          |   |\n'
                                   '| \__________/  O |\n'
                                   '~~~~~~~~~~\n'
                                   )
        else:
            if self.__channel == 0:
                self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||     MTV           |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')
            elif self.__channel == 1:
                self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  BBC News      |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')
            elif self.__channel == 2:
                self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  Iron Chef       |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')
            elif self.__channel == 3:
                self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  Succession     |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')

    def mute(self) -> None:
        """
        Method to mute the television
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.volume_up_button.setEnabled(True)
                self.volume_down_button.setEnabled(True)
                self.volume_slider.setValue(self.__volume)
                self.volume_slider.setEnabled(True)
            elif not self.__muted:
                self.volume_up_button.setEnabled(False)
                self.volume_down_button.setEnabled(False)
                self.volume_slider.setEnabled(False)
                self.volume_slider.setValue(0)
        else:
            pass

    def channel_up(self) -> None:
        """
        Function to change the channel forward once
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
                if self.__channel == 0:
                    self.tv_screen.setText('_______________\n'
                                           '| /~~~~~~~~\ ||||\n'
                                           '||     MTV           |...|\n'
                                           '||    is playing     |   |\n'
                                           '| \__________/  O |\n'
                                           '~~~~~~~~~~\n')
                elif self.__channel == 1:
                    self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  BBC News      |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')
                elif self.__channel == 2:
                    self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  Iron Chef       |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')
                elif self.__channel == 3:
                    self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  Succession     |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')

    def channel_down(self) -> None:
        """
        Function to change the channel back once
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
                if self.__channel == 0:
                    self.tv_screen.setText('_______________\n'
                                           '| /~~~~~~~~\ ||||\n'
                                           '||     MTV           |...|\n'
                                           '||    is playing     |   |\n'
                                           '| \__________/  O |\n'
                                           '~~~~~~~~~~\n')
                elif self.__channel == 1:
                    self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  BBC News      |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')
                elif self.__channel == 2:
                    self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  Iron Chef       |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')
                elif self.__channel == 3:
                    self.tv_screen.setText('_______________\n'
                                       '| /~~~~~~~~\ ||||\n'
                                       '||  Succession     |...|\n'
                                       '||    is playing     |   |\n'
                                       '| \__________/  O |\n'
                                       '~~~~~~~~~~\n')

    def volume_up(self) -> None:
        """
        Function to turn the volume up once
        """
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
                self.volume_slider.setValue(self.__volume)

    def volume_down(self) -> None:
        """
        Function to turn the volume down once
        """
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
                self.volume_slider.setValue(self.__volume)
