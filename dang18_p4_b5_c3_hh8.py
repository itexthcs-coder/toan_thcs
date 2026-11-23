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


def bt_dang18_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (-1.5,0);
\\coordinate (C) at (1.5,0);
\\coordinate (B) at (0,2.6);
\\coordinate (D) at (0,-2.6);
\\coordinate (M) at (-0.95,-0.95);
\\coordinate (N) at (0.55,-1.65);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (B)--(D) (B)--(M) (B)--(N) (M)--(N);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (M) circle (1pt) node[below left] {$M$};
\\fill (N) circle (1pt) node[below right] {$N$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thoi $ABCD$ có $\\widehat{BAD} = 60^\\circ$ và cạnh bằng $a$. Một góc $\\widehat{xBy} = 60^\\circ$ quay quanh đỉnh $B$ sao cho tia $Bx$ cắt cạnh $AD$ tại $M$, tia $By$ cắt cạnh $CD$ tại $N$ ($M$ khác $A, D$). \\\\
a) Chứng minh $\\Delta ABM = \\Delta DBN$. \\\\
b) Chứng minh $\\Delta BMN$ là tam giác đều và tổng $MD + DN$ luôn không đổi khi góc $\\widehat{xBy}$ quay quanh $B$.%s'''
                         % (hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Vì $ABCD$ là hình thoi có $\\widehat{BAD} = 60^\\circ$ nên $\\Delta ABD$ và $\\Delta BCD$ là các tam giác đều cạnh $a$.\\\\
Suy ra $AB = BD = a$, $\\widehat{ABD} = 60^\\circ$ và $\\widehat{BDN} = 60^\\circ = \\widehat{BAM}$.\\\\
Ta có $\\widehat{ABM} + \\widehat{MBD} = \\widehat{ABD} = 60^\\circ$ và $\\widehat{DBN} + \\widehat{MBD} = \\widehat{MBN} = 60^\\circ$, suy ra $\\widehat{ABM} = \\widehat{DBN}$.\\\\
Xét $\\Delta ABM$ và $\\Delta DBN$ có: $\\widehat{BAM} = \\widehat{BDN} = 60^\\circ$, $AB = BD = a$, $\\widehat{ABM} = \\widehat{DBN}$.\\\\
Suy ra $\\Delta ABM = \\Delta DBN$ (g.c.g).
\\item Từ $\\Delta ABM = \\Delta DBN$ suy ra $BM = BN$ và $AM = DN$.\\\\
Xét $\\Delta BMN$ cân tại $B$ có $\\widehat{MBN} = 60^\\circ$ nên $\\Delta BMN$ là tam giác đều.\\\\
Mặt khác, ta có $MD + DN = MD + AM = AD = a$ (không đổi).\\\\
Vậy $\\Delta BMN$ là tam giác đều và tổng $MD + DN$ luôn bằng $a$ không đổi khi góc $\\widehat{xBy}$ quay quanh đỉnh $B$.
\\end{enumEX} \n''')

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
