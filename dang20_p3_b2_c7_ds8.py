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
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang20_p3_b2_c7_ds8(self):
    # Dạng 20: Giải bài toán bằng cách lập phương trình - San nước giữa hai bình (bảo toàn lượng nước)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.randint(10, 25)
        S = 7 * k
        x_val = 4 * k
        kq_str = str(x_val)
        
        noidungcauhoi = ('''Hai bình chứa nước có tổng dung tích là $%s$ lít. Nếu đổ nước từ bình thứ nhất sang bình thứ hai cho đầy thì bình thứ nhất chỉ còn lại một nửa dung tích của nó. Nếu đổ nước từ bình thứ hai sang bình thứ nhất cho đầy thì bình thứ hai chỉ còn lại $\\frac{1}{3}$ dung tích của nó (ban đầu cả hai bình đều không đầy và tổng lượng nước không đổi). Tính dung tích của bình thứ nhất (đơn vị: lít).'''
                         % (S))
        
        loigiai = ('''Gọi dung tích của bình thứ nhất là $x$ (lít) (điều kiện: $0 < x < %s$). \\\\
Vì tổng dung tích của hai bình là $%s$ lít nên dung tích của bình thứ hai là $%s - x$ (lít). \\\\
- Khi đổ nước từ bình thứ nhất sang đầy bình thứ hai, bình thứ hai chứa $%s - x$ (lít) và bình thứ nhất còn lại $\\frac{1}{2}x$ (lít), nên tổng lượng nước ở cả hai bình là: $\\frac{1}{2}x + (%s - x)$ (lít). \\\\
- Khi đổ nước từ bình thứ hai sang đầy bình thứ nhất, bình thứ nhất chứa $x$ (lít) và bình thứ hai còn lại $\\frac{1}{3}(%s - x)$ (lít), nên tổng lượng nước ở cả hai bình là: $x + \\frac{1}{3}(%s - x)$ (lít). \\\\
Vì tổng lượng nước trong hai bình không đổi nên ta có phương trình: \\\\
$\\frac{1}{2}x + (%s - x) = x + \\frac{1}{3}(%s - x)$ \\\\
$\\Leftrightarrow 3x + 6(%s - x) = 6x + 2(%s - x)$ \\\\
$\\Leftrightarrow 3x + %s - 6x = 6x + %s - 2x$ \\\\
$\\Leftrightarrow -3x + %s = 4x + %s$ \\\\
$\\Leftrightarrow -7x = -%s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy dung tích của bình thứ nhất là $%s$ lít.'''
                   % (S, S, S,
                      S, S,
                      S, S,
                      S, S,
                      S, S,
                      6*S, 2*S,
                      6*S, 2*S,
                      4*S, x_val,
                      x_val))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
