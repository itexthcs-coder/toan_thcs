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


def bt_dang14_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k_len = randint(2, 4)
        p_inc = random.choice([10, 20, 30])
        p_dec = random.choice([10, 20, 30])
        factor_inc = Decimal(100 + p_inc) / Decimal(100)
        factor_dec = Decimal(100 - p_dec) / Decimal(100)
        ratio_s = factor_inc * factor_dec
        a_new = Decimal(k_len) * ratio_s
        
        a_new_str = str(a_new).rstrip('0').rstrip('.').replace('.', ',')
        f_inc_str = str(factor_inc).rstrip('0').rstrip('.').replace('.', ',')
        f_dec_str = str(factor_dec).rstrip('0').rstrip('.').replace('.', ',')
        
        diff_pct = (ratio_s - Decimal(1)) * Decimal(100)
        if diff_pct < 0:
            status_str = "giảm"
            pct_val_str = str(abs(diff_pct)).rstrip('0').rstrip('.').replace('.', ',')
        elif diff_pct > 0:
            status_str = "tăng"
            pct_val_str = str(diff_pct).rstrip('0').rstrip('.').replace('.', ',')
        else:
            status_str = "không đổi"
            pct_val_str = "0"

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chữ nhật $ABCD$ có chiều dài $AB = %sx$ (cm) và chiều rộng $BC = x$ (cm) với $x > 0$. \\\\
a) Lập công thức biểu diễn diện tích $S$ ($\\text{cm}^2$) của hình chữ nhật $ABCD$ theo $x$. \\\\
b) Nếu tăng chiều dài thêm $%s\\%%$ và giảm chiều rộng đi $%s\\%%$ thì diện tích hình chữ nhật mới $S'$ là hàm số bậc hai nào theo $x$? Diện tích mới %s bao nhiêu phần trăm so với diện tích ban đầu?'''
                         %(latex(k_len), latex(p_inc), latex(p_dec), status_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Diện tích của hình chữ nhật $ABCD$ ban đầu là: \\\\
$S = AB \\cdot BC = %sx \\cdot x = %sx^2$ ($\\text{cm}^2$).
\\item Chiều dài mới của hình chữ nhật sau khi tăng thêm $%s\\%%$ là: \\\\
$AB' = %sx \\cdot (100\\%% + %s\\%%) = %sx \\cdot %s$ (cm). \\\\
Chiều rộng mới của hình chữ nhật sau khi giảm đi $%s\\%%$ là: \\\\
$BC' = x \\cdot (100\\%% - %s\\%%) = %sx$ (cm). \\\\
Diện tích hình chữ nhật mới là: \\\\
$S' = AB' \\cdot BC' = (%sx \\cdot %s) \\cdot (%sx) = %sx^2$ ($\\text{cm}^2$). \\\\
Tỷ số giữa diện tích mới và diện tích ban đầu là: \\\\
$\\frac{S'}{S} = \\frac{%sx^2}{%sx^2} = %s = %s\\%%$. \\\\
Vậy diện tích mới %s $%s\\%%$ so với diện tích ban đầu.
\\end{enumEX}'''
                   %(latex(k_len), latex(k_len),
                     latex(p_inc), latex(k_len), latex(p_inc), latex(k_len), f_inc_str,
                     latex(p_dec), latex(p_dec), f_dec_str,
                     latex(k_len), f_inc_str, f_dec_str, a_new_str,
                     a_new_str, latex(k_len), str(ratio_s).rstrip('0').rstrip('.').replace('.', ','), str(ratio_s * 100).rstrip('0').rstrip('.').replace('.', ','),
                     status_str, pct_val_str
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
