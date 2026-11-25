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


def bt_dang13_p4_b2_c5_ds8(self):
    # Dạng 13 (Tự luận - Vận dụng): Điều chỉnh cơ cấu ngân sách và vẽ lại biểu đồ hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tn = random.choice([20, 30, 40])
        sh = tn * 50 // 100
        gd = tn * 20 // 100
        gt = tn * 15 // 100
        tk = tn * 15 // 100
        chuyen = gt * 40 // 100
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.5);
        \\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (180:1.5) (0,0) -- (252:1.5) (0,0) -- (284.4:1.5);
        \\node at (90:0.9) {$50\\%$};
        \\node at (216:0.9) {$20\\%$};
        \\node at (268:1.05) {$9\\%$};
        \\node at (322:0.95) {$21\\%$};
        \\node[right] at (1.9, 0.8) {Sinh hoạt: $50\\%$};
        \\node[right] at (1.9, 0.25) {Giáo dục: $20\\%$};
        \\node[right] at (1.9, -0.3) {Giải trí: $9\\%$};
        \\node[right] at (1.9, -0.85) {Tiết kiệm: $21\\%$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Gia đình chị Mai có tổng thu nhập tháng là $%s\\,000\\,000$ đồng được phân bổ như sau: Chi tiêu sinh hoạt ($50\\%%$), Giáo dục ($20\\%%$), Giải trí ($15\\%%$) và Tiết kiệm ($15\\%%$).\\\\
        a) Tính số tiền cụ thể gia đình chị Mai dành cho mỗi khoản mục trong tháng.\\\\
        b) Sang tháng sau, tổng thu nhập không đổi nhưng gia đình chị quyết định cắt giảm $40\\%%$ số tiền của khoản Giải trí để chuyển toàn bộ sang khoản Tiết kiệm. Hãy lập bảng tỉ lệ phần trăm mới của bốn khoản mục và vẽ biểu đồ hình quạt tròn biểu diễn cơ cấu chi tiêu mới này."""
                         % tn)
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Số tiền cụ thể cho từng khoản mục trong tháng là:\\\\
        - Chi tiêu sinh hoạt: $%s\\,000\\,000 \\cdot 50\\%% = %s\\,000\\,000$ (đồng).\\\\
        - Giáo dục: $%s\\,000\\,000 \\cdot 20\\%% = %s\\,000\\,000$ (đồng).\\\\
        - Giải trí: $%s\\,000\\,000 \\cdot 15\\%% = %s\\,000\\,000$ (đồng).\\\\
        - Tiết kiệm: $%s\\,000\\,000 \\cdot 15\\%% = %s\\,000\\,000$ (đồng).
        \\item Khi cắt giảm $40\\%%$ của khoản Giải trí ($15\\%%$ thu nhập), tỉ lệ cắt giảm tương ứng với $15\\%% \\cdot 40\\%% = 6\\%%$ tổng thu nhập (tức $%s\\,000\\,000$ đồng).\\\\
        Do đó cơ cấu tỉ lệ phần trăm mới là: Sinh hoạt $50\\%%$; Giáo dục $20\\%%$; Giải trí $15\\%% - 6\\%% = 9\\%%$; Tiết kiệm $15\\%% + 6\\%% = 21\\%%$.\\\\
        Bảng tỉ lệ mới và biểu đồ hình quạt tròn tương ứng:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Khoản mục} & Sinh hoạt & Giáo dục & Giải trí & Tiết kiệm \\\\
        \\hline
        \\textbf{Tỉ lệ mới} & $50\\%%$ & $20\\%%$ & $9\\%%$ & $21\\%%$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}%s
        \\end{enumEX}""" % (tn, sh, tn, gd, tn, gt, tn, tk, chuyen, tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
