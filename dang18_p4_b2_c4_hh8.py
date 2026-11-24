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

def bt_dang18_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bc = random.choice([6, 8, 10, 12])
        h_tong = random.choice([4, 6, 8])
        mn = bc // 2
        pq = bc / 4 if bc % 4 != 0 else bc // 4
        h_thang = h_tong / 4 if h_tong % 4 != 0 else h_tong // 4

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (2.2,3.4);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.4,0);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(A)!0.5!(C)$);
\\coordinate (P) at ($(A)!0.5!(M)$);
\\coordinate (Q) at ($(A)!0.5!(N)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N) (P)--(Q);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (Q) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một khung giàn giáo trang trí sự kiện có dạng tam giác cân $ABC$ tại $A$ với chiều rộng chân đế $BC = %s\\text{ m}$ và chiều cao tổng thể của khung bằng $%s\\text{ m}$. Để tăng độ chịu lực, kỹ sư thiết kế lắp đặt thanh giằng ngang tầng một $MN$ nối trung điểm của $AB$ và $AC$, và tiếp tục lắp thanh giằng ngang tầng hai $PQ$ nối trung điểm của $AM$ và $AN$ (như hình vẽ).\\
a) Tính chiều dài thanh giằng ngang $MN$ và thanh giằng ngang $PQ$.\\
b) Chứng minh tứ giác $MNPQ$ là hình thang cân và tính chiều cao của khung thang $MNPQ$.%s''' % (fmt_num(bc), fmt_num(h_tong), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $ABC$ có $M, N$ lần lượt là trung điểm của $AB$ và $AC$ nên $MN$ là đường trung bình của tam giác $ABC$, suy ra $MN = \\dfrac{1}{2}BC = \\dfrac{1}{2} \\cdot %s = %s\\text{ m}$.\\
Xét tam giác $AMN$ có $P, Q$ lần lượt là trung điểm của $AM$ và $AN$ nên $PQ$ là đường trung bình của tam giác $AMN$, suy ra $PQ = \\dfrac{1}{2}MN = \\dfrac{1}{2} \\cdot %s = %s\\text{ m}$.
\\item Vì $PQ$ là đường trung bình của tam giác $AMN$ nên $PQ // MN$, suy ra tứ giác $MNPQ$ là hình thang.\\
Mặt khác, tam giác $ABC$ cân tại $A$ nên $\\widehat{B} = \\widehat{C}$, mà $MN // BC$ nên $\\widehat{AMN} = \\widehat{B}$ và $\\widehat{ANM} = \\widehat{C}$ (đồng vị), suy ra $\\widehat{AMN} = \\widehat{ANM}$ (hay $\\widehat{PMN} = \\widehat{QNM}$).\\
Hình thang $MNPQ$ có hai góc kề một đáy bằng nhau nên là hình thang cân.\\
Kẻ đường cao $AH = %s\\text{ m}$ của tam giác $ABC$ ($H \\in BC$), cắt $MN$ tại $I$ và cắt $PQ$ tại $K$.\\
Vì $MN$ là đường trung bình của tam giác $ABC$ nên $I$ là trung điểm $AH$, suy ra $AI = \\dfrac{1}{2}AH = %s\\text{ m}$.\\
Vì $PQ$ là đường trung bình của tam giác $AMN$ nên $K$ là trung điểm $AI$, suy ra chiều cao của khung thang $MNPQ$ là $KI = \\dfrac{1}{2}AI = %s\\text{ m}$.
\\end{enumEX}''' % (fmt_num(bc), fmt_num(mn), fmt_num(mn), fmt_num(pq), fmt_num(h_tong), fmt_num(h_tong / 2), fmt_num(h_thang)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
