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


def bt_dang16_p3_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh_lon = random.choice([10, 12, 14, 15])
        k_ti_le = random.choice([3, 4])
        # S_nho = k_ti_le * S_thang => S_lon = S_nho + 6 * (S_nho / k_ti_le) = S_nho * (1 + 6/k_ti_le)
        # k_ti_le = 3 => S_lon = 3 * S_nho => x = canh_lon / sqrt(3)
        # k_ti_le = 4 => S_lon = 2.5 * S_nho => x = canh_lon / sqrt(2.5)
        if k_ti_le == 3:
            val = canh_lon / math.sqrt(3)
            mau_so = 3
        else:
            val = canh_lon / math.sqrt(2.5)
            mau_so = 2.5
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\foreach \\i in {0,60,...,300} {
    \\coordinate (A\\i) at (\\i:1.9);
    \\coordinate (B\\i) at (\\i:1.1);
    \\draw[line width=1pt] (A\\i)--(B\\i);
}
\\draw[line width=1pt] (A0)--(A60)--(A120)--(A180)--(A240)--(A300)--cycle;
\\draw[line width=1pt] (B0)--(B60)--(B120)--(B180)--(B240)--(B300)--cycle;
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Một xưởng mộc chế tác một khay đựng bánh kẹo bằng gỗ có dạng hình lục giác đều cạnh $%s\\text{ cm}$. Bên trong khay được ngăn thành $7$ ô gồm một ô hình lục giác đều nhỏ ở chính giữa cạnh $x\\text{ cm}$ và $6$ ô hình thang cân bằng nhau xung quanh (như hình vẽ). Để diện tích ô lục giác đều nhỏ ở chính giữa bằng $%s$ lần diện tích của mỗi ô hình thang cân thì độ dài cạnh $x$ bằng bao nhiêu centimét? (làm tròn kết quả đến hàng phần trăm). %s'''
                         % (canh_lon, k_ti_le, hinh_tikz))

        if k_ti_le == 3:
            loigiai = ('''Gọi $S_1$ là diện tích mỗi ô hình thang cân và $S_2$ là diện tích ô lục giác đều nhỏ ở chính giữa. \\
Theo đề bài $S_2 = 3 S_1 \\Rightarrow S_1 = \\frac{1}{3} S_2$. \\
Diện tích toàn bộ khay lục giác đều lớn là $S = S_2 + 6 S_1 = S_2 + 6 \\cdot \\frac{1}{3} S_2 = 3 S_2$. \\
Mặt khác tỉ số diện tích của hai lục giác đều bằng bình phương tỉ số hai cạnh tương ứng nên:
$$\\left(\\frac{x}{%s}\\right)^2 = \\frac{S_2}{S} = \\frac{1}{3} \\Rightarrow x = \\frac{%s}{\\sqrt{3}} \\approx %s\\text{ (cm)}.$$'''
                       % (canh_lon, canh_lon, kq_str))
        else:
            loigiai = ('''Gọi $S_1$ là diện tích mỗi ô hình thang cân và $S_2$ là diện tích ô lục giác đều nhỏ ở chính giữa. \\
Theo đề bài $S_2 = 4 S_1 \\Rightarrow S_1 = \\frac{1}{4} S_2$. \\
Diện tích toàn bộ khay lục giác đều lớn là $S = S_2 + 6 S_1 = S_2 + 6 \\cdot \\frac{1}{4} S_2 = 2,5 S_2$. \\
Mặt khác tỉ số diện tích của hai lục giác đều bằng bình phương tỉ số hai cạnh tương ứng nên:
$$\\left(\\frac{x}{%s}\\right)^2 = \\frac{S_2}{S} = \\frac{1}{2,5} \\Rightarrow x = \\frac{%s}{\\sqrt{2,5}} \\approx %s\\text{ (cm)}.$$'''
                       % (canh_lon, canh_lon, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
