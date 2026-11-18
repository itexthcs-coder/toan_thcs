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

def bt_dang17_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d_val = randint(30, 75)
        delta_p = 15**2 + 200 * d_val
        v_val = -15 + math.sqrt(delta_p)
        
        number = Decimal(str(v_val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Quãng đường phanh $d$ (tính bằng mét) của một chiếc ô tô chạy trên đường nhựa khô được tính gần đúng bởi công thức $d = 0,005v^2 + 0,15v$, trong đó $v$ ($\\text{km/h}$) là vận tốc của xe tại thời điểm bắt đầu đạp phanh. Nếu lực lượng chức năng đo được vết trượt phanh trên đường dài $%s\\text{ m}$ thì vận tốc của xe khi bắt đầu phanh là bao nhiêu $\\text{km/h}$ (làm tròn kết quả đến hàng đơn vị)?'''
                         %(str(d_val)
                         ))

        # Nội dung lời giải
        loigiai = ('''Thay $d = %s$ vào công thức $d = 0,005v^2 + 0,15v$, ta được phương trình bậc hai ẩn $v$ ($v > 0$): \\\\
                   $0,005v^2 + 0,15v = %s \\Leftrightarrow v^2 + 30v - %s = 0$. \\\\
                   Xét phương trình trên có $a = 1$, $b' = 15$, $c = -%s$. \\\\
                   Tính biệt thức thu gọn $\\Delta' = 15^2 - 1 \\cdot (-%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $v_1 = -15 + \\sqrt{%s} \\approx %s$ (thỏa mãn $v > 0$); \\\\
                   $v_2 = -15 - \\sqrt{%s} < 0$ (loại). \\\\
                   Vậy vận tốc của xe khi bắt đầu đạp phanh là khoảng $%s\\text{ km/h}$.'''
                   %(str(d_val),
                     str(d_val), str(200 * d_val),
                     str(200 * d_val),
                     str(200 * d_val), str(delta_p),
                     str(delta_p), str(round(v_val, 2)).replace('.', ','),
                     str(delta_p),
                     kq_str
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)

    # Xuất câu trắc nghiệm trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
