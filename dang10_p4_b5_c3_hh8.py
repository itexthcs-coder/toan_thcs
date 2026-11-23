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


def bt_dang10_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh = random.choice([80, 100, 120, 140, 160])
        tong_val = 6 * canh + 2 * canh * math.sqrt(2)
        number = Decimal(float(tong_val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (2.6,2.6);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at (1.3,2.6);
\\coordinate (N) at (2.6,1.3);
\\coordinate (P) at (1.3,0);
\\coordinate (Q) at (0,1.3);
\\coordinate (O) at (1.3,1.3);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N)--(P)--(Q)--cycle (M)--(P) (N)--(Q);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[below] {$P$};
\\fill (Q) circle (1pt) node[left] {$Q$};
\\fill (O) circle (1pt) node[below right] {$O$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một khung cửa sổ trang trí bằng gỗ có dạng hình vuông $ABCD$ cạnh $%s\\text{ cm}$. Người thợ mộc nối trung điểm bốn cạnh $AB, BC, CD, DA$ lần lượt là $M, N, P, Q$ để tạo thành một khung hoa văn bên trong, đồng thời lắp hai thanh nẹp chéo $MP$ và $NQ$ cắt nhau tại $O$. \\\\
a) Chứng minh khung hoa văn $MNPQ$ là một hình vuông. \\\\
b) Tính tổng chiều dài các thanh gỗ cần dùng để làm toàn bộ khung viền ngoài $ABCD$, khung hoa văn $MNPQ$ và hai thanh nẹp chéo $MP, NQ$ (làm tròn kết quả đến hàng đơn vị của xăng-ti-mét).%s'''
                         % (canh, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Vì $ABCD$ là hình vuông nên $AC = BD$ và $AC \\perp BD$.\\\\
Áp dụng tính chất đường trung bình của tam giác, ta có:\\\\
$MN = PQ = \\dfrac{AC}{2}$ và $MN // PQ // AC$;\\\\
$NP = QM = \\dfrac{BD}{2}$ và $NP // QM // BD$.\\\\
Suy ra $MN = NP = PQ = QM$ nên tứ giác $MNPQ$ là hình thoi.\\\\
Lại có $AC \\perp BD$, $MN // AC$ và $NP // BD$ nên $MN \\perp NP$, tức là $\\widehat{MNP} = 90^\\circ$.\\\\
Hình thoi $MNPQ$ có một góc vuông nên là hình vuông.
\\item Độ dài khung viền ngoài $ABCD$ là $4 \\cdot %s = %s\\text{ (cm)}$.\\\\
Áp dụng định lí Pythagore vào $\\Delta ABC$ vuông tại $B$, ta có đường chéo $AC = BD = %s\\sqrt{2}\\text{ (cm)}$.\\\\
Cạnh của hình vuông $MNPQ$ là $MN = \\dfrac{AC}{2} = %s\\sqrt{2}\\text{ (cm)}$, suy ra chu vi khung hoa văn $MNPQ$ là $4 \\cdot %s\\sqrt{2} = %s\\sqrt{2}\\text{ (cm)}$.\\\\
Hai thanh nẹp chéo $MP$ và $NQ$ của hình vuông $MNPQ$ có độ dài bằng nhau và bằng cạnh hình vuông $ABCD$: $MP = NQ = %s\\text{ cm}$, nên tổng độ dài hai nẹp chéo là $2 \\cdot %s = %s\\text{ (cm)}$.\\\\
Vậy tổng chiều dài các thanh gỗ cần dùng là:\\\\
$L = %s + %s\\sqrt{2} + %s = %s + %s\\sqrt{2} \\approx %s\\text{ (cm)}$.
\\end{enumEX} \n'''
                   % (canh, 4 * canh, canh, canh // 2, canh // 2, 2 * canh, canh, canh, 2 * canh,
                      4 * canh, 2 * canh, 2 * canh, 6 * canh, 2 * canh, kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
