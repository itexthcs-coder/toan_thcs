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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang16_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        p = randint(2, 4)
        q = randint(p + 1, 6)
        while math.gcd(p, q) != 1:
            q = randint(p + 1, 7)
            
        m_ratio = p ** 2
        w_ratio = q ** 2
        ans_ratio = Rational(q, p)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Động năng $W_d$ (tính bằng Jun, ký hiệu J) của một vật có khối lượng $m$ (kg) chuyển động với vận tốc $v$ (m/s) được tính theo công thức $W_d = \\dfrac{1}{2}mv^2$, từ đó suy ra vận tốc $v = \\sqrt{\\dfrac{2W_d}{m}}$. Một ô tô tải và một ô tô con cùng di chuyển trên đường cao tốc. Biết khối lượng của ô tô tải gấp $%s$ lần khối lượng của ô tô con, nhưng động năng của ô tô tải lại gấp $%s$ lần động năng của ô tô con. Hỏi vận tốc của ô tô tải gấp bao nhiêu lần vận tốc của ô tô con?'''
                         % (m_ratio, w_ratio))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $m_1, W_1, v_1$ lần lượt là khối lượng, động năng, vận tốc của ô tô tải và $m_2, W_2, v_2$ lần lượt là khối lượng, động năng, vận tốc của ô tô con ($m_1, m_2, W_1, W_2 > 0$).\\\\
        Theo đề bài, ta có $m_1 = %sm_2$ và $W_1 = %sW_2$.\\\\
        Áp dụng quy tắc chia các căn bậc hai, tỉ số vận tốc giữa ô tô tải và ô tô con là:
        $$\\dfrac{v_1}{v_2} = \\dfrac{\\sqrt{\\dfrac{2W_1}{m_1}}}{\\sqrt{\\dfrac{2W_2}{m_2}}} = \\sqrt{\\dfrac{2W_1}{m_1} : \\dfrac{2W_2}{m_2}} = \\sqrt{\\dfrac{2 \\cdot %sW_2}{%sm_2} \\cdot \\dfrac{m_2}{2W_2}} = \\sqrt{\\dfrac{%s}{%s}} = \\dfrac{%s}{%s}.$$
        Vậy vận tốc của ô tô tải gấp $%s$ lần vận tốc của ô tô con.'''
                   % (m_ratio, w_ratio,
                      w_ratio, m_ratio, w_ratio, m_ratio, q, p,
                      latex(ans_ratio)))
    
    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
