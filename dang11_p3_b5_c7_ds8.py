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


def bt_dang11_p3_b5_c7_ds8(self):
    # Dang 11: Xac dinh he so cua duong thang chua canh hinh binh hanh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        xa = random.choice([2, 3, 4, 5])
        xc = random.choice([1, 2])
        k = random.choice([2, 3, 4])
        yc = k * xc
        a_res = k
        b_res = -a_res * xa
        ans = a_res + b_res
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-1,0) -- (4.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1) -- (0,3) node[left] {$y$};\n'
            '\\draw[line width=1pt] (0,0) -- (2.5,0) -- (3.5,2.2) -- (1,2.2) -- cycle;\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (2.5,0) circle (1pt) node[below] {$A$};\n'
            '\\fill (3.5,2.2) circle (1pt) node[right] {$B$};\n'
            '\\fill (1,2.2) circle (1pt) node[above left] {$C$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho hình bình hành $OABC$ trên mặt phẳng tọa độ $Oxy$ với $O(0; 0)$, $A(%s; 0)$ và $C(%s; %s)$. '
            'Đường thẳng chứa cạnh $AB$ có phương trình $y = ax + b$. Tính giá trị $a + b$.\n%s'
            % (xa, xc, yc, tikz)
        )
        
        loigiai = (
            'Đường thẳng $OC$ đi qua gốc tọa độ $O(0; 0)$ nên có dạng $y = a_1 x$.\\ '
            'Vì $OC$ đi qua điểm $C(%s; %s)$ nên ta có: $%s = a_1 \\cdot %s \\Leftrightarrow a_1 = %s$.\\ '
            'Trong hình bình hành $OABC$, cạnh $AB$ song song với cạnh $OC$ nên đường thẳng $AB$ có hệ số góc $a = a_1 = %s$.\\ '
            'Phương trình đường thẳng $AB$ có dạng $y = %sx + b$. Vì đường thẳng này đi qua điểm $A(%s; 0)$ nên:\\ '
            '$0 = %s \\cdot %s + b \\Leftrightarrow b = %s$.\\ '
            'Vậy giá trị cần tính là: $a + b = %s + (%s) = %s$.'
            % (xc, yc, yc, xc, k, k, k, xa, k, xa, b_res, a_res, b_res, ans)
        )
        
        dapan = '\\shortans[0]{$%s$}\n' % ans

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
