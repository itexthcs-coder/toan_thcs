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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_dang4_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p = randint(2, 5)
        t1 = randint(2, 6)
        t2 = randint(-2, -1)
        while p**2 + 4*t2 <= 0:
            t2 += 1
            
        B_t = -(t1 + t2)
        C_t = t1 * t2
        kq = 2 * p
        kq_str = str(kq)
        
        dau_B = '+' if B_t >= 0 else '-'
        dau_C = '+' if C_t >= 0 else '-'
        eq_t_str = 't^2 %s %st %s %s = 0' % (dau_B, abs(B_t), dau_C, abs(C_t))
        eq_x_str = '(x^2 - %sx)^2 %s %s(x^2 - %sx) %s %s = 0' % (p, dau_B, abs(B_t), p, dau_C, abs(C_t))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tính tổng tất cả các nghiệm thực của phương trình $%s$.'''
                         %(eq_x_str
                         ))

        # Nội dung lời giải
        loigiai = ('''Đặt $t = x^2 - %sx$, phương trình đã cho trở thành: \\\\
                   $%s$. \\\\
                   Giải phương trình bậc hai ẩn $t$ có $\\Delta = (%s)^2 - 4 \\cdot 1 \\cdot (%s) = %s > 0$, ta tìm được hai nghiệm phân biệt $t_1 = %s$ và $t_2 = %s$. \\\\
                   - Với $t = %s$, ta có $x^2 - %sx - %s = 0$. Phương trình có $\\Delta_1 = %s > 0$ nên có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn $x_1 + x_2 = %s$. \\\\
                   - Với $t = %s$, ta có $x^2 - %sx + %s = 0$. Phương trình có $\\Delta_2 = %s > 0$ nên có hai nghiệm phân biệt $x_3, x_4$ thỏa mãn $x_3 + x_4 = %s$. \\\\
                   Vậy tổng tất cả các nghiệm thực của phương trình là $%s + %s = %s$.'''
                   %(str(p), eq_t_str,
                     str(B_t), str(C_t), str(B_t**2 - 4*C_t), str(t1), str(t2),
                     str(t1), str(p), str(t1), str(p**2 + 4*t1), str(p),
                     str(t2), str(p), str(-t2), str(p**2 + 4*t2), str(p),
                     str(p), str(p), kq_str
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)

    # Xuất câu trắc nghiệm trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
