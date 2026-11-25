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


def bt_dang19_p3_b2_c5_ds8(self):
    # Dạng 19 (Vận dụng): Tính tỉ lệ phần trăm giảm từ mốc đầu đến mốc cuối trên biểu đồ đoạn thẳng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t9 = random.choice([2000, 2500, 3000])
        pct_giam = random.choice([48, 52, 56, 60])
        t12 = t9 - (t9 * pct_giam // 100)
        t10 = t9 - (t9 * 20 // 100)
        t11 = (t10 + t12) // 2
        kq_str = str(pct_giam)
        
        s9 = f"{t9:,}".replace(",", "\\,")
        s10 = f"{t10:,}".replace(",", "\\,")
        s11 = f"{t11:,}".replace(",", "\\,")
        s12 = f"{t12:,}".replace(",", "\\,")
        s_diff = f"{(t9 - t12):,}".replace(",", "\\,")
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.6) node[above] {Số túi};
        \\draw[line width=1pt, ->] (0,0) -- (5.6,0) node[right] {Tháng};
        \\coordinate (A) at (0.9,2.2);
        \\coordinate (B) at (2.2,1.6);
        \\coordinate (C) at (3.5,1.1);
        \\coordinate (D) at (4.8,0.6);
        \\draw[line width=1pt] (A)--(B)--(C)--(D);
        \\fill (A) circle (1pt) node[above right] {$%s$};
        \\fill (B) circle (1pt) node[above right] {$%s$};
        \\fill (C) circle (1pt) node[above right] {$%s$};
        \\fill (D) circle (1pt) node[above right] {$%s$};
        \\node[below] at (0.9,0) {Tháng 9};
        \\node[below] at (2.2,0) {Tháng 10};
        \\node[below] at (3.5,0) {Tháng 11};
        \\node[below] at (4.8,0) {Tháng 12};
        \\end{tikzpicture}
        \\end{center}""" % (s9, s10, s11, s12))
        
        noidungcauhoi = (
            "Biểu đồ đoạn thẳng dưới đây theo dõi lượng túi ni-lông một cửa hàng phát miễn phí cho khách qua các tháng nhờ chiến dịch ``Sống xanh'':"
            + tikz_code +
            "Hỏi lượng túi ni-lông phát ra trong tháng $12$ đã giảm bao nhiêu phần trăm so với tháng $9$?"
        )
        
        loigiai = ("""Quan sát biểu đồ đoạn thẳng, lượng túi ni-lông phát ra tháng $9$ là $%s$ túi và tháng $12$ là $%s$ túi.\\\\
        Lượng túi ni-lông tháng $12$ giảm đi so với tháng $9$ là:
        $$%s - %s = %s \\text{ (túi)}.$$
        Tỉ lệ phần trăm lượng túi ni-lông phát ra trong tháng $12$ giảm so với tháng $9$ là:
        $$\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$"""
                   % (s9, s12, s9, s12, s_diff, s_diff, s9, pct_giam))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
