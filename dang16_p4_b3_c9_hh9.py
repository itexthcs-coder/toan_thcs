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


def bt_dang16_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        nua_rong, cao, r_val = random.choice([(4, 3, 5), (3, 4, 5), (8, 6, 10), (12, 5, 13)])
        rong = 2 * nua_rong
        so_vom = random.choice([10, 12, 15, 20])
        don_gia = random.choice([150, 180, 200])
        chieu_dai_1 = Decimal(str(3.14 * r_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        tong_dai = Decimal(str(3.14 * r_val * so_vom))
        tong_tien = (tong_dai * Decimal(str(don_gia))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (M) at (-2.5,0);
\\coordinate (N) at (2.5,0);
\\coordinate (A) at (-1.6,0);
\\coordinate (B) at (1.6,0);
\\coordinate (C) at (1.6,1.8);
\\coordinate (D) at (-1.6,1.8);
\\draw[line width=1pt] (N) arc (0:180:2.5);
\\draw[line width=1pt] (M)--(N);
\\draw[line width=1pt] (A)--(D)--(C)--(B);
\\fill (O) circle (1pt) node[below] {$O$};
\\node[above] at (0,1.8) {$%s\\text{ m}$};
\\node[left] at (-1.6,0.9) {$%s\\text{ m}$};
\\end{tikzpicture}
\\end{center}''' % (rong, cao))

        noidungcauhoi = ('''Một trang trại nông nghiệp công nghệ cao muốn dựng một khung nhà kính có mặt cắt ngang gồm một khung chữ nhật chiều rộng $%s\\text{ m}$, chiều cao $%s\\text{ m}$ và phía bên ngoài được bao bọc bởi một vòm thép uốn cong dạng nửa đường tròn đi qua hai đỉnh phía trên của khung chữ nhật, nhận mặt đất chứa chân khung làm đường kính. \\\\
a) Tính bán kính của vòm thép hình nửa đường tròn đó. \\\\
b) Tính chiều dài thanh thép cần dùng để uốn một vòm nửa đường tròn và tổng chi phí mua thép làm $%s$ vòm như thế, biết giá thép đã bao gồm công uốn là $%s\\,000$ đồng/mét (lấy $\\pi \\approx 3,14$, làm tròn chi phí đến hàng nghìn đồng).%s''' % (rong, cao, so_vom, don_gia, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $O$ là trung điểm của đoạn thẳng nối hai chân khung chữ nhật. Khi đó $O$ là tâm của nửa đường tròn và khoảng cách từ $O$ đến mỗi chân khung là $\\dfrac{%s}{2} = %s\\text{ (m)}$.\\\\
Áp dụng định lí Pythagore, bán kính của vòm thép nửa đường tròn là:\\\\
$R = \\sqrt{%s^2 + %s^2} = %s\\text{ (m)}$.
\\item Chiều dài thanh thép cần dùng để uốn một vòm nửa đường tròn là:\\\\
$L = \\pi R \\approx 3,14 \\cdot %s = %s\\text{ (m)}$.\\\\
Tổng chiều dài thanh thép dùng cho $%s$ vòm là $%s \\cdot %s = %s\\text{ (m)}$.\\\\
Tổng chi phí mua thép làm $%s$ vòm là $%s \\cdot %s \\approx %s\\text{ (nghìn đồng)}$ (tức khoảng $%s\\,000$ đồng).
\\end{enumEX}''' % (rong, nua_rong, nua_rong, cao, r_val, r_val, str(chieu_dai_1).replace('.', ','), so_vom, str(chieu_dai_1).replace('.', ','), so_vom, str(tong_dai).replace('.', ','), so_vom, str(tong_dai).replace('.', ','), don_gia, str(tong_tien), str(tong_tien)))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
