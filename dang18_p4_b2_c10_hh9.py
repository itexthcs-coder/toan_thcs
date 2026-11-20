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


def bt_dang18_p4_b2_c10_hh9(self):
    R_be = 10 # đường kính 20cm
    h_be = 25
    h_nuoc = 18
    r_bi = 3
    # Thả 5 viên bi bán kính 3cm => V_5bi = 5 * 4/3 * pi * 27 = 180*pi => delta_h = 180*pi / (pi * 100) = 1,8 cm
    so_bi = random.choice([5, 10])
    V_bi_heso = (so_bi * 4 * (r_bi**3)) // 3
    delta_h = V_bi_heso / (R_be**2)
    delta_h_str = str(delta_h).replace('.', ',')
    h_sau = h_nuoc + delta_h
    h_sau_str = str(h_sau).replace('.', ',')
    # Số bi tối đa không tràn: V_trong = pi * 100 * (25 - 18) = 700*pi; V_1bi = 36*pi => 700 / 36 = 19,44 => tối đa 19 viên!
    so_bi_max = (R_be**2 * (h_be - h_nuoc)) // ((4 * r_bi**3) // 3)

    noidungcauhoi = ('''Một bể nuôi cá cảnh dạng hình trụ có đường kính đáy bên trong bằng $20\\text{ cm}$ và chiều cao $25\\text{ cm}$, hiện đang chứa nước ở độ cao $18\\text{ cm}$. Người ta thả chìm hoàn toàn $%s$ viên sỏi trang trí dạng hình cầu giống hệt nhau có bán kính $r = 3\\text{ cm}$ vào bể.\\\na) Tính tổng thể tích của $%s$ viên sỏi trang trí đó (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần trăm của $\\text{cm}^3$).\\\nb) Hỏi mực nước trong bể dâng lên cao bao nhiêu $\\text{cm}$ so với đáy bể?\\\nc) Hỏi có thể thả thêm nhiều nhất bao nhiêu viên sỏi như vậy nữa để nước trong bể không bị tràn ra ngoài?'''
                     % (so_bi, so_bi))

    V_bi_314 = Decimal(str(V_bi_heso * 3.14)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    V_bi_314_str = str(V_bi_314).replace('.', ',')

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thể tích của một viên sỏi hình cầu bán kính $r = 3\\text{ cm}$ là: $V_1 = \\dfrac{4}{3}\\pi \\cdot 3^3 = 36\\pi\\text{ (cm}^3\\text{)}$.\\\nTổng thể tích của $%s$ viên sỏi là:
$$V_{%s} = %s \\cdot 36\\pi = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (cm}^3\\text{)}.$$
\\item Bán kính đáy bên trong của bể cá là $R = \\dfrac{20}{2} = 10\\text{ (cm)}$.\\\nĐộ cao mực nước dâng thêm khi thả $%s$ viên sỏi là:
$$\\Delta h = \\dfrac{V_{%s}}{\\pi R^2} = \\dfrac{%s\\pi}{\\pi \\cdot 10^2} = %s\\text{ (cm)}.$$
Mực nước trong bể lúc này cao so với đáy bể là: $h = 18 + %s = %s\\text{ (cm)}$.
\\item Thể tích phần không gian trống ban đầu trong bể là:
$$V_{\\text{trống}} = \\pi R^2 (25 - 18) = \\pi \\cdot 10^2 \\cdot 7 = 700\\pi\\text{ (cm}^3\\text{)}.$$
Tổng số viên sỏi tối đa bể chứa được mà nước không tràn là phần nguyên của $\\dfrac{700\\pi}{36\\pi} \\approx 19,44$, tức là $19$ viên sỏi.\\\nVậy có thể thả thêm nhiều nhất $19 - %s = %s$ viên sỏi nữa.
\\end{enumEX}'''
               % (so_bi, so_bi, so_bi, V_bi_heso, V_bi_heso, V_bi_314_str, so_bi, so_bi, V_bi_heso, delta_h_str, delta_h_str, h_sau_str, so_bi, 19 - so_bi))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
