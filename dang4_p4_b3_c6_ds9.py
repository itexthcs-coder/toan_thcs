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


def bt_dang4_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            x1_val = randint(-3, 2)
            x2_val = randint(3, 8)
            if x1_val != x2_val:
                S_val = x1_val + x2_val
                if S_val > 0:
                    break
        p_val = randint(2, 4)
        q_val = p_val + 1
        k_val = p_val*x1_val + q_val*x2_val
        c_val = randint(1, 5)
        m_ans = x1_val*x2_val + c_val
        dk_m = Rational(S_val**2 + 4*c_val, 4)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình $x^{2} - %sx + m - %s = 0$. Tìm giá trị của tham số $m$ để phương trình có hai nghiệm $x_{1}, x_{2}$ thỏa mãn hệ thức $%sx_{1} + %sx_{2} = %s$.'''
                         % (latex(S_val), latex(c_val), latex(p_val), latex(q_val), latex(k_val)))
        
        # Nội dung lời giải
        loigiai = ('''Ta có: $\\Delta = (-%s)^{2} - 4 \\cdot 1 \\cdot (m - %s) = %s - 4m$. \\\\
Để phương trình có hai nghiệm $x_{1}, x_{2}$ thì $\\Delta \\ge 0 \\Leftrightarrow %s - 4m \\ge 0 \\Leftrightarrow m \\le %s$. \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = %s \\quad (1) \\\\ x_{1}x_{2} = m - %s \\quad (2) \\end{cases}$. \\\\
Kết hợp $(1)$ với giả thiết $%sx_{1} + %sx_{2} = %s$, ta có hệ phương trình: \\\\
$\\begin{cases} x_{1} + x_{2} = %s \\\\ %sx_{1} + %sx_{2} = %s \\end{cases} \\Leftrightarrow \\begin{cases} %sx_{1} + %sx_{2} = %s \\\\ %sx_{1} + %sx_{2} = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_{2} = %s \\\\ x_{1} = %s \\end{cases}$. \\\\
Thay $x_{1} = %s$ và $x_{2} = %s$ vào $(2)$, ta được: \\\\
$%s \\cdot (%s) = m - %s \\Leftrightarrow m = %s$ (thỏa mãn điều kiện $m \\le %s$). \\\\
Vậy $m = %s$ là giá trị cần tìm.'''
                   % (latex(S_val), latex(c_val), latex(S_val**2 + 4*c_val),
                      latex(S_val**2 + 4*c_val), latex(dk_m),
                      latex(S_val), latex(c_val),
                      latex(p_val), latex(q_val), latex(k_val),
                      latex(S_val), latex(p_val), latex(q_val), latex(k_val),
                      latex(p_val), latex(p_val), latex(p_val*S_val),
                      latex(p_val), latex(q_val), latex(k_val),
                      latex(x2_val), latex(x1_val),
                      latex(x1_val), latex(x2_val),
                      latex(x1_val), latex(x2_val), latex(c_val), latex(m_ans), latex(dk_m),
                      latex(m_ans)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
