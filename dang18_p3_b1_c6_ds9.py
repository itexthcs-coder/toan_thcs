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


def bt_dang18_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        L_cau = random.choice([8, 10, 12])
        half_L = L_cau // 2
        H_cau = Decimal(str(random.choice([3.2, 3.6, 4.0, 4.5])))
        W_thuyen = random.choice([3, 4])
        half_W = W_thuyen / 2
        H_thuyen = Decimal(str(random.choice([2.0, 2.2, 2.5])))

        H_cau_float = float(H_cau)
        a_val = -H_cau_float / (half_L**2)
        y_mep = a_val * (half_W**2)
        h_vom_tai_mep = H_cau_float + y_mep
        khoang_cach = h_vom_tai_mep - float(H_thuyen)

        number = Decimal(str(khoang_cach))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
        H_cau_str = str(H_cau).replace('.', ',')
        H_thuyen_str = str(H_thuyen).replace('.', ',')
        half_W_str = str(half_W).replace('.', ',') if half_W % 1 != 0 else str(int(half_W))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc thuyền chở hàng có bề rộng thân thuyền là $%s\\text{ m}$, phần mui thuyền nhô lên khỏi mặt nước cao $%s\\text{ m}$ (mặt cắt ngang phần mui coi như hình chữ nhật). Thuyền cần đi qua một gầm cầu vòm dạng parabol có chiều rộng chân cầu tại mặt nước là $%s\\text{ m}$ và khoảng cách từ đỉnh vòm xuống mặt nước là $%s\\text{ m}$. Hỏi khoảng cách an toàn tối thiểu theo phương thẳng đứng từ nóc mui thuyền tới trần vòm cầu khi thuyền đi chính giữa gầm cầu là bao nhiêu mét? (Làm tròn đến hàng phần trăm).
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-3.5) -- (0,1.2) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-3:3] plot (\\x, {-0.32*(\\x)^2});
\\draw[line width=1pt] (-3.3,-2.88) -- (3.3,-2.88) node[right] {Mặt nước};
\\draw[line width=1pt] (-1.2,-2.88) -- (-1.2,-1.1) -- (1.2,-1.1) -- (1.2,-2.88);
\\coordinate (O) at (0,0);
\\coordinate (A) at (-3,-2.88);
\\coordinate (B) at (3,-2.88);
\\coordinate (K) at (1.2,-0.4608);
\\coordinate (M) at (1.2,-1.1);
\\draw[line width=1pt, dashed] (K)--(M);
\\fill (O) circle (1pt) node[above left] {$O$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (K) circle (1pt) node[above right] {$K$};
\\fill (M) circle (1pt) node[right] {$M$};
\\end{tikzpicture}
\\end{center}'''
                         % (str(W_thuyen), H_thuyen_str, str(L_cau), H_cau_str))

        # Nội dung lời giải
        loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho gốc tọa độ $O(0;0)$ trùng với đỉnh vòm cầu, trục $Oy$ hướng thẳng đứng lên trên và trục $Ox$ nằm ngang tiếp xúc với đỉnh vòm cầu. \\\\
Vì chiều rộng chân cầu là $%s\\text{ m}$ và khoảng cách từ đỉnh vòm xuống mặt nước là $%s\\text{ m}$ nên hai chân cầu tại mặt nước có tọa độ là $A(-%s; -%s)$ và $B(%s; -%s)$. \\\\
Thay tọa độ điểm $B(%s; -%s)$ vào phương trình parabol $y = ax^2$, ta được: \\\\
$-%s = a \\cdot %s^2 \\Leftrightarrow a = -\\dfrac{%s}{%s}$. \\\\
Khi thuyền đi chính giữa gầm cầu, hai mép ngoài của mui thuyền cách trục đối xứng $Oy$ một khoảng bằng $\\dfrac{%s}{2} = %s\\text{ m}$. \\\\
Tại vị trí $x = %s$, điểm $K$ trên vòm cầu có tung độ là: \\\\
$y_K = -\\dfrac{%s}{%s} \\cdot (%s)^2$. \\\\
Chiều cao từ mặt nước lên tới điểm $K$ trên trần vòm cầu là: \\\\
$h_K = %s + y_K = %s - \\dfrac{%s}{%s} \\cdot (%s)^2$. \\\\
Khoảng cách an toàn tối thiểu theo phương thẳng đứng từ nóc mui thuyền cao $%s\\text{ m}$ tới trần vòm cầu là: \\\\
$d = h_K - %s \\approx %s\\text{ (m)}$.'''
                   % (str(L_cau), H_cau_str, str(half_L), H_cau_str, str(half_L), H_cau_str,
                      str(half_L), H_cau_str,
                      H_cau_str, str(half_L), H_cau_str, str(half_L**2),
                      str(W_thuyen), half_W_str,
                      half_W_str,
                      H_cau_str, str(half_L**2), half_W_str,
                      H_cau_str, H_cau_str, H_cau_str, str(half_L**2), half_W_str,
                      H_thuyen_str,
                      H_thuyen_str, str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
