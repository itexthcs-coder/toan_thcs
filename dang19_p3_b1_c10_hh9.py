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


def bt_dang19_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (Decimal('1.5'), Decimal('2'), Decimal('2.5'), 80),
            (Decimal('1.5'), Decimal('2'), Decimal('2.5'), 120),
            (Decimal('3'), Decimal('4'), Decimal('5'), 50),
            (Decimal('3'), Decimal('4'), Decimal('5'), 60)
        ]
        r_val, h_val, l_val, gia_nghin = random.choice(cau_hinh)
        sxq_pi = r_val * l_val
        sxq_m2 = sxq_pi * Decimal('3.14')
        tien_nghin = (sxq_m2 * Decimal(str(gia_nghin))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

        def fmt(val):
            s = f"{val:f}".rstrip('0').rstrip('.')
            return s.replace('.', ',')

        r_s = fmt(r_val)
        h_s = fmt(h_val)
        l_s = fmt(l_val)
        sxq_pi_s = fmt(sxq_pi)
        sxq_m2_s = fmt(sxq_m2)
        kq_str = str(tien_nghin)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc lều cắm trại có dạng hình nón với bán kính đáy bằng $%s\\text{ m}$ và chiều cao bằng $%s\\text{ m}$ (như hình vẽ). Biết giá vải bạt chống thấm để may toàn bộ mặt xung quanh của lều (không tính đáy lều và phần mép may) là $%s\\,000\\text{ đồng/m}^2$. Tính số tiền vải bạt cần dùng để may chiếc lều đó theo đơn vị nghìn đồng (làm tròn kết quả đến hàng đơn vị, lấy $\\pi \\approx 3,14$).
\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (S) at (0,2.6);
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.6,0);
\\coordinate (B) at (1.6,0);
\\draw[line width=1pt] (S)--(A) (S)--(B);
\\draw[line width=1pt] (-1.6,0) arc (180:360:1.6 and 0.35);
\\draw[line width=1pt, dashed] (1.6,0) arc (0:180:1.6 and 0.35);
\\draw[line width=1pt, dashed] (S)--(O)--(B);
\\node[left] at (0,1.3) {$h$};
\\node[below] at (0.8,0) {$r$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_s, h_s, gia_nghin))

        # Nội dung lời giải
        loigiai = ('''Độ dài đường sinh của chiếc lều hình nón là:
$$l = \\sqrt{r^2 + h^2} = \\sqrt{(%s)^2 + (%s)^2} = %s\\text{ (m)}.$$
Diện tích vải bạt cần dùng để may mặt xung quanh chiếc lều là:
$$S_{xq} = \\pi r l = \\pi \\cdot %s \\cdot %s = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (m}^2\\text{)}.$$
Số tiền vải bạt cần dùng là:
$$%s \\cdot %s \\approx %s\\text{ (nghìn đồng)}.$$'''
                   % (r_s, h_s, l_s, r_s, l_s, sxq_pi_s, sxq_pi_s, sxq_m2_s, sxq_m2_s, gia_nghin, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
