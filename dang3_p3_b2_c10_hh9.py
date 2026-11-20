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


def bt_dang3_p3_b2_c10_hh9(self):
    # O nằm giữa đỉnh S và tâm H của đáy nón: R = 5k, OH = 3k => r_day = 4k, h_non = R + OH = 8k
    k = random.choice([1, 2, 3])
    R = 5 * k
    OH = 3 * k
    r_day = 4 * k
    h_non = R + OH
    # V_non = 1/3 * pi * r_day^2 * h_non = 1/3 * pi * 16k^2 * 8k = 128/3 * k^3 * pi
    # Nếu chọn k = 3 => R = 15, OH = 9, r_day = 12, h_non = 24 => V_non = 1/3 * 144 * 24 * pi = 1152*pi (<= 9999!)
    k = 3
    R = 5 * k
    OH = 3 * k
    r_day = 4 * k
    h_non = R + OH
    # Random biến thể k=3 hoặc trường hợp O nằm ngoài SH (h_non = R - OH = 2k)
    mode = random.choice([1, 2])
    if mode == 1:
        k = 3
        R, OH, r_day = 15, 9, 12
        h_non = R + OH
        V_heso = (r_day**2 * h_non) // 3
        mo_ta = 'chứa tâm $O$'
        ct_h = 'R + OH = %s + %s = %s' % (R, OH, h_non)
    else:
        k = random.choice([3, 6])
        R, OH, r_day = 5 * k, 3 * k, 4 * k
        h_non = R - OH
        V_heso = (r_day**2 * h_non) // 3
        mo_ta = 'không chứa tâm $O$'
        ct_h = 'R - OH = %s - %s = %s' % (R, OH, h_non)
    kq_str = str(V_heso)

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (S) at (0,2);
\\coordinate (H) at (0,-1.2);
\\coordinate (A) at (-1.6,-1.2);
\\coordinate (B) at (1.6,-1.2);
\\draw[line width=1pt] (O) circle (2cm);
\\draw[line width=1pt] (A) arc (180:360:1.6cm and 0.4cm);
\\draw[line width=1pt, dashed] (B) arc (0:180:1.6cm and 0.4cm);
\\draw[line width=1pt] (A)--(S)--(B);
\\draw[line width=1pt, dashed] (S)--(H)--(B) (O)--(B);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (S) circle (1pt) node[above] {$S$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (B) circle (1pt) node[right] {$B$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho hình cầu tâm $O$ bán kính $R = %s\\text{ cm}$. Một hình nón có đỉnh $S$ và đường tròn đáy tâm $H$ cùng nằm trên mặt cầu đó (đoạn thẳng $SH$ %s), biết khoảng cách $OH = %s\\text{ cm}$. Thể tích của hình nón bằng $a\\pi\\text{ cm}^3$. Tìm giá trị của $a$.%s'''
                     % (R, mo_ta, OH, hinh_ve))

    loigiai = ('''Lấy điểm $B$ nằm trên đường tròn đáy tâm $H$ của hình nón, ta có $OB = R = %s\\text{ cm}$ và $OH \\perp HB$.\\\nBán kính đáy của hình nón là:
$$r = HB = \\sqrt{OB^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Vì đoạn thẳng $SH$ %s nên chiều cao của hình nón là:
$$h = SH = %s\\text{ (cm)}.$$
Thể tích của hình nón là:
$$V = \\dfrac{1}{3}\\pi r^2 h = \\dfrac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Vậy $a = %s$.'''
               % (R, R, OH, r_day, mo_ta, ct_h, r_day, h_non, V_heso, V_heso))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
