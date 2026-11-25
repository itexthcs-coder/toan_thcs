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


def bt_dang9_p4_b2_c5_ds8(self):
    # Dạng 9 (Tự luận - Vận dụng): Biện luận tính hợp lý của cả hai loại biểu đồ theo mục đích người dùng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        ak, qa, vay = 150 * k, 250 * k, 100 * k
        tong = ak + qa + vay
        
        tikz_col = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.4) node[above] {Số lượng (chiếc)};
        \\draw[line width=1pt, ->] (0,0) -- (5.0,0) node[right] {Mặt hàng};
        \\draw[line width=1pt, fill=black!25] (0.6,0) rectangle (1.3,1.2); \\node[above] at (0.95,1.2) {$%s$}; \\node[below] at (0.95,0) {Áo khoác};
        \\draw[line width=1pt, fill=black!25] (2.0,0) rectangle (2.7,2.0); \\node[above] at (2.35,2.0) {$%s$}; \\node[below] at (2.35,0) {Quần âu};
        \\draw[line width=1pt, fill=black!25] (3.4,0) rectangle (4.1,0.8); \\node[above] at (3.75,0.8) {$%s$}; \\node[below] at (3.75,0) {Váy};
        \\end{tikzpicture}
        \\end{center}""" % (ak, qa, vay))
        
        tikz_pie = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.4);
        \\draw[line width=1pt] (0,0) -- (0:1.4) (0,0) -- (108:1.4) (0,0) -- (288:1.4);
        \\node at (54:0.85) {$30\\%$};
        \\node at (198:0.85) {$50\\%$};
        \\node at (324:0.85) {$20\\%$};
        \\node[right] at (1.8, 0.5) {Áo khoác: $30\\%$};
        \\node[right] at (1.8, 0.0) {Quần âu: $50\\%$};
        \\node[right] at (1.8, -0.5) {Váy: $20\\%$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Một cửa hàng thời trang thống kê số lượng sản phẩm bán được trong tháng $10$ gồm: $%s$ chiếc áo khoác, $%s$ chiếc quần âu và $%s$ chiếc váy.\\\\
        - Bạn An nói: ``Tớ sẽ dùng biểu đồ cột để biểu diễn bảng thống kê này.''\\\\
        - Bạn Bình nói: ``Tớ lại muốn dùng biểu đồ hình quạt tròn để biểu diễn.''\\\\
        Theo em, bạn nào chọn đúng? Hãy giải thích mục đích của từng bạn và vẽ cả hai loại biểu đồ đó để minh họa.""" % (ak, qa, vay))
        
        loigiai = ("""- \\textbf{Cả hai bạn đều chọn đúng} vì việc lựa chọn biểu đồ phụ thuộc vào mục đích phân tích của người dùng.\\\\
        - Bạn An dùng \\textbf{biểu đồ cột} nhằm so sánh trực quan \\textbf{số lượng cụ thể} bán ra của từng mặt hàng ($%s$; $%s$; $%s$ chiếc).%s
        - Bạn Bình dùng \\textbf{biểu đồ hình quạt tròn} nhằm thể hiện \\textbf{cơ cấu tỉ trọng phần trăm} của mỗi mặt hàng trong tổng số $%s$ sản phẩm bán ra (Áo khoác chiếm $\\dfrac{%s}{%s} = 30\\%%$, Quần âu chiếm $\\dfrac{%s}{%s} = 50\\%%$, Váy chiếm $\\dfrac{%s}{%s} = 20\\%%$).%s"""
                   % (ak, qa, vay, tikz_col, tong, ak, tong, qa, tong, vay, tong, tikz_pie))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
