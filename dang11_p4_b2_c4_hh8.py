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

def bt_dang11_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.6,3.4);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.6,0);
\\coordinate (H) at (1.6,1.2);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (N) at ($(A)!0.5!(C)$);
\\coordinate (P) at ($(H)!0.5!(A)$);
\\coordinate (Q) at ($(H)!0.5!(B)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N)--(P)--(Q)--cycle;
\\draw[line width=1pt, dashed] (A)--(H) (B)--(H) (C)--(H);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (Q) circle (1pt) node[above left] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tam giác $ABC$ nhọn có các đường cao $BD$ và $CE$ cắt nhau tại trực tâm $H$. Gọi $M, N, P, Q$ lần lượt là trung điểm của $BC, AC, HA, HB$ (như hình vẽ).\\
a) Chứng minh $MN // AB$ và $PQ // AB$.\\
b) Chứng minh $NP // CH$ và $MQ // CH$.\\
c) Chứng minh tứ giác $MNPQ$ là hình chữ nhật.%s''' % (hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $ABC$ có $M, N$ lần lượt là trung điểm của $BC$ và $AC$ nên $MN$ là đường trung bình của tam giác $ABC$, suy ra $MN // AB$ và $MN = \\dfrac{1}{2}AB$.\\
Xét tam giác $HAB$ có $P, Q$ lần lượt là trung điểm của $HA$ và $HB$ nên $PQ$ là đường trung bình của tam giác $HAB$, suy ra $PQ // AB$ và $PQ = \\dfrac{1}{2}AB$.
\\item Xét tam giác $HAC$ có $P, N$ lần lượt là trung điểm của $HA$ và $AC$ nên $NP$ là đường trung bình của tam giác $HAC$, suy ra $NP // CH$.\\
Xét tam giác $HBC$ có $Q, M$ lần lượt là trung điểm của $HB$ và $BC$ nên $MQ$ là đường trung bình của tam giác $HBC$, suy ra $MQ // CH$.
\\item Từ câu a), ta có $MN // PQ$ và $MN = PQ$ (cùng bằng $\\dfrac{1}{2}AB$) nên tứ giác $MNPQ$ là hình bình hành.\\
Mặt khác, vì $H$ là trực tâm của tam giác $ABC$ nên $CH \\perp AB$.\\
Lại có $NP // CH$ và $MN // AB$ nên $NP \\perp MN$, hay $\\widehat{MNP} = 90^\\circ$.\\
Hình bình hành $MNPQ$ có một góc vuông nên $MNPQ$ là hình chữ nhật.
\\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
