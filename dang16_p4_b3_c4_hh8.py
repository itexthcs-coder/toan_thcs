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

def bt_dang16_p4_b3_c4_hh8(self):
    # Dạng 16: Bài toán chuyển động gặp nhau trong khuôn viên hình vuông (Thực tế)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t_minh = random.choice([15, 20, 25])
        t_nam = 2 * t_minh
        phut_xp_nam = 60 - t_minh

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,3);\n'
            '\\coordinate (A) at (3,3);\n'
            '\\coordinate (D) at (3,0);\n'
            '\\coordinate (C) at (0,0);\n'
            '\\coordinate (M) at ($(B)!0.5!(A)$);\n'
            '\\coordinate (I) at (intersection of A--C and M--D);\n'
            '\\draw[line width=1pt] (B)--(A)--(D)--(C)--cycle (A)--(C) (M)--(D);\n'
            '\\fill (A) circle (1pt) node[above right] {$A$};\n'
            '\\fill (B) circle (1pt) node[above left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below left] {$C$};\n'
            '\\fill (D) circle (1pt) node[below right] {$D$};\n'
            '\\fill (M) circle (1pt) node[above] {$M$};\n'
            '\\fill (I) circle (1pt) node[below left] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Một quảng trường hình vuông $ABCD$. Bạn Minh đứng ở vị trí $M$ là trung điểm của cạnh $AB$, bạn Nam đứng ở vị trí đỉnh $D$. Hai bạn cùng đi bộ với cùng một vận tốc trên con đường thẳng $MD$ để gặp nhau tại giao điểm $I$ của $MD$ và đường chéo $AC$.\\\\\n'
            'a) Chứng minh $AC$ là tia phân giác của góc $DAB$, từ đó tính tỉ số độ dài hai quãng đường $\\frac{IM}{ID}$.\\\\\n'
            'b) Biết bạn Minh xuất phát lúc $7\\text{ giờ}$ và đến điểm $I$ lúc $7\\text{ giờ } %s\\text{ phút}$. Hỏi bạn Nam phải xuất phát lúc mấy giờ để gặp bạn Minh tại $I$ đúng lúc $7\\text{ giờ } %s\\text{ phút}$?\n%s'
            % (t_minh, t_minh, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1} \n'
            '\\item Vì $ABCD$ là hình vuông nên $AB = AD = CD = BC$, suy ra $\\Delta ABC = \\Delta ADC$ (c.c.c) $\\Rightarrow \\widehat{BAC} = \\widehat{DAC}$. Do đó $AC$ là tia phân giác của góc $DAB$.\\\\'
            'Xét tam giác $AMD$ có $AI$ là đường phân giác của góc $A$ nên theo tính chất đường phân giác, ta có: $\\frac{IM}{ID} = \\frac{AM}{AD}$.\\\\'
            'Mà $M$ là trung điểm của $AB$ và $AB = AD$ nên $\\frac{AM}{AD} = \\frac{1}{2}$, suy ra $\\frac{IM}{ID} = \\frac{1}{2}$. \n'
            '\\item Vì hai bạn đi với cùng một vận tốc mà quãng đường $ID = 2IM$ nên thời gian bạn Nam đi từ $D$ đến $I$ gấp đôi thời gian bạn Minh đi từ $M$ đến $I$.\\\\'
            'Thời gian bạn Minh đi là $%s\\text{ phút}$ nên thời gian bạn Nam đi là $2 \\cdot %s = %s\\text{ phút}$.\\\\'
            'Để đến điểm $I$ lúc $7\\text{ giờ } %s\\text{ phút}$, bạn Nam phải xuất phát trước bạn Minh $%s\\text{ phút}$, tức là lúc $6\\text{ giờ } %s\\text{ phút}$. \n'
            '\\end{enumEX} \n'
            % (t_minh, t_minh, t_nam, t_minh, t_minh, phut_xp_nam)
        )

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
