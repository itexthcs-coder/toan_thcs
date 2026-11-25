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

def bt_dang20_p3_b3_c5_ds8(self):
    # Dạng 20: Bài toán tìm số lượng thành phần từ biểu đồ hình quạt tròn khi biết tổng và hiệu hai thành phần
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong_sp = random.choice([400, 500, 600, 800])
        p_quan, p_pk, diff_ao_vay = random.choice([
            (28, 12, 16),
            (26, 14, 12),
            (30, 10, 20),
            (25, 15, 14)
        ])
        tong_av = 100 - (p_quan + p_pk)
        p_ao = int((tong_av + diff_ao_vay) // 2)
        p_vay = tong_av - p_ao
        so_ao = int(tong_sp * p_ao // 100)
        kq_str = str(so_ao)
        
        a1 = round(p_ao * 3.6, 1)
        a2 = round((p_ao + p_quan) * 3.6, 1)
        a3 = round((p_ao + p_quan + p_vay) * 3.6, 1)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.9) arc (0:%s:1.9) -- cycle;\n' % a1 +
            '\\draw[line width=1pt, fill=black!25] (0,0) -- (%s:1.9) arc (%s:%s:1.9) -- cycle;\n' % (a1, a1, a2) +
            '\\draw[line width=1pt, fill=black!40] (0,0) -- (%s:1.9) arc (%s:%s:1.9) -- cycle;\n' % (a2, a2, a3) +
            '\\draw[line width=1pt, fill=white] (0,0) -- (%s:1.9) arc (%s:360:1.9) -- cycle;\n' % (a3, a3) +
            '\\node at (%s:1.2) {$x\\%%$};\n' % round(a1/2, 1) +
            '\\node at (%s:1.25) {$%s\\%%$};\n' % (round((a1+a2)/2, 1), p_quan) +
            '\\node at (%s:1.25) {$y\\%%$};\n' % round((a2+a3)/2, 1) +
            '\\node at (%s:1.4) {$%s\\%%$};\n' % (round((a3+360)/2, 1), p_pk) +
            '\\draw[line width=1pt, fill=black!10] (2.6,1.2) rectangle (3.0,1.5) node[right, yshift=-4pt] {Áo sơ mi};\n' +
            '\\draw[line width=1pt, fill=black!25] (2.6,0.4) rectangle (3.0,0.7) node[right, yshift=-4pt] {Quần âu};\n' +
            '\\draw[line width=1pt, fill=black!40] (2.6,-0.4) rectangle (3.0,-0.1) node[right, yshift=-4pt] {Váy đầm};\n' +
            '\\draw[line width=1pt, fill=white] (2.6,-1.2) rectangle (3.0,-0.9) node[right, yshift=-4pt] {Phụ kiện};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một cửa hàng thời trang bán được tổng cộng $%s$ sản phẩm trong tuần lễ khai trương gồm bốn mặt hàng. Biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu số lượng sản phẩm bán ra (biết Áo sơ mi chiếm tỉ lệ nhiều hơn Váy đầm là $%s\\%%$):\n' % (tong_sp, diff_ao_vay) +
                         tikz_code + '\n' +
                         'Tính số chiếc Áo sơ mi cửa hàng đã bán được trong tuần lễ đó.')
        
        loigiai = ('Tổng tỉ lệ phần trăm của hai mặt hàng Áo sơ mi và Váy đầm là:\\\\' +
                   '$$x\\%% + y\\%% = 100\\%% - (%s\\%% + %s\\%%) = %s\\%%.$$\\\\' +
                   'Vì Áo sơ mi chiếm tỉ lệ nhiều hơn Váy đầm là $%s\\%%$ nên tỉ lệ Áo sơ mi là:\\\\' +
                   '$$x\\%% = \\dfrac{%s\\%% + %s\\%%}{2} = %s\\%%.$$\\\\' +
                   'Số chiếc Áo sơ mi cửa hàng đã bán được là:\\\\' +
                   '$$%s \\cdot %s\\%% = %s \\text{ (chiếc)}.$$'
                   ) % (p_quan, p_pk, tong_av, diff_ao_vay, tong_av, diff_ao_vay, p_ao, tong_sp, p_ao, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
