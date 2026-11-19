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


def bt_dang12_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        BC = random.choice([8, 10, 12, 14, 16])

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (-2,0);\n'
            '\\coordinate (C) at (2,0);\n'
            '\\coordinate (M) at (0,0);\n'
            '\\coordinate (A) at (-0.6,2.8);\n'
            '\\coordinate (E) at ($(A)!(B)!(C)$);\n'
            '\\coordinate (F) at ($(A)!(C)!(B)$);\n'
            '\\coordinate (H) at (intersection of B--E and C--F);\n'
            '\\coordinate (I) at ($(A)!0.5!(H)$);\n'
            '\\draw[line width=1pt] (2,0) arc (0:180:2cm);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (B)--(E) (C)--(F) (E)--(F);\n'
            '\\draw[line width=1pt, dashed] (M)--(E) (M)--(F);\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (M) circle (1pt) node[below] {$M$};\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (E) circle (1pt) node[above right] {$E$};\n'
            '\\fill (F) circle (1pt) node[above left] {$F$};\n'
            '\\fill (H) circle (1pt) node[below right] {$H$};\n'
            '\\fill (I) circle (1pt) node[left] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tam giác $ABC$ nhọn có $BC = %s\\text{ cm}$, các đường cao $BE$ và $CF$ cắt nhau tại $H$. Gọi $M$ là trung điểm của cạnh $BC$ như hình vẽ.\\\\'
            'a) Chứng minh bốn điểm $B, F, E, C$ cùng nằm trên đường tròn tâm $M$ đường kính $BC$ và tính bán kính đường tròn đó.\\\\'
            'b) Chứng minh $\\widehat{AEF} = \\widehat{ABC}$ và $\\triangle AEF \\backsim \\triangle ABC$.\\\\'
            'c) Chứng minh bốn điểm $A, F, H, E$ cùng nằm trên một đường tròn và xác định tâm của đường tròn đó.\n%s'
            % (BC, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Xét $\\triangle BFC$ vuông tại $F$ có $FM$ là đường trung tuyến ứng với cạnh huyền $BC$ nên $MF = MB = MC = \\dfrac{BC}{2} = %s\\text{ cm}$.\\\\'
            'Tương tự, $\\triangle BEC$ vuông tại $E$ có $EM$ là đường trung tuyến ứng với cạnh huyền $BC$ nên $ME = MB = MC = %s\\text{ cm}$.\\\\'
            'Suy ra $MB = MC = ME = MF = %s\\text{ cm}$, do đó bốn điểm $B, F, E, C$ cùng nằm trên đường tròn tâm $M$ đường kính $BC$ bán kính $%s\\text{ cm}$.\n'
            '\\item Xét đường tròn $(M)$, hai góc nội tiếp $\\widehat{EBC}$ và $\\widehat{EFC}$ cùng chắn cung nhỏ $EC$ nên $\\widehat{EBC} = \\widehat{EFC}$.\\\\'
            'Ta có $\\widehat{AEF} + \\widehat{FEC} = 180^\\circ$ (kề bù) và $\\widehat{ABC} + \\widehat{FEC} = (90^\\circ - \\widehat{FCB}) + (90^\\circ + \\widehat{EFC}) = 180^\\circ$, suy ra $\\widehat{AEF} = \\widehat{ABC}$.\\\\'
            'Xét $\\triangle AEF$ và $\\triangle ABC$ có $\\widehat{A}$ chung và $\\widehat{AEF} = \\widehat{ABC}$ nên $\\triangle AEF \\backsim \\triangle ABC$ (g.g).\n'
            '\\item Gọi $I$ là trung điểm của đoạn thẳng $AH$. Xét $\\triangle AFH$ vuông tại $F$ có $FI$ là đường trung tuyến ứng với cạnh huyền $AH$ nên $IF = IA = IH$.\\\\'
            'Tương tự, $\\triangle AEH$ vuông tại $E$ có $EI$ là đường trung tuyến ứng với cạnh huyền $AH$ nên $IE = IA = IH$.\\\\'
            'Vậy $IA = IF = IH = IE$, do đó bốn điểm $A, F, H, E$ cùng nằm trên đường tròn tâm $I$ (trung điểm của $AH$) đường kính $AH$.\n'
            '\\end{enumEX}'
            % (BC // 2, BC // 2, BC // 2, BC // 2)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
