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


def bt_dang6_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
        a0, b0, c0 = random.choice(bo_so)
        oa = a0
        ob = b0
        ab = c0
        d_val = Rational(oa * ob, ab)
        r_val = random.choice([d_val, d_val - 1, d_val + 1])
        d_dec = Decimal(str(float(d_val))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
        r_dec = Decimal(str(float(r_val))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
        d_str = str(d_dec).replace('.', ',')
        r_str = str(r_dec).replace('.', ',')

        if d_val < r_val:
            ket_luan = "vì $d < R$ nên đường thẳng $AB$ và đường tròn $(O; %s)$ cắt nhau tại hai điểm phân biệt." % r_str
        elif d_val == r_val:
            ket_luan = "vì $d = R$ nên đường thẳng $AB$ và đường tròn $(O; %s)$ tiếp xúc với nhau." % r_str
        else:
            ket_luan = "vì $d > R$ nên đường thẳng $AB$ và đường tròn $(O; %s)$ không giao nhau." % r_str

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(%s; 0)$ và $B(0; %s)$. Xác định vị trí tương đối của đường thẳng $AB$ và đường tròn tâm $O$ bán kính $R = %s$. \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (O) at (0,0);
            \\coordinate (A) at (2.4,0);
            \\coordinate (B) at (0,3.2);
            \\coordinate (H) at (1.536,1.152);
            \\draw[line width=1pt, ->] (-2.5,0)--(3.5,0) node[below] {$x$};
            \\draw[line width=1pt, ->] (0,-2.5)--(0,4) node[left] {$y$};
            \\draw[line width=1pt] (O) circle (1.92);
            \\draw[line width=1pt] (-0.8,4.26)--(3.2,-1.06);
            \\draw[line width=1pt, dashed] (O)--(H);
            \\fill (O) circle (1pt) node[below left] {$O$};
            \\fill (A) circle (1pt) node[below] {$A$};
            \\fill (B) circle (1pt) node[left] {$B$};
            \\fill (H) circle (1pt) node[above right] {$H$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(oa), latex(ob), r_str))

        # Nội dung lời giải
        loigiai = ('''Trên mặt phẳng tọa độ $Oxy$, điểm $A(%s; 0)$ nằm trên trục $Ox$ và điểm $B(0; %s)$ nằm trên trục $Oy$ nên tam giác $OAB$ vuông tại $O$ với $OA = %s$ và $OB = %s$. \\\\
        Áp dụng định lí Pythagore trong tam giác vuông $OAB$: \\\\
        $AB = \\sqrt{OA^2 + OB^2} = \\sqrt{%s^2 + %s^2} = %s$. \\\\
        Kẻ $OH \\perp AB$ tại $H$. Khoảng cách từ tâm $O$ đến đường thẳng $AB$ chính là độ dài đường cao $OH$. \\\\
        Áp dụng hệ thức lượng trong tam giác vuông $OAB$, ta có: \\\\
        $OH \\cdot AB = OA \\cdot OB \\Rightarrow d = OH = \\dfrac{%s \\cdot %s}{%s} = %s$. \\\\
        So sánh khoảng cách $d = %s$ với bán kính $R = %s$, %s'''
        %(latex(oa), latex(ob), latex(oa), latex(ob), latex(oa), latex(ob), latex(ab), latex(oa), latex(ob), latex(ab), d_str, d_str, r_str, ket_luan))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
