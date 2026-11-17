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


def bt_dang18_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(2, 1, '0,5'), (4, 2, '1'), (6, 3, '1,5')]
        d, R, h_str = random.choice(bo_so)
        val = (R ** 2) * (3.14 / 3 - math.sqrt(3) / 4)
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một bồn chứa nhiên liệu hình trụ đặt nằm ngang có đường kính mặt cắt ngang là $%d\\text{ m}$. Khi đo mực nhiên liệu trong bồn, người ta thấy chiều cao cột nhiên liệu tính từ đáy bồn lên là $%s\\text{ m}$. Tính diện tích phần mặt cắt ngang của khối nhiên liệu trong bồn theo đơn vị $\\text{m}^2$ (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần trăm).
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\fill[yellow!35] (210:1.7) arc (210:330:1.7) -- cycle;
\\draw[thick] (0,0) circle (1.7);
\\draw (210:1.7) -- (330:1.7);
\\draw[dashed] (0,0) -- (210:1.7);
\\draw[dashed] (0,0) -- (330:1.7);
\\draw[dashed] (0,0) -- (0,-1.7);
\\fill (0,0) circle (1.5pt) node[above] {$O$};
\\node[left] at (210:1.7) {$A$};
\\node[right] at (330:1.7) {$B$};
\\node[below] at (0,-1.7) {$C$};
\\end{tikzpicture}
\\end{center}''' % (d, h_str))

        # Nội dung lời giải
        loigiai = ('''Bán kính mặt cắt ngang hình tròn của bồn là $R = \\dfrac{%d}{2} = %d\\text{ (m)}$. \\\\
Gọi $AB$ là dây cung biểu thị mặt thoáng nhiên liệu, $H$ là trung điểm $AB$ và $C$ là điểm thấp nhất của đáy bồn ($HC = %s\\text{ m}$). \\\\
Khoảng cách từ tâm $O$ đến mặt thoáng nhiên liệu là $OH = R - HC = %d - %s = %s\\text{ (m)}$. \\\\
Trong tam giác $OAH$ vuông tại $H$, ta có $\\cos\\widehat{AOH} = \\dfrac{OH}{OA} = \\dfrac{%s}{%d} = \\dfrac{1}{2} \\Rightarrow \\widehat{AOH} = 60^\\circ \\Rightarrow \\widehat{AOB} = 120^\\circ$. \\\\
Diện tích phần mặt cắt ngang của khối nhiên liệu (hình viên phân cung $120^\\circ$) là:
$$S = S_q - S_{\\triangle OAB} = \\dfrac{120}{360}\\pi R^2 - \\dfrac{1}{2}R^2\\sin 120^\\circ = %d^2\\left(\\dfrac{\\pi}{3} - \\dfrac{\\sqrt{3}}{4}\\right) \\approx %d \\cdot \\left(\\dfrac{3,14}{3} - \\dfrac{\\sqrt{3}}{4}\\right) \\approx %s\\text{ (m}^2\\text{)}.$$''' % (
            d, R, h_str, R, h_str, h_str, h_str, R, R, R ** 2, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
