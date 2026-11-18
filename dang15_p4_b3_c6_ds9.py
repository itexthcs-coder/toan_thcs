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


def bt_dang15_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            k_val = randint(2, 6)
            c_val = randint(1, 5)
            vp_val = c_val - 2*k_val + 4
            if vp_val != 0 and abs(vp_val) != 1:
                break

        uoc_list = []
        for d in range(-abs(vp_val), abs(vp_val) + 1):
            if d != 0 and vp_val % d == 0:
                d2 = vp_val // d
                if d < d2:
                    uoc_list.append((d, d2))
                    
        m_list = []
        lines_uoc = []
        for d1, d2 in uoc_list:
            x1_c = d1 + 2
            x2_c = d2 + 2
            m_c = x1_c + x2_c - k_val
            m_list.append(m_c)
            lines_uoc.append("$\\begin{cases} x_{1} - 2 = %s \\\\ x_{2} - 2 = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_{1} = %s \\\\ x_{2} = %s \\end{cases} \\Rightarrow m = %s + %s - %s = %s$"
                             % (latex(d1), latex(d2), latex(x1_c), latex(x2_c), latex(x1_c), latex(x2_c), latex(k_val), latex(m_c)))
        
        m_list = sorted(list(set(m_list)))
        str_m_ans = "; ".join([latex(val) for val in m_list])
        str_cases = " \\\\ ".join(lines_uoc)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Tìm tất cả các giá trị nguyên của tham số $m$ để phương trình $x^{2} - (m + %s)x + 2m + %s = 0$ có hai nghiệm phân biệt $x_{1}, x_{2}$ đều là các số nguyên.'''
                         % (latex(k_val), latex(c_val)))
        
        # Nội dung lời giải
        loigiai = ('''Giả sử phương trình có hai nghiệm phân biệt nguyên $x_{1}, x_{2}$ (không mất tính tổng quát, giả sử $x_{1} < x_{2}$). \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = m + %s \\\\ x_{1}x_{2} = 2m + %s \\end{cases}$. \\\\
Khử tham số $m$ từ hai hệ thức trên, ta được: \\\\
$x_{1}x_{2} - 2(x_{1} + x_{2}) = (2m + %s) - 2(m + %s) \\Leftrightarrow x_{1}x_{2} - 2x_{1} - 2x_{2} = %s$ \\\\
$\\Leftrightarrow (x_{1} - 2)(x_{2} - 2) = %s$. \\\\
Vì $x_{1}, x_{2} \\in \\mathbb{Z}$ và $x_{1} < x_{2}$ nên $x_{1} - 2$ và $x_{2} - 2$ là các ước nguyên phân biệt của $%s$ với $x_{1} - 2 < x_{2} - 2$. Ta có các trường hợp sau: \\\\
%s. \\\\
Thử lại, với các giá trị $m \\in \\{%s\\}$, phương trình đều có hai nghiệm nguyên phân biệt. \\\\
Vậy $m \\in \\{%s\\}$ là các giá trị cần tìm.'''
                   % (latex(k_val), latex(c_val),
                      latex(c_val), latex(k_val), latex(c_val - 2*k_val),
                      latex(vp_val),
                      latex(vp_val),
                      str_cases,
                      str_m_ans,
                      str_m_ans))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
