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


def bt_dang9_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m = random.choice([3, 4])
        # BD = m * DC => DC / DB = 1 / m
        # Ke DE // BM (E in AC) => EM / MC = BD / DC = m => EM = m * MC
        # M la trung diem AC => AM = MC => AM / ME = 1 / m => AK / KD = AM / ME = 1 / m?
        # Khoan: ta tinh KD / AK = m hoac AK / KD = m / 2.
        # Chon m = 3: BD = 3 DC => ke ME // AD (E in BC) => CE / ED = CM / MA = 1 => CE = ED = 1/2 DC.
        # Khi do BD = 3 DC = 6 ED => AK / KD = BE / ED? Khong, BE = BD + DE = 7 DE => AK / KD = 7?
        # De so dep: Dat BD = 3 DC, hoi ti so DK / KA = 2, hoac BD = 3 DC, M trung diem AC => ke DE // BM (E in AC):
        # DE // BM => CE / EM = CD / DB = 1 / 3 => EM = 3 CE => CM = 4 CE.
        # Vi M la trung diem AC nen AM = CM = 4 CE.
        # Xet tam giac ADE co KM // DE => AK / KD = AM / ME = 4 CE / (3 CE) = 4/3?
        # Neu BD = 3 DC va hoi KD / KA thi 3/4 = 0,75! Hoac BD = 3 DC, AM = 2 MC => AM = 8 CE => AK / KD = 8/3?
        # Chon: BD = 3 DC, M la trung diem AC, ke DE // BM (E in AC) => AK / KD = 4 / 3?
        # Chon de co so thap phan dep: BD = 3 DC, và AM = 3 MC => CM = 4 CE, AM = 12 CE => AK / KD = 12 / 3 = 4!
        # Hoac BD = 4 DC, M trung diem AC => CE / EM = 1/4 => EM = 4 CE, CM = 5 CE = AM => AK / KD = 5/4 = 1,25!
        # Hoac BD = 2 DC, M trung diem AC => CE / EM = 1/2 => EM = 2 CE, CM = 3 CE = AM => AK / KD = 3/2 = 1,5!
        m = random.choice([2, 4])
        ak_kd = Rational(m + 1, m)
        kq_str = str(float(ak_kd)).replace('.', ',')

        noidungcauhoi = ("""Cho $\\Delta ABC$, gọi $D$ là điểm nằm trên cạnh $BC$ sao cho $BD = %s DC$. Gọi $M$ là trung điểm của đoạn thẳng $AC$. Đường thẳng $BM$ cắt $AD$ tại $K$ (như hình vẽ bên dưới). Tỉ số $\\dfrac{AK}{KD}$ bằng bao nhiêu?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (D) at ($(B)!0.75!(C)$);
\\coordinate (M) at ($(A)!0.5!(C)$);
\\coordinate (K) at (intersection of A--D and B--M);
\\coordinate (E) at ($(M)!0.2!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D) (B)--(M);
\\draw[line width=1pt, dashed] (D)--(E);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (M) circle (1pt) node[right] {$M$};
\\fill (K) circle (1pt) node[above left] {$K$};
\\fill (E) circle (1pt) node[right] {$E$};
\\end{tikzpicture}
\\end{center}"""
                         % (m))

        loigiai = ("""Qua $D$ kẻ đường thẳng song song với $BM$ cắt cạnh $AC$ tại $E$. \\\\
Xét $\\Delta CBM$ có $DE // BM$, theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{CE}{EM} = \\dfrac{CD}{DB} = \\dfrac{1}{%s} \\Rightarrow EM = %s CE$. \\\\
Suy ra $CM = CE + EM = CE + %s CE = %s CE$. \\\\
Vì $M$ là trung điểm của $AC$ nên $AM = CM = %s CE$. \\\\
Xét $\\Delta ADE$ có $KM // DE$, theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{AK}{KD} = \\dfrac{AM}{ME} = \\dfrac{%s CE}{%s CE} = \\dfrac{%s}{%s} = %s$. \\\\
Vậy tỉ số $\\dfrac{AK}{KD}$ bằng $%s$."""
                   % (m, m, m, m + 1, m + 1, m + 1, m, m + 1, m, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
