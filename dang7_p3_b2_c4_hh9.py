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


def bt_dang7_p3_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        sau = random.choice([150, 200, 250, 300])
        goc = 21
        v_kmh = 9
        v_ms = 2.5
        v_ms_str = '2,5'

        qd_val = sau / math.sin(math.radians(goc))
        tg_val = qd_val / v_ms

        qd_str = str(Decimal(str(qd_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        number = Decimal(str(tg_val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (H) at (4.2,0);
    \\coordinate (B) at (4.2,-1.6);
    \\draw[line width=1pt] (A)--(H) (A)--(B);
    \\draw[line width=1pt, dashed] (H)--(B);
    \\draw[line width=1pt] (3.98,0)--(3.98,-0.22)--(4.2,-0.22);
    \\draw[line width=1pt] (0.65,0) arc (0:-21:0.65);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (H) circle (1pt) node[above right] {$H$};
    \\fill (B) circle (1pt) node[below right] {$B$};
    \\node[right] at (4.2,-0.8) {$%s\\text{ m}$};
    \\node at (0.98,-0.18) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (sau, goc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong một buổi tập trận, một tàu ngầm đang ở trên mặt biển tại điểm $A$ bắt đầu di chuyển theo đường thẳng tạo với mặt nước biển một góc $%s^\\circ$ để lặn xuống với tốc độ không đổi $%s\\text{ km/h}$ (như hình vẽ). Hỏi sau bao nhiêu giây (kể từ lúc bắt đầu lặn) thì tàu ngầm ở độ sâu $%s\\text{ m}$ so với mặt nước biển (làm tròn kết quả đến hàng đơn vị)?
    %s''' % (goc, v_kmh, sau, hinhve))

        # Nội dung lời giải
        loigiai = ('''Gọi $B$ là vị trí tàu ngầm khi ở độ sâu $BH = %s\\text{ m}$ so với mặt nước biển $AH$.\\\\
    Xét tam giác $ABH$ vuông tại $H$, ta có $BH = AB \\cdot \\sin \\widehat{BAH}$.\\\\
    Suy ra quãng đường tàu ngầm đã di chuyển là $AB = \\dfrac{BH}{\\sin %s^\\circ} = \\dfrac{%s}{\\sin %s^\\circ} \\approx %s\\text{ (m)}$.\\\\
    Đổi vận tốc $v = %s\\text{ km/h} = %s\\text{ m/s}$.\\\\
    Vậy thời gian để tàu ngầm đạt độ sâu $%s\\text{ m}$ là $t = \\dfrac{AB}{v} \\approx \\dfrac{%s}{%s} \\approx %s\\text{ (giây)}$.'''
                   % (sau, goc, sau, goc, qd_str,
                      v_kmh, v_ms_str,
                      sau, qd_str, v_ms_str, str(kq_str)))

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
