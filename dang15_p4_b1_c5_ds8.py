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


def bt_dang15_p4_b1_c5_ds8(self):
    # Dạng 15: Kiểm định và làm sạch dữ liệu trong sản xuất nông sản xuất khẩu
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        while True:
            w1 = random.randint(380, 460)
            w2 = random.randint(380, 460)
            w3 = random.randint(380, 460)
            w4 = random.randint(380, 460)
            w5 = random.randint(380, 460)
            w6_true = random.randint(410, 450)
            if w6_true % 10 != 0 and len({w1, w2, w3, w4, w5, w6_true}) >= 5 and (w1 + w2 + w3 + w4 + w5 + w6_true) % 6 == 0:
                break

        w6_true_str = "%s,0" % w6_true
        w6_sai_str = "%s,%s" % (w6_true // 10, w6_true % 10)

        day = ["%s,0" % w1, "%s,0" % w2, "%s,0" % w3, w6_sai_str, "%s,0" % w4, "%s,0" % w5]
        random.shuffle(day)
        day_str = ";\\; ".join(day)

        tb_val = Decimal(w1 + w2 + w3 + w4 + w5 + w6_true) / Decimal(6)
        tb_str = str(tb_val).replace('.', ',')
        if tb_str.endswith(',0'):
            tb_str = tb_str[:-2]

        noidungcauhoi = ('''Một hợp tác xã thu hoạch xoài xuất khẩu quy định mỗi quả xoài đạt chuẩn loại $1$ phải có khối lượng từ $350\\,\\text{g}$ đến $500\\,\\text{g}$. Nhân viên kiểm tra cân ngẫu nhiên $6$ quả xoài trong một lô hàng đạt chuẩn và ghi lại dãy số liệu (đơn vị: gam):
$$%s$$
a) Số liệu khối lượng quả xoài thuộc loại số liệu nào? Phương pháp thu thập dữ liệu ở đây là gì?\\\\
b) Chỉ ra giá trị bất thường trong dãy số liệu trên (biết nhân viên đã gõ thiếu một chữ số $0$ ở cuối phần nguyên do lỗi bàn phím), khôi phục số liệu đúng và tính khối lượng trung bình của $6$ quả xoài.'''
                         % day_str)

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Khối lượng quả xoài thu được từ phép cân đo và có thể nhận giá trị thực tùy ý trong một khoảng nên thuộc loại \\textbf{số liệu liên tục}. Nhân viên trực tiếp cân từng quả xoài trên lô hàng nên đây là \\textbf{phương pháp thu thập dữ liệu trực tiếp}.
\\item Trong dãy số liệu $%s$, giá trị $%s\\,\\text{g}$ là bất thường vì nhỏ hơn nhiều so với quy chuẩn $350\\,\\text{g} - 500\\,\\text{g}$.\\\\
Do nhân viên gõ thiếu chữ số $0$ ở cuối phần nguyên nên giá trị đúng của quả xoài đó là $%s\\,\\text{g}$.\\\\
Khối lượng trung bình của cả $6$ quả xoài sau khi khôi phục số liệu đúng là:
$$\\dfrac{%s,0 + %s,0 + %s,0 + %s,0 + %s,0 + %s}{6} = %s\\,(\\text{g}).$$
\\end{enumEX}'''
                   % (day_str, w6_sai_str, w6_true_str,
                      w1, w2, w3, w4, w5, w6_true_str, tb_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
