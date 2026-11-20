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


def bt_dang13_p4_b2_c10_hh9(self):
    # Cho thể tích V = 36*pi (R = 3) hoặc V = 288*pi (R = 6)
    R = random.choice([3, 6])
    V_heso = (4 * R**3) // 3
    S_cau = 4 * R**2
    # Hình trụ có chiều cao h = 2R và cùng thể tích V => pi * r^2 * (2r) = 4/3 * pi * R^3 => r = R * cbrt(2/3)
    # Hoặc cho hình trụ có bán kính đáy r_tru = R => h_tru = 4/3 * R => S_tp_tru = 2*pi*R*(4/3*R) + 2*pi*R^2 = 14/3 * pi * R^2 > 4*pi*R^2!
    h_tru = Rational(4, 3) * R
    S_tru = Rational(14, 3) * R**2

    noidungcauhoi = ('''Xét một hình cầu có bán kính $R = %s\\text{ cm}$ và một hình trụ có bán kính đáy bằng bán kính của hình cầu ($r = R = %s\\text{ cm}$) sao cho hai hình có thể tích bằng nhau.\\\na) Tính thể tích chung của hai hình đó.\\\nb) Tính chiều cao của hình trụ.\\\nc) So sánh diện tích mặt cầu và diện tích toàn phần của hình trụ đó.'''
                     % (R, R))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thể tích chung của hai hình là thể tích của hình cầu bán kính $R = %s\\text{ cm}$:
$$V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\item Gọi $h$ là chiều cao của hình trụ. Vì $V_{\\text{trụ}} = V$ nên:
$$\\pi R^2 h = %s\\pi \\Rightarrow %s^2 \\cdot h = %s \\Rightarrow h = %s\\text{ (cm)}.$$
\\item Diện tích mặt cầu là: $S_{\\text{cầu}} = 4\\pi R^2 = 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}$.\\\nDiện tích toàn phần của hình trụ là:
$$S_{\\text{tp trụ}} = 2\\pi R h + 2\\pi R^2 = 2\\pi \\cdot %s \\cdot %s + 2\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}.$$
Vì $%s\\pi < %s\\pi$ nên diện tích mặt cầu nhỏ hơn diện tích toàn phần của hình trụ (hiệu diện tích là $%s\\pi\\text{ cm}^2$).
\\end{enumEX}'''
               % (R, R, V_heso, V_heso, R, V_heso, latex(h_tru), R, S_cau, R, latex(h_tru), R, latex(S_tru), S_cau, latex(S_tru), latex(S_tru - S_cau)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
