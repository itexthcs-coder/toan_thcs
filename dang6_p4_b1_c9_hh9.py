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


def bt_dang6_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(5, 14)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (110:2);\n'
            '\\coordinate (D) at (-70:2);\n'
            '\\coordinate (B) at (215:2);\n'
            '\\coordinate (C) at (325:2);\n'
            '\\coordinate (E) at ($(A)!(B)!(C)$);\n'
            '\\coordinate (F) at ($(A)!(C)!(B)$);\n'
            '\\coordinate (H) at (intersection of B--E and C--F);\n'
            '\\coordinate (M) at ($(B)!0.5!(C)$);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D) (B)--(D)--(C) (B)--(E) (C)--(F) (H)--(D) (O)--(M);\n'
            '\\fill (O) circle (1pt) node[above right] {$O$};\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (E) circle (1pt) node[above right] {$E$};\n'
            '\\fill (F) circle (1pt) node[above left] {$F$};\n'
            '\\fill (H) circle (1pt) node[left] {$H$};\n'
            '\\fill (M) circle (1pt) node[below] {$M$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tam giác $ABC$ nhọn ($AB < AC$) nội tiếp đường tròn $(O; %s\\text{ cm})$. Hai đường cao $BE$ và $CF$ cắt nhau tại trực tâm $H$. Vẽ đường kính $AD$ của đường tròn $(O)$ như hình vẽ.\\'
            'a) Chứng minh $\\widehat{ABD} = \\widehat{ACD} = 90^\\circ$.\\'
            'b) Chứng minh tứ giác $BHCD$ là hình bình hành.\\'
            'c) Gọi $M$ là trung điểm của cạnh $BC$. Chứng minh ba điểm $H, M, D$ thẳng hàng và $AH = 2OM$.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong đường tròn $(O; %s\\text{ cm})$, các góc nội tiếp $\\widehat{ABD}$ và $\\widehat{ACD}$ cùng chắn nửa đường tròn đường kính $AD$ nên $\\widehat{ABD} = \\widehat{ACD} = 90^\\circ$.\n'
            '\\item Ta có $BH \\perp AC$ (do $BE$ là đường cao) và $CD \\perp AC$ (do $\\widehat{ACD} = 90^\\circ$) nên $BH // CD$.\\'
            'Tương tự, $CH \\perp AB$ (do $CF$ là đường cao) và $BD \\perp AB$ (do $\\widehat{ABD} = 90^\\circ$) nên $CH // BD$.\\'
            'Tứ giác $BHCD$ có các cặp cạnh đối song song nên $BHCD$ là hình bình hành.\n'
            '\\item Vì $BHCD$ là hình bình hành nên hai đường chéo $BC$ và $HD$ cắt nhau tại trung điểm của mỗi đường. Mà $M$ là trung điểm của $BC$ nên $M$ cũng là trung điểm của $HD$, suy ra ba điểm $H, M, D$ thẳng hàng.\\'
            'Xét $\\triangle AHD$ có $O$ là trung điểm của $AD$ và $M$ là trung điểm của $HD$ nên $OM$ là đường trung bình của $\\triangle AHD$, suy ra $AH = 2OM$.\n'
            '\\end{enumEX}'
            % (R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
