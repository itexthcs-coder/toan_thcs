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


def bt_dang13_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            p_val = randint(1, 5)
            q_val = randint(2, 11)
            if int(math.isqrt(q_val))**2 != q_val:
                break
        S_val = 2*p_val
        P_val = p_val**2 - q_val
        a_ans = -S_val
        b_ans = P_val
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Tìm hai số nguyên $a$ và $b$ biết rằng phương trình $x^{2} + ax + b = 0$ nhận $x_{1} = %s + \\sqrt{%s}$ làm nghiệm.'''
                         % (latex(p_val), latex(q_val)))
        
        # Nội dung lời giải
        loigiai = ('''Gọi $x_{2}$ là nghiệm còn lại của phương trình $x^{2} + ax + b = 0$. \\\\
Theo định lí Viète, ta có: $x_{1} + x_{2} = -a \\Rightarrow x_{2} = -a - x_{1} = -a - %s - \\sqrt{%s}$. \\\\
Mặt khác, tích hai nghiệm là $x_{1}x_{2} = b$: \\\\
$b = (%s + \\sqrt{%s})(-a - %s - \\sqrt{%s})$ \\\\
$= -%sa - %s - %s\\sqrt{%s} - a\\sqrt{%s} - %s\\sqrt{%s} - %s$ \\\\
$= (-%sa - %s) - (a + %s)\\sqrt{%s}$. \\\\
Vì $a, b$ là các số nguyên và $\\sqrt{%s}$ là số vô tỉ nên đẳng thức trên xảy ra khi và chỉ khi: \\\\
$\\begin{cases} a + %s = 0 \\\\ -%sa - %s = b \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = -%s \\cdot (%s) - %s = %s \\end{cases}$. \\\\
Vậy hai số nguyên cần tìm là $a = %s$ và $b = %s$.'''
                   % (latex(p_val), latex(q_val),
                      latex(p_val), latex(q_val), latex(p_val), latex(q_val),
                      latex(p_val), latex(p_val**2), latex(p_val), latex(q_val), latex(q_val), latex(p_val), latex(q_val), latex(q_val),
                      latex(p_val), latex(p_val**2 + q_val), latex(2*p_val), latex(q_val),
                      latex(q_val),
                      latex(2*p_val), latex(p_val), latex(p_val**2 + q_val), latex(a_ans), latex(p_val), latex(a_ans), latex(p_val**2 + q_val), latex(b_ans),
                      latex(a_ans), latex(b_ans)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
