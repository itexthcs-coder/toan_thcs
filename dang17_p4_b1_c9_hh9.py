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


def bt_dang17_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([10, 12, 16, 20, 24])
        val_OH = (R * math.sqrt(2)) / 2.0
        kq_OH = str(Decimal(str(val_OH)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (225:2);\n'
            '\\coordinate (B) at (315:2);\n'
            '\\coordinate (M) at (90:2);\n'
            '\\coordinate (N) at (-90:2);\n'
            '\\coordinate (H) at (0,-1.414);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B) (M)--(N) (A)--(M)--(B)--(N)--cycle (O)--(A) (O)--(B);\n'
            '\\fill (O) circle (1pt) node[above right] {$O$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (M) circle (1pt) node[above] {$M$};\n'
            '\\fill (N) circle (1pt) node[below] {$N$};\n'
            '\\fill (H) circle (1pt) node[below right] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Tại một nút giao thông hình vòng xuyến có đường bao ngoài là đường tròn $(O; %s\\text{ m})$, người ta đặt hai cột đèn tín hiệu tại $A$ và $B$ trên vòng xuyến sao cho khoảng cách giữa hai cột đèn là $AB = %s\\sqrt{2}\\text{ m}$. Một camera giám sát đặt tại điểm $M$ trên cung lớn $AB$ của vòng xuyến để quan sát đoạn đường giữa hai cột đèn như hình vẽ.\\'
            'a) Tính số đo góc ở tâm $\\widehat{AOB}$ và góc quan sát $\\widehat{AMB}$ của camera.\\'
            'b) Tính khoảng cách từ tâm $O$ của vòng xuyến đến đoạn thẳng nối hai cột đèn $AB$ (làm tròn đến hàng phần trăm).\\'
            'c) Lắp thêm một camera phụ tại điểm $N$ trên vòng xuyến sao cho đường thẳng $MN$ đi qua tâm $O$ và vuông góc với $AB$ ($N$ thuộc cung nhỏ $AB$). Tính diện tích tứ giác $AMBN$.\n%s'
            % (R, R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Xét $\\triangle OAB$ có $OA^2 + OB^2 = %s^2 + %s^2 = %s = (%s\\sqrt{2})^2 = AB^2$. Theo định lí Pythagore đảo, $\\triangle OAB$ vuông tại $O$, suy ra góc ở tâm $\\widehat{AOB} = 90^\\circ$.\\'
            'Góc nội tiếp $\\widehat{AMB}$ và góc ở tâm $\\widehat{AOB}$ cùng chắn cung nhỏ $AB$ nên $\\widehat{AMB} = \\dfrac{1}{2}\\widehat{AOB} = 45^\\circ$.\n'
            '\\item Gọi $H$ là giao điểm của $MN$ và $AB$. Vì $MN \\perp AB$ tại $H$ và $\\triangle OAB$ vuông cân tại $O$ nên đường cao $OH = \\dfrac{OA}{\\sqrt{2}} = \\dfrac{%s}{\\sqrt{2}} \\approx %s\\text{ m}$.\n'
            '\\item Vì $MN$ là đường kính của $(O; %s\\text{ m})$ nên $MN = 2 \\cdot %s = %s\\text{ m}$ và $MN \\perp AB$.\\'
            'Diện tích tứ giác $AMBN$ có hai đường chéo vuông góc là $S_{AMBN} = \\dfrac{1}{2} \\cdot MN \\cdot AB = \\dfrac{1}{2} \\cdot %s \\cdot %s\\sqrt{2} = %s\\sqrt{2}\\text{ m}^2$.\n'
            '\\end{enumEX}'
            % (R, R, 2 * R * R, R, R, kq_OH, R, R, 2 * R, 2 * R, R, R * R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
