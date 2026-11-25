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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang10_p4_b2_c6_ds8(self):
    # Dạng 10: Tìm giá trị nhỏ nhất và giá trị lớn nhất của phân thức dạng (ax^2 + bx + c)/(x^2 + 1)
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        noidungcauhoi = ('Cho phân thức $S = \\dfrac{2x^2 + 4x + 5}{x^2 + 1}$.\\\n'
                         'a) Chứng minh rằng $S \\ge 1$ với mọi $x \\in \\mathbb{R}$. Dấu đẳng thức xảy ra khi nào?\\\n'
                         'b) Chứng minh rằng $S \\le 6$ với mọi $x \\in \\mathbb{R}$ bằng cách xét hiệu $6 - S$. Từ đó kết luận giá trị lớn nhất của $S$.')

        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Vì $x^2 + 1 > 0$ với mọi $x \\in \\mathbb{R}$ nên phân thức $S$ xác định với mọi $x \\in \\mathbb{R}$.\\\n'
                   'Ta tách tử thức như sau: $2x^2 + 4x + 5 = (x^2 + 1) + (x^2 + 4x + 4) = (x^2 + 1) + (x + 2)^2$.\\\n'
                   'Do đó $S = \\dfrac{(x^2 + 1) + (x + 2)^2}{x^2 + 1} = 1 + \\dfrac{(x + 2)^2}{x^2 + 1}$.\\\n'
                   'Vì $(x + 2)^2 \\ge 0$ và $x^2 + 1 > 0$ với mọi $x \\in \\mathbb{R}$ nên $\\dfrac{(x + 2)^2}{x^2 + 1} \\ge 0$, suy ra $S \\ge 1$ với mọi $x \\in \\mathbb{R}$.\\\n'
                   'Dấu đẳng thức xảy ra khi $x + 2 = 0 \\Leftrightarrow x = -2$.\n'
                   '\\item Xét hiệu $6 - S$:\\\n'
                   '$6 - S = 6 - \\dfrac{2x^2 + 4x + 5}{x^2 + 1} = \\dfrac{6(x^2 + 1) - (2x^2 + 4x + 5)}{x^2 + 1} = \\dfrac{4x^2 - 4x + 1}{x^2 + 1} = \\dfrac{(2x - 1)^2}{x^2 + 1}$.\\\n'
                   'Vì $(2x - 1)^2 \\ge 0$ và $x^2 + 1 > 0$ với mọi $x \\in \\mathbb{R}$ nên $6 - S \\ge 0 \\Leftrightarrow S \\le 6$ với mọi $x \\in \\mathbb{R}$.\\\n'
                   'Dấu đẳng thức xảy ra khi $2x - 1 = 0 \\Leftrightarrow x = \\dfrac{1}{2}$. Vậy giá trị lớn nhất của $S$ là $6$.\n'
                   '\\end{enumEX}')

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
