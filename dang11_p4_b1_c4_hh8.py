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


def bt_dang11_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_canh = [(12, 18, Rational(36, 5)), (10, 15, Rational(6, 1)), (12, 24, Rational(8, 1)), (15, 30, Rational(10, 1))]
        ab, ac, x_val = random.choice(bo_canh)
        if x_val.is_Integer:
            x_s = str(int(x_val))
        else:
            x_s = str(float(x_val)).replace('.', ',')

        noidungcauhoi = ("""Cho $\\Delta ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Tia phân giác của góc $A$ cắt cạnh $BC$ tại $D$. Qua $D$ kẻ đường thẳng song song với $AC$ cắt $AB$ tại $M$ và kẻ đường thẳng song song với $AB$ cắt $AC$ tại $N$ (như hình vẽ bên dưới). \\\\
a) Chứng minh rằng tứ giác $AMDN$ là hình thoi. \\\\
b) Tính độ dài cạnh của hình thoi $AMDN$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.5,0);
\\coordinate (D) at ($(B)!0.4!(C)$);
\\coordinate (M) at ($(B)!0.4!(A)$);
\\coordinate (N) at ($(C)!0.6!(A)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D) (D)--(M) (D)--(N);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}"""
                         % (ab, ac))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Tứ giác $AMDN$ có $DM // AN$ (vì $DM // AC$) và $DN // AM$ (vì $DN // AB$) nên $AMDN$ là hình bình hành. \\\\
Mặt khác, $AD$ là tia phân giác của $\\widehat{MAN}$ nên hình bình hành $AMDN$ là hình thoi (dấu hiệu nhận biết).
\\item Gọi độ dài cạnh của hình thoi $AMDN$ là $x\\text{ (cm)}$ ($x > 0$), ta có $AM = MD = DN = NA = x\\text{ (cm)}$ và $BM = AB - AM = %s - x\\text{ (cm)}$. \\\\
Xét $\\Delta ABC$ có $MD // AC$, theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{BM}{AB} = \\dfrac{MD}{AC} \\Rightarrow \\dfrac{%s - x}{%s} = \\dfrac{x}{%s}$. \\\\
Suy ra $%s(%s - x) = %s x \\Leftrightarrow %s - %s x = %s x \\Leftrightarrow %s x = %s \\Leftrightarrow x = %s\\text{ (cm)}$. \\\\
Vậy độ dài cạnh của hình thoi $AMDN$ bằng $%s\\text{ cm}$.
\\end{enumEX}"""
                   % (ab, ab, ab, ac,
                      ac, ab, ab, ac * ab, ac, ab, ab + ac, ac * ab, x_s, x_s))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
