from controller_remote import *


def main():
    application = QApplication([])
    window = Television()
    window.show()
    application.exec_()


if __name__ == '__main__':
    main()
