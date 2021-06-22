#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------
# FiveEmu main file
# This file is part of FiveEmu
# Copyright (C) 2021 lmcapacho
# License GPLv3
# ------------------------------

import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from menubar import MenuBar


class fivemu(QMainWindow):
    def __init__(self):
        super().__init__()

        menuBar = MenuBar()
        self.setMenuBar(menuBar)


if __name__ == "__main__":
    app = QApplication([])
    window = fivemu()
    window.showMaximized()
    sys.exit(app.exec())
