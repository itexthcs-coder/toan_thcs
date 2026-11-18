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


def bt_dang2_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            a_val = randint(1, 3)
            b_val = 2*a_val + 1
            m_ans = randint(1, 5)
            if m_ans > -a_val**2:
                k_val = 2*(m_ans**2) + (2*b_val - 8*a_val)*m_ans + 4*(a_val**2)
                m_other = (4*a_val - b_val) - m_ans
                if m_other != m_ans:
                    break

        heso_m_delta = b_val - 2*a_val
        const_delta = a_val**2
        dk_m = Rational(-const_delta, heso_m_delta)
        
        heso_m_pt = 2*b_val - 8*a_val
        const_pt = 4*(a_val**2) - k_val
        str_heso_m_pt = "+ %s" % latex(heso_m_pt) if heso_m_pt >= 0 else "- %s" % latex(abs(heso_m_pt))
        str_const_pt = "+ %s" % latex(const_pt) if const_pt >= 0 else "- %s" % latex(abs(const_pt))
        
        if m_other > dk_m:
            ketluan = "m \\in \\{%s; %s\\}" % (latex(min(m_ans, m_other)), latex(max(m_ans, m_other)))
            nhanxet_other = "thỏa mãn điều kiện"
        else:
            ketluan = "m = %s" % latex(m_ans)
            nhanxet_other = "không thỏa mãn điều kiện"

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình $x^{2} - 2(m - %s)x + m^{2} - %sm = 0$ ($m$ là tham số). Tìm các giá trị của $m$ để phương trình có hai nghiệm phân biệt $x_{1}, x_{2}$ thỏa mãn $x_{1}^{2} + x_{2}^{2} = %s$.'''
                         % (latex(a_val), latex(b_val), latex(k_val)))
        
        # Nội dung lời giải
        loigiai = ('''Ta có: $\\Delta' = [-(m - %s)]^{2} - 1 \\cdot (m^{2} - %sm) = m^{2} - %sm + %s - m^{2} + %sm = m + %s$. \\\\
Để phương trình có hai nghiệm phân biệt $x_{1}, x_{2}$ thì $\\Delta' > 0 \\Leftrightarrow m + %s > 0 \\Leftrightarrow m > %s$. \\\\
Theo định lí Viète, ta có: $\\begin{cases} x_{1} + x_{2} = 2(m - %s) \\\\ x_{1}x_{2} = m^{2} - %sm \\end{cases}$. \\\\
Theo đề bài: $x_{1}^{2} + x_{2}^{2} = %s \\Leftrightarrow (x_{1} + x_{2})^{2} - 2x_{1}x_{2} = %s$ \\\\
$\\Leftrightarrow 4(m - %s)^{2} - 2(m^{2} - %sm) = %s$ \\\\
$\\Leftrightarrow 4m^{2} - %sm + %s - 2m^{2} + %sm - %s = 0$ \\\\
$\\Leftrightarrow 2m^{2} %sm %s = 0$. \\\\
Giải phương trình bậc hai trên, ta được hai nghiệm là $m_{1} = %s$ (thỏa mãn điều kiện) và $m_{2} = %s$ (%s). \\\\
Vậy giá trị cần tìm là $%s$.'''
                   % (latex(a_val), latex(b_val), latex(2*a_val), latex(const_delta), latex(b_val), latex(const_delta),
                      latex(const_delta), latex(dk_m),
                      latex(a_val), latex(b_val),
                      latex(k_val), latex(k_val),
                      latex(a_val), latex(b_val), latex(k_val),
                      latex(8*a_val), latex(4*a_val**2), latex(2*b_val), latex(k_val),
                      str_heso_m_pt, str_const_pt,
                      latex(m_ans), latex(m_other), nhanxet_other, ketluan))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
