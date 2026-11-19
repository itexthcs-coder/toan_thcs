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


def bt_dang15_p4_b1_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(5, 14)

        # Đã sửa đổi tọa độ để A, C, B, D cắt nhau thực sự bên trong đường tròn và IA < IB
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (110:2);\n'
            '\\coordinate (B) at (320:2);\n'
            '\\coordinate (C) at (220:2);\n'
            '\\coordinate (D) at (70:2);\n'
            '\\coordinate (I) at (intersection of A--B and C--D);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B) (C)--(D) (A)--(C) (B)--(D) (B)--(C) (A)--(D);\n'
            '\\draw[line width=1pt, dashed] (O)--(I);\n'
            '\\fill (O) circle (1pt) node[right] {$O$};\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[below left] {$C$};\n'
            '\\fill (D) circle (1pt) node[above right] {$D$};\n'
            '\\fill (I) circle (1pt) node[below] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        # Đã sửa lại thứ tự điểm trên đường tròn thành A, C, B, D
        noidungcauhoi = (
            'Cho đường tròn $(O; %s\\text{ cm})$ và hai dây cung bằng nhau $AB$ và $CD$ cắt nhau tại điểm $I$ nằm bên trong đường tròn (theo thứ tự các điểm $A, C, B, D$ trên đường tròn và $IA < IB$) như hình vẽ.\\\\'
            'a) Chứng minh $\\text{sđ}\\overset\\frown{AC} = \\text{sđ}\\overset\\frown{BD}$.\\\\'
            'b) Chứng minh $IA = ID$ và $IB = IC$.\\\\'
            'c) Chứng minh $AD // BC$ và đường thẳng $OI$ là đường trung trực của đoạn thẳng $AD$.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong đường tròn $(O; %s\\text{ cm})$, hai dây cung bằng nhau $AB = CD$ căng hai cung nhỏ bằng nhau nên $\\text{sđ}\\overset\\frown{AB} = \\text{sđ}\\overset\\frown{CD}$.\\\\'
            'Trừ cả hai vế cho $\\text{sđ}\\overset\\frown{CB}$, ta được $\\text{sđ}\\overset\\frown{AB} - \\text{sđ}\\overset\\frown{CB} = \\text{sđ}\\overset\\frown{CD} - \\text{sđ}\\overset\\frown{CB} \\Rightarrow \\text{sđ}\\overset\\frown{AC} = \\text{sđ}\\overset\\frown{BD}$.\n'
            '\\item Hai góc nội tiếp $\\widehat{ABC}$ và $\\widehat{DCB}$ lần lượt chắn hai cung bằng nhau $AC$ và $BD$ nên $\\widehat{IBC} = \\widehat{ICB}$, suy ra $\\triangle IBC$ cân tại $I$ và $IB = IC$.\\\\'
            'Mặt khác, $AB = CD$ nên $AB - IB = CD - IC \\Rightarrow IA = ID$.\n'
            '\\item Hai góc nội tiếp $\\widehat{CAD}$ và $\\widehat{ACB}$ lần lượt chắn hai cung bằng nhau $CD$ và $AB$ nên $\\widehat{CAD} = \\widehat{ACB}$, mà hai góc này ở vị trí so le trong nên $AD // BC$.\\\\'
            'Vì $IA = ID$ và $OA = OD = %s\\text{ cm}$ nên $OI$ là đường trung trực của đoạn thẳng $AD$.\n'
            '\\end{enumEX}'
            % (R, R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' + str(noidungcauhoi) +
            '\\loigiai{ \n' + str(loigiai) + '}\n'
            '\\end{ex}\n \\end{minipage} \n\n')
    return content
