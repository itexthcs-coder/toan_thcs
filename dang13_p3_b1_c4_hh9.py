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


def bt_dang13_p3_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        rong = randint(15, 45) * 10
        goc = randint(35, 70)
        quang_duong = rong / math.sin(math.radians(goc))
        number = Decimal(str(quang_duong))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(int(kq))
        qd_1tp = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        qd_1tp_str = str(qd_1tp).replace('.', ',')

        # Hình vẽ TikZ
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (H) at (0,2.5);
    \\coordinate (B) at (2.2,2.5);
    \\draw[line width=1pt] (-0.8,0)--(3.2,0);
    \\draw[line width=1pt] (-0.8,2.5)--(3.2,2.5);
    \\draw[line width=1pt, dashed] (A)--(H);
    \\draw[line width=1pt] (A)--(B);
    \\draw[line width=1pt] (0,2.2)--(0.3,2.2)--(0.3,2.5);
    \\fill (A) circle (1pt) node[below] {$A$};
    \\fill (H) circle (1pt) node[above] {$H$};
    \\fill (B) circle (1pt) node[above] {$B$};
    \\node[left] at (0,1.25) {$%s\\text{ m}$};
    \\node[above right] at (0.2,0) {$%s^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (str(rong), str(goc)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một con thuyền đi qua một khúc sông rộng $%s\\text{ m}$. Do dòng nước chảy mạnh nên đường đi của thuyền tạo với bờ sông một góc $%s^\\circ$. Tính quãng đường thực tế thuyền đã đi được để sang tới bờ bên kia (đơn vị: mét, làm tròn đến hàng đơn vị). %s'''
                         % (str(rong), str(goc), hinh_ve))

        # Nội dung lời giải
        loigiai = ('''Gọi $A$ là điểm xuất phát, $B$ là điểm thuyền cập bến ở bờ bên kia và $AH = %s\\text{ m}$ là chiều rộng khúc sông ($AH \\perp HB$). \\\\
Vì hai bờ sông song song nên góc tạo bởi đường đi $AB$ với bờ sông bằng $\\widehat{ABH} = %s^\\circ$. \\\\
Xét tam giác $AHB$ vuông tại $H$, ta có: \\\\
$\\sin \\widehat{ABH} = \\dfrac{AH}{AB}$. \\\\
Suy ra quãng đường thuyền đi được là: \\\\
$AB = \\dfrac{AH}{\\sin %s^\\circ} = \\dfrac{%s}{\\sin %s^\\circ} \\approx %s\\text{ (m)}$. \\\\
Làm tròn đến hàng đơn vị, quãng đường thuyền đi được là $%s\\text{ m}$.'''
                   % (str(rong), str(goc), str(goc), str(rong), str(goc), qd_1tp_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \end{minipage} \n\n')
    return content
