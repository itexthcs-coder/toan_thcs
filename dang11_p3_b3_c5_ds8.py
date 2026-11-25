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

def bt_dang11_p3_b3_c5_ds8(self):
    # Dạng 11: Tìm số lượng thành phần khi biết tổng hai phần đối lập trên biểu đồ hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p_xmd = 24
        p_xdd = 18
        p_xm_tong = 70
        p_xd_tong = 100 - p_xm_tong # 30
        p_xdt = p_xd_tong - p_xdd # 12
        p_xmx = p_xm_tong - p_xmd # 46
        diff_xd = p_xdd - p_xdt # 6
        
        hieu_xd = random.choice([30, 36, 42, 48])
        tong_xe = int(hieu_xd * 100 // diff_xd)
        so_xmx = int(tong_xe * p_xmx // 100)
        kq_str = str(so_xmx)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.9) arc (0:86.4:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!25] (0,0) -- (86.4:1.9) arc (86.4:252:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!40] (0,0) -- (252:1.9) arc (252:316.8:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (316.8:1.9) arc (316.8:360:1.9) -- cycle;\n' +
            '\\node at (43:1.2) {$24\\%%$};\n' +
            '\\node at (169:1.15) {$x\\%%$};\n' +
            '\\node at (284:1.25) {$18\\%%$};\n' +
            '\\node at (338:1.35) {$y\\%%$};\n' +
            '\\draw[line width=1pt, fill=black!10] (2.6,1.2) rectangle (3.0,1.5) node[right, yshift=-4pt] {Xe máy điện};\n' +
            '\\draw[line width=1pt, fill=black!25] (2.6,0.4) rectangle (3.0,0.7) node[right, yshift=-4pt] {Xe máy xăng};\n' +
            '\\draw[line width=1pt, fill=black!40] (2.6,-0.4) rectangle (3.0,-0.1) node[right, yshift=-4pt] {Xe đạp điện};\n' +
            '\\draw[line width=1pt, fill=white] (2.6,-1.2) rectangle (3.0,-0.9) node[right, yshift=-4pt] {Xe đạp thường};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây thống kê tỉ lệ các loại phương tiện gửi tại một bãi xe thông minh:\n' +
                         tikz_code + '\n' +
                         'Biết số lượng xe đạp thường ít hơn số lượng xe đạp điện là $%s$ chiếc và tổng số xe máy (gồm cả xe máy điện và xe máy xăng) chiếm $70\\%%$ tổng số xe trong bãi. Tính số lượng xe máy xăng đang gửi tại bãi.' % hieu_xd)
        
        loigiai = ('Vì tổng số xe máy chiếm $70\\%%$ tổng số xe nên tổng số xe đạp chiếm: $100\\%% - 70\\%% = 30\\%%$.\\\\' +
                   'Tỉ lệ xe đạp thường là: $y\\%% = 30\\%% - 18\\%% = 12\\%%$.\\\\' +
                   'Chênh lệch tỉ lệ giữa xe đạp điện và xe đạp thường là $18\\%% - 12\\%% = 6\\%%$ ứng với $%s$ chiếc, do đó tổng số xe trong bãi là:\\\\' +
                   '$$\\dfrac{%s}{6\\%%} = %s \\text{ (chiếc)}.$$\\\\' +
                   'Tỉ lệ xe máy xăng là: $x\\%% = 70\\%% - 24\\%% = 46\\%%$.\\\\' +
                   'Vậy số lượng xe máy xăng đang gửi tại bãi là: $%s \\cdot 46\\%% = %s$ (chiếc).'
                   ) % (hieu_xd, hieu_xd, tong_xe, tong_xe, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
