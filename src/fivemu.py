#!/usr/bin/env python
# -*- coding: utf-8 -*-

#####################################################################
# FiveEmu main file.
#
# Copyright (c) 2021 lmcapacho
#
# This file is part of FiveEmu.
#
# FiveEmu is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FiveEmu is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FiveEmu.  If not, see <http://www.gnu.org/licenses/>.
#####################################################################

import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class fivemu(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication([])
    window = fivemu()
    window.showMaximized()
    sys.exit(app.exec())
