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


def bt_dang12_p4_b2_c10_hh9(self):
    r = random.choice([2, 3, 4])
    R = 4 * r
    OO1 = R + r
    AB = 4 * r
    S_ht = ((R + r) * AB) // 2

    noidungcauhoi = ('''Cho hai hình cầu tâm $O$ bán kính $R = %s\\text{ cm}$ và tâm $O_1$ bán kính $r = %s\\text{ cm}$ tiếp xúc ngoài với nhau tại $M$ và cùng nằm trên một mặt phẳng $(P)$, lần lượt tiếp xúc với $(P)$ tại $A$ và $B$.\\\na) Chứng minh tứ giác $OO_1BA$ là hình thang vuông và tính độ dài đoạn thẳng $AB$.\\\nb) Tính diện tích của tứ giác $OO_1BA$.\\\nc) Gọi $I$ là hình chiếu vuông góc của tiếp điểm $M$ lên mặt phẳng $(P)$. Tính độ dài đoạn thẳng $MI$.'''
                     % (R, r))

    # MI = (R*r*2) / (R+r) = (8*r^2) / (5*r) = 8r/5
    MI_val = Rational(2 * R * r, R + r)

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $(P)$ tiếp xúc với hai mặt cầu tại $A$ và $B$ nên $OA \\perp AB$ và $O_1B \\perp AB$, suy ra $OA // O_1B$ nên tứ giác $OO_1BA$ là hình thang vuông tại $A$ và $B$.\\\nKẻ $O_1H \\perp OA$ tại $H$, ta có $OH = OA - O_1B = R - r = %s\\text{ (cm)}$ và $OO_1 = R + r = %s\\text{ (cm)}$.\\\nÁp dụng định lí Pythagore trong $\\triangle OHO_1$ vuông tại $H$:
$$AB = O_1H = \\sqrt{OO_1^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
\\item Diện tích hình thang vuông $OO_1BA$ là:
$$S_{OO_1BA} = \\dfrac{(OA + O_1B) \\cdot AB}{2} = \\dfrac{(%s + %s) \\cdot %s}{2} = %s\\text{ (cm}^2\\text{)}.$$
\\item Vì $M$ nằm trên đoạn $OO_1$ với $\\dfrac{OM}{OO_1} = \\dfrac{R}{R + r}$ và $MI // OA // O_1B$, áp dụng định lí Thalès trong hình thang ta có:
$$MI = \\dfrac{2Rr}{R + r} = \\dfrac{2 \\cdot %s \\cdot %s}{%s + %s} = %s\\text{ (cm)}.$$
\\end{enumEX}'''
               % (R - r, OO1, OO1, R - r, AB, R, r, AB, S_ht, R, r, R, r, latex(MI_val)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
