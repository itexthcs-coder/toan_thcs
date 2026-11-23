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


def bt_dang15_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # AD = 2 DB => DB = 1/3 AB; AE = 3 EC => EC = 1/4 AC
        # Qua D ke song song BC cat AC tai M => MC = 1/3 AC = 4/12 AC, EC = 3/12 AC => ME = 1/12 AC
        # DF // EC va EF // DB (neu EF // AB) => DF = EC = 1/4 AC!
        # Wait: neu EF // AB va DF // BC thi DFEC khong phai hinh binh hanh, ma DF // BC cat EF // AB tai F:
        # Goi G la giao cua DF va AC => CG / CA = BD / BA = 1 / 3 => CG = 1/3 AC.
        # Trong tam giac CGF co EF // AB (tuc EF // CG? Khong, EF // AB va AB cat AC tai A).
        # De don gian va chuan: Goi F la giao diem cua duong thang qua D song song voi BC va duong thang qua E song song voi AB.
        # Khi do qua D ke song song BC cat AC tai K => AK / AC = AD / AB = 2 / 3 => AK = 2/3 AC.
        # Ma AE = 3/4 AC => KE = AE - AK = (3/4 - 2/3) AC = 1/12 AC.
        # Mat khac DK // BC, EF // AB => Xet tam giac AEF co DK // EF? Khong, DK // BC con EF // AB!
        # Sua tinh huong de tuyet doi chinh xac va dep:
        # Cho tam giac ABC, D thuoc AB sao cho AD = 2 DB, E thuoc AC sao cho AE = 3 EC.
        # Duong thang qua E song song voi BC cat AB tai M; duong thang qua D song song voi AC cat BC tai N.
        # Hoac: Qua E ke song song voi AB cat BC tai F; qua F ke song song voi AC cat AB tai K. Tinh AK!
        # AE = 3 EC => EC / AC = 1 / 4 => BF / BC = 1 / 4 => FC / BC = 3 / 4 => AK / AB = 3 / 4!
        # Vay AK = 3/4 AB! Rat dep va chuan!
        m = random.choice([2, 3, 4])
        # AE = m * EC => EC / AC = 1 / (m + 1) => BF / BC = 1 / (m + 1) => FC / BC = m / (m + 1)
        # AK / AB = FC / BC = m / (m + 1)
        ab = (m + 1) * random.choice([4, 6])
        ak = (m * ab) // (m + 1)
        kq_str = str(ak)

        noidungcauhoi = ("""Cho $\\Delta ABC$ có $AB = %s\\text{ cm}$. Trên cạnh $AC$ lấy điểm $E$ sao cho $AE = %s EC$. Đường thẳng qua $E$ song song với $AB$ cắt cạnh $BC$ tại $F$. Đường thẳng qua $F$ song song với $AC$ cắt cạnh $AB$ tại $K$ (như hình vẽ bên dưới). Độ dài đoạn thẳng $AK$ bằng bao nhiêu $\\text{cm}$?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.5,0);
\\coordinate (E) at ($(A)!0.75!(C)$);
\\coordinate (F) at ($(B)!0.25!(C)$);
\\coordinate (K) at ($(A)!0.75!(B)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (E)--(F) (F)--(K);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (F) circle (1pt) node[below] {$F$};
\\fill (K) circle (1pt) node[left] {$K$};
\\end{tikzpicture}
\\end{center}"""
                         % (ab, m))

        loigiai = ("""Vì $AE = %s EC$ nên $AC = AE + EC = %s EC + EC = %s EC$, suy ra $\\dfrac{AE}{AC} = \\dfrac{%s}{%s}$. \\\\
Xét $\\Delta ABC$ có $EF // AB$, theo định lí Thalès trong tam giác ta có: $\\dfrac{CF}{CB} = \\dfrac{AE}{AC} = \\dfrac{%s}{%s}$. \\\\
Xét $\\Delta ABC$ có $FK // AC$, theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{AK}{AB} = \\dfrac{CF}{CB} = \\dfrac{%s}{%s} \\Rightarrow AK = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$. \\\\
Vậy độ dài đoạn thẳng $AK$ bằng $%s\\text{ cm}$."""
                   % (m, m, m + 1, m, m + 1, m, m + 1,
                      m, m + 1, m, m + 1, ab, ak, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
