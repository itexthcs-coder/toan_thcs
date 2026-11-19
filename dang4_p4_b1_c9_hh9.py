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


def bt_dang4_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(5, 15)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (-2,0);\n'
            '\\coordinate (B) at (2,0);\n'
            '\\coordinate (C) at (125:2);\n'
            '\\coordinate (D) at (0.8,0);\n'
            '\\coordinate (F) at (0.8,2.76);\n'
            '\\coordinate (E) at (intersection of B--C and D--F);\n'
            '\\coordinate (M) at (-42:2);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B) (A)--(F)--(B) (D)--(F) (B)--(M) (A)--(M);\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (E) circle (1pt) node[above right] {$E$};\n'
            '\\fill (F) circle (1pt) node[above] {$F$};\n'
            '\\fill (M) circle (1pt) node[below right] {$M$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho đường tròn $(O; %s\\text{ cm})$ đường kính $AB$. Lấy điểm $C$ nằm trên đường tròn $(O)$ ($CA < CB$) và điểm $D$ nằm trên đoạn thẳng $OB$ ($D$ khác $O, B$). Đường thẳng qua $D$ vuông góc với $AB$ cắt $BC$ tại $E$ và cắt đường thẳng $AC$ tại $F$ như hình vẽ.\\\\'
            'a) Chứng minh $\\widehat{ACB} = 90^\\circ$ và $\\triangle BDE \\backsim \\triangle BCA$.\\\\'
            'b) Chứng minh $BD \\cdot BA = BE \\cdot BC$.\\\\'
            'c) Đường thẳng $BF$ cắt đường tròn $(O)$ tại điểm thứ hai là $M$. Chứng minh ba điểm $A, E, M$ thẳng hàng.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong đường tròn $(O; %s\\text{ cm})$, góc nội tiếp $\\widehat{ACB}$ chắn nửa đường tròn đường kính $AB$ nên $\\widehat{ACB} = 90^\\circ$.\\\\'
            'Xét $\\triangle BDE$ và $\\triangle BCA$ có $\\widehat{BDE} = \\widehat{BCA} = 90^\\circ$ và $\\widehat{B}$ chung nên $\\triangle BDE \\backsim \\triangle BCA$ (g.g).\n'
            '\\item Từ $\\triangle BDE \\backsim \\triangle BCA$, ta suy ra $\\dfrac{BD}{BC} = \\dfrac{BE}{BA} \\Rightarrow BD \\cdot BA = BE \\cdot BC$.\n'
            '\\item Xét $\\triangle FAB$ có $BC \\perp AF$ (do $\\widehat{ACB} = 90^\\circ$) và $FD \\perp AB$ (giả thiết). Hai đường cao $BC$ và $FD$ cắt nhau tại $E$ nên $E$ là trực tâm của $\\triangle FAB$, suy ra $AE \\perp BF$.\\\\'
            'Mặt khác, trong đường tròn $(O)$, góc nội tiếp $\\widehat{AMB}$ chắn nửa đường tròn đường kính $AB$ nên $\\widehat{AMB} = 90^\\circ$, hay $AM \\perp BF$.\\\\'
            'Qua điểm $A$ nằm ngoài đường thẳng $BF$, có hai đường thẳng $AE$ và $AM$ cùng vuông góc với $BF$ nên ba điểm $A, E, M$ thẳng hàng.\n'
            '\\end{enumEX}'
            % (R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
