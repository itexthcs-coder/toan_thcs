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


def bt_dang16_p3_b1_c5_ds8(self):
    # Dạng 16: Tính cỡ mẫu khảo sát đảm bảo tính đại diện theo tỉ lệ phần trăm
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        ti_le = random.choice([5, 10])
        buoc = 20 if ti_le == 5 else 10
        h6 = random.randint(12, 18) * buoc
        h7 = random.randint(12, 18) * buoc
        h8 = random.randint(12, 18) * buoc
        h9 = random.randint(12, 18) * buoc

        m6 = h6 * ti_le // 100
        m7 = h7 * ti_le // 100
        m8 = h8 * ti_le // 100
        m9 = h9 * ti_le // 100
        tong_phieu = m6 + m7 + m8 + m9
        kq_str = str(tong_phieu)

        bang_hs = (
            "\\begin{center}\n"
            "\\begin{tabular}{|l|c|c|c|c|}\n"
            "\\hline\n"
            "\\textbf{Khối lớp} & Khối $6$ & Khối $7$ & Khối $8$ & Khối $9$ \\\\\n"
            "\\hline\n"
            "\\textbf{Số học sinh} & $%s$ & $%s$ & $%s$ & $%s$ \\\\\n"
            "\\hline\n"
            "\\end{tabular}\n"
            "\\end{center}"
            % (h6, h7, h8, h9)
        )

        noidungcauhoi = ('''Một trường trung học cơ sở có số lượng học sinh ở $4$ khối lớp được thống kê trong bảng sau:
%s
Để khảo sát thời gian tự học ở nhà (số liệu liên tục) đảm bảo tính đại diện cho học sinh toàn trường, nhà trường chọn ngẫu nhiên $%s\\%%$ số học sinh ở mỗi khối lớp để phát phiếu hỏi trực tiếp. Hỏi tổng số phiếu khảo sát cần phát ra là bao nhiêu?'''
                         % (bang_hs, ti_le))

        loigiai = ('''Số học sinh được chọn ngẫu nhiên ở từng khối lớp để đảm bảo tính đại diện là:\\\\
- Khối $6$: $%s \\cdot %s\\%% = %s$ (học sinh).\\\\
- Khối $7$: $%s \\cdot %s\\%% = %s$ (học sinh).\\\\
- Khối $8$: $%s \\cdot %s\\%% = %s$ (học sinh).\\\\
- Khối $9$: $%s \\cdot %s\\%% = %s$ (học sinh).\\\\
Tổng số phiếu khảo sát cần phát ra là:
$$%s + %s + %s + %s = %s\\text{ (phiếu)}.$$'''
                   % (h6, ti_le, m6, h7, ti_le, m7, h8, ti_le, m8, h9, ti_le, m9,
                      m6, m7, m8, m9, kq_str))

    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
