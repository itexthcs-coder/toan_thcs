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


def bt_dang20_p4_b3_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y = symbols('x y')
        a = randint(4, 6)
        b = randint(2, 4)
        c1 = randint(35, 45)
        c2 = randint(30, 40)
        tong_hang = c1 + c2
        
        P1 = a*x**2*y - b*x*y**2 + c1
        P2 = b*x*y**2 - a*x**2*y + c2
        
        pts = [(1, 1), (-1, 2), (2, 1), (-2, 1)]
        p1_vals = [int(P1.subs({x: px, y: py})) for px, py in pts]
        p2_dung = [int(P2.subs({x: px, y: py})) for px, py in pts]
        
        p2_hien_thi = list(p2_dung)
        p2_hien_thi[2] += 10
        
        noidungcauhoi = ('''Trong hệ thống giám sát năng lượng của một tòa nhà thông minh, hai đồng hồ đo công suất nhánh $P_1$ và $P_2$ (đơn vị: $\\text{kW}$) được lập trình theo hai đa thức:
                         $$P_1 = %s \\quad \\text{và} \\quad P_2 = %s.$$
                         Bảng thống kê dưới đây ghi lại số liệu đo được tại $4$ khung giờ cao điểm trong ngày:
                         \\begin{center}
                         \\begin{tabular}{|c|c|c|c|c|}
                         \\hline
                         Khung giờ & $8\\text{h}00$ & $11\\text{h}00$ & $15\\text{h}00$ & $19\\text{h}00$ \\\\
                         \\hline
                         $P_1$ ($\\text{kW}$) & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                         \\hline
                         $P_2$ ($\\text{kW}$) & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                         \\hline
                         \\end{tabular}
                         \\end{center}
                         Kỹ thuật viên phát hiện có một khung giờ bị sai số liệu do lỗi truyền tín hiệu từ đồng hồ $P_2$. Bằng phương pháp đại số (không tính lại giá trị $x, y$), hãy chỉ ra khung giờ bị lỗi đó và tính lại giá trị đúng của $P_2$.'''
                         % (latex(P1), latex(P2),
                            p1_vals[0], p1_vals[1], p1_vals[2], p1_vals[3],
                            p2_hien_thi[0], p2_hien_thi[1], p2_hien_thi[2], p2_hien_thi[3]))
        
        loigiai = ('''Ta xét tổng của hai đa thức $P_1$ và $P_2$:
                    \\begin{align*}
                    P_1 + P_2 &= (%s) + (%s) \\\\
                    &= (%s - %s) + (-%s + %s) + (%s + %s) \\\\
                    &= %s.
                    \\end{align*}
                    Như vậy, với mọi giá trị của $x$ và $y$, tổng công suất $P_1 + P_2$ luôn bằng $%s\\text{ kW}$. \\\\
                    Kiểm tra tổng $P_1 + P_2$ tại từng khung giờ trong bảng thống kê:
                    - Lúc $8\\text{h}00$: $%s + %s = %s$ (đúng).
                    - Lúc $11\\text{h}00$: $%s + %s = %s$ (đúng).
                    - Lúc $15\\text{h}00$: $%s + %s = %s \\neq %s$ (sai).
                    - Lúc $19\\text{h}00$: $%s + %s = %s$ (đúng). \\\\
                    Vậy khung giờ bị lỗi số liệu là $15\\text{h}00$ và giá trị đúng của $P_2$ tại khung giờ đó là:
                    $$P_2 = %s - %s = %s\\text{ kW}.$$'''
                   % (latex(P1), latex(P2),
                      latex(a*x**2*y), latex(a*x**2*y), latex(b*x*y**2), latex(b*x*y**2), c1, c2, tong_hang,
                      tong_hang,
                      p1_vals[0], p2_hien_thi[0], tong_hang,
                      p1_vals[1], p2_hien_thi[1], tong_hang,
                      p1_vals[2], p2_hien_thi[2], p1_vals[2] + p2_hien_thi[2], tong_hang,
                      p1_vals[3], p2_hien_thi[3], tong_hang,
                      tong_hang, p1_vals[2], p2_dung[2]))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
