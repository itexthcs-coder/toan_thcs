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


def bt_dang15_p1_b1_c4_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.randint(2, 4)
        b = random.randint(a + 1, 7)
        while math.gcd(a, b) != 1:
            b = random.randint(a + 1, 7)
        k1 = random.randint(2, 3)
        k2 = random.randint(2, 4)
        while k1 == k2:
            k2 = random.randint(2, 4)
        oa = a * k1
        oc = b * k1
        ob = a * k2
        od = b * k2

        # Các đáp án trắc nghiệm
        du = ['$%s\\text{ cm}$' % (od)]
        da = random.choice(du)
        s = ['$%s\\text{ cm}$' % (od + 2),
             '$%s\\text{ cm}$' % (od - 1),
             '$%s\\text{ cm}$' % (oa + ob),
             '$%s\\text{ cm}$' % (oc + 1),
             '$%s\\text{ cm}$' % (od + 4)]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hai đoạn thẳng $AC$ và $BD$ cắt nhau tại $O$ sao cho $\\widehat{OAB} = \\widehat{OCD}$ như hình vẽ bên dưới. Biết $OA = %s\\text{ cm}$, $OC = %s\\text{ cm}$ và $OB = %s\\text{ cm}$. Độ dài đoạn thẳng $OD$ bằng
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (2,1.6);
\\coordinate (A) at (0.6,3);
\\coordinate (B) at (3.2,3);
\\coordinate (C) at (3.8,0);
\\coordinate (D) at (0.4,0);
\\draw[line width=1pt] (A)--(B)--(D)--(C)--cycle;
\\draw[line width=1pt] ($(A)+(0.35,0)$) arc (0:-45:0.35);
\\draw[line width=1pt] ($(C)+(-0.35,0)$) arc (180:135:0.35);
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (oa, oc, ob))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Ta có $\\widehat{OAB} = \\widehat{OCD}$, mà hai góc này ở vị trí so le trong nên $AB // CD$.\\\\
Trên tia đối của tia $OC$ lấy điểm $A'$ sao cho $OA' = OA = %s\\text{ cm}$, trên tia đối của tia $OD$ lấy điểm $B'$ sao cho $OB' = OB = %s\\text{ cm}$, khi đó $A'B' // AB // CD$.\\\\
Xét $\\Delta OCD$ có $A'B' // CD$, theo định lí Thalès trong tam giác ta có:\\\\
$\\dfrac{OA'}{OC} = \\dfrac{OB'}{OD}$ hay $\\dfrac{OA}{OC} = \\dfrac{OB}{OD}$.\\\\
Thay số vào tỉ lệ thức trên, ta được:\\\\
$\\dfrac{%s}{%s} = \\dfrac{%s}{OD} \\Rightarrow OD = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$.\\\\
Vậy độ dài đoạn thẳng $OD$ bằng $%s\\text{ cm}$.'''
                   % (oa, ob, oa, oc, ob, oc, ob, oa, od, od))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
