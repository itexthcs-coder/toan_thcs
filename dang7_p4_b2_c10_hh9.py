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


def bt_dang7_p4_b2_c10_hh9(self):
    # V_tru + V_non = V_cau => pi*r1^2*h1 + 1/3*pi*r2^2*h2 = 4/3*pi*R^3
    # Chọn R = 6 => 4/3 * R^3 = 288. V_tru = 180 (r1 = 6, h1 = 5), V_non = 108 (r2 = 6, h2 = 9) -> 180 + 108 = 288!
    # Hoặc nhân tỉ lệ k = 1, 2: R = 6k, r1 = 6k, h1 = 5k, r2 = 6k, h2 = 9k!
    k = random.choice([1, 2])
    R = 6 * k
    r1, h1 = 6 * k, 5 * k
    r2, h2 = 6 * k, 9 * k
    V_tru = r1**2 * h1
    V_non = (r2**2 * h2) // 3
    V_cau = V_tru + V_non
    S_cau = 4 * R**2

    noidungcauhoi = ('''Người ta đun nóng chảy hoàn toàn hai khối kim loại đồng chất: một khối hình trụ đặc có bán kính đáy $r_1 = %s\\text{ cm}$, chiều cao $h_1 = %s\\text{ cm}$ và một khối hình nón đặc có bán kính đáy $r_2 = %s\\text{ cm}$, chiều cao $h_2 = %s\\text{ cm}$ để đúc thành một khối cầu đặc duy nhất (coi hao hụt không đáng kể).\\\na) Tính tổng thể tích của hai khối kim loại ban đầu.\\\nb) Tính bán kính của khối cầu tạo thành.\\\nc) Tính diện tích bề mặt của khối cầu tạo thành.'''
                     % (r1, h1, r2, h2))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thể tích khối hình trụ là: $V_1 = \\pi r_1^2 h_1 = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nThể tích khối hình nón là: $V_2 = \\dfrac{1}{3}\\pi r_2^2 h_2 = \\dfrac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nTổng thể tích hai khối kim loại ban đầu là: $V = V_1 + V_2 = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.
\\item Gọi $R$ ($\\text{cm}$) là bán kính của khối cầu tạo thành ($R > 0$). Do thể tích bảo toàn nên:
$$\\dfrac{4}{3}\\pi R^3 = %s\\pi \\Rightarrow R^3 = \\dfrac{3 \\cdot %s}{4} = %s \\Rightarrow R = %s\\text{ (cm)}.$$
\\item Diện tích bề mặt của khối cầu tạo thành là:
$$S = 4\\pi R^2 = 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
               % (r1, h1, V_tru, r2, h2, V_non, V_tru, V_non, V_cau, V_cau, V_cau, R**3, R, R, S_cau))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
