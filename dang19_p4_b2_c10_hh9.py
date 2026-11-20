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


def bt_dang19_p4_b2_c10_hh9(self):
    d_dc = random.choice([20, 30, 40]) # cm
    R_dc = d_dc // 2
    C_xd_dc = Decimal(str(math.pi * d_dc)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    C_xd_str = str(C_xd_dc).replace('.', ',')
    S_dc = Decimal(str(4 * math.pi * (R_dc**2))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    S_dc_str = str(S_dc).replace('.', ',')
    # Vĩ tuyến 60 độ Bắc có bán kính r_60 = R * cos(60) = R / 2 => chu vi = pi * R
    C_60 = Decimal(str(math.pi * R_dc)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    C_60_str = str(C_60).replace('.', ',')

    noidungcauhoi = ('''Một quả địa cầu dùng trong dạy học Địa lí có dạng hình cầu với đường kính bằng $%s\\text{ cm}$.\\\na) Tính diện tích bề mặt của quả địa cầu đó (làm tròn kết quả đến hàng phần trăm của $\\text{cm}^2$).\\\nb) Tính độ dài của đường Xích đạo được vẽ trên quả địa cầu đó (làm tròn đến hàng phần trăm của $\\text{cm}$).\\\nc) Đường vĩ tuyến $60^\\circ$ Bắc trên quả địa cầu là một đường tròn nằm trong mặt phẳng song song với mặt phẳng Xích đạo và có bán kính bằng một nửa bán kính của quả địa cầu. Tính độ dài đường vĩ tuyến $60^\\circ$ Bắc trên quả địa cầu đó (làm tròn đến hàng phần trăm của $\\text{cm}$).'''
                     % (d_dc))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Bán kính của quả địa cầu là: $R = \\dfrac{%s}{2} = %s\\text{ (cm)}$.\\\nDiện tích bề mặt của quả địa cầu là:
$$S = 4\\pi R^2 = 4\\pi \\cdot %s^2 = %s\\pi \\approx %s\\text{ (cm}^2\\text{)}.$$
\\item Đường Xích đạo là một đường tròn lớn của quả địa cầu nên có bán kính bằng $R = %s\\text{ cm}$.\\\nĐộ dài đường Xích đạo trên quả địa cầu là:
$$C_{\\text{XĐ}} = 2\\pi R = 2\\pi \\cdot %s = %s\\pi \\approx %s\\text{ (cm)}.$$
\\item Bán kính của đường vĩ tuyến $60^\\circ$ Bắc trên quả địa cầu là: $r = \\dfrac{R}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$.\\\nĐộ dài của đường vĩ tuyến $60^\\circ$ Bắc trên quả địa cầu là:
$$C_{60^\\circ} = 2\\pi r = 2\\pi \\cdot %s = %s\\pi \\approx %s\\text{ (cm)}.$$
\\end{enumEX}'''
               % (d_dc, R_dc, R_dc, 4 * R_dc**2, S_dc_str, R_dc, R_dc, 2 * R_dc, C_xd_str, R_dc, R_dc / 2 if R_dc % 2 != 0 else R_dc // 2, R_dc / 2 if R_dc % 2 != 0 else R_dc // 2, R_dc, C_60_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
