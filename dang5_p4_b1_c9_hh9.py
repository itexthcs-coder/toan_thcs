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


def bt_dang5_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(4, 12)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (M) at (-4,0);\n'
            '\\coordinate (A) at (120:2);\n'
            '\\coordinate (B) at (-120:2);\n'
            '\\coordinate (H) at (-1,0);\n'
            '\\coordinate (C) at (155:2);\n'
            '\\coordinate (D) at (35:2);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (M)--(A)--(O)--(B)--cycle (M)--(O) (A)--(B) (M)--(D) (A)--(C) (A)--(D) (H)--(C) (O)--(D);\n'
            '\\fill (O) circle (1pt) node[right] {$O$};\n'
            '\\fill (M) circle (1pt) node[left] {$M$};\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below] {$B$};\n'
            '\\fill (H) circle (1pt) node[below right] {$H$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[above right] {$D$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Từ điểm $M$ nằm bên ngoài đường tròn $(O; %s\\text{ cm})$, vẽ hai tiếp tuyến $MA, MB$ với đường tròn ($A, B$ là hai tiếp điểm) và một cát tuyến $MCD$ không đi qua tâm $O$ ($C$ nằm giữa $M$ và $D$). Gọi $H$ là giao điểm của $OM$ và $AB$ như hình vẽ.\\\\'
            'a) Chứng minh $OM \\perp AB$ tại $H$ và $MA^2 = MH \\cdot MO$.\\\\'
            'b) Chứng minh $\\triangle MAC \\backsim \\triangle MDA$ và $MA^2 = MC \\cdot MD$.\\\\'
            'c) Chứng minh $\\widehat{MHC} = \\widehat{MDO}$.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Theo tính chất hai tiếp tuyến cắt nhau, ta có $MA = MB$, lại có $OA = OB = %s\\text{ cm}$ nên $OM$ là đường trung trực của đoạn thẳng $AB$, suy ra $OM \\perp AB$ tại $H$.\\\\'
            'Xét $\\triangle MHA$ và $\\triangle MAO$ vuông lần lượt tại $H$ và $A$ có $\\widehat{M}$ chung nên $\\triangle MHA \\backsim \\triangle MAO$ (g.g), suy ra $\\dfrac{MH}{MA} = \\dfrac{MA}{MO} \\Rightarrow MA^2 = MH \\cdot MO$.\n'
            '\\item Trong đường tròn $(O)$, góc tạo bởi tia tiếp tuyến và dây cung $\\widehat{MAC}$ và góc nội tiếp $\\widehat{MDA}$ cùng chắn cung nhỏ $AC$ nên $\\widehat{MAC} = \\widehat{MDA}$.\\\\'
            'Xét $\\triangle MAC$ và $\\triangle MDA$ có $\\widehat{M}$ chung và $\\widehat{MAC} = \\widehat{MDA}$ nên $\\triangle MAC \\backsim \\triangle MDA$ (g.g), suy ra $\\dfrac{MA}{MD} = \\dfrac{MC}{MA} \\Rightarrow MA^2 = MC \\cdot MD$.\n'
            '\\item Từ câu a) và câu b), ta có $MH \\cdot MO = MC \\cdot MD \\Rightarrow \\dfrac{MH}{MD} = \\dfrac{MC}{MO}$.\\\\'
            'Xét $\\triangle MHC$ và $\\triangle MDO$ có $\\widehat{M}$ chung và $\\dfrac{MH}{MD} = \\dfrac{MC}{MO}$ nên $\\triangle MHC \\backsim \\triangle MDO$ (c.g.c), suy ra $\\widehat{MHC} = \\widehat{MDO}$.\n'
            '\\end{enumEX}'
            % (R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
