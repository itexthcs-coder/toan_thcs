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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang17_p3_b1_c5_ds8(self):
    # Dạng 17: Làm sạch dữ liệu thực tế về thời gian xem ti vi mỗi ngày
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        while True:
            t1 = random.randint(10, 28)
            t2 = random.randint(10, 28)
            t3 = random.randint(10, 28)
            t4 = random.randint(10, 28)
            t5 = random.randint(10, 28)
            if len({t1, t2, t3, t4, t5}) == 5 and (t1 + t2 + t3 + t4 + t5) % 5 == 0:
                break
        t_vo_li = random.randint(25, 32)
        t_vo_li_str = "%s,5" % t_vo_li

        def fmt1(v):
            s = str(Decimal(v) / Decimal(10)).replace('.', ',')
            if s.endswith(',0'):
                return s[:-2]
            return s

        day = [fmt1(t1), fmt1(t2), fmt1(t3), fmt1(t4), fmt1(t5), t_vo_li_str]
        random.shuffle(day)
        day_str = ";\\; ".join(day)

        tb = Decimal(t1 + t2 + t3 + t4 + t5) / Decimal(50)
        kq_str = str(tb).replace('.', ',')
        if kq_str.endswith(',0'):
            kq_str = kq_str[:-2]

        noidungcauhoi = ('''Khảo sát thời gian xem ti vi mỗi ngày (đơn vị: giờ) của $6$ học sinh, thu được dãy số liệu liên tục sau:
$$%s$$
Sau khi loại bỏ giá trị không hợp lí, hãy tính thời gian xem ti vi trung bình mỗi ngày (đơn vị: giờ) của nhóm học sinh còn lại.''' % day_str)

        loigiai = ('''Vì một ngày chỉ có $24$ giờ nên thời gian xem ti vi mỗi ngày không thể vượt quá $24$ giờ. Do đó giá trị $%s$ không hợp lí và bị loại bỏ.\\\\
Năm số liệu hợp lí còn lại là: $%s;\\; %s;\\; %s;\\; %s;\\; %s$.\\\\
Thời gian xem ti vi trung bình mỗi ngày của $5$ học sinh còn lại là:
$$\\dfrac{%s + %s + %s + %s + %s}{5} = %s\\text{ (giờ)}.$$'''
                   % (t_vo_li_str, fmt1(t1), fmt1(t2), fmt1(t3), fmt1(t4), fmt1(t5),
                      fmt1(t1), fmt1(t2), fmt1(t3), fmt1(t4), fmt1(t5), kq_str))

    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
