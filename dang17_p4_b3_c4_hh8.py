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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang17_p4_b3_c4_hh8(self):
    # Dạng 17: Đo chiều rộng khúc sông hoặc ao cá bằng phương pháp đường trung bình (Thực tế)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_pythagore = [
            (240, 320, 400, 120, 160, 200, 9600),
            (180, 240, 300, 90, 120, 150, 5400),
            (300, 400, 500, 150, 200, 250, 15000)
        ]
        ab, ac, bc, ap, aq, pq, dt = random.choice(bo_pythagore)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,3.2);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4.6,0);\n'
            '\\coordinate (P) at ($(A)!0.5!(B)$);\n'
            '\\coordinate (Q) at ($(A)!0.5!(C)$);\n'
            '\\draw[line width=1pt, dashed] (A)--(B)--(C)--cycle;\n'
            '\\draw[line width=1pt] (P)--(Q);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (P) circle (1pt) node[left] {$P$};\n'
            '\\fill (Q) circle (1pt) node[above right] {$Q$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Để đo khoảng cách giữa hai cọc mốc $P$ và $Q$ nằm ở hai bên bờ một hồ nước, đội khảo sát chọn một điểm $A$ trên bãi đất trống rồi xác định hai điểm $B, C$ sao cho $P$ là trung điểm của $AB$ và $Q$ là trung điểm của $AC$. Họ đo được $AB = %s\\text{ m}$, $AC = %s\\text{ m}$ và $BC = %s\\text{ m}$.\\\\\n'
            'a) Tính khoảng cách thực tế giữa hai cọc mốc $P$ và $Q$.\\\\\n'
            'b) Chứng minh tam giác $APQ$ vuông tại $P$ và tính diện tích tam giác $APQ$.\n%s'
            % (ab, ac, bc, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1} \n'
            '\\item Trong tam giác $ABC$, vì $P$ là trung điểm của $AB$ và $Q$ là trung điểm của $AC$ nên $PQ$ là đường trung bình của tam giác $ABC$.\\\\'
            'Theo tính chất đường trung bình của tam giác, khoảng cách giữa hai cọc mốc $P$ và $Q$ là $PQ = \\frac{1}{2}BC = \\frac{1}{2} \\cdot %s = %s\\text{ m}$. \n'
            '\\item Ta có $AP = \\frac{1}{2}AB = %s\\text{ m}$, $AQ = \\frac{1}{2}AC = %s\\text{ m}$ và $PQ = %s\\text{ m}$.\\\\'
            'Xét tam giác $APQ$ có $AP^2 + PQ^2 = %s^2 + %s^2 = %s = %s^2 = AQ^2$.\\\\'
            'Theo định lí Pythagore đảo, tam giác $APQ$ vuông tại $P$.\\\\'
            'Diện tích tam giác $APQ$ vuông tại $P$ là $S_{\\Delta APQ} = \\frac{1}{2} \\cdot AP \\cdot PQ = \\frac{1}{2} \\cdot %s \\cdot %s = %s\\text{ m}^2$. \n'
            '\\end{enumEX} \n'
            % (bc, pq, ap, aq, pq, ap, pq, ap * ap + pq * pq, aq, ap, pq, dt)
        )

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
