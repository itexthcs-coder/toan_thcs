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


def bt_dang12_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            a_val = randint(2, 6)
            k_val = randint(1, 5)
            if math.gcd(a_val, k_val) == 1:
                break
        x1_val = randint(2, 6)
        x2_frac = Rational(k_val, a_val)
        b_val = -(a_val*x1_val + k_val)
        c_val = k_val*x1_val
        S_frac = Rational(-b_val, a_val)
        P_frac = Rational(c_val, a_val)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Không dùng công thức nghiệm, hãy phân tích đa thức $P(x) = %sx^{2} - %sx + %s$ thành nhân tử bằng cách nhẩm hai nghiệm của đa thức rồi áp dụng công thức $ax^{2} + bx + c = a(x - x_{1})(x - x_{2})$.'''
                         % (latex(a_val), latex(abs(b_val)), latex(c_val)))
        
        # Nội dung lời giải
        loigiai = ('''Xét phương trình bậc hai $%sx^{2} - %sx + %s = 0$ có $a = %s, b = %s, c = %s$. \\\\
Giả sử phương trình có hai nghiệm $x_{1}, x_{2}$. Theo định lí Viète, ta có: \\\\
$\\begin{cases} x_{1} + x_{2} = -\\dfrac{b}{a} = %s \\\\ x_{1}x_{2} = \\dfrac{c}{a} = %s \\end{cases}$. \\\\
Nhẩm nghiệm ta thấy hai số $x_{1} = %s$ và $x_{2} = %s$ có tổng bằng $%s + %s = %s$ và tích bằng $%s \\cdot %s = %s$ nên $x_{1} = %s$ và $x_{2} = %s$ là hai nghiệm của phương trình. \\\\
Áp dụng công thức phân tích đa thức thành nhân tử, ta được: \\\\
$P(x) = %s(x - %s)\\left(x - %s\\right) = (x - %s)(%sx - %s)$.'''
                   % (latex(a_val), latex(abs(b_val)), latex(c_val), latex(a_val), latex(b_val), latex(c_val),
                      latex(S_frac), latex(P_frac),
                      latex(x1_val), latex(x2_frac), latex(x1_val), latex(x2_frac), latex(S_frac), latex(x1_val), latex(x2_frac), latex(P_frac), latex(x1_val), latex(x2_frac),
                      latex(a_val), latex(x1_val), latex(x2_frac), latex(x1_val), latex(a_val), latex(k_val)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
