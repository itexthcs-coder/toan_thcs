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


def bt_dang15_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        h_cyl = random.choice([2, 3, 4, 5])
        cases = [(Decimal('1.2'), Decimal('1.44'), 20), (Decimal('1.5'), Decimal('2.25'), 50), (Decimal('1.6'), Decimal('2.56'), 60)]
        k_rad, k_vol, pct_inc = random.choice(cases)
        
        a_coef = Decimal('3.14') * Decimal(h_cyl)
        a_str = str(a_coef).rstrip('0').rstrip('.').replace('.', ',')
        k_vol_str = str(k_vol).replace('.', ',')
        k_rad_str = str(k_rad).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một bể chứa nước hình trụ có chiều cao cố định là $h = %s$ m và bán kính đáy là $R$ (m). \\\\
a) Viết công thức tính thể tích $V$ ($\\text{m}^3$) của bể nước theo $R$ (lấy $\\pi \\approx 3,14$). \\\\
b) Người ta muốn mở rộng bể để sức chứa tăng gấp $%s$ lần mà vẫn giữ nguyên chiều cao. Hỏi bán kính đáy $R$ phải tăng thêm bao nhiêu phần trăm?'''
                         %(latex(h_cyl), k_vol_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thể tích của bể chứa nước hình trụ là: \\\\
$V = \\pi R^2 h \\approx 3,14 \\cdot R^2 \\cdot %s = %sR^2$ ($\\text{m}^3$).
\\item Gọi bán kính đáy mới của bể nước là $R'$ (m) ($R' > 0$). \\\\
Thể tích mới của bể nước khi giữ nguyên chiều cao là $V' = %s(R')^2$ ($\\text{m}^3$). \\\\
Theo đề bài, sức chứa tăng gấp $%s$ lần nên ta có: \\\\
$V' = %sV \\Leftrightarrow %s(R')^2 = %s \\cdot %sR^2 \\Leftrightarrow (R')^2 = %sR^2$. \\\\
Vì $R' > 0$ và $R > 0$ nên lấy căn bậc hai hai vế, ta được: \\\\
$R' = \\sqrt{%s}R = %sR = %s\\%% R$. \\\\
Vậy bán kính đáy $R$ phải tăng thêm $%s\\%%$.
\\end{enumEX}'''
                   %(latex(h_cyl), a_str,
                     a_str,
                     k_vol_str, k_vol_str, a_str, k_vol_str, a_str, k_vol_str,
                     k_vol_str, k_rad_str, latex(100 + pct_inc),
                     latex(pct_inc)
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
