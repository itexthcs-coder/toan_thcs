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


def bt_dang11_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (4, 10, 5, 4, 52),
            (6, 12, 5, 4, 84),
            (2, 8, 5, 4, 28),
            (6, 16, 13, 12, 148)
        ]
        ab_val, cd_val, ad_val, h_thang, k_val = random.choice(cau_hinh)
        r_nho = ab_val // 2
        r_lon = cd_val // 2
        hieu_r = r_lon - r_nho
        kq_str = str(k_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thang cân $ABCD$ ($AB // CD$) có đáy nhỏ $AB = %s\\text{ cm}$, đáy lớn $CD = %s\\text{ cm}$ và cạnh bên $AD = %s\\text{ cm}$ (như hình vẽ). Quay hình thang cân $ABCD$ một vòng quanh trục đối xứng của nó (đường thẳng đi qua trung điểm hai đáy), ta được một hình nón cụt. Biết thể tích của hình nón cụt tạo thành bằng $k\\pi\\text{ (cm}^3\\text{)}$, tìm giá trị của $k$.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (-1,1.8);
\\coordinate (B) at (1,1.8);
\\coordinate (D) at (-2,0);
\\coordinate (C) at (2,0);
\\draw[line width=1pt] (0,1.8) ellipse (1 and 0.25);
\\draw[line width=1pt] (-2,0) arc (180:360:2 and 0.4);
\\draw[line width=1pt, dashed] (2,0) arc (0:180:2 and 0.4);
\\draw[line width=1pt] (A)--(D) (B)--(C);
\\draw[line width=1pt, dashed] (0,2.3)--(0,-0.5) (D)--(C);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (C) circle (1pt) node[right] {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (ab_val, cd_val, ad_val))

        # Nội dung lời giải
        loigiai = ('''Hình nón cụt tạo thành có bán kính đáy nhỏ là $r = \\frac{AB}{2} = %s\\text{ cm}$ và bán kính đáy lớn là $R = \\frac{CD}{2} = %s\\text{ cm}$. \\\\
Hạ đường cao $AH$ của hình thang cân ($H \\in CD$), ta có $DH = R - r = %s - %s = %s\\text{ cm}$. \\\\
Chiều cao của hình nón cụt là: $h = AH = \\sqrt{AD^2 - DH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}$. \\\\
Áp dụng công thức tính thể tích hình nón cụt (hiệu thể tích hình nón lớn và hình nón nhỏ đồng dạng ở phần đỉnh):
$$V = \\frac{1}{3}\\pi h (R^2 + Rr + r^2) = \\frac{1}{3}\\pi \\cdot %s \\cdot (%s^2 + %s \\cdot %s + %s^2) = %s\\pi\\text{ (cm}^3\\text{)}.$$
Vậy $k = %s$.'''
                   % (r_nho, r_lon, r_lon, r_nho, hieu_r, ad_val, hieu_r, h_thang,
                      h_thang, r_lon, r_lon, r_nho, r_nho, k_val, k_val))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
