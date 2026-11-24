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


def fmt_num(val):
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return str(val).replace('.', ',')

def bt_dang20_p3_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mn = random.choice([20, 22, 24, 25, 28, 30])
        mq = random.choice([14, 15, 16, 18, 20])
        cv_mnpq = (mn + mq) * 2
        s_mnpq = mn * mq
        s_abcd = s_mnpq * 2
        kq_str = fmt_num(s_abcd)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (2.2,3.4);
\\coordinate (B) at (0,1.8);
\\coordinate (C) at (2.2,0);
\\coordinate (D) at (4.4,1.8);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(B)!0.5!(C)$);
\\coordinate (P) at ($(C)!0.5!(D)$);
\\coordinate (Q) at ($(D)!0.5!(A)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N)--(P)--(Q)--cycle;
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (N) circle (1pt) node[below left] {$N$};
\\fill (P) circle (1pt) node[below right] {$P$};
\\fill (Q) circle (1pt) node[above right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một chiếc diều có khung là tứ giác $ABCD$ với hai thanh tre chéo $AC \\perp BD$. Người ta dán một lớp giấy màu hình tứ giác $MNPQ$ nối trung điểm bốn cạnh $AB, BC, CD, DA$ ở phần giữa cánh diều (như hình vẽ). Biết phần giấy màu $MNPQ$ có chu vi bằng $%s\\text{ cm}$ và chiều dài $MN = %s\\text{ cm}$. Tính diện tích toàn bộ cánh diều $ABCD$ (đơn vị: $\\text{cm}^2$).%s''' % (fmt_num(cv_mnpq), fmt_num(mn), hinhve))

        loigiai = ('''Ta có $MN // PQ // AC$, $MQ // NP // BD$ và $AC \\perp BD$ nên tứ giác $MNPQ$ là hình chữ nhật.\\
Nửa chu vi hình chữ nhật $MNPQ$ là $MN + MQ = \\dfrac{%s}{2} = %s\\text{ cm}$, suy ra $MQ = %s - %s = %s\\text{ cm}$.\\
Diện tích phần giấy màu $MNPQ$ là $S_{MNPQ} = MN \\cdot MQ = %s \\cdot %s = %s\\text{ cm}^2$.\\
Vì $AC = 2MN$ và $BD = 2MQ$ nên diện tích toàn bộ cánh diều $ABCD$ là:\\
$S_{ABCD} = \\dfrac{1}{2}AC \\cdot BD = \\dfrac{1}{2} \\cdot (2MN) \\cdot (2MQ) = 2 S_{MNPQ} = 2 \\cdot %s = %s\\text{ cm}^2$.''' % (fmt_num(cv_mnpq), fmt_num(mn + mq), fmt_num(mn + mq), fmt_num(mn), fmt_num(mq), fmt_num(mn), fmt_num(mq), fmt_num(s_mnpq), fmt_num(s_mnpq), kq_str))

    dapan = '\n\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
