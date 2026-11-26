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


def bt_dang19_p4_b2_c7_ds8(self):
    # Dạng 19: Ứng dụng - Bài toán tài chính tiêu dùng giảm giá hai lần liên tiếp
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        gia_goc = random.choice([15, 20, 25, 30])  # triệu đồng
        giam1 = random.choice([10, 15, 20])
        giam2 = random.choice([5, 8, 10])
        
        he_so1 = Rational(100 - giam1, 100)
        he_so2 = Rational(100 - giam2, 100)
        he_so_tong = he_so1 * he_so2
        gia_tra = gia_goc * he_so_tong
        
        def fmt_dec(val):
            d = Decimal(float(val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP).normalize()
            s = format(d, 'f')
            return s.replace('.', ',')
            
        gia_tra_vnd = int(round(float(gia_tra) * 1000000))
        gia_tra_vnd_str = f"{gia_tra_vnd:,}".replace(',', '\\,')
        gia_goc_vnd_str = f"{gia_goc * 1000000:,}".replace(',', '\\,')
        
        noidungcauhoi = ('''Nhân dịp khai trương, một cửa hàng điện tử áp dụng chương trình ưu đãi cho một chiếc máy tính bảng: giảm giá trực tiếp $%s\\%%$ trên giá niêm yết; nếu khách hàng thanh toán bằng ví điện tử thì được giảm tiếp $%s\\%%$ trên giá đã giảm ở lần thứ nhất. Chị Lan mua chiếc máy tính bảng đó và thanh toán bằng ví điện tử với số tiền thực trả là $%s$ đồng. Hỏi giá niêm yết ban đầu của chiếc máy tính bảng là bao nhiêu?'''
                         % (giam1, giam2, gia_tra_vnd_str))
        
        loigiai = ('''Đổi $%s\\text{ đồng} = %s\\text{ triệu đồng}$. \\\\
Gọi giá niêm yết ban đầu của chiếc máy tính bảng là $x$ (triệu đồng) (điều kiện: $x > 0$). \\\\
- Giá của chiếc máy tính bảng sau khi giảm $%s\\%%$ lần thứ nhất là: \\\\
$x \\cdot (100\\%% - %s\\%%) = %sx$ (triệu đồng). \\\\
- Số tiền thực trả sau khi giảm tiếp $%s\\%%$ trên giá đã giảm ở lần thứ nhất là: \\\\
$%sx \\cdot (100\\%% - %s\\%%) = %sx \\cdot %s = %sx$ (triệu đồng). \\\\
Theo đề bài, chị Lan thanh toán hết $%s$ triệu đồng nên ta có phương trình: \\\\
$%sx = %s \\Leftrightarrow x = \\frac{%s}{%s} = %s$ (thỏa mãn điều kiện). \\\\
Vậy giá niêm yết ban đầu của chiếc máy tính bảng là $%s$ đồng ($%s$ triệu đồng).'''
                   % (gia_tra_vnd_str, fmt_dec(gia_tra),
                      giam1, giam1, fmt_dec(he_so1),
                      giam2, fmt_dec(he_so1), giam2, fmt_dec(he_so1), fmt_dec(he_so2), fmt_dec(he_so_tong),
                      fmt_dec(gia_tra),
                      fmt_dec(he_so_tong), fmt_dec(gia_tra), fmt_dec(gia_tra), fmt_dec(he_so_tong), gia_goc,
                      gia_goc_vnd_str, gia_goc))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
