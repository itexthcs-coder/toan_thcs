# -*- coding: utf-8 -*-
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


def bt_dang20_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        so_buoc = random.choice([2, 3, 4, 5])
        goc_moi_buoc = random.choice([60, 120])
        tong_goc = so_buoc * goc_moi_buoc
        so_cung = (tong_goc // 60) % 6
        dinh = ["A", "B", "C", "D", "E", "F"]
        vi_tri_dung = dinh[(1 + so_cung) % 6]

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.7);
\\coordinate (B) at (30:1.7);
\\coordinate (C) at (-30:1.7);
\\coordinate (D) at (-90:1.7);
\\coordinate (E) at (-150:1.7);
\\coordinate (F) at (150:1.7);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--(E)--(F)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (E) circle (1pt) node[left] {$E$};
\\fill (F) circle (1pt) node[left] {$F$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Trên một dây chuyền đóng gói tự động có một mâm xoay hình tròn tâm $O$, trên mép mâm gắn $6$ khay chứa sản phẩm đặt tại các đỉnh $A, B, C, D, E, F$ của một lục giác đều nội tiếp $(O)$ theo thứ tự thuận chiều kim đồng hồ (như hình vẽ). Robot gắp sản phẩm được đặt cố định tại vị trí tương ứng với đỉnh $A$. \\\\
a) Liệt kê tất cả các góc quay thuận chiều $\\alpha^\\circ$ ($0^\\circ < \\alpha^\\circ \\le 360^\\circ$) của mâm xoay quanh tâm $O$ để sau khi quay, tại vị trí robot luôn có đúng một khay sản phẩm dừng lại. \\\\
b) Nếu mâm xoay thực hiện liên tiếp $%s$ bước quay thuận chiều kim đồng hồ, mỗi bước quay một góc $%s^\\circ$, thì khay ban đầu ở vị trí $B$ sẽ dừng lại ở vị trí của khay nào? Giải thích. %s'''
                         % (so_buoc, goc_moi_buoc, hinh_tikz))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $6$ khay sản phẩm tạo thành các đỉnh của lục giác đều $ABCDEF$ nội tiếp đường tròn $(O)$ nên mỗi cung nhỏ giữa hai khay liên tiếp có số đo bằng $\\frac{360^\\circ}{6} = 60^\\circ$. \\\\
Để tại vị trí robot luôn có một khay sản phẩm dừng lại thì phép quay thuận chiều tâm $O$ phải giữ nguyên lục giác đều $ABCDEF$. Do đó các góc quay thuận chiều $\\alpha^\\circ$ ($0^\\circ < \\alpha^\\circ \\le 360^\\circ$) thỏa mãn gồm $6$ góc:
$$60^\\circ; \\; 120^\\circ; \\; 180^\\circ; \\; 240^\\circ; \\; 300^\\circ; \\; 360^\\circ.$$
\\item Sau $%s$ bước quay thuận chiều kim đồng hồ, mỗi bước $%s^\\circ$, tổng góc quay mà mâm xoay đã thực hiện theo chiều kim đồng hồ là:
$$%s \\cdot %s^\\circ = %s^\\circ.$$
Vì mỗi cung nhỏ giữa hai đỉnh liên tiếp của lục giác đều bằng $60^\\circ$ nên góc quay $%s^\\circ$ tương ứng với việc di chuyển thuận chiều kim đồng hồ qua $\\frac{%s^\\circ}{60^\\circ} = %s$ khoảng khay. \\\\
Bắt đầu từ vị trí $B$, đi thuận chiều kim đồng hồ theo thứ tự $A, B, C, D, E, F$ qua $%s$ khoảng khay, khay ban đầu ở vị trí $B$ sẽ dừng lại ở vị trí của khay $%s$.
\\end{enumEX}'''
                   % (so_buoc, goc_moi_buoc, so_buoc, goc_moi_buoc, tong_goc, tong_goc, tong_goc, tong_goc // 60, tong_goc // 60, vi_tri_dung))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
