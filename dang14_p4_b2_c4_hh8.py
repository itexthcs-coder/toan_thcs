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

def bt_dang14_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bc = random.choice([10, 12, 14, 16, 18, 20])
        ma = bc // 2

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (A) at (1.0,1.9);
\\coordinate (D) at (3.6,2.1);
\\coordinate (N) at ($(A)!0.5!(D)$);
\\coordinate (P) at ($(A)!0.5!(B)$);
\\coordinate (Q) at ($(D)!0.5!(C)$);
\\draw[line width=1pt] (B)--(A)--(C)--cycle (B)--(D)--(C) (A)--(D) (M)--(A) (M)--(D) (M)--(N) (M)--(P) (M)--(Q);
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (D) circle (1pt) node[above right] {$D$};
\\fill (N) circle (1pt) node[above] {$N$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (Q) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hai tam giác vuông $ABC$ và $DBC$ cùng vuông tại $A$ và $D$ nằm trên cùng một nửa mặt phẳng bờ $BC$ ($BC = %s\\text{ cm}$). Gọi $M, N$ lần lượt là trung điểm của $BC$ và $AD$ (như hình vẽ).\\
a) Tính độ dài các đoạn thẳng $MA$ và $MD$.\\
b) Chứng minh $MN \\perp AD$.\\
c) Gọi $P, Q$ lần lượt là trung điểm của $AB$ và $DC$. Chứng minh $MP \\perp AB$ và $MQ \\perp DC$.%s''' % (fmt_num(bc), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong tam giác $ABC$ vuông tại $A$, $MA$ là đường trung tuyến ứng với cạnh huyền $BC$ nên $MA = \\dfrac{1}{2}BC = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.\\
Tương tự, trong tam giác $DBC$ vuông tại $D$, $MD$ là đường trung tuyến ứng với cạnh huyền $BC$ nên $MD = \\dfrac{1}{2}BC = %s\\text{ cm}$.
\\item Theo câu a), ta có $MA = MD$ nên tam giác $MAD$ cân tại $M$.\\
Mà $N$ là trung điểm của cạnh đáy $AD$ nên đường trung tuyến $MN$ đồng thời là đường cao của tam giác $MAD$, suy ra $MN \\perp AD$.
\\item Xét tam giác $ABC$ có $M, P$ lần lượt là trung điểm của $BC$ và $AB$ nên $MP$ là đường trung bình của tam giác $ABC$, suy ra $MP // AC$. Mà $AC \\perp AB$ (do tam giác $ABC$ vuông tại $A$) nên $MP \\perp AB$.\\
Tương tự, xét tam giác $DBC$ có $M, Q$ lần lượt là trung điểm của $BC$ và $DC$ nên $MQ$ là đường trung bình của tam giác $DBC$, suy ra $MQ // BD$. Mà $BD \\perp DC$ (do tam giác $DBC$ vuông tại $D$) nên $MQ \\perp DC$.
\\end{enumEX}''' % (fmt_num(bc), fmt_num(ma), fmt_num(ma)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
