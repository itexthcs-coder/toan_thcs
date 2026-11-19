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


def bt_dang13_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(4, 15)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (-2,0);\n'
            '\\coordinate (B) at (2,0);\n'
            '\\coordinate (C) at (125:2);\n'
            '\\coordinate (H) at ($(A)!(C)!(B)$);\n'
            '\\draw[line width=1pt] (2,0) arc (0:180:2cm) -- cycle;\n'
            '\\draw[line width=1pt] (A)--(C)--(B) (C)--(H);\n'
            '\\draw[line width=1pt, dashed] (O)--(C);\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho nửa đường tròn $(O; %s\\text{ cm})$ đường kính $AB$. Lấy điểm $C$ di động trên nửa đường tròn ($C$ khác $A, B$). Kẻ $CH \\perp AB$ tại $H$ như hình vẽ.\\\\'
            'a) Chứng minh $\\widehat{ACB} = 90^\\circ$ và $CH^2 = HA \\cdot HB$.\\\\'
            'b) Tìm vị trí của điểm $C$ trên nửa đường tròn để độ dài đoạn thẳng $CH$ đạt giá trị lớn nhất và tính giá trị lớn nhất đó.\\\\'
            'c) Tìm vị trí của điểm $C$ trên nửa đường tròn để chu vi tam giác $ABC$ đạt giá trị lớn nhất.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong nửa đường tròn $(O; %s\\text{ cm})$ đường kính $AB$, góc nội tiếp $\\widehat{ACB}$ chắn nửa đường tròn nên $\\widehat{ACB} = 90^\\circ$.\\\\'
            'Xét hai tam giác vuông $\\triangle CHA$ và $\\triangle BHC$ có $\\widehat{HCA} = \\widehat{HBC}$ (cùng phụ với $\\widehat{HAC}$) nên $\\triangle CHA \\backsim \\triangle BHC$ (g.g), suy ra $\\dfrac{CH}{HB} = \\dfrac{HA}{CH} \\Rightarrow CH^2 = HA \\cdot HB$.\n'
            '\\item Xét $\\triangle OCH$ vuông tại $H$ (hoặc $H \\equiv O$), ta luôn có $CH \\le OC = %s\\text{ cm}$.\\\\'
            'Dấu ``=\" xảy ra khi và chỉ khi $H \\equiv O$, tức là $OC \\perp AB$ hay $C$ là điểm chính giữa của nửa đường tròn. Vậy $CH$ đạt giá trị lớn nhất bằng $%s\\text{ cm}$.\n'
            '\\item Chu vi $\\triangle ABC$ là $P = AB + AC + BC = %s + AC + BC$. Do đó $P$ lớn nhất khi $AC + BC$ lớn nhất.\\\\'
            'Áp dụng bất đẳng thức $(AC - BC)^2 \\ge 0$, ta có $(AC + BC)^2 \\le 2(AC^2 + BC^2) = 2AB^2 = 2 \\cdot %s^2 = %s \\Rightarrow AC + BC \\le %s\\sqrt{2}\\text{ cm}$.\\\\'
            'Dấu ``=\" xảy ra khi $AC = BC$, tức là $C$ là điểm chính giữa của nửa đường tròn $(O)$. Vậy chu vi $\\triangle ABC$ đạt giá trị lớn nhất bằng $(%s + %s\\sqrt{2})\\text{ cm}$ khi $C$ nằm chính giữa nửa đường tròn.\n'
            '\\end{enumEX}'
            % (R, R, R, 2 * R, 2 * R, 2 * (2 * R) * (2 * R), 2 * R, 2 * R, 2 * R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
