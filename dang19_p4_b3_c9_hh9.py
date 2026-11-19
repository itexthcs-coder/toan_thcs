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


def bt_dang19_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab, bc, ad, cd, ac = random.choice([(300, 400, 140, 480, 500), (600, 800, 280, 960, 1000), (500, 1200, 660, 1120, 1300)])
        r_val = ac // 2

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (C) at (4,0);
\\coordinate (O) at (2,0);
\\coordinate (B) at (1.44,1.92);
\\coordinate (D) at (2.8,-1.833);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt, dashed] (A)--(C);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trên bản đồ quy hoạch một khu đô thị mới, bốn khu chung cư đặt tại bốn vị trí $A, B, C, D$ tạo thành một tứ giác có $\\widehat{ABC} = 90^\\circ$ và $\\widehat{ADC} = 90^\\circ$. Biết khoảng cách giữa hai khu $A$ và $B$ là $%s\\text{ m}$, giữa $B$ và $C$ là $%s\\text{ m}$, và khoảng cách giữa hai khu $A$ và $D$ là $%s\\text{ m}$. \\\\
a) Giải thích vì sao có thể đặt một trạm y tế lưu động tại vị trí $O$ cách đều cả bốn khu chung cư $A, B, C, D$ và tính khoảng cách từ trạm y tế đó đến mỗi khu chung cư. \\\\
b) Tính khoảng cách đường chim bay giữa hai khu chung cư $C$ và $D$.%s''' % (ab, bc, ad, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $O$ là trung điểm của đoạn thẳng $AC$.\\\\
Xét tam giác $ABC$ vuông tại $B$ có $OB$ là đường trung tuyến ứng với cạnh huyền $AC$ nên $OA = OB = OC = \\dfrac{AC}{2}$.\\\\
Xét tam giác $ADC$ vuông tại $D$ có $OD$ là đường trung tuyến ứng với cạnh huyền $AC$ nên $OA = OD = OC = \\dfrac{AC}{2}$.\\\\
Suy ra $OA = OB = OC = OD = \\dfrac{AC}{2}$, nên có thể đặt trạm y tế lưu động tại trung điểm $O$ của $AC$ để cách đều cả bốn khu chung cư.\\\\
Áp dụng định lí Pythagore cho tam giác $ABC$ vuông tại $B$, ta có $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (m)}$.\\\\
Khoảng cách từ trạm y tế $O$ đến mỗi khu chung cư là $R = \\dfrac{AC}{2} = \\dfrac{%s}{2} = %s\\text{ (m)}$.
\\item Áp dụng định lí Pythagore cho tam giác $ADC$ vuông tại $D$, ta có:\\\\
$CD = \\sqrt{AC^2 - AD^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (m)}$.\\\\
Vậy khoảng cách đường chim bay giữa hai khu chung cư $C$ và $D$ là $%s\\text{ m}$.
\\end{enumEX}''' % (ab, bc, ac, ac, r_val, ac, ad, cd, cd))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
