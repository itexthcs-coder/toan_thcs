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


def bt_dang16_p3_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        nua_rong, cao, r_val = random.choice([(1.6, 3.0, 3.4), (1.5, 2.0, 2.5), (1.2, 1.6, 2.0), (2.4, 3.2, 4.0)])
        rong = 2 * nua_rong
        don_gia = random.choice([200, 250, 300])
        rong_str = str(rong).replace('.', ',')
        nua_rong_str = str(nua_rong).replace('.', ',')
        cao_str = str(cao).replace('.0', '').replace('.', ',')
        r_str = str(r_val).replace('.', ',')
        chieu_dai = Decimal(str(3.14 * r_val))
        chi_phi = (chieu_dai * Decimal(str(don_gia))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(chi_phi)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (M) at (-2.4,0);
\\coordinate (N) at (2.4,0);
\\coordinate (A) at (-1.3,0);
\\coordinate (B) at (1.3,0);
\\coordinate (C) at (1.3,2);
\\coordinate (D) at (-1.3,2);
\\draw[line width=1pt] (N) arc (0:180:2.4);
\\draw[line width=1pt] (M)--(N);
\\draw[line width=1pt] (A)--(D)--(C)--(B);
\\fill (O) circle (1pt) node[below] {$O$};
\\node[above] at (0,2) {$%s\\text{ m}$};
\\node[left] at (-1.3,1) {$%s\\text{ m}$};
\\end{tikzpicture}
\\end{center}''' % (rong_str, cao_str))

        noidungcauhoi = ('''Một gia đình cần làm một khung cổng sắt hình chữ nhật có chiều rộng $%s\\text{ m}$ và chiều cao $%s\\text{ m}$, phía bên ngoài được bao bởi một khung thép uốn hình nửa đường tròn đi qua hai đỉnh trên của cổng và nhận đường thẳng chứa chân cổng làm đường kính. Biết giá gia công và vật tư cho mỗi mét dài khung thép vòm là $%s\\,000$ đồng. Tính số tiền làm khung thép vòm nửa đường tròn đó (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng nghìn đồng, đơn vị: nghìn đồng).%s''' % (rong_str, cao_str, don_gia, hinhve))

        loigiai = ('''Gọi $O$ là trung điểm của đoạn thẳng nối hai chân cổng. Khoảng cách từ $O$ đến mỗi chân cổng là $\\dfrac{%s}{2} = %s\\text{ (m)}$.\\\\
Áp dụng định lí Pythagore, bán kính của vòm nửa đường tròn là:\\\\
$R = \\sqrt{%s^2 + %s^2} = %s\\text{ (m)}$.\\\\
Chiều dài khung thép uốn thành nửa đường tròn là $L = \\pi R \\approx 3,14 \\cdot %s = %s\\text{ (m)}$.\\\\
Số tiền làm khung thép vòm nửa đường tròn đó là $%s \\cdot %s \\approx %s\\text{ (nghìn đồng)}$.''' % (rong_str, nua_rong_str, nua_rong_str, cao_str, r_str, r_str, str(chieu_dai).replace('.', ','), str(chieu_dai).replace('.', ','), don_gia, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
