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


def bt_dang18_p3_b1_c5_ds8(self):
    # Dạng 18: Kiểm soát chất lượng sản xuất qua dữ liệu rời rạc
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        while True:
            a1 = random.randint(16, 20)
            a2 = random.randint(16, 20)
            a3 = random.randint(16, 20)
            a4 = random.randint(16, 20)
            tong_dat = a1 + a2 + a3 + a4
            if len({a1, a2, a3, a4}) >= 3 and (tong_dat * 100) % 80 == 0:
                break
        a_sai = random.randint(21, 24)
        day = [str(a1), str(a2), str(a3), str(a4), str(a_sai)]
        random.shuffle(day)
        day_str = ";\\; ".join(day)

        ti_le = Decimal(tong_dat * 100) / Decimal(80)
        kq_str = str(ti_le).replace('.', ',')
        if kq_str.endswith(',0'):
            kq_str = kq_str[:-2]

        noidungcauhoi = ('''Một xưởng may kiểm tra ngẫu nhiên $5$ lô hàng, mỗi lô lấy đúng $20$ chiếc áo để đếm số đường chỉ lỗi trên mỗi chiếc áo (số liệu rời rạc). Số lượng áo đạt chuẩn (có $0$ lỗi) ở $5$ lô được ghi lại như sau:
$$%s$$
Sau khi loại bỏ giá trị không hợp lí, hãy tính tỉ lệ phần trăm áo đạt chuẩn trên tổng số áo đã kiểm tra của $4$ lô hợp lí còn lại.''' % day_str)

        loigiai = ('''Vì mỗi lô chỉ kiểm tra $20$ chiếc áo nên số áo đạt chuẩn trong một lô không thể vượt quá $20$. Do đó giá trị $%s$ không hợp lí và bị loại bỏ.\\\\
Tổng số áo đạt chuẩn trong $4$ lô hợp lí còn lại là:
$$%s + %s + %s + %s = %s\\text{ (chiếc)}.$$
Tổng số áo đã kiểm tra của $4$ lô hợp lí là $4 \\cdot 20 = 80$ (chiếc).\\\\
Tỉ lệ phần trăm áo đạt chuẩn là:
$$\\dfrac{%s}{80} \\cdot 100\\%% = %s\\%%.$$'''
                   % (a_sai, a1, a2, a3, a4, tong_dat, tong_dat, kq_str))

    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
