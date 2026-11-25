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


def bt_dang14_p4_b2_c5_ds8(self):
    # Dạng 14 (Tự luận - Vận dụng): Đánh giá sai lầm chọn tỉ xích và vẽ lại biểu đồ đoạn thẳng chuẩn xác
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        def fmt_vn(val):
            return f"{val:.2f}".replace(".", ",")
        d = Decimal(str(random.choice([0.00, 0.20, 0.40])))
        n1 = Decimal('6.12') + d
        n2 = Decimal('6.18') + d
        n3 = Decimal('6.25') + d
        n4 = Decimal('6.21') + d
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Mực nước (m)};
        \\draw[line width=1pt, ->] (0,0) -- (5.6,0) node[right] {Ngày};
        \\coordinate (A) at (0.9,0.7);
        \\coordinate (B) at (2.2,1.3);
        \\coordinate (C) at (3.5,2.0);
        \\coordinate (D) at (4.8,1.6);
        \\draw[line width=1pt] (A)--(B)--(C)--(D);
        \\fill (A) circle (1pt) node[below right] {$%s$};
        \\fill (B) circle (1pt) node[above left] {$%s$};
        \\fill (C) circle (1pt) node[above] {$%s$};
        \\fill (D) circle (1pt) node[above right] {$%s$};
        \\node[below] at (0.9,0) {Ngày 1};
        \\node[below] at (2.2,0) {Ngày 2};
        \\node[below] at (3.5,0) {Ngày 3};
        \\node[below] at (4.8,0) {Ngày 4};
        \\end{tikzpicture}
        \\end{center}""" % (fmt_vn(n1), fmt_vn(n2), fmt_vn(n3), fmt_vn(n4)))
        
        noidungcauhoi = ("""Một bạn học sinh thu thập số liệu về chiều cao mực nước sông Hồng tại một trạm đo trong $4$ ngày liên tiếp: Ngày 1 là $%s\\text{ m}$; Ngày 2 là $%s\\text{ m}$; Ngày 3 là $%s\\text{ m}$; Ngày 4 là $%s\\text{ m}$. Bạn đó vẽ biểu đồ cột với trục tung bắt đầu từ $0\\text{ m}$ đến $10\\text{ m}$ (mỗi vạch chia ứng với $2\\text{ m}$) và kết luận rằng mực nước sông hầu như không thay đổi.\\\\
        a) Hãy chỉ ra hạn chế trong cách chọn tỉ xích trục tung của bạn học sinh đó.\\\\
        b) Theo em, nên dùng loại biểu đồ nào để thấy rõ nhất sự lên xuống của mực nước sông qua $4$ ngày trên? Hãy vẽ biểu đồ đó."""
                         % (fmt_vn(n1), fmt_vn(n2), fmt_vn(n3), fmt_vn(n4)))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Hạn chế: Các số liệu mực nước chỉ dao động trong khoảng hẹp từ $%s\\text{ m}$ đến $%s\\text{ m}$ (chênh lệch tối đa $0,13\\text{ m}$). Khi chia trục tung từ $0$ đến $10\\text{ m}$ với bước chia quá lớn ($2\\text{ m}$), độ cao bốn cột gần như bằng nhau nên che lấp sự biến động thực tế của mực nước.
        \\item Để thấy rõ xu hướng lên xuống của mực nước qua các ngày, ta nên dùng \textbf{biểu đồ đoạn thẳng} với khoảng chia trục tung thu hẹp quanh vùng biến thiên:%s
        \\end{enumEX}""" % (fmt_vn(n1), fmt_vn(n3), tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
