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


def bt_dang14_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a_val = randint(1, 4)
        c_val = randint(2, 6)
        m_ans = randint(a_val + 1, a_val + 4)
        k_frac = Rational(-(4*(m_ans - a_val)**2 + 2*c_val), c_val)
        m_other = 2*a_val - m_ans
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình $x^{2} - 2(m - %s)x - %s = 0$. Chứng minh rằng phương trình luôn có hai nghiệm phân biệt khác $0$ với mọi $m$, và tìm giá trị của $m$ để $\\dfrac{x_{1}}{x_{2}} + \\dfrac{x_{2}}{x_{1}} = %s$.'''
                         % (latex(a_val), latex(c_val), latex(k_frac)))
        
        # Nội dung lời giải
        loigiai = ('''Ta có: $a \\cdot c = 1 \\cdot (-%s) = -%s < 0$ với mọi $m$. \\\\
Do đó phương trình luôn có hai nghiệm trái dấu $x_{1}, x_{2}$ (nên $x_{1} \\ne 0, x_{2} \\ne 0$) với mọi $m$. \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = 2(m - %s) \\\\ x_{1}x_{2} = -%s \\end{cases}$. \\\\
Ta có: $\\dfrac{x_{1}}{x_{2}} + \\dfrac{x_{2}}{x_{1}} = %s \\Leftrightarrow \\dfrac{x_{1}^{2} + x_{2}^{2}}{x_{1}x_{2}} = %s \\Leftrightarrow \\dfrac{(x_{1} + x_{2})^{2} - 2x_{1}x_{2}}{x_{1}x_{2}} = %s$ \\\\
$\\Leftrightarrow \\dfrac{4(m - %s)^{2} - 2 \\cdot (-%s)}{-%s} = %s \\Leftrightarrow 4(m - %s)^{2} + %s = %s$ \\\\
$\\Leftrightarrow 4(m - %s)^{2} = %s \\Leftrightarrow (m - %s)^{2} = %s$ \\\\
$\\Leftrightarrow \\left[\\begin{array}{l} m - %s = %s \\\\ m - %s = -%s \\end{array}\\right. \\Leftrightarrow \\left[\\begin{array}{l} m = %s \\\\ m = %s \\end{array}\\right.$. \\\\
Vậy $m \\in \\{%s; %s\\}$ là các giá trị cần tìm.'''
                   % (latex(c_val), latex(c_val),
                      latex(a_val), latex(c_val),
                      latex(k_frac), latex(k_frac), latex(k_frac),
                      latex(a_val), latex(c_val), latex(c_val), latex(k_frac), latex(a_val), latex(2*c_val), latex(-k_frac * c_val),
                      latex(a_val), latex(-k_frac * c_val - 2*c_val), latex(a_val), latex((m_ans - a_val)**2),
                      latex(a_val), latex(m_ans - a_val), latex(a_val), latex(m_ans - a_val), latex(m_ans), latex(m_other),
                      latex(m_other), latex(m_ans)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
