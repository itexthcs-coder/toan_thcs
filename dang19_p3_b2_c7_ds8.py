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


def bt_dang19_p3_b2_c7_ds8(self):
    # Dạng 19: Giải bài toán bằng cách lập phương trình - Toán phần trăm lãi lỗ kinh doanh
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        von = random.choice([10, 15, 20, 25, 30])
        phan_ban = random.choice([(3, 4), (4, 5)])
        tu_p, mau_p = phan_ban
        lai_pct = random.choice([20, 25, 30])
        lo_pct = random.choice([10, 15, 20])
        
        dt1 = Rational(von * tu_p, mau_p) * Rational(100 + lai_pct, 100)
        dt2 = Rational(von * (mau_p - tu_p), mau_p) * Rational(100 - lo_pct, 100)
        tong_dt = dt1 + dt2
        lai_rong = tong_dt - von
        
        def fmt_dec(val):
            if val.q == 1:
                return str(val.p)
            d = Decimal(float(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
            s = format(d, 'f')
            return s.replace('.', ',')
            
        kq_str = fmt_dec(lai_rong)
        
        noidungcauhoi = ('''Một cửa hàng nhập về một lô hàng trái cây với tổng chi phí là $%s$ triệu đồng. Cửa hàng bán ra $\\frac{%s}{%s}$ số trái cây với giá cao hơn $%s\\%%$ so với giá nhập, phần còn lại do bảo quản lâu nên cửa hàng bán hạ giá thấp hơn $%s\\%%$ so với giá nhập. Hỏi sau khi bán hết lô hàng, cửa hàng lãi được bao nhiêu triệu đồng?'''
                         % (von, tu_p, mau_p, lai_pct, lo_pct))
        
        loigiai = ('''Gọi số tiền lãi sau khi bán hết lô hàng của cửa hàng là $x$ (triệu đồng). \\\\
Giá vốn của $\\frac{%s}{%s}$ lô hàng đầu là: $%s \\cdot \\frac{%s}{%s} = %s$ (triệu đồng). \\\\
Số tiền thu được khi bán $\\frac{%s}{%s}$ lô hàng đầu với giá cao hơn $%s\\%%$ là: \\\\
$%s \\cdot (100\\%% + %s\\%%) = %s \\cdot %s = %s$ (triệu đồng). \\\\
Giá vốn của phần hàng còn lại là: $%s - %s = %s$ (triệu đồng). \\\\
Số tiền thu được khi bán phần hàng còn lại với giá thấp hơn $%s\\%%$ là: \\\\
$%s \\cdot (100\\%% - %s\\%%) = %s \\cdot %s = %s$ (triệu đồng). \\\\
Theo đề bài, tổng số tiền thu được bằng tổng tiền vốn và tiền lãi nên ta có phương trình: \\\\
$%s + %s = %s + x$ \\\\
$\\Leftrightarrow %s = %s + x \\Leftrightarrow x = %s$ (triệu đồng). \\\\
Vậy sau khi bán hết lô hàng, cửa hàng lãi được $%s$ triệu đồng.'''
                   % (tu_p, mau_p, von, tu_p, mau_p, fmt_dec(Rational(von*tu_p, mau_p)),
                      tu_p, mau_p, lai_pct,
                      fmt_dec(Rational(von*tu_p, mau_p)), lai_pct, fmt_dec(Rational(von*tu_p, mau_p)), fmt_dec(Rational(100+lai_pct, 100)), fmt_dec(dt1),
                      von, fmt_dec(Rational(von*tu_p, mau_p)), fmt_dec(Rational(von*(mau_p-tu_p), mau_p)),
                      lo_pct,
                      fmt_dec(Rational(von*(mau_p-tu_p), mau_p)), lo_pct, fmt_dec(Rational(von*(mau_p-tu_p), mau_p)), fmt_dec(Rational(100-lo_pct, 100)), fmt_dec(dt2),
                      fmt_dec(dt1), fmt_dec(dt2), von,
                      fmt_dec(tong_dt), von, kq_str,
                      kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
