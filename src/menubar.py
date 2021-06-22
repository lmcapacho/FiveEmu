#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------
# FiveEmu Menu Bar Class
# This file is part of FiveEmu
# Copyright (C) 2021 lmcapacho
# License GPLv3
# ------------------------------

from PySide6 import QtWidgets


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self):
        super(MenuBar, self).__init__()

        self.addMenu("&File")
        self.addMenu("&Edit")
        self.addMenu("&Build")
        self.addMenu("&Debug")
        self.addMenu("&Help")
