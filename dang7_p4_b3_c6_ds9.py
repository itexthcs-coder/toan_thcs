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


def bt_dang7_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            c_val = randint(1, 4)
            m_ans = randint(1, 5)
            if 2*m_ans + 1 - c_val > 0:
                k_frac = Rational(2*(m_ans + 1), m_ans**2 + c_val)
                m_other = Rational(2*k_frac.q, k_frac.p) - m_ans
                if m_other != m_ans:
                    break

        dk_m = Rational(c_val - 1, 2)
        A_m = k_frac.p
        B_m = -2 * k_frac.q
        C_m = k_frac.p * c_val - 2 * k_frac.q
        
        str_1_minus_c = "+ %s" % latex(1 - c_val) if (1 - c_val) >= 0 else "- %s" % latex(abs(1 - c_val))
        str_B_m = "+ %s" % latex(B_m) if B_m >= 0 else "- %s" % latex(abs(B_m))
        str_C_m = "+ %s" % latex(C_m) if C_m >= 0 else "- %s" % latex(abs(C_m))
        
        if m_other > dk_m:
            ketluan = "m \\in \\{%s; %s\\}" % (latex(min(m_ans, m_other)), latex(max(m_ans, m_other)))
            nx_other = "thỏa mãn điều kiện"
        else:
            ketluan = "m = %s" % latex(m_ans)
            nx_other = "không thỏa mãn điều kiện"

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tìm tham số $m$ để phương trình $x^{2} - 2(m + 1)x + m^{2} + %s = 0$ có hai nghiệm phân biệt $x_{1}, x_{2}$ cùng dương và thỏa mãn $\\dfrac{1}{x_{1}} + \\dfrac{1}{x_{2}} = %s$.'''
                         % (latex(c_val), latex(k_frac)))
        
        # Nội dung lời giải
        loigiai = ('''Ta có: $\\Delta' = [-(m + 1)]^{2} - 1 \\cdot (m^{2} + %s) = m^{2} + 2m + 1 - m^{2} - %s = 2m %s$. \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = 2(m + 1) \\\\ x_{1}x_{2} = m^{2} + %s \\end{cases}$. \\\\
Để phương trình có hai nghiệm phân biệt cùng dương thì: \\\\
$\\begin{cases} \\Delta' > 0 \\\\ x_{1} + x_{2} > 0 \\\\ x_{1}x_{2} > 0 \\end{cases} \\Leftrightarrow \\begin{cases} 2m %s > 0 \\\\ 2(m + 1) > 0 \\\\ m^{2} + %s > 0 \\end{cases} \\Leftrightarrow \\begin{cases} m > %s \\\\ m > -1 \\\\ \\text{luôn đúng với mọi } m \\end{cases} \\Leftrightarrow m > %s$. \\\\
Theo đề bài: $\\dfrac{1}{x_{1}} + \\dfrac{1}{x_{2}} = %s \\Leftrightarrow \\dfrac{x_{1} + x_{2}}{x_{1}x_{2}} = %s \\Leftrightarrow \\dfrac{2(m + 1)}{m^{2} + %s} = %s$ \\\\
$\\Leftrightarrow %s(m^{2} + %s) = %s(m + 1) \\Leftrightarrow %sm^{2} %sm %s = 0$. \\\\
Giải phương trình trên, ta được $m_{1} = %s$ (thỏa mãn điều kiện) và $m_{2} = %s$ (%s). \\\\
Vậy giá trị cần tìm là $%s$.'''
                   % (latex(c_val), latex(c_val), str_1_minus_c,
                      latex(c_val),
                      str_1_minus_c, latex(c_val), latex(dk_m), latex(dk_m),
                      latex(k_frac), latex(k_frac), latex(c_val), latex(k_frac),
                      latex(k_frac.p), latex(c_val), latex(2*k_frac.q),
                      latex(A_m), str_B_m, str_C_m,
                      latex(m_ans), latex(m_other), nx_other,
                      ketluan))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
