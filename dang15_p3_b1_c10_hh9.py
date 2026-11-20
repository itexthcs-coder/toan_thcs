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


def bt_dang15_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ab_val = random.randint(4, 7)
        ad_val = ab_val + random.randint(2, 4)
        v1_pi = (ad_val ** 2) * ab_val
        v2_pi = (ab_val ** 2) * ad_val
        hieu_pi = v1_pi - v2_pi
        hieu_approx = (Decimal(str(hieu_pi)) * Decimal('3.14')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(hieu_approx)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chữ nhật $ABCD$ có $AB = %s\\text{ cm}$, $AD = %s\\text{ cm}$. Gọi $V_1$ là thể tích hình trụ tạo thành khi quay hình chữ nhật quanh cạnh $AB$, và $V_2$ là thể tích hình trụ tạo thành khi quay hình chữ nhật quanh cạnh $AD$ (như hình vẽ). Tính giá trị của hiệu $V_1 - V_2$ theo đơn vị $\\text{cm}^3$ (làm tròn kết quả đến hàng đơn vị, lấy $\\pi \\approx 3,14$).
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,1.8);
\\coordinate (B) at (0,0);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (2.6,1.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[above] {$D$};
\\node[left] at (0,0.9) {$%s\\text{ cm}$};
\\node[below] at (1.3,0) {$%s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}'''
                         % (ab_val, ad_val, ab_val, ad_val))

        # Nội dung lời giải
        loigiai = ('''Khi quay hình chữ nhật quanh cạnh $AB$, hình trụ tạo thành có bán kính đáy $R_1 = AD = %s\\text{ cm}$ và chiều cao $h_1 = AB = %s\\text{ cm}$:
$$V_1 = \\pi R_1^2 h_1 = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Khi quay hình chữ nhật quanh cạnh $AD$, hình trụ tạo thành có bán kính đáy $R_2 = AB = %s\\text{ cm}$ và chiều cao $h_2 = AD = %s\\text{ cm}$:
$$V_2 = \\pi R_2^2 h_2 = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Hiệu thể tích cần tìm là:
$$V_1 - V_2 = %s\\pi - %s\\pi = %s\\pi \\approx %s \\cdot 3,14 \\approx %s\\text{ (cm}^3\\text{)}.$$'''
                   % (ad_val, ab_val, ad_val, ab_val, v1_pi,
                      ab_val, ad_val, ab_val, ad_val, v2_pi,
                      v1_pi, v2_pi, hieu_pi, hieu_pi, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
