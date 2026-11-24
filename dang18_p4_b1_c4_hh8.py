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


def bt_dang18_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cd_10 = random.choice([15, 16, 18])
        ed_10 = random.choice([15, 20])
        k = random.choice([18, 20, 25])
        eb_10 = ed_10 * k
        bd_10 = eb_10 - ed_10
        ab_10 = cd_10 * k

        def s10(v):
            return str(v / 10).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ("""Để xác định chiều cao $AB$ của một tháp truyền hình đứng vuông góc với mặt sân bằng phẳng, một nhóm học sinh cắm thẳng đứng một cọc tiêu $CD$ cao $%s\\text{ m}$ cách chân tháp $B$ một khoảng $BD = %s\\text{ m}$. Sau đó, một bạn học sinh lùi ra xa theo đường thẳng $BD$ đến vị trí $E$ (sao cho $D$ nằm giữa $B$ và $E$) thì thấy đỉnh cọc $C$ che khuất vừa đúng đỉnh tháp $A$ (ba điểm $E$, $C$, $A$ thẳng hàng) như hình vẽ bên dưới. Đo khoảng cách từ vị trí đứng $E$ đến chân cọc $D$ được $ED = %s\\text{ m}$ (coi mắt người quan sát đặt sát mặt đất tại $E$). Tính chiều cao $AB$ của tháp truyền hình.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (A) at (0,3.2);
\\coordinate (E) at (4.8,0);
\\coordinate (D) at (3.6,0);
\\coordinate (C) at (3.6,0.8);
\\draw[line width=1pt] (A)--(B)--(E)--cycle (C)--(D);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\draw[line width=1pt] (3.6,0.25)--(3.85,0.25)--(3.85,0);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (E) circle (1pt) node[below right] {$E$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\end{tikzpicture}
\\end{center}"""
                         % (s10(cd_10), s10(bd_10), s10(ed_10)))

        loigiai = ("""Ta có khoảng cách từ vị trí đứng $E$ đến chân tháp $B$ là: \\\\
$EB = ED + DB = %s + %s = %s\\text{ (m)}$. \\\\
Vì tháp truyền hình $AB$ và cọc tiêu $CD$ cùng thẳng đứng vuông góc với mặt đất $EB$ nên $CD // AB$. \\\\
Xét $\\Delta EAB$ có $CD // AB$ ($C \\in EA$, $D \\in EB$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{CD}{AB} = \\dfrac{ED}{EB}$. \\\\
Thay $CD = %s\\text{ m}$, $ED = %s\\text{ m}$, $EB = %s\\text{ m}$ vào hệ thức trên, ta được: \\\\
$\\dfrac{%s}{AB} = \\dfrac{%s}{%s} \\Rightarrow AB = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (m)}$. \\\\
Vậy chiều cao của tháp truyền hình bằng $%s\\text{ m}$."""
                   % (s10(ed_10), s10(bd_10), s10(eb_10),
                      s10(cd_10), s10(ed_10), s10(eb_10),
                      s10(cd_10), s10(ed_10), s10(eb_10), s10(cd_10), s10(eb_10), s10(ed_10), s10(ab_10),
                      s10(ab_10)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
