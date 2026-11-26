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


def bt_dang18_p4_b2_c7_ds8(self):
    # Dạng 18: Ứng dụng - Bài toán hóa học pha chế dung dịch nồng độ phần trăm
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        m_dd = random.choice([300, 400, 500, 600])
        c1 = random.choice([15, 20, 25])
        c2 = random.choice([10, 12])
        while c2 >= c1 or (m_dd * (c1 - c2)) % c2 != 0:
            m_dd = random.choice([300, 400, 500, 600])
            c1 = random.choice([15, 18, 20, 24, 25])
            c2 = random.choice([10, 12, 15])
            
        m_muoi = (m_dd * c1) // 100
        x_val = (m_dd * (c1 - c2)) // c2
        c2_dec = str(Decimal(c2) / Decimal(100)).replace('.', ',')
        
        noidungcauhoi = ('''Trong phòng thí nghiệm có $%s\\text{ g}$ dung dịch muối ăn ($\\text{NaCl}$) có nồng độ $%s\\%%$. Hỏi người ta cần phải pha thêm vào dung dịch đó bao nhiêu gam nước tinh khiết để thu được một dung dịch muối ăn mới có nồng độ $%s\\%%$?'''
                         % (m_dd, c1, c2))
        
        loigiai = ('''Gọi khối lượng nước tinh khiết cần pha thêm vào dung dịch là $x\\text{ (g)}$ (điều kiện: $x > 0$). \\\\
- Khối lượng muối ăn ($\\text{NaCl}$) nguyên chất có trong $%s\\text{ g}$ dung dịch ban đầu là: \\\\
$%s \\cdot %s\\%% = %s\\text{ (g)}$. \\\\
- Khi pha thêm $x\\text{ (g)}$ nước tinh khiết thì khối lượng muối ăn nguyên chất không đổi (vẫn bằng $%s\\text{ g}$), còn tổng khối lượng dung dịch mới thu được là $%s + x\\text{ (g)}$. \\\\
Vì dung dịch mới có nồng độ $%s\\%%$ nên ta có phương trình: \\\\
$\\frac{%s}{%s + x} = %s$ \\\\
$\\Leftrightarrow %s(%s + x) = %s$ \\\\
$\\Leftrightarrow %s + %sx = %s$ \\\\
$\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy cần phải pha thêm $%s\\text{ g}$ nước tinh khiết.'''
                   % (m_dd,
                      m_dd, c1, m_muoi,
                      m_muoi, m_dd,
                      c2,
                      m_muoi, m_dd, c2_dec,
                      c2_dec, m_dd, m_muoi,
                      (m_dd * c2) // 100, c2_dec, m_muoi,
                      c2_dec, m_muoi - (m_dd * c2) // 100, x_val,
                      x_val))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
