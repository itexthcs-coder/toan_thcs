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


def bt_dang20_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        p, q = random.choice([(3, 5), (4, 5), (3, 4)])
        half_W = Decimal(str(q)) * Decimal(str(random.choice([0.2, 0.4])))
        W_cua = 2 * half_W
        H_cua = Decimal(str(q**2)) * Decimal('0.1')
        d_dinh = Decimal(str(p**2)) * Decimal('0.1')
        h_nep = H_cua - d_dinh
        L_nep = 2 * half_W * Decimal(str(p)) / Decimal(str(q))

        W_cua_str = str(W_cua.normalize()).replace('.', ',')
        half_W_str = str(half_W.normalize()).replace('.', ',')
        H_cua_str = str(H_cua.normalize()).replace('.', ',')
        h_nep_str = str(h_nep.normalize()).replace('.', ',')
        d_dinh_str = str(d_dinh.normalize()).replace('.', ',')
        L_nep_str = str(L_nep.normalize()).replace('.', ',')
        a_abs_str = str((H_cua / (half_W**2)).normalize()).replace('.', ',')
        half_L_str = str((L_nep / 2).normalize()).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cửa sổ kính trang trí có dạng hình parabol với chiều rộng đáy ngang là $%s\\text{ m}$ và chiều cao từ đáy lên đỉnh vòm là $%s\\text{ m}$. Người thợ muốn lắp một thanh nẹp nhôm nằm ngang song song với đáy cửa sổ ở độ cao $%s\\text{ m}$ tính từ đáy cửa sổ lên. Chiều dài của thanh nẹp nhôm đó bằng bao nhiêu mét?
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3,0) -- (3,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-4.2) -- (0,1.2) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.2:2.2] plot (\\x, {-0.75*(\\x)^2});
\\draw[line width=1pt] (-2.2,-3.63) -- (2.2,-3.63);
\\draw[line width=1pt] (-1.32,-1.3068) -- (1.32,-1.3068);
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2.2,-3.63);
\\coordinate (B) at (2.2,-3.63);
\\coordinate (C) at (-1.32,-1.3068);
\\coordinate (D) at (1.32,-1.3068);
\\fill (O) circle (1pt) node[above left] {$O$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[left] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (W_cua_str, H_cua_str, h_nep_str))

        # Nội dung lời giải
        loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho gốc tọa độ $O(0;0)$ trùng với đỉnh vòm cửa sổ, trục $Oy$ hướng thẳng đứng lên trên và trục $Ox$ tiếp xúc với đỉnh vòm. \\\\
Vì cửa sổ có chiều rộng đáy ngang là $%s\\text{ m}$ và chiều cao $%s\\text{ m}$ nên hai góc đáy của cửa sổ có tọa độ là $A(-%s; -%s)$ và $B(%s; -%s)$. \\\\
Thay tọa độ điểm $B(%s; -%s)$ vào phương trình parabol $y = ax^2$, ta có: \\\\
$-%s = a \\cdot (%s)^2 \\Leftrightarrow a = -\\dfrac{%s}{(%s)^2} = -%s$. \\\\
Suy ra phương trình parabol của khung cửa sổ là $y = -%s x^2$. \\\\
Thanh nẹp nhôm $CD$ nằm ngang ở độ cao $%s\\text{ m}$ tính từ đáy cửa sổ lên nên khoảng cách từ đỉnh vòm $O$ xuống thanh nẹp $CD$ là: \\\\
$%s - %s = %s\\text{ (m)}$. \\\\
Do đó hai đầu mút $C$ và $D$ của thanh nẹp có tung độ $y = -%s$. Thay $y = -%s$ vào phương trình parabol, ta được: \\\\
$-%s = -%s x^2 \\Leftrightarrow x^2 = \\dfrac{%s}{%s} \\Leftrightarrow x = %s$ hoặc $x = -%s$. \\\\
Chiều dài của thanh nẹp nhôm $CD$ là: \\\\
$CD = |%s - (-%s)| = %s\\text{ (m)}$. \\\\
Vậy chiều dài của thanh nẹp nhôm bằng $%s\\text{ m}$.'''
                   % (W_cua_str, H_cua_str, half_W_str, H_cua_str, half_W_str, H_cua_str,
                      half_W_str, H_cua_str,
                      H_cua_str, half_W_str, H_cua_str, half_W_str, a_abs_str,
                      a_abs_str,
                      h_nep_str,
                      H_cua_str, h_nep_str, d_dinh_str,
                      d_dinh_str, d_dinh_str,
                      d_dinh_str, a_abs_str, d_dinh_str, a_abs_str,
                      half_L_str, half_L_str,
                      half_L_str, half_L_str, L_nep_str,
                      L_nep_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (L_nep_str)

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
