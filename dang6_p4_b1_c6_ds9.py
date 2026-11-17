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


def bt_dang6_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = randint(1, 3)
        a_par = Rational(1, 2 * k)
        x_a = -k
        y_a = a_par * (x_a**2)
        x_b = 4 * k
        y_b = a_par * (x_b**2)
        m_line = Rational(3, 2)
        b_line = 2 * k
        
        oa_sq = x_a**2 + y_a**2
        ob_sq = x_b**2 + y_b**2
        ab_sq = (x_b - x_a)**2 + (y_b - y_a)**2

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho parabol $(P): y = %sx^2$ và đường thẳng $(d): y = %sx + %s$. \\\\
a) Tìm tọa độ các giao điểm $A$ và $B$ của $(P)$ và $(d)$ (biết điểm $A$ có hoành độ âm). \\\\
b) Chứng minh rằng tam giác $OAB$ là một tam giác vuông.'''
                         %(latex(a_par), latex(m_line), latex(b_line)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Hoành độ giao điểm của $(P)$ và $(d)$ là nghiệm của phương trình: \\\\
$%sx^2 = %sx + %s$ \\\\
$%sx^2 - %sx - %s = 0$ \\\\
$x^2 - %sx - %s = 0$ \\\\
$(x + %s)(x - %s) = 0$ \\\\
Suy ra $x = %s$ hoặc $x = %s$. \\\\
Với $x = %s$, ta có $y = %s \\cdot (%s)^2 = %s$. \\\\
Với $x = %s$, ta có $y = %s \\cdot %s^2 = %s$. \\\\
Vì điểm $A$ có hoành độ âm nên tọa độ hai giao điểm là $A(%s; %s)$ và $B(%s; %s)$.
\\item Áp dụng công thức tính khoảng cách giữa hai điểm trên mặt phẳng tọa độ $Oxy$, ta có: \\\\
$OA^2 = (%s - 0)^2 + (%s - 0)^2 = %s$ \\\\
$OB^2 = (%s - 0)^2 + (%s - 0)^2 = %s$ \\\\
$AB^2 = (%s - (%s))^2 + (%s - %s)^2 = %s$ \\\\
Ta thấy $OA^2 + OB^2 = %s + %s = %s = AB^2$. \\\\
Theo định lý Pythagore đảo, tam giác $OAB$ vuông tại $O$.
\\end{enumEX}'''
                   %(latex(a_par), latex(m_line), latex(b_line),
                     latex(a_par), latex(m_line), latex(b_line),
                     latex(3*k), latex(4*(k**2)),
                     latex(k), latex(4*k),
                     latex(x_a), latex(x_b),
                     latex(x_a), latex(a_par), latex(x_a), latex(y_a),
                     latex(x_b), latex(a_par), latex(x_b), latex(y_b),
                     latex(x_a), latex(y_a), latex(x_b), latex(y_b),
                     latex(x_a), latex(y_a), latex(oa_sq),
                     latex(x_b), latex(y_b), latex(ob_sq),
                     latex(x_b), latex(x_a), latex(y_b), latex(y_a), latex(ab_sq),
                     latex(oa_sq), latex(ob_sq), latex(ab_sq)
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
