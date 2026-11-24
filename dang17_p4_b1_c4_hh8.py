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


def bt_dang17_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab_10 = 36
        ac_10 = 42
        am_10 = 12
        an_10 = 14
        mp_10 = 12
        nq_sai_10 = random.choice([15, 16])
        nq_dung_10 = 14
        lech_10 = nq_sai_10 - nq_dung_10

        def s10(v):
            return str(v / 10).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ("""Một khung giàn giáo chữ A được dựng bởi hai thanh thép chính $AB = %s\\text{ m}$ và $AC = %s\\text{ m}$ giao nhau tại đỉnh $A$ và đặt trên mặt nền phẳng $BC$. Công nhân lắp hai sàn thao tác ngang $MN$ và $PQ$ ($M, P \\in AB$ và $N, Q \\in AC$) như hình vẽ bên dưới. Khi kiểm tra bằng thước đo, kĩ sư giám sát ghi nhận $AM = %s\\text{ m}$, $AN = %s\\text{ m}$, $MP = %s\\text{ m}$ và $NQ = %s\\text{ m}$. \\\\
a) Sàn thao tác $MN$ có song song với mặt nền $BC$ không? Vì sao? \\\\
b) Sàn thao tác $PQ$ có song song với sàn $MN$ không? Nếu chưa song song (giữ nguyên vị trí điểm $P$), cần dịch chuyển điểm $Q$ trên thanh $AC$ một đoạn bằng bao nhiêu mét và theo chiều nào để $PQ // MN$?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.2,0);
\\coordinate (M) at ($(A)!0.3333!(B)$);
\\coordinate (N) at ($(A)!0.3333!(C)$);
\\coordinate (P) at ($(A)!0.6667!(B)$);
\\coordinate (Q) at ($(A)!0.72!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N) (P)--(Q);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (Q) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}"""
                         % (s10(ab_10), s10(ac_10), s10(am_10), s10(an_10), s10(mp_10), s10(nq_sai_10)))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Xét $\\Delta ABC$ có $M \\in AB$, $N \\in AC$, ta có: \\\\
$\\dfrac{AM}{AB} = \\dfrac{%s}{%s} = \\dfrac{1}{3}$ và $\\dfrac{AN}{AC} = \\dfrac{%s}{%s} = \\dfrac{1}{3}$. \\\\
Vì $\\dfrac{AM}{AB} = \\dfrac{AN}{AC} = \\dfrac{1}{3}$ nên sàn thao tác $MN$ song song với mặt nền $BC$ (theo định lí Thalès đảo).
\\item Xét $\\Delta APQ$ có $M \\in AP$, $N \\in AQ$, ta có: $\\dfrac{AM}{MP} = \\dfrac{%s}{%s} = 1$, còn $\\dfrac{AN}{NQ} = \\dfrac{%s}{%s} \\neq 1$. \\\\
Vì $\\dfrac{AM}{MP} \\neq \\dfrac{AN}{NQ}$ nên sàn thao tác $PQ$ không song song với sàn $MN$. \\\\
Để $PQ // MN$, theo định lí Thalès ta phải có $\\dfrac{AN}{NQ} = \\dfrac{AM}{MP} = 1 \\Rightarrow NQ = AN = %s\\text{ m}$. \\\\
Do hiện tại $NQ = %s\\text{ m}$ nên ta cần dịch chuyển điểm $Q$ trên thanh $AC$ hướng về phía đỉnh $A$ (lên trên) một đoạn bằng: $%s - %s = %s\\text{ (m)}$."""
                   % (s10(am_10), s10(ab_10), s10(an_10), s10(ac_10),
                      s10(am_10), s10(mp_10), s10(an_10), s10(nq_sai_10),
                      s10(nq_dung_10), s10(nq_sai_10), s10(nq_sai_10), s10(nq_dung_10), s10(lech_10)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
