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


def bt_dang15_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Tam giac ABC vuong tai A: AB = 15, AC = 20 => BC = 25, duong cao AH = 12.
        # Hinh chu nhat MNPQ co MN = 10 tren BC => PQ = 10 // BC => chieu rong MQ = AH * (1 - PQ/BC) = 12 * (1 - 10/25) = 7.2
        k = random.choice([1, 2])
        ab = 15 * k
        ac = 20 * k
        bc = 25 * k
        ah = 12 * k
        mn = 10 * k
        mq_val = Rational(ah * (bc - mn), bc)
        mq_s = str(int(mq_val)) if mq_val.is_Integer else str(float(mq_val)).replace('.', ',')

        noidungcauhoi = ("""Cho $\\Delta ABC$ vuông tại $A$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Một hình chữ nhật $MNPQ$ nội tiếp trong tam giác sao cho cạnh $MN$ nằm trên cạnh huyền $BC$, đỉnh $P \\in AC$ và đỉnh $Q \\in AB$ (như hình vẽ bên dưới). Biết chiều dài $MN = %s\\text{ cm}$, tính chiều rộng $MQ$ của hình chữ nhật $MNPQ$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (C) at (5,0);
\\coordinate (A) at (1.8,2.4);
\\coordinate (H) at (1.8,0);
\\coordinate (M) at (1.08,0);
\\coordinate (N) at (3.08,0);
\\coordinate (Q) at (1.08,1.44);
\\coordinate (P) at (3.08,1.44);
\\coordinate (I) at (1.8,1.44);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N)--(P)--(Q)--cycle;
\\draw[line width=1pt, dashed] (A)--(H);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\fill (Q) circle (1pt) node[above left] {$Q$};
\\fill (P) circle (1pt) node[above right] {$P$};
\\fill (I) circle (1pt) node[above right] {$I$};
\\end{tikzpicture}
\\end{center}"""
                         % (ab, ac, mn))

        loigiai = ("""Áp dụng định lí Pythagore cho $\\Delta ABC$ vuông tại $A$, ta có: \\\\
$BC = \\sqrt{AB^2 + AC^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$. \\\\
Kẻ đường cao $AH$ của $\\Delta ABC$ ($H \\in BC$), cắt $PQ$ tại $I$. Khi đó $AH = \\dfrac{AB \\cdot AC}{BC} = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$. \\\\
Vì $MNPQ$ là hình chữ nhật nên $PQ = MN = %s\\text{ cm}$, $PQ // BC$ và $IH = MQ$. \\\\
Xét $\\Delta ABC$ có $PQ // BC$, theo định lí Thalès trong tam giác ta có: $\\dfrac{AQ}{AB} = \\dfrac{PQ}{BC} = \\dfrac{%s}{%s} = \\dfrac{2}{5}$. \\\\
Xét $\\Delta ABH$ có $QI // BH$ (vì $PQ // BC$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{AI}{AH} = \\dfrac{AQ}{AB} = \\dfrac{2}{5} \\Rightarrow AI = \\dfrac{2}{5} \\cdot %s = %s\\text{ (cm)}$. \\\\
Vậy chiều rộng $MQ$ của hình chữ nhật $MNPQ$ là: $MQ = IH = AH - AI = %s - %s = %s\\text{ (cm)}$."""
                   % (ab, ac, bc,
                      ab, ac, bc, ah,
                      mn,
                      mn, bc,
                      ah, str(float(Rational(2 * ah, 5))).rstrip('0').rstrip('.').replace('.', ','),
                      ah, str(float(Rational(2 * ah, 5))).rstrip('0').rstrip('.').replace('.', ','), mq_s))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
