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


def bt_dang20_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R1 = randint(16, 25)
        R2 = randint(6, 12)
        hieu_R = R1 - R2
        OO_p = randint(R1 + R2 + 2, R1 + R2 + 12)
        AB_val = math.sqrt(OO_p**2 - hieu_R**2)
        number = Decimal(AB_val)
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (Op) at (4.0,0);
\\coordinate (A) at (0.54, 1.72);
\\coordinate (B) at (4.24, 0.76);
\\coordinate (H) at (0.30, 0.96);
\\draw[line width=1pt] (O) circle (1.8cm);
\\draw[line width=1pt] (Op) circle (0.8cm);
\\draw[line width=1pt] (O)--(Op) (A)--(B) (O)--(A) (Op)--(B);
\\draw[line width=1pt, dashed] (Op)--(H);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (Op) circle (1pt) node[below] {$O'$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (H) circle (1pt) node[left] {$H$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một hệ thống truyền động sử dụng dây curoa mắc qua hai bánh đà (puly) hình tròn ở ngoài nhau có bán kính lần lượt là $%s\\text{ cm}$ và $%s\\text{ cm}$, khoảng cách giữa hai tâm trục là $%s\\text{ cm}$. Phần dây curoa thẳng không tiếp xúc với bánh đà ở nhánh trên có độ dài là bao nhiêu $\\text{cm}$? (Làm tròn kết quả đến hàng phần mười).\\\\
%s''' % (R1, R2, OO_p, hinhve))

        loigiai = ('''Phần dây curoa thẳng không tiếp xúc với hai bánh đà ở nhánh trên chính là đoạn tiếp tuyến chung ngoài $AB$ của hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$. \\\\
Ta có $OA \\perp AB$ tại $A$ và $O'B \\perp AB$ tại $B$. \\\\
Kẻ $O'H \\perp OA$ tại $H$, tứ giác $ABO'H$ là hình chữ nhật nên $AB = O'H$ và $AH = O'B = %s\\text{ cm}$. \\\\
Suy ra $OH = OA - AH = %s - %s = %s\\text{ (cm)}$. \\\\
Áp dụng định lí Pythagore vào tam giác $OHO'$ vuông tại $H$, ta có: \\\\
$AB = O'H = \\sqrt{OO'^2 - OH^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s} \\approx %s\\text{ (cm)}$.'''
                   % (R1, R2, R2, R1, R2, hieu_R, OO_p, hieu_R, OO_p**2 - hieu_R**2, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
