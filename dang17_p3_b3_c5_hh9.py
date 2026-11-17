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


def bt_dang17_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(6, 1.5, '1,5', 3.75, '3,75'), (8, 2, '2', 5, '5'), (6, 1, '1', 5, '5'), (8, 1, '1', 8.5, '8,5'), (4, 1, '1', 2.5, '2,5')]
        a, h, h_str, R, R_str = random.choice(bo_so)
        half_a = a // 2
        alpha_deg = math.degrees(math.asin(half_a / R))
        n_deg = 2 * alpha_deg
        val = (n_deg / 180) * 3.14 * R
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cổng chào có phần mái vòm phía trên là một cung tròn có chiều rộng nhịp (độ dài dây cung căng ngang chân vòm) là $%d\\text{ m}$ và chiều cao thông thủy của vòm (khoảng cách từ điểm cao nhất của vòm xuống dây cung) là $%s\\text{ m}$. Tính độ dài cung tròn của mái vòm đó theo đơn vị mét (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần trăm).
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\draw[ultra thick] (35:2.4) arc (35:145:2.4);
\\draw (35:2.4) -- (145:2.4);
\\draw[dashed] (0,0) -- (35:2.4);
\\draw[dashed] (0,0) -- (145:2.4);
\\draw[dashed] (0,0) -- (0,2.4);
\\fill (0,0) circle (1.5pt) node[below] {$O$};
\\fill (0,1.38) circle (1.5pt) node[below left] {$H$};
\\fill (0,2.4) circle (1.5pt) node[above] {$C$};
\\node[left] at (145:2.4) {$A$};
\\node[right] at (35:2.4) {$B$};
\\end{tikzpicture}
\\end{center}''' % (a, h_str))

        # Nội dung lời giải
        loigiai = ('''Mô hình hóa mái vòm bởi cung tròn $ACB$ tâm $O$, bán kính $R$, dây cung $AB = %d\\text{ m}$, $H$ là trung điểm của $AB$ và $C$ là điểm cao nhất của vòm ($HC = %s\\text{ m}$). \\\\
Ta có $OH \\perp AB$, $AH = \\dfrac{AB}{2} = %d\\text{ m}$ và $OH = R - %s$. \\\\
Áp dụng định lí Pythagore trong tam giác $OAH$ vuông tại $H$, ta có:
$$R^2 = AH^2 + OH^2 \\Leftrightarrow R^2 = %d^2 + (R - %s)^2 \\Leftrightarrow R = %s\\text{ (m)}.$$
Trong tam giác vuông $OAH$, ta có $\\sin\\widehat{AOH} = \\dfrac{AH}{OA} = \\dfrac{%d}{%s} \\Rightarrow \\widehat{AOH} \\approx %.2f^\\circ \\Rightarrow \\widehat{AOB} = 2\\widehat{AOH} \\approx %.2f^\\circ$. \\\\
Độ dài cung tròn của mái vòm là:
$$l = \\dfrac{\\widehat{AOB}}{180^\\circ}\\pi R \\approx \\dfrac{%.2f}{180} \\cdot 3,14 \\cdot %s \\approx %s\\text{ (m)}.$$''' % (
            a, h_str, half_a, h_str, half_a, h_str, R_str, half_a, R_str, alpha_deg, n_deg, n_deg, R_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
