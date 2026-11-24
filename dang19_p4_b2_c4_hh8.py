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

def bt_dang19_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([10, 12, 14, 16, 18])
        cd = ab + random.choice([6, 8, 10, 12])
        mi = cd // 2
        in_len = ab // 2
        mn = mi + in_len

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.0,2.8);
\\coordinate (B) at (3.2,2.8);
\\coordinate (C) at (4.8,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at ($(A)!0.5!(D)$);
\\coordinate (N) at ($(B)!0.5!(C)$);
\\coordinate (I) at ($(A)!0.5!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N) (A)--(C);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (I) circle (1pt) node[above right] {$I$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một nhịp cầu vượt dành cho người đi bộ có mặt cắt bên dạng hình thang cân $ABCD$ ($AB // CD$), trong đó mặt sàn cầu trên dài $AB = %s\\text{ m}$ và khoảng cách giữa hai mố cầu dưới dài $CD = %s\\text{ m}$. Kỹ sư bố trí một thanh dầm đỡ ngang $MN$ nối trung điểm $M$ của $AD$ và trung điểm $N$ của $BC$. Đường chéo giằng chịu lực $AC$ cắt thanh dầm ngang $MN$ tại điểm $I$ (như hình vẽ).\\
a) Chứng minh $I$ là trung điểm của đường chéo $AC$ và tính độ dài hai đoạn $MI$, $IN$.\\
b) Tính chiều dài tổng cộng của thanh dầm đỡ ngang $MN$.%s''' % (fmt_num(ab), fmt_num(cd), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $MN$ nối trung điểm hai cạnh bên $AD$ và $BC$ của hình thang $ABCD$ nên $MN // AB // CD$.\\
Xét tam giác $ADC$, đường thẳng $MI$ đi qua trung điểm $M$ của cạnh $AD$ và song song với cạnh $CD$ nên đi qua trung điểm $I$ của cạnh $AC$.\\
Khi đó $MI$ là đường trung bình của tam giác $ADC$, suy ra $MI = \\dfrac{1}{2}CD = \\dfrac{1}{2} \\cdot %s = %s\\text{ m}$.\\
Xét tam giác $ABC$ có $I$ là trung điểm của $AC$ và $N$ là trung điểm của $BC$ nên $IN$ là đường trung bình của tam giác $ABC$, suy ra $IN = \\dfrac{1}{2}AB = \\dfrac{1}{2} \\cdot %s = %s\\text{ m}$.
\\item Vì điểm $I$ nằm giữa hai điểm $M$ và $N$ nên chiều dài tổng cộng của thanh dầm đỡ ngang $MN$ là:\\
$MN = MI + IN = %s + %s = %s\\text{ m}$.
\\end{enumEX}''' % (fmt_num(cd), fmt_num(mi), fmt_num(ab), fmt_num(in_len), fmt_num(mi), fmt_num(in_len), fmt_num(mn)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
