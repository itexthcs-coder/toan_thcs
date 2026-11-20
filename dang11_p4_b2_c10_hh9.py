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


def bt_dang11_p4_b2_c10_hh9(self):
    R = 3
    h_tru = randint(8, 12)
    h_non = 4
    l_non = 5
    V_tru = R**2 * h_tru
    V_non = Rational(1, 3) * R**2 * h_non
    V_nuacau = Rational(2, 3) * R**3
    V_conlai = V_tru - V_non - V_nuacau
    S_tp = 2 * R * h_tru + R * l_non + 2 * R**2

    noidungcauhoi = ('''Từ một khối gỗ đặc hình trụ có bán kính đáy $R = %s\\text{ cm}$ và chiều cao $h = %s\\text{ cm}$, người ta khoét ở mặt đáy trên một hình nón có bán kính đáy $R = %s\\text{ cm}$, chiều cao $h_1 = %s\\text{ cm}$ và khoét ở mặt đáy dưới một nửa hình cầu có bán kính $R = %s\\text{ cm}$.\\\na) Tính tổng thể tích phần gỗ bị khoét đi.\\\nb) Tính thể tích phần gỗ còn lại.\\\nc) Tính diện tích toàn bộ bề mặt của khối gỗ sau khi khoét.'''
                     % (R, h_tru, R, h_non, R))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thể tích phần hình nón bị khoét đi là: $V_{\\text{nón}} = \\dfrac{1}{3}\\pi R^2 h_1 = \\dfrac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nThể tích phần nửa hình cầu bị khoét đi là: $V_{\\text{nửa cầu}} = \\dfrac{2}{3}\\pi R^3 = \\dfrac{2}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nTổng thể tích phần gỗ bị khoét đi là: $V_{\\text{khoét}} = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.
\\item Thể tích khối gỗ hình trụ ban đầu là: $V_{\\text{trụ}} = \\pi R^2 h = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nThể tích phần gỗ còn lại là: $V = V_{\\text{trụ}} - V_{\\text{khoét}} = %s\\pi - %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.
\\item Độ dài đường sinh phần nón bị khoét là: $l = \\sqrt{R^2 + h_1^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$.\\\nDiện tích toàn bộ bề mặt khối gỗ sau khi khoét gồm mặt xung quanh hình trụ, mặt xung quanh hình nón và mặt lõm nửa mặt cầu:
$$S = 2\\pi R h + \\pi R l + 2\\pi R^2 = 2\\pi \\cdot %s \\cdot %s + \\pi \\cdot %s \\cdot %s + 2\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
               % (R, h_non, latex(V_non), R, latex(V_nuacau), latex(V_non), latex(V_nuacau), latex(V_non + V_nuacau), R, h_tru, V_tru, V_tru, latex(V_non + V_nuacau), latex(V_conlai), R, h_non, l_non, R, h_tru, R, l_non, R, S_tp))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
