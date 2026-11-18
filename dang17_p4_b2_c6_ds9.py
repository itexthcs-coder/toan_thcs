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


def bt_dang17_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        b_choices = [(0.8, 1.8, 18, -2), (0.7, 1.5, 16, -2), (0.9, 2.0, 20, -2)]
        b_val, c_val, x1, x2 = random.choice(b_choices)
        
        str_b = str(b_val).replace('.', ',')
        str_c = str(c_val).replace('.', ',')
        
        B_pt = int(round(20 * b_val))
        C_pt = int(round(20 * c_val))
        delta = B_pt**2 + 4*C_pt
        
        # Vẽ hình minh họa theo đúng chuẩn TikZ (không random tọa độ điểm)
        hinhve = ('''\\begin{center}
                   \\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                   \\draw[->, line width=1pt] (-0.5,0) -- (5.5,0) node[below] {$x$};
                   \\draw[->, line width=1pt] (0,-0.4) -- (0,3) node[left] {$h$};
                   \\draw[line width=1pt, smooth, samples=100, domain=0:4.5] plot(\\x, {-0.25*(\\x)^2 + 1.0*\\x + 0.5625});
                   \\coordinate (O) at (0,0);
                   \\coordinate (A) at (0,0.5625);
                   \\coordinate (B) at (4.5,0);
                   \\fill (O) circle (1pt) node[below left] {$O$};
                   \\fill (A) circle (1pt) node[left] {$A$};
                   \\fill (B) circle (1pt) node[below] {$B$};
                   \\end{tikzpicture}
                   \\end{center}''')
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một vận động viên đẩy tạ ném quả tạ từ độ cao $%s\\text{ m}$ so với mặt đất. Quỹ đạo bay của quả tạ được mô hình hóa bởi công thức $h = -0,05x^2 + %sx + %s$, trong đó $h$ (mét) là độ cao của quả tạ so với mặt đất và $x$ (mét) là khoảng cách theo phương ngang từ vị trí ném đến điểm chiếu của quả tạ trên mặt đất (như hình vẽ minh họa). Hỏi quả tạ chạm đất cách vị trí ném bao xa theo phương ngang? %s'''
                         %(str_c, str_b, str_c, hinhve
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Quả tạ chạm đất khi độ cao của quả tạ so với mặt đất bằng $0$, tức là $h = 0$. \\\\
                   Thay $h = 0$ vào công thức quỹ đạo, ta được phương trình: \\\\
                   $-0,05x^2 + %sx + %s = 0$. \\\\
                   Nhân cả hai vế của phương trình với $-20$, ta được phương trình bậc hai hệ số nguyên: \\\\
                   $x^2 - %sx - %s = 0$. \\\\
                   Phương trình bậc hai trên có $a = 1$, $b = -%s$, $c = -%s$. \\\\
                   Ta có biệt thức $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot (-%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $x_1 = \\dfrac{%s + \\sqrt{%s}}{2 \\cdot 1} = %s$ (thỏa mãn điều kiện $x > 0$); \\\\
                   $x_2 = \\dfrac{%s - \\sqrt{%s}}{2 \\cdot 1} = %s$ (không thỏa mãn điều kiện nên loại). \\\\
                   Vậy quả tạ chạm đất cách vị trí ném $%s\\text{ m}$ theo phương ngang.'''
                   %(str_b, str_c,
                     latex(B_pt), latex(C_pt),
                     latex(B_pt), latex(C_pt),
                     latex(B_pt), latex(C_pt), latex(delta),
                     latex(B_pt), latex(delta), latex(x1),
                     latex(B_pt), latex(delta), latex(x2),
                     latex(x1)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
