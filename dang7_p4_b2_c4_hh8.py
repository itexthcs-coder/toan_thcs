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

def bt_dang7_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,3.4);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.4,3.4);
\\coordinate (D) at (0,2.0);
\\coordinate (E) at (1.4,3.4);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (N) at ($(C)!0.5!(E)$);
\\coordinate (P) at ($(E)!0.5!(D)$);
\\coordinate (Q) at ($(D)!0.5!(B)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (D)--(E) (M)--(N)--(P)--(Q)--cycle;
\\draw[line width=1pt, dashed] (B)--(E) (C)--(D);
\\draw[line width=1pt] (0,3.1)--(0.3,3.1)--(0.3,3.4);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[above] {$E$};
\\fill (M) circle (1pt) node[below right] {$M$};
\\fill (N) circle (1pt) node[above right] {$N$};
\\fill (P) circle (1pt) node[above left] {$P$};
\\fill (Q) circle (1pt) node[left] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tam giác $ABC$ vuông cân tại $A$. Trên các cạnh $AB$ và $AC$ lần lượt lấy các điểm $D$ và $E$ sao cho $AD = AE$. Gọi $M, N, P, Q$ lần lượt là trung điểm của $BC, CE, ED, DB$ (như hình vẽ).\\
a) Chứng minh tứ giác $MNPQ$ là hình bình hành.\\
b) Chứng minh $BE = CD$ và $BE \\perp CD$.\\
c) Chứng minh tứ giác $MNPQ$ là hình vuông.%s''' % (hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $CBE$ có $M, N$ lần lượt là trung điểm của $BC$ và $CE$ nên $MN$ là đường trung bình của tam giác $CBE$, suy ra $MN // BE$ và $MN = \\dfrac{1}{2}BE$.\\
Xét tam giác $DBE$ có $Q, P$ lần lượt là trung điểm của $DB$ và $DE$ nên $QP$ là đường trung bình của tam giác $DBE$, suy ra $QP // BE$ và $QP = \\dfrac{1}{2}BE$.\\
Do đó $MN // QP$ và $MN = QP$, suy ra tứ giác $MNPQ$ là hình bình hành.
\\item Xét $\\Delta ABE$ và $\\Delta ACD$ có $AB = AC$ (do tam giác $ABC$ vuông cân tại $A$), $\\widehat{BAE} = \\widehat{CAD} = 90^\\circ$, $AE = AD$ (giả thiết).\\
Suy ra $\\Delta ABE = \\Delta ACD$ (c.g.c), do đó $BE = CD$ và $\\widehat{ABE} = \\widehat{ACD}$.\\
Gọi $K$ là giao điểm của $BE$ và $CD$. Trong tam giác $ABC$ vuông tại $A$, ta có $\\widehat{ABC} + \\widehat{ACB} = 90^\\circ$, suy ra $\\widehat{KBC} + \\widehat{KCB} = (\\widehat{ABC} - \\widehat{ABE}) + (\\widehat{ACB} + \\widehat{ACD}) = 90^\\circ$.\\
Do đó $\\widehat{BKC} = 90^\\circ$, hay $BE \\perp CD$.
\\item Xét tam giác $BCD$ có $M, Q$ lần lượt là trung điểm của $BC$ và $BD$ nên $MQ$ là đường trung bình của tam giác $BCD$, suy ra $MQ // CD$ và $MQ = \\dfrac{1}{2}CD$.\\
Vì $BE = CD$ nên $MN = MQ$, hình bình hành $MNPQ$ có hai cạnh kề bằng nhau nên là hình thoi.\\
Mặt khác, $MN // BE$, $MQ // CD$ và $BE \\perp CD$ nên $MN \\perp MQ$, hay $\\widehat{QMN} = 90^\\circ$.\\
Hình thoi $MNPQ$ có một góc vuông nên $MNPQ$ là hình vuông.
\\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
