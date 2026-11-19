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


def bt_dang19_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d_tru = random.choice([16, 20, 24, 30])
        r_tru = d_tru // 2
        h_oc = random.choice([12, 15, 18, 20])
        s_tron = 3.14 * (r_tru ** 2)
        s_lg = 1.5 * (r_tru ** 2) * 1.73
        v_bo_di = (s_tron - s_lg) * h_oc
        number = Decimal(str(v_bo_di))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\foreach \\i in {0,60,...,300} {
    \\coordinate (A\\i) at (\\i:1.7);
}
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (A0)--(A60)--(A120)--(A180)--(A240)--(A300)--cycle;
\\draw[line width=1pt, dashed] (A180)--(A0);
\\fill (O) circle (1pt) node[below] {$O$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Trong một xưởng cơ khí, người ta tiện một thanh thép hình trụ tròn đặc có đường kính đáy $%s\\text{ mm}$ và chiều cao phần đầu ốc $%s\\text{ mm}$ để tạo thành đầu một chiếc đinh ốc có dạng hình lăng trụ đứng đáy là lục giác đều lớn nhất có thể (tiết diện đáy minh họa như hình vẽ). Tính thể tích phần thép bị tiện bỏ đi (lấy $\\pi \\approx 3,14$ và $\\sqrt{3} \\approx 1,73$, làm tròn kết quả đến hàng đơn vị theo $\\text{mm}^3$). %s'''
                         % (d_tru, h_oc, hinh_tikz))

        loigiai = ('''Bán kính đáy của thanh thép hình trụ là $R = \\frac{%s}{2} = %s\\text{ (mm)}$. \\\\
Diện tích đáy của thanh thép hình trụ tròn là:
$$S_{\\text{tròn}} = \\pi R^2 \\approx 3,14 \\cdot %s^2 = %s\\text{ (mm}^2\\text{)}.$$
Để đầu đinh ốc có tiết diện lục giác đều lớn nhất thì lục giác đều đáy phải nội tiếp đường tròn đáy của hình trụ, do đó độ dài mỗi cạnh của lục giác đều bằng bán kính $R = %s\\text{ mm}$. \\\\
Diện tích đáy hình lục giác đều của đầu đinh ốc là:
$$S_{\\text{lục giác}} = 6 \\cdot \\frac{%s^2\\sqrt{3}}{4} = %s\\sqrt{3} \\approx %s \\cdot 1,73 = %s\\text{ (mm}^2\\text{)}.$$
Diện tích phần đáy bị tiện bỏ đi là:
$$S_{\\text{bỏ đi}} = S_{\\text{tròn}} - S_{\\text{lục giác}} \\approx %s - %s = %s\\text{ (mm}^2\\text{)}.$$
Vậy thể tích phần thép bị tiện bỏ đi là:
$$V_{\\text{bỏ đi}} = S_{\\text{bỏ đi}} \\cdot h \\approx %s \\cdot %s = %s \\approx %s\\text{ (mm}^3\\text{)}.$$'''
                   % (d_tru, r_tru, r_tru, str(round(s_tron, 2)).replace('.', ','), r_tru,
                      r_tru, 3 * (r_tru ** 2) // 2, 3 * (r_tru ** 2) // 2, str(round(s_lg, 2)).replace('.', ','),
                      str(round(s_tron, 2)).replace('.', ','), str(round(s_lg, 2)).replace('.', ','), str(round(s_tron - s_lg, 2)).replace('.', ','),
                      str(round(s_tron - s_lg, 2)).replace('.', ','), h_oc, str(round(v_bo_di, 2)).replace('.', ','), kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
