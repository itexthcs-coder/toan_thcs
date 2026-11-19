# -*- coding: utf-8 -*-
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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang3_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = random.randint(3, 9)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.8);
\\coordinate (B) at (150:1.8);
\\coordinate (C) at (210:1.8);
\\coordinate (D) at (270:1.8);
\\coordinate (E) at (330:1.8);
\\coordinate (F) at (30:1.8);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--(E)--(F)--cycle;
\\draw[line width=1pt, dashed] (A)--(C)--(E)--cycle (B)--(D)--(F)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[left] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (F) circle (1pt) node[right] {$F$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho lục giác đều $ABCDEF$ nội tiếp đường tròn $(O)$ bán kính $R = %s\\text{ cm}$ (như hình vẽ). Kẻ hai tam giác đều $ACE$ và $BDF$. Gọi $M, N, P, Q, R, S$ lần lượt là giao điểm của các cặp đường chéo $(AC, BF)$, $(AC, BD)$, $(CE, BD)$, $(CE, DF)$, $(EA, DF)$ và $(EA, BF)$. Chứng minh rằng $MNPQRS$ là một lục giác đều. %s'''
                         % (r, hinh_tikz))

        loigiai = ('''Lục giác đều $ABCDEF$ nội tiếp đường tròn $(O)$ chia đường tròn thành $6$ cung nhỏ bằng nhau, mỗi cung có số đo bằng $\\frac{360^\\circ}{6} = 60^\\circ$. \\
Xét $\\triangle ABM$, ta có các góc nội tiếp $\\widehat{BAM} = \\widehat{BAC} = \\frac{1}{2}\\text{sđ}\\wideparen{BC} = 30^\\circ$ và $\\widehat{ABM} = \\widehat{ABF} = \\frac{1}{2}\\text{sđ}\\wideparen{AF} = 30^\\circ$. \\
Do đó $\\triangle ABM$ cân tại $M$ và $\\widehat{AMB} = 180^\\circ - 30^\\circ - 30^\\circ = 120^\\circ$. \\
Suy ra góc trong $\\widehat{SMN}$ của đa giác $MNPQRS$ (đối đỉnh với $\\widehat{AMB}$) cũng bằng $120^\\circ$. \\
Chứng minh hoàn toàn tương tự cho các tam giác cân bằng nhau $\\triangle ABM = \\triangle BCN = \\triangle CDP = \\triangle DEQ = \\triangle EFR = \\triangle FAS$ (g.c.g), ta có: \\
- Các góc trong tại các đỉnh $M, N, P, Q, R, S$ của đa giác $MNPQRS$ đều bằng $120^\\circ$. \\
- Các đoạn thẳng $AM = MB = BN = NC = CP = PD = DQ = QE = ER = RF = FS = SA$. \\
Mà $AC = AM + MN + NC$ và các cạnh của hai tam giác đều $ACE, BDF$ đều bằng nhau ($AC = CE = EA = BD = DF = FB$), nên ta suy ra:
$$MN = NP = PQ = QR = RS = SM.$$
Vậy đa giác lồi $MNPQRS$ có tất cả các cạnh bằng nhau và các góc bằng nhau nên là một lục giác đều.''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
