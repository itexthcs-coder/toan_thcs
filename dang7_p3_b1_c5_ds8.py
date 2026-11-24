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


def bt_dang7_p3_b1_c5_ds8(self):
    # Dạng 7: Xác định số lượng dãy thuộc nhóm dữ liệu không là số, có thể sắp thứ tự
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        co_thu_tu = [
            ("Nhọn, Vuông, Tù, Bẹt", "sắp xếp theo số đo góc tăng dần"),
            ("Tam giác, Tứ giác, Ngũ giác, Lục giác", "sắp xếp theo số cạnh của đa giác tăng dần"),
            ("Kém, Trung bình, Khá, Giỏi", "sắp xếp theo mức độ học lực tăng dần"),
            ("Rất dễ, Dễ, Trung bình, Khó, Rất khó", "sắp xếp theo mức độ khó tăng dần")
        ]
        khong_thu_tu = [
            ("Đỏ, Xanh, Vàng, Tím", "tên màu sắc không có thứ bậc"),
            ("Hình tròn, Hình elip, Hình parabol", "tên đường cong không có thứ tự hơn kém"),
            ("Vuông cân, Đều, Thường", "tên phân loại dạng tam giác không xếp thứ bậc")
        ]
        n_co = random.choice([2, 3, 4])
        n_khong = 5 - n_co
        chon_co = random.sample(co_thu_tu, n_co)
        chon_khong = random.sample(khong_thu_tu, n_khong)
        all_items = [(x[0], True, x[1]) for x in chon_co] + [(x[0], False, x[1]) for x in chon_khong]
        random.shuffle(all_items)

        labels = ['A', 'B', 'C', 'D', 'E']
        lines = []
        gt_lines = []
        for idx, (txt, is_ord, reason) in enumerate(all_items):
            lines.append("- Dãy %s: \\textit{%s}." % (labels[idx], txt))
            if is_ord:
                gt_lines.append("- Dãy %s (%s): có thể sắp thứ tự (%s)." % (labels[idx], txt, reason))
            else:
                gt_lines.append("- Dãy %s (%s): không thể sắp thứ tự (%s)." % (labels[idx], txt, reason))

        sep_nl = "\\\\ \n"
        lines_str = sep_nl.join(lines)
        gt_str = sep_nl.join(gt_lines)
        kq_str = str(n_co)

        noidungcauhoi = ('''Xét $5$ dãy dữ liệu không là số sau:\\\\
%s\\\\
Có bao nhiêu dãy thuộc nhóm \\textbf{dữ liệu không là số, có thể sắp thứ tự}?''' % lines_str)

        loigiai = ('''Ta kiểm tra khả năng sắp xếp thứ tự của từng dãy dữ liệu:\\\\
%s\\\\
Vậy có tất cả $%s$ dãy thuộc nhóm dữ liệu không là số, có thể sắp thứ tự.''' % (gt_str, kq_str))

    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
