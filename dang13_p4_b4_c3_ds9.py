# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

def bt_dang13_p4_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        u0 = randint(1, 3)
        v0 = randint(u0 + 1, 5)
        S = u0 + v0
        P = u0 * v0
        tong_lap_phuong = u0**3 + v0**3
        x0 = u0**3
        y0 = v0**3

        noidungcauhoi = ('''Giải hệ phương trình: \\\\
                         $\\left\\{ \\begin{array}{l} \\sqrt[3]{x} + \\sqrt[3]{y} = %s \\\\ x + y = %s \\end{array} \\right.$'''
                         % (str(S), str(tong_lap_phuong)))

        loigiai = ('''Đặt $u = \\sqrt[3]{x}$ và $v = \\sqrt[3]{y}$. Hệ phương trình trở thành: \\\\
                   $\\left\\{ \\begin{array}{l} u + v = %s \\\\ u^3 + v^3 = %s \\end{array} \\right. \\Leftrightarrow \\left\\{ \\begin{array}{l} u + v = %s \\\\ (u + v)^3 - 3uv(u + v) = %s \\end{array} \\right.$ \\\\
                   Thay $u + v = %s$ vào phương trình thứ hai, ta được: \\\\
                   $%s^3 - 3uv \\cdot %s = %s \\Leftrightarrow %s - %suv = %s \\Leftrightarrow uv = %s$. \\\\
                   Khi đó $u, v$ là hai nghiệm của phương trình: $t^2 - %st + %s = 0 \\Leftrightarrow (t - %s)(t - %s) = 0 \\Leftrightarrow t = %s$ hoặc $t = %s$. \\\\
                   - Với $u = %s, v = %s \\Rightarrow \\sqrt[3]{x} = %s, \\sqrt[3]{y} = %s \\Rightarrow x = %s, y = %s$. \\\\
                   - Với $u = %s, v = %s \\Rightarrow \\sqrt[3]{x} = %s, \\sqrt[3]{y} = %s \\Rightarrow x = %s, y = %s$. \\\\
                   Vậy hệ phương trình có hai nghiệm $(x; y) \\in \\left\\{(%s; %s), (%s; %s)\\right\\}$.'''
                   % (str(S), str(tong_lap_phuong), str(S), str(tong_lap_phuong),
                      str(S), str(S), str(S), str(tong_lap_phuong), str(S**3), str(3*S), str(tong_lap_phuong), str(P),
                      str(S), str(P), str(u0), str(v0), str(u0), str(v0),
                      str(u0), str(v0), str(u0), str(v0), str(x0), str(y0),
                      str(v0), str(u0), str(v0), str(u0), str(y0), str(x0),
                      str(x0), str(y0), str(y0), str(x0)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
