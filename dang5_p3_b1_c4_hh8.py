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


def bt_dang5_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mb_dec = random.choice([3.5, 4.5, 5.5, 6.5])
        nc_dec = random.choice([4.0, 5.0, 6.0, 7.5])
        am_val = Rational(str(mb_dec)) * 2
        an_val = Rational(str(nc_dec)) * 2
        tong_val = am_val + an_val
        mb_s = str(mb_dec).replace('.', ',')
        nc_s = str(nc_dec).rstrip('0').rstrip('.').replace('.', ',')
        am_s = str(int(am_val)) if am_val.is_Integer else str(float(am_val)).replace('.', ',')
        an_s = str(int(an_val)) if an_val.is_Integer else str(float(an_val)).replace('.', ',')
        kq_str = str(int(tong_val)) if tong_val.is_Integer else str(float(tong_val)).replace('.', ',')

        noidungcauhoi = ("""Cho $\\Delta ABC$ có trọng tâm $G$. Đường thẳng đi qua $G$ và song song với cạnh $BC$ cắt các cạnh $AB$, $AC$ lần lượt tại $M$ và $N$ (như hình vẽ bên dưới). Biết $MB = %s\\text{ cm}$ và $NC = %s\\text{ cm}$. Tổng độ dài hai đoạn thẳng $AM + AN$ bằng bao nhiêu $\\text{cm}$?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (D) at ($(B)!0.5!(C)$);
\\coordinate (G) at ($(A)!0.6667!(D)$);
\\coordinate (M) at ($(A)!0.6667!(B)$);
\\coordinate (N) at ($(A)!0.6667!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N);
\\draw[line width=1pt, dashed] (A)--(D);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (G) circle (1pt) node[below right] {$G$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}"""
                         % (mb_s, nc_s))

        loigiai = ("""Gọi $D$ là trung điểm của cạnh $BC$, khi đó $AD$ là đường trung tuyến của $\\Delta ABC$. \\\\
Vì $G$ là trọng tâm của $\\Delta ABC$ nên $\\dfrac{AG}{AD} = \\dfrac{2}{3} \\Rightarrow \\dfrac{AG}{GD} = 2$. \\\\
Xét $\\Delta ABD$ có $MG // BD$, theo định lí Thalès ta có: $\\dfrac{AM}{MB} = \\dfrac{AG}{GD} = 2 \\Rightarrow AM = 2 MB = 2 \\cdot %s = %s\\text{ (cm)}$. \\\\
Xét $\\Delta ACD$ có $GN // DC$, theo định lí Thalès ta có: $\\dfrac{AN}{NC} = \\dfrac{AG}{GD} = 2 \\Rightarrow AN = 2 NC = 2 \\cdot %s = %s\\text{ (cm)}$. \\\\
Vậy $AM + AN = %s + %s = %s\\text{ (cm)}$."""
                   % (mb_s, am_s, nc_s, an_s, am_s, an_s, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
