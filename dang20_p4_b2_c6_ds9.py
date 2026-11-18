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


def bt_dang20_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (40, 2, 18, 9, 2),
            (60, 3, 27, 9, 2),
            (48, 4, 20, 5, 1),
            (36, 3, 15, 5, 1)
        ]
        S, vn, vc, num_t, den_t = random.choice(cases)
        
        if den_t == 2:
            t_text = "%s\\text{ giờ } 30\\text{ phút}" %(latex(num_t // 2))
            t_frac = "\\dfrac{%s}{2}" %(latex(num_t))
        else:
            t_text = "%s\\text{ giờ}" %(latex(num_t))
            t_frac = "%s" %(latex(num_t))
            
        a_pt = num_t
        b_pt = -2 * S * den_t
        c_pt = -num_t * (vn**2)
        delta = b_pt**2 - 4 * a_pt * c_pt
        x_loai = Rational(-b_pt - int(math.isqrt(delta)), 2 * a_pt)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một ca nô xuôi dòng trên một khúc sông dài $%s\\text{ km}$ rồi ngược dòng trở về điểm xuất phát. Tổng thời gian cả đi lẫn về của ca nô là $%s$. Tính vận tốc riêng của ca nô khi nước yên lặng, biết rằng vận tốc dòng nước là $%s\\text{ km/h}$.'''
                         %(latex(S), t_text, latex(vn)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Đổi đơn vị thời gian: $%s = %s\\text{ giờ}$. \\\\
                   Gọi vận tốc riêng của ca nô khi nước yên lặng là $x$ ($\\text{km/h}$), điều kiện: $x > %s$. \\\\
                   Khi đó: \\\\
                   - Vận tốc của ca nô khi xuôi dòng là $x + %s$ ($\\text{km/h}$), thời gian xuôi dòng là $\\dfrac{%s}{x + %s}$ (giờ). \\\\
                   - Vận tốc của ca nô khi ngược dòng là $x - %s$ ($\\text{km/h}$), thời gian ngược dòng là $\\dfrac{%s}{x - %s}$ (giờ). \\\\
                   Vì tổng thời gian cả đi lẫn về của ca nô là $%s\\text{ giờ}$ nên ta có phương trình: \\\\
                   $\\dfrac{%s}{x + %s} + \\dfrac{%s}{x - %s} = %s$. \\\\
                   Quy đồng mẫu thức và khử mẫu (với $x > %s$), ta được: \\\\
                   $%s \\cdot %s(x - %s) + %s \\cdot %s(x + %s) = %s(x^2 - %s^2)$ \\\\
                   $\\Leftrightarrow %sx = %sx^2 - %s$ \\\\
                   $\\Leftrightarrow %sx^2 - %sx - %s = 0$. \\\\
                   Phương trình bậc hai trên có $a = %s$, $b = %s$, $c = %s$. \\\\
                   Ta có biệt thức $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot (%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $x_1 = \\dfrac{%s + \\sqrt{%s}}{2 \\cdot %s} = %s$ (thỏa mãn điều kiện $x > %s$); \\\\
                   $x_2 = \\dfrac{%s - \\sqrt{%s}}{2 \\cdot %s} = %s$ (không thỏa mãn điều kiện nên loại). \\\\
                   Vậy vận tốc riêng của ca nô khi nước yên lặng là $%s\\text{ km/h}$.'''
                   %(t_text, t_frac,
                     latex(vn),
                     latex(vn), latex(S), latex(vn),
                     latex(vn), latex(S), latex(vn),
                     t_frac,
                     latex(S), latex(vn), latex(S), latex(vn), t_frac,
                     latex(vn),
                     latex(S), latex(den_t), latex(vn), latex(S), latex(den_t), latex(vn), latex(num_t), latex(vn),
                     latex(2*S*den_t), latex(num_t), latex(num_t*(vn**2)),
                     latex(a_pt), latex(abs(b_pt)), latex(abs(c_pt)),
                     latex(a_pt), latex(b_pt), latex(c_pt),
                     latex(b_pt), latex(a_pt), latex(c_pt), latex(delta),
                     latex(-b_pt), latex(delta), latex(a_pt), latex(vc), latex(vn),
                     latex(-b_pt), latex(delta), latex(a_pt), latex(x_loai),
                     latex(vc)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
