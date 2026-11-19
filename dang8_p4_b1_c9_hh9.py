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


def bt_dang8_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([8, 10, 12, 14])
        r = R // 2

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (O1) at (-1,0);\n'
            '\\coordinate (A) at (-2,0);\n'
            '\\coordinate (C) at (50:2);\n'
            '\\coordinate (B) at ($(A)!0.5!(C)$);\n'
            '\\coordinate (E) at (-40:2);\n'
            '\\coordinate (D) at ($(A)!0.5!(E)$);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (O1) circle (1cm);\n'
            '\\draw[line width=1pt] (A)--(C) (A)--(E) (B)--(D) (C)--(E) (O1)--(B) (O)--(C);\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (O1) circle (1pt) node[below] {$O\'$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[above left] {$B$};\n'
            '\\fill (C) circle (1pt) node[above right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below left] {$D$};\n'
            '\\fill (E) circle (1pt) node[below right] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O\'; %s\\text{ cm})$ tiếp xúc trong tại điểm $A$. Một cát tuyến qua $A$ cắt $(O\')$ tại $B$ và cắt $(O)$ tại $C$ ($B$ nằm giữa $A$ và $C$). Một cát tuyến thứ hai qua $A$ cắt $(O\')$ tại $D$ và cắt $(O)$ tại $E$ ($D$ nằm giữa $A$ và $E$) như hình vẽ.\\'
            'a) Chứng minh $\\triangle O\'AB$ và $\\triangle OAC$ là các tam giác cân.\\'
            'b) Chứng minh $O\'B // OC$ và suy ra $BD // CE$.\\'
            'c) Tính tỉ số $\\dfrac{BD}{CE}$.\n%s'
            % (R, r, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong đường tròn $(O\'; %s\\text{ cm})$, ta có $O\'A = O\'B = %s\\text{ cm}$ nên $\\triangle O\'AB$ cân tại $O\'$. Trong đường tròn $(O; %s\\text{ cm})$, ta có $OA = OC = %s\\text{ cm}$ nên $\\triangle OAC$ cân tại $O$.\n'
            '\\item Vì hai đường tròn $(O)$ và $(O\')$ tiếp xúc trong tại $A$ nên ba điểm $A, O\', O$ thẳng hàng.\\'
            'Do $\\triangle O\'AB$ cân tại $O\'$ nên $\\widehat{O\'BA} = \\widehat{O\'AB}$, và $\\triangle OAC$ cân tại $O$ nên $\\widehat{OCA} = \\widehat{OAC}$. Suy ra $\\widehat{O\'BA} = \\widehat{OCA}$ (cùng bằng $\\widehat{OAC}$), mà hai góc này ở vị trí đồng vị nên $O\'B // OC$.\\'
            'Theo định lí Thalès trong $\\triangle OAC$, ta có $\\dfrac{AB}{AC} = \\dfrac{AO\'}{AO} = \\dfrac{%s}{%s} = \\dfrac{1}{2}$. Chứng minh tương tự với cát tuyến $ADE$, ta cũng có $O\'D // OE$ và $\\dfrac{AD}{AE} = \\dfrac{AO\'}{AO} = \\dfrac{1}{2}$. Suy ra $\\dfrac{AB}{AC} = \\dfrac{AD}{AE}$, theo định lí Thalès đảo ta được $BD // CE$.\n'
            '\\item Vì $BD // CE$ nên theo hệ quả định lí Thalès trong $\\triangle ACE$, ta có $\\dfrac{BD}{CE} = \\dfrac{AB}{AC} = \\dfrac{1}{2}$.\n'
            '\\end{enumEX}'
            % (r, r, R, R, r, R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
