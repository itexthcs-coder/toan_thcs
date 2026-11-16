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


def bt_dang14_p3_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bong1 = random.choice([20, 25, 30])
        g1 = 40
        g2 = 60
        cao_val = bong1 * math.tan(math.radians(g1))
        bong2_val = cao_val / math.tan(math.radians(g2))

        cao_str = str(Decimal(str(cao_val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',')
        number = Decimal(str(bong2_val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (C) at (0,0);
    \\coordinate (D) at (1.5,0);
    \\coordinate (B) at (3.6,0);
    \\coordinate (A) at (3.6,3.0);
    \\draw[line width=1pt] (C)--(B)--(A)--cycle (A)--(D);
    \\draw[line width=1pt] (3.38,0)--(3.38,0.22)--(3.6,0.22);
    \\draw[line width=1pt] (0.65,0) arc (0:40:0.65);
    \\draw[line width=1pt] (2.0,0) arc (0:60:0.5);
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (B) circle (1pt) node[below right] {$B$};
    \\fill (C) circle (1pt) node[below left] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\node[below] at (1.8,-0.25) {$%s\\text{ m}$};
    \\node at (0.95,0.22) {$%s^\\circ$};
    \\node at (2.25,0.3) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (bong1, g1, g2))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Vào buổi sáng, khi tia nắng mặt trời tạo với mặt đất một góc $%s^\\circ$ thì bóng $BC$ của một cái cây $AB$ trên mặt đất dài $%s\\text{ m}$. Đến buổi trưa, khi tia nắng mặt trời tạo với mặt đất một góc $%s^\\circ$ thì bóng $BD$ của cái cây đó trên mặt đất dài bao nhiêu mét (như hình vẽ, làm tròn kết quả đến hàng phần mười)?
    %s''' % (g1, bong1, g2, hinhve))

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $ABC$ vuông tại $B$, chiều cao của cây là:\\\\
    $AB = BC \\cdot \\tan C = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ (m)}$.\\\\
    Xét tam giác $ABD$ vuông tại $B$, chiều dài bóng cây vào buổi trưa là:\\\\
    $BD = AB \\cdot \\cot \\widehat{ADB} \\approx %s \\cdot \\cot %s^\\circ = \\dfrac{%s}{\\sqrt{3}} \\approx %s\\text{ (m)}$.'''
                   % (bong1, g1, cao_str,
                      cao_str, g2, cao_str, str(kq_str)))

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
