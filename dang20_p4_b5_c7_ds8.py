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

def fmt_so(val):
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        if val < 0:
            return '-\\frac{%s}{%s}' % (abs(val.numerator), val.denominator)
        return '\\frac{%s}{%s}' % (val.numerator, val.denominator)
    if isinstance(val, float):
        s = ('%g' % val).replace('.', ',')
        return s
    return str(val)

def fmt_dt(a, b):
    if a == 1:
        sa = 'x'
    elif a == -1:
        sa = '-x'
    else:
        sa = '%sx' % fmt_so(a)
    if b == 0:
        return sa
    elif b > 0:
        return '%s + %s' % (sa, fmt_so(b))
    else:
        return '%s - %s' % (sa, fmt_so(abs(b)))

def bt_dang20_p4_b5_c7_ds8(self):
    # Dạng 20: Bài toán thực tế về hàm chi phí, doanh thu và điểm hòa vốn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cp_bien = random.choice([0.12, 0.15, 0.2]) # trieu dong
        gia_ban = cp_bien + random.choice([0.08, 0.1, 0.15])
        x_hv = random.choice([120, 150, 180, 200])
        cp_cd = int(round((gia_ban - cp_bien) * x_hv))
        
        cp_bien_nghin = int(round(cp_bien * 1000))
        gia_ban_nghin = int(round(gia_ban * 1000))
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (0,0) -- (4.5,0) node[below] {$x$ (sản phẩm)};\n'
            '\\draw[->, line width=1pt] (0,0) -- (0,3.8) node[left] {Triệu đồng};\n'
            '\\draw[line width=1pt] (0,1.1) -- (4,3.1) node[right] {$C(x)$};\n'
            '\\draw[line width=1pt] (0,0) -- (3.8,3.6) node[right] {$R(x)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (2.46,2.33) circle (1pt) node[above left] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Một xưởng thủ công mỹ nghệ có chi phí cố định hằng tháng (tiền thuê mặt bằng, khấu hao máy móc) là $%s\\text{ triệu đồng}$ và chi phí nguyên vật liệu, nhân công để làm ra mỗi sản phẩm là $%s\\text{ nghìn đồng}$. Xưởng bán mỗi sản phẩm ra thị trường với giá $%s\\text{ nghìn đồng}$. Gọi $x$ là số sản phẩm sản xuất và bán ra trong một tháng ($x \\in \\mathbb{N}^*$).\\\n'
            'a) Viết hàm số biểu diễn tổng chi phí $C(x)$ và tổng doanh thu $R(x)$ (đơn vị: triệu đồng) theo số sản phẩm $x$.\\\n'
            'b) So sánh hệ số góc của hai đường thẳng biểu diễn $C(x)$ và $R(x)$. Giải thích vì sao nếu hệ số góc của $R(x)$ nhỏ hơn hoặc bằng hệ số góc của $C(x)$ thì xưởng không bao giờ có lãi.\\\n'
            'c) Tìm số sản phẩm tối thiểu xưởng cần bán được trong tháng để bắt đầu có lãi.'
            % (cp_cd, cp_bien_nghin, gia_ban_nghin)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Đổi $%s\\text{ nghìn đồng} = %s\\text{ triệu đồng}$; $%s\\text{ nghìn đồng} = %s\\text{ triệu đồng}$.\\\n'
            'Tổng chi phí trong tháng gồm chi phí cố định và chi phí sản xuất $x$ sản phẩm: $C(x) = %sx + %s$ (triệu đồng).\\\n'
            'Tổng doanh thu khi bán $x$ sản phẩm là: $R(x) = %sx$ (triệu đồng).\n'
            '\\item Đường thẳng biểu diễn $C(x)$ có hệ số góc $a_C = %s$, đường thẳng biểu diễn $R(x)$ có hệ số góc $a_R = %s$. Ta thấy $a_R > a_C$ (vì $%s > %s$).\\\n'
            'Nếu $a_R \\le a_C$ thì hoặc hai đường thẳng song song ($a_R = a_C$), hoặc đường thẳng $R(x)$ có độ dốc nhỏ hơn $C(x)$ ($a_R < a_C$). Vì tại $x = 0$ ta có $R(0) = 0 < C(0) = %s$ nên với mọi $x > 0$, đường thẳng $R(x)$ luôn nằm phía dưới đường thẳng $C(x)$ (doanh thu luôn nhỏ hơn chi phí), do đó xưởng không bao giờ có lãi.\n'
            '\\item Xưởng hòa vốn khi $R(x) = C(x) \\Leftrightarrow %sx = %sx + %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (sản phẩm).\\\n'
            'Vậy xưởng cần bán được tối thiểu $%s$ sản phẩm trong tháng để bắt đầu có lãi.%s\n'
            '\\end{enumEX}'
            % (cp_bien_nghin, fmt_so(cp_bien), gia_ban_nghin, fmt_so(gia_ban),
               fmt_so(cp_bien), cp_cd, fmt_so(gia_ban),
               fmt_so(cp_bien), fmt_so(gia_ban), fmt_so(gia_ban), fmt_so(cp_bien), cp_cd,
               fmt_so(gia_ban), fmt_so(cp_bien), cp_cd, fmt_so(round(gia_ban - cp_bien, 4)), cp_cd, x_hv, x_hv + 1, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
