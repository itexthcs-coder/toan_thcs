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


def bt_dang17_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        r_val = random.choice([3, 4])
        d_val = 2 * r_val
        h_val = random.choice([20, 25, 30])
        so_vong = random.choice([15, 20, 25])
        sxq_1vong = 2 * r_val * h_val
        sxq_tong_pi = so_vong * sxq_1vong
        s_cm2 = Decimal(str(sxq_tong_pi)) * Decimal('3.14')
        s_m2 = (s_cm2 / Decimal('10000')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        s_cm2_str = str(s_cm2.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        kq_str = str(s_m2).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cây lăn sơn tường có dạng một hình trụ với đường kính đáy bằng $%s\\text{ cm}$ và chiều dài (chiều cao) bằng $%s\\text{ cm}$ (như hình vẽ). Sau khi lăn trọn $%s$ vòng trên một bức tường phẳng (không chồng lấn), cây lăn sơn đã phủ sơn được một diện tích bằng bao nhiêu $\\text{m}^2$ (làm tròn kết quả đến hàng phần trăm, lấy $\\pi \\approx 3,14$)?
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0.8) ellipse (0.25 and 0.7);
\\draw[line width=1pt] (3.2,0.1) arc (-90:90:0.25 and 0.7);
\\draw[line width=1pt, dashed] (3.2,1.5) arc (90:270:0.25 and 0.7);
\\draw[line width=1pt] (0,0.1)--(3.2,0.1) (0,1.5)--(3.2,1.5);
\\draw[line width=1pt] (3.45,0.8)--(3.8,0.8)--(3.8,0)--(2.2,0)--(2.2,-0.8);
\\end{tikzpicture}
\\end{center}'''
                         % (d_val, h_val, so_vong))

        # Nội dung lời giải
        loigiai = ('''Bán kính đáy của cây lăn sơn hình trụ là: $R = \\frac{%s}{2} = %s\\text{ (cm)}$. \\\\
Diện tích tường được phủ sơn sau khi lăn trọn $1$ vòng chính là diện tích xung quanh của hình trụ:
$$S_{xq} = 2\\pi R h = 2\\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}.$$
Diện tích tường được phủ sơn sau khi lăn trọn $%s$ vòng là:
$$S = %s \\cdot %s\\pi = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (cm}^2\\text{)} \\approx %s\\text{ (m}^2\\text{)}.$$'''
                   % (d_val, r_val, r_val, h_val, sxq_1vong, so_vong, so_vong, sxq_1vong,
                      sxq_tong_pi, sxq_tong_pi, s_cm2_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
