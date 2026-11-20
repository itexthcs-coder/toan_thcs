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


def bt_dang2_p4_b2_c10_hh9(self):
    k = random.choice([1, 2])
    R = 5 * k
    OH = 3 * k
    r_day = 4 * k
    # Trường hợp đoạn nối đỉnh và tâm đáy chứa tâm O: h = R + OH = 8k => l = sqrt(r_day^2 + h^2) = sqrt(16k^2 + 64k^2) = 4k*sqrt(5)
    h1 = R + OH
    l1_coef = 4 * k
    V1 = Rational(1, 3) * r_day**2 * h1
    # Trường hợp đoạn nối đỉnh và tâm đáy không chứa tâm O: h = R - OH = 2k => l = sqrt(16k^2 + 4k^2) = 2k*sqrt(5)
    h2 = R - OH
    l2_coef = 2 * k
    V2 = Rational(1, 3) * r_day**2 * h2

    noidungcauhoi = ('''Cho hình cầu tâm $O$ bán kính $R = %s\\text{ cm}$ và một hình nón có đỉnh $S$, đường tròn đáy tâm $H$ cùng nằm trên mặt cầu đó. Biết khoảng cách từ tâm $O$ của mặt cầu đến mặt phẳng đáy của hình nón bằng $%s\\text{ cm}$.\\\na) Tính bán kính đáy của hình nón.\\\nb) Tính thể tích của hình nón trong trường hợp tâm $O$ nằm giữa đỉnh $S$ và tâm $H$.\\\nc) Tính độ dài đường sinh của hình nón trong trường hợp tâm $O$ nằm ngoài đoạn thẳng $SH$.'''
                     % (R, OH))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Lấy một điểm $B$ nằm trên đường tròn đáy tâm $H$ của hình nón, ta có $OB = R = %s\\text{ cm}$, $OH = %s\\text{ cm}$ và $OH \\perp HB$.\\\nÁp dụng định lí Pythagore trong tam giác $OHB$ vuông tại $H$, bán kính đáy hình nón là:
$$r = HB = \\sqrt{OB^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
\\item Khi tâm $O$ nằm giữa đỉnh $S$ và tâm $H$ của đáy nón thì chiều cao của hình nón là:
$$h_1 = SH = SO + OH = R + OH = %s + %s = %s\\text{ (cm)}.$$
Thể tích của hình nón là:
$$V_1 = \\dfrac{1}{3}\\pi r^2 h_1 = \\dfrac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\item Khi tâm $O$ nằm ngoài đoạn thẳng $SH$ thì chiều cao của hình nón là:
$$h_2 = SH = SO - OH = R - OH = %s - %s = %s\\text{ (cm)}.$$
Độ dài đường sinh của hình nón là:
$$l_2 = SB = \\sqrt{HB^2 + SH^2} = \\sqrt{%s^2 + %s^2} = %s\\sqrt{5}\\text{ (cm)}.$$
\\end{enumEX}'''
               % (R, OH, R, OH, r_day, R, OH, h1, r_day, h1, latex(V1), R, OH, h2, r_day, h2, l2_coef))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
