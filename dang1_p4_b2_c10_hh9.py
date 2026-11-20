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


def bt_dang1_p4_b2_c10_hh9(self):
    # Bộ số Pythagore không gian: (1, 2, 2 -> 3), (2, 3, 6 -> 7), (3, 4, 12 -> 13), (4, 4, 7 -> 9)
    bo_so = random.choice([
        (2, 4, 4, 6),
        (4, 6, 12, 14),
        (6, 8, 24, 26),
        (8, 8, 14, 18)
    ])
    a, b, c, d = bo_so
    R = d // 2
    S_cau = 4 * R**2
    V_cau = Rational(4, 3) * R**3
    V_hh = a * b * c

    noidungcauhoi = ('''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có kích thước ba cạnh lần lượt là $AB = %s\\text{ cm}$, $AD = %s\\text{ cm}$ và $AA' = %s\\text{ cm}$.\\\na) Tính đường kính và bán kính của mặt cầu đi qua tất cả $8$ đỉnh của hình hộp chữ nhật đó.\\\nb) Tính diện tích mặt cầu và thể tích của khối cầu giới hạn bởi mặt cầu trên.\\\nc) Tính tỉ số giữa thể tích hình hộp chữ nhật và thể tích khối cầu đó (làm tròn kết quả đến hàng phần trăm).'''
                     % (a, b, c))

    pct_val = Decimal(str(V_hh / float(V_cau * math.pi))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    pct_str = str(pct_val).replace('.', ',')

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tâm của mặt cầu đi qua $8$ đỉnh của hình hộp chữ nhật là trung điểm $O$ của đường chéo $AC'$.\\\nĐộ dài đường chéo $AC'$ (đường kính của mặt cầu) là:
$$d = AC' = \\sqrt{AB^2 + AD^2 + AA'^2} = \\sqrt{%s^2 + %s^2 + %s^2} = %s\\text{ (cm)}.$$
Bán kính của mặt cầu là: $R = \\dfrac{d}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$.
\\item Diện tích mặt cầu là:
$$S = 4\\pi R^2 = 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}.$$
Thể tích của khối cầu là:
$$V_{\\text{cầu}} = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\item Thể tích của hình hộp chữ nhật là: $V_{\\text{hh}} = %s \\cdot %s \\cdot %s = %s\\text{ (cm}^3\\text{)}$.\\\nTỉ số thể tích giữa hình hộp chữ nhật và khối cầu là:
$$\\dfrac{V_{\\text{hh}}}{V_{\\text{cầu}}} = \\dfrac{%s}{%s\\pi} \\approx %s.$$
\\end{enumEX}'''
               % (a, b, c, d, d, R, R, S_cau, R, latex(V_cau), a, b, c, V_hh, V_hh, latex(V_cau), pct_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
