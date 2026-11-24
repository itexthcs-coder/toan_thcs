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

def bt_dang6_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.0,2.8);
\\coordinate (B) at (4.8,2.8);
\\coordinate (C) at (3.8,0);
\\coordinate (D) at (0,0);
\\coordinate (O) at (2.4,1.4);
\\coordinate (E) at ($(O)!0.5!(D)$);
\\coordinate (F) at ($(O)!0.5!(B)$);
\\coordinate (M) at ($(C)!0.5!(D)$);
\\coordinate (N) at ($(A)!0.5!(B)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D) (A)--(M) (C)--(N);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (O) circle (1pt) node[above] {$O$};
\\fill (E) circle (1pt) node[below right] {$E$};
\\fill (F) circle (1pt) node[above left] {$F$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[above] {$N$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Gọi $E, F$ lần lượt là trung điểm của $OD$ và $OB$. Tia $AE$ cắt cạnh $CD$ tại $M$, tia $CF$ cắt cạnh $AB$ tại $N$ (như hình vẽ).\\
a) Chứng minh $DE = EF = FB$.\\
b) Chứng minh $EM$ là đường trung bình của tam giác $DNC$ và $FN$ là đường trung bình của tam giác $BMA$.\\
c) Chứng minh $M$ là trung điểm của $CD$, $N$ là trung điểm của $AB$ và tứ giác $AMCN$ là hình bình hành.%s''' % (hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $ABCD$ là hình bình hành nên $O$ là trung điểm của $AC$ và $BD$, suy ra $OD = OB$.\\
Lại có $E, F$ lần lượt là trung điểm của $OD$ và $OB$ nên $DE = EO = \\dfrac{1}{2}OD$ và $OF = FB = \\dfrac{1}{2}OB$.\\
Do đó $DE = EO = OF = FB$, suy ra $EF = EO + OF = DE = FB$, hay $DE = EF = FB$.
\\item Xét tứ giác $AECF$ có hai đường chéo $AC$ và $EF$ cắt nhau tại trung điểm $O$ của mỗi đường ($OA = OC$ và $OE = OF$) nên $AECF$ là hình bình hành.\\
Suy ra $AE // CF$, hay $EM // NC$ và $FN // AM$.\\
Xét tam giác $DNC$ có $E$ là trung điểm của $DF$ ($DE = EF$) và $EM // NC$ nên $M$ là trung điểm của $CD$, do đó $EM$ là đường trung bình của tam giác $DNC$.\\
Tương tự, xét tam giác $BMA$ có $F$ là trung điểm của $BE$ ($BF = FE$) và $FN // AM$ nên $N$ là trung điểm của $AB$, do đó $FN$ là đường trung bình của tam giác $BMA$.
\\item Theo chứng minh trên, $M$ là trung điểm của $CD$ và $N$ là trung điểm của $AB$.\\
Suy ra $AN = \\dfrac{1}{2}AB$ và $CM = \\dfrac{1}{2}CD$. Mà $AB // CD$ và $AB = CD$ nên $AN // CM$ và $AN = CM$.\\
Vậy tứ giác $AMCN$ là hình bình hành.
\\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
