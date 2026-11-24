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


def bt_dang13_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        s_abc = 9 * random.choice([10, 12, 15, 20])
        s_amp = s_abc // 9
        s_anq = (4 * s_abc) // 9
        s_mnpq = s_anq - s_amp

        noidungcauhoi = ("""Cho $\\Delta ABC$ có diện tích bằng $%s\\text{ cm}^2$. Trên cạnh $AB$ lấy hai điểm $M$, $N$ sao cho $AM = MN = NB$. Qua $M$ và $N$ lần lượt vẽ các đường thẳng song song với $BC$, cắt cạnh $AC$ tại $P$ và $Q$ (như hình vẽ bên dưới). Tính diện tích của tứ giác $MNPQ$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.5,0);
\\coordinate (M) at ($(A)!0.3333!(B)$);
\\coordinate (P) at ($(A)!0.3333!(C)$);
\\coordinate (N) at ($(A)!0.6667!(B)$);
\\coordinate (Q) at ($(A)!0.6667!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(P) (N)--(Q);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (P) circle (1pt) node[right] {$P$};
\\fill (N) circle (1pt) node[left] {$N$};
\\fill (Q) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}"""
                         % (s_abc))

        loigiai = ("""Vì $AM = MN = NB$ nên $AM = \\dfrac{1}{3} AB$ và $AN = \\dfrac{2}{3} AB$. \\\\
Xét $\\Delta ABC$ có $MP // BC$, theo định lí Thalès trong tam giác ta có: $\\dfrac{AP}{AC} = \\dfrac{AM}{AB} = \\dfrac{1}{3}$. \\\\
Tương tự, với $NQ // BC$, theo định lí Thalès ta có: $\\dfrac{AQ}{AC} = \\dfrac{AN}{AB} = \\dfrac{2}{3}$. \\\\
Ta có: $\\dfrac{S_{\\Delta AMP}}{S_{\\Delta ABC}} = \\dfrac{AM}{AB} \\cdot \\dfrac{AP}{AC} = \\dfrac{1}{3} \\cdot \\dfrac{1}{3} = \\dfrac{1}{9} \\Rightarrow S_{\\Delta AMP} = \\dfrac{1}{9} \\cdot %s = %s\\text{ (cm}^2\\text{)}$. \\\\
Và $\\dfrac{S_{\\Delta ANQ}}{S_{\\Delta ABC}} = \\dfrac{AN}{AB} \\cdot \\dfrac{AQ}{AC} = \\dfrac{2}{3} \\cdot \\dfrac{2}{3} = \\dfrac{4}{9} \\Rightarrow S_{\\Delta ANQ} = \\dfrac{4}{9} \\cdot %s = %s\\text{ (cm}^2\\text{)}$. \\\\
Vậy diện tích của tứ giác $MNPQ$ là: \\\\
$S_{MNPQ} = S_{\\Delta ANQ} - S_{\\Delta AMP} = %s - %s = %s\\text{ (cm}^2\\text{)}$."""
                   % (s_abc, s_amp, s_abc, s_anq, s_anq, s_amp, s_mnpq))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
