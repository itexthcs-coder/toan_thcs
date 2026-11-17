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


def bt_dang12_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R1 = random.choice([10, 12, 14, 15])
        R2 = random.choice([6, 7, 8, 9])
        n1 = random.choice([60, 75, 80, 90])
        n2 = random.choice([20, 30, 40])
        n_tong = n1 + n2
        val = (n1 / 360) * 3.14 * (R1 ** 2) + (n2 / 360) * 3.14 * (R2 ** 2)
        number = Decimal(str(val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một vòi phun nước tự động đặt ở góc của một khu vườn hình chữ nhật có thể phun nước xa tối đa $%d\\text{ m}$ và xoay đều qua lại một góc $%d^\\circ$. Để tránh nước phun ướt lối đi lát gạch, người làm vườn lắp thêm tấm chắn làm giảm bán kính phun ở phần góc $%d^\\circ$ cuối xuống chỉ còn $%d\\text{ m}$ (phần góc $%d^\\circ$ còn lại vẫn phun xa $%d\\text{ m}$). Tính tổng diện tích mặt cỏ được tưới nước theo đơn vị $\\text{m}^2$ (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng đơn vị).
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\fill[green!22] (0,0) -- (2.5,0) arc (0:75:2.5) -- cycle;
\\fill[green!12] (0,0) -- (75:1.65) arc (75:110:1.65) -- cycle;
\\draw (0,0) -- (2.5,0) arc (0:75:2.5) -- cycle;
\\draw (0,0) -- (75:1.65) arc (75:110:1.65) -- cycle;
\\fill (0,0) circle (2pt) node[below left] {$O$};
\\node at (37:1.4) {$%d^\\circ$};
\\node at (92:1.0) {$%d^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (R1, n_tong, n2, R2, n1, R1, n1, n2))

        # Nội dung lời giải
        loigiai = ('''Vùng mặt cỏ được tưới nước gồm hai hình quạt tròn có chung đỉnh tại vị trí đặt vòi phun: \\\\
- Hình quạt thứ nhất có bán kính $R_1 = %d\\text{ m}$, góc ở tâm $n_1 = %d^\\circ$, diện tích là:
$$S_1 = \\dfrac{%d}{360}\\pi \\cdot %d^2.$$
- Hình quạt thứ hai có bán kính $R_2 = %d\\text{ m}$, góc ở tâm $n_2 = %d^\\circ$, diện tích là:
$$S_2 = \\dfrac{%d}{360}\\pi \\cdot %d^2.$$
Tổng diện tích mặt cỏ được tưới nước là:
$$S = S_1 + S_2 \\approx \\dfrac{%d}{360} \\cdot 3,14 \\cdot %d + \\dfrac{%d}{360} \\cdot 3,14 \\cdot %d \\approx %s\\text{ (m}^2\\text{)}.$$''' % (
            R1, n1, n1, R1, R2, n2, n2, R2, n1, R1 ** 2, n2, R2 ** 2, kq_str))

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
