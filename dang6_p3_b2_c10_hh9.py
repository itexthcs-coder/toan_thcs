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


def bt_dang6_p3_b2_c10_hh9(self):
    r1 = random.choice([3, 6])
    r2 = random.choice([3, 6])
    S1 = 4 * r1**2
    V1 = (4 * r1**3) // 3
    S2 = 4 * r2**2
    V2 = (4 * r2**3) // 3
    tong = S1 + V1 + r2 + V2
    kq_str = str(tong)

    noidungcauhoi = ('''Cho hai hình cầu $(H_1)$ và $(H_2)$ có các thông số (tính theo hệ số của $\\pi$ đối với diện tích và thể tích) như sau:\\\n- Hình cầu $(H_1)$ có bán kính $R_1 = %s\\text{ cm}$, diện tích mặt cầu bằng $x\\pi\\text{ cm}^2$ và thể tích bằng $y\\pi\\text{ cm}^3$.\\\n- Hình cầu $(H_2)$ có bán kính $R_2 = z\\text{ cm}$, diện tích mặt cầu bằng $%s\\pi\\text{ cm}^2$ và thể tích bằng $t\\pi\\text{ cm}^3$.\\\nTính giá trị của tổng $x + y + z + t$.''' % (r1, S2))

    loigiai = ('''Đối với hình cầu $(H_1)$ có bán kính $R_1 = %s\\text{ cm}$:\\\n- Diện tích mặt cầu: $S_1 = 4\\pi R_1^2 = 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)} \\Rightarrow x = %s$.\\\n- Thể tích hình cầu: $V_1 = \\dfrac{4}{3}\\pi R_1^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)} \\Rightarrow y = %s$.\\\nĐối với hình cầu $(H_2)$ có diện tích mặt cầu bằng $%s\\pi\\text{ cm}^2$:\\\n- Ta có $4\\pi R_2^2 = %s\\pi \\Rightarrow R_2^2 = %s \\Rightarrow R_2 = %s\\text{ (cm)} \\Rightarrow z = %s$.\\\n- Thể tích hình cầu: $V_2 = \\dfrac{4}{3}\\pi R_2^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)} \\Rightarrow t = %s$.\\\nVậy $x + y + z + t = %s + %s + %s + %s = %s$.'''
               % (r1, r1, S1, S1, r1, V1, V1, S2, S2, r2**2, r2, r2, r2, V2, V2, S1, V1, r2, V2, tong))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
