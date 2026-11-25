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


def bt_dang20_p4_b2_c6_ds8(self):
    # Dạng 20: Tài chính & Kinh doanh - Bài toán điểm hòa vốn và chi phí trung bình trên một sản phẩm
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        cp_cd = 36
        cp_bd = Decimal('0.12')
        gia_ban = Decimal('0.20')
        x1 = 150
        x2 = 600
        c1 = (Decimal(cp_cd) / Decimal(x1) + cp_bd).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        c2 = (Decimal(cp_cd) / Decimal(x2) + cp_bd).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        sp_hoa_von = int(Decimal(cp_cd) / (gia_ban - cp_bd))

        cp_bd_str = str(cp_bd).replace('.', ',')
        gia_ban_str = str(gia_ban).replace('.', ',')
        c1_str = str(c1).replace('.', ',')
        c2_str = str(c2).replace('.', ',')
        chenh_str = str(gia_ban - cp_bd).replace('.', ',')

        noidungcauhoi = ('Một xưởng thủ công mỹ nghệ đầu tư chi phí cố định ban đầu (máy móc, mặt bằng) là $%s$ triệu đồng. Chi phí nguyên vật liệu và nhân công trực tiếp để làm ra mỗi sản phẩm là $%s$ triệu đồng.\\\n'
                         'a) Viết phân thức biểu thị chi phí trung bình $\\overline{C}(x)$ (tính theo triệu đồng) để sản xuất một sản phẩm khi xưởng làm ra $x$ sản phẩm ($x \\in \\mathbb{N}^*$).\\\n'
                         'b) Tính chi phí trung bình trên một sản phẩm khi xưởng sản xuất được $%s$ sản phẩm và khi sản xuất được $%s$ sản phẩm.\\\n'
                         'c) Xưởng bán mỗi sản phẩm ra thị trường với giá $%s$ triệu đồng. Hỏi xưởng cần sản xuất và bán được ít nhất bao nhiêu sản phẩm để bắt đầu thu được lợi nhuận (tức là chi phí trung bình thấp hơn giá bán)?'
                         % (cp_cd, cp_bd_str, x1, x2, gia_ban_str))

        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Tổng chi phí để sản xuất $x$ sản phẩm là $(%s + %sx)$ triệu đồng.\\\n'
                   'Phân thức biểu thị chi phí trung bình để sản xuất một sản phẩm là $\\overline{C}(x) = \\dfrac{%s + %sx}{x}$ (triệu đồng).\n'
                   '\\item Thay lần lượt $x = %s$ và $x = %s$ vào phân thức $\\overline{C}(x)$:\\\n'
                   '- Khi $x = %s$: $\\overline{C}(%s) = \\dfrac{%s + %s \\cdot %s}{%s} = \\dfrac{54}{%s} = %s$ (triệu đồng).\\\n'
                   '- Khi $x = %s$: $\\overline{C}(%s) = \\dfrac{%s + %s \\cdot %s}{%s} = \\dfrac{108}{%s} = %s$ (triệu đồng).\n'
                   '\\item Để xưởng thu được lợi nhuận thì chi phí trung bình phải thấp hơn giá bán, tức là $\\overline{C}(x) < %s$.\\\n'
                   'Với $x \\in \\mathbb{N}^*$, ta có $\\dfrac{%s + %sx}{x} < %s \\Leftrightarrow %s + %sx < %sx \\Leftrightarrow %sx > %s \\Leftrightarrow x > %s$.\\\n'
                   'Vì $x \\in \\mathbb{N}^*$ nên giá trị nhỏ nhất của $x$ là $%s$. Vậy xưởng cần sản xuất và bán được ít nhất $%s$ sản phẩm để bắt đầu có lãi.\n'
                   '\\end{enumEX}'
                   % (cp_cd, cp_bd_str, cp_cd, cp_bd_str,
                      x1, x2, x1, x1, cp_cd, cp_bd_str, x1, x1, x1, c1_str,
                      x2, x2, cp_cd, cp_bd_str, x2, x2, x2, c2_str,
                      gia_ban_str, cp_cd, cp_bd_str, gia_ban_str, cp_cd, cp_bd_str, gia_ban_str, chenh_str, cp_cd, sp_hoa_von,
                      sp_hoa_von + 1, sp_hoa_von + 1))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
