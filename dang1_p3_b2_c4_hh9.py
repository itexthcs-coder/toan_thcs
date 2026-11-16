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


def bt_dang1_p3_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2, 3])
        hb = 3 * k
        hc = 6 * k
        ah_sym = 2 * k * sqrt(3)
        ac_sym = 4 * k * sqrt(3)
        ab_sym = k * sqrt(21)

        ah_val = 2 * k * math.sqrt(3)
        ac_val = 4 * k * math.sqrt(3)
        ab_val = k * math.sqrt(21)
        bc_val = 9 * k
        cv_val = ab_val + ac_val + bc_val

        number = Decimal(str(cv_val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (H) at (1.5,0);
    \\coordinate (C) at (4.5,0);
    \\coordinate (A) at (1.5,1.73);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(H);
    \\draw[line width=1pt] (1.5,0.22)--(1.72,0.22)--(1.72,0);
    \\draw[line width=1pt] (1.5,1.25) arc (270:330:0.48);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\node[below] at (0.75,0) {$%s\\text{ cm}$};
    \\node[below] at (3.0,0) {$%s\\text{ cm}$};
    \\node at (1.82,1.15) {$60^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (hb, hc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ có chân đường cao $AH$ nằm giữa $B$ và $C$. Biết $HB = %s\\text{ cm}$, $HC = %s\\text{ cm}$ và $\\widehat{HAC} = 60^\\circ$ (như hình vẽ). Tính chu vi của tam giác $ABC$ theo đơn vị xentimét (làm tròn kết quả đến hàng phần mười).
    %s''' % (hb, hc, hinhve))

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $AHC$ vuông tại $H$, ta có:\\\\
    $AH = HC \\cdot \\cot \\widehat{HAC} = %s \\cdot \\cot 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{3} = %s\\text{ (cm)}$.\\\\
    $AC = \\dfrac{HC}{\\sin \\widehat{HAC}} = \\dfrac{%s}{\\sin 60^\\circ} = \\dfrac{%s}{\\dfrac{\\sqrt{3}}{2}} = %s\\text{ (cm)}$.\\\\
    Xét tam giác $ABH$ vuông tại $H$, áp dụng định lí Pythagore ta có:\\\\
    $AB = \\sqrt{HB^2 + AH^2} = \\sqrt{%s^2 + (%s)^2} = %s\\text{ (cm)}$.\\\\
    Ta có $BC = HB + HC = %s + %s = %s\\text{ (cm)}$.\\\\
    Vậy chu vi tam giác $ABC$ là $P = AB + BC + AC = %s + %s + %s \\approx %s\\text{ (cm)}$.'''
                   % (hc, hc, latex(ah_sym),
                      hc, hc, latex(ac_sym),
                      hb, latex(ah_sym), latex(ab_sym),
                      hb, hc, bc_val,
                      latex(ab_sym), bc_val, latex(ac_sym), str(kq_str)))

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
