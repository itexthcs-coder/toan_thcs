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


def bt_dang4_p4_b2_c10_hh9(self):
    # S2 - S1 = 4*pi*((R + a)^2 - R^2) = 4*pi*(2aR + a^2)
    a = random.choice([2, 3, 4])
    R = randint(4, 10)
    S_tang_heso = 4 * (2 * a * R + a**2)
    V_bandau = Rational(4, 3) * R**3
    V_sau = Rational(4, 3) * (R + a)**3

    noidungcauhoi = ('''Nếu tăng bán kính của một hình cầu thêm $%s\\text{ cm}$ thì diện tích mặt cầu của nó tăng thêm $%s\\pi\\text{ cm}^2$.\\\na) Tính bán kính ban đầu của hình cầu đó.\\\nb) Tính diện tích mặt cầu ban đầu và diện tích mặt cầu sau khi tăng bán kính.\\\nc) Thể tích của hình cầu tăng thêm bao nhiêu lần $\\pi\\text{ cm}^3$?'''
                     % (a, S_tang_heso))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $R$ ($\\text{cm}$) là bán kính ban đầu của hình cầu ($R > 0$).\\\nBán kính của hình cầu sau khi tăng thêm là $R + %s\\text{ (cm)}$.\\\nTheo đề bài, diện tích mặt cầu tăng thêm $%s\\pi\\text{ cm}^2$ nên ta có phương trình:
$$4\\pi (R + %s)^2 - 4\\pi R^2 = %s\\pi \\Leftrightarrow (R + %s)^2 - R^2 = %s \\Leftrightarrow %sR + %s = %s \\Leftrightarrow %sR = %s \\Leftrightarrow R = %s\\text{ (cm)}.$$
Vậy bán kính ban đầu của hình cầu là $%s\\text{ cm}$.
\\item Diện tích mặt cầu ban đầu là: $S_1 = 4\\pi R^2 = 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}$.\\\nDiện tích mặt cầu sau khi tăng bán kính là: $S_2 = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^2\\text{)}$.
\\item Thể tích ban đầu của hình cầu là: $V_1 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nThể tích hình cầu sau khi tăng bán kính là: $V_2 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nVậy thể tích hình cầu tăng thêm là: $V_2 - V_1 = %s\\pi - %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.
\\end{enumEX}'''
               % (a, S_tang_heso, a, S_tang_heso, a, S_tang_heso // 4, 2 * a, a**2, S_tang_heso // 4, 2 * a, (S_tang_heso // 4) - a**2, R, R, R, 4 * R**2, 4 * R**2, S_tang_heso, 4 * (R + a)**2, R, latex(V_bandau), R + a, latex(V_sau), latex(V_sau), latex(V_bandau), latex(V_sau - V_bandau)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
