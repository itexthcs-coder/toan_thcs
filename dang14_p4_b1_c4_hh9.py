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


def bt_dang14_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bc = 2 * randint(4, 12)
        k = bc // 2

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (H) at (1.8,0);
    \\coordinate (C) at (4.9,0);
    \\coordinate (A) at (1.8,3.1);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt, dashed] (A)--(H);
    \\draw[line width=1pt] (1.8,0.3)--(2.1,0.3)--(2.1,0);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\node[above right] at (0.2,0) {$60^\\circ$};
    \\node[above left] at (4.5,0) {$45^\\circ$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác nhọn $ABC$ có cạnh $BC = %s\\text{ cm}$, $\\widehat{B} = 60^\\circ$ và $\\widehat{C} = 45^\\circ$. Kẻ đường cao $AH$ ($H \\in BC$). %s \\\\
a) Tính độ dài đường cao $AH$. \\\\
b) Tính độ dài các cạnh $AB$, $AC$ và diện tích tam giác $ABC$.'''
                         % (str(bc), hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
\\item Đặt $AH = x$ ($x > 0$). \\\\
Xét tam giác $ABH$ vuông tại $H$ có $\\widehat{B} = 60^\\circ$, ta có: \\\\
$\\tan B = \\dfrac{AH}{BH} \\Rightarrow BH = \\dfrac{AH}{\\tan 60^\\circ} = \\dfrac{x}{\\sqrt{3}}$. \\\\
Xét tam giác $ACH$ vuông tại $H$ có $\\widehat{C} = 45^\\circ$, suy ra tam giác $ACH$ vuông cân tại $H$, do đó $CH = AH = x$. \\\\
Vì tam giác $ABC$ nhọn nên điểm $H$ nằm giữa $B$ và $C$, suy ra: \\\\
$BH + CH = BC \\Leftrightarrow \\dfrac{x}{\\sqrt{3}} + x = %s \\Leftrightarrow x\\left(\\dfrac{1 + \\sqrt{3}}{\\sqrt{3}}\\right) = %s$. \\\\
Suy ra $x = \\dfrac{%s\\sqrt{3}}{\\sqrt{3} + 1} = \\dfrac{%s\\sqrt{3}(\\sqrt{3} - 1)}{2} = %s(3 - \\sqrt{3})\\text{ (cm)}$. \\\\
Vậy $AH = %s(3 - \\sqrt{3})\\text{ cm}$. \n
\\item Xét tam giác $ABH$ vuông tại $H$, ta có: \\\\
$AB = \\dfrac{AH}{\\sin 60^\\circ} = \\dfrac{%s(3 - \\sqrt{3})}{\\dfrac{\\sqrt{3}}{2}} = %s(\\sqrt{3} - 1)\\text{ (cm)}$. \\\\
Xét tam giác $ACH$ vuông cân tại $H$, ta có: \\\\
$AC = \\dfrac{AH}{\\sin 45^\\circ} = %s(3 - \\sqrt{3})\\sqrt{2}\\text{ (cm)}$. \\\\
Diện tích tam giác $ABC$ là: \\\\
$S_{ABC} = \\dfrac{1}{2} \\cdot AH \\cdot BC = \\dfrac{1}{2} \\cdot %s(3 - \\sqrt{3}) \\cdot %s = %s(3 - \\sqrt{3})\\text{ (cm}^2\\text{)}$. \n
\\end{enumEX} \n'''
                   % (str(bc), str(bc), str(bc), str(bc), str(k), str(k),
                      str(k), str(2 * k), str(k),
                      str(k), str(bc), str(k * bc // 2)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \end{minipage} \n\n')
    return content
