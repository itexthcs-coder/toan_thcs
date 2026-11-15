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
### CÔNG CỤ
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


def bt_dang9_p4_b3_c2_ds9(self):
    m = symbols('m')
    m0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4, 5])
    k = random.choice([-3, -2, 2, 3])

    he_so_expr = m - m0
    hang_so_expr = k * (m - m0)
    dau = random.choice(['>', '<', r'\ge', r'\le'])
    map_dau = {r'\le': r'\ge', r'\ge': r'\le', '<': '>', '>': '<'}
    dau_kq = map_dau[dau]

    dau_hang_so = f"+ {latex(hang_so_expr)}" if k > 0 else f"- {latex(-hang_so_expr)}"

    noidungcauhoi = (
        f"Cho bất phương trình $({latex(he_so_expr)})x {dau_hang_so} {dau} 0$ (với $m$ là tham số).\\\n"
        f"a) Tìm điều kiện của $m$ để bất phương trình đã cho là bất phương trình bậc nhất một ẩn.\\\n"
        f"b) Giải bất phương trình đã cho khi $m < {m0}$."
    )

    loigiai = (
        f"\\begin{{enumEX}}[a)]{{1}}\n"
        f"\\item Bất phương trình đã cho là bất phương trình bậc nhất một ẩn khi hệ số của $x$ khác $0$, tức là:\\\n"
        f"${latex(he_so_expr)} \\ne 0 \\Leftrightarrow m \\ne {m0}$.\n"
        f"\\item Khi $m < {m0}$ thì ${latex(he_so_expr)} < 0$. Ta có:\\\n"
        f"$({latex(he_so_expr)})x {dau_hang_so} {dau} 0$\\\n"
        f"$({latex(he_so_expr)})x {dau} {latex(-hang_so_expr)}$\\\n"
        f"Chia cả hai vế của bất phương trình cho số âm ${latex(he_so_expr)}$ và đổi chiều bất đẳng thức, ta được:\\\n"
        f"$x {dau_kq} \\dfrac{{{latex(-hang_so_expr)}}}{{{latex(he_so_expr)}}}$\\\n"
        f"$x {dau_kq} {-k}$.\\\n"
        f"Vậy với $m < {m0}$, nghiệm của bất phương trình là $x {dau_kq} {-k}$.\n"
        f"\\end{{enumEX}}"
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
