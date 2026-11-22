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


def bt_dang20_p4_b4_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (0,1.8);
\\coordinate (C) at (2.4,0);
\\coordinate (D) at (-1.8,0);
\\coordinate (E) at (-1.8,1.8);
\\coordinate (F) at (0,-2.4);
\\coordinate (G) at (2.4,-2.4);
\\coordinate (M) at (0.3,-0.3);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(B)--(E)--(D)--cycle (A)--(C)--(G)--(F)--cycle (E)--(G) (D)--(F) (A)--(M);
\\fill (A) circle (1pt) node[above right] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[above left] {$E$};
\\fill (F) circle (1pt) node[below left] {$F$};
\\fill (G) circle (1pt) node[below right] {$G$};
\\fill (M) circle (1pt) node[below right] {$M$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho $\\triangle ABC$ vuông tại $A$. Dựng ở phía ngoài $\\triangle ABC$ các hình chữ nhật $ABED$ và $ACGF$ sao cho $AB = AD$ và $AC = AF$. \\\\
a) Chứng minh ba điểm $D, A, C$ thẳng hàng và ba điểm $B, A, F$ thẳng hàng. \\\\
b) Gọi $M$ là trung điểm của đoạn thẳng $EG$. Chứng minh $AM \\perp BC$. %s'''
                         % (hinh_ve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $ABED$ là hình chữ nhật nên $\\widehat{DAB} = 90^\\circ$. \\\\
Lại có $\\widehat{BAC} = 90^\\circ$ ($\\triangle ABC$ vuông tại $A$) và tia $AB$ nằm giữa hai tia $AD, AC$ nên: \\\\
$\\widehat{DAC} = \\widehat{DAB} + \\widehat{BAC} = 90^\\circ + 90^\\circ = 180^\\circ$, suy ra ba điểm $D, A, C$ thẳng hàng. \\\\
Tương tự, vì $ACGF$ là hình chữ nhật nên $\\widehat{CAF} = 90^\\circ$, do đó $\\widehat{BAF} = \\widehat{BAC} + \\widehat{CAF} = 90^\\circ + 90^\\circ = 180^\\circ$, suy ra ba điểm $B, A, F$ thẳng hàng.
\\item Vì $ABED$ và $ACGF$ là các hình chữ nhật nên $\\widehat{EAD} = 90^\\circ$ và $\\widehat{CAG} = 90^\\circ$. \\\\
Mà $D, A, C$ thẳng hàng nên $\\widehat{EAG} = \\widehat{EAC} - \\widehat{GAC} = 180^\\circ - 90^\\circ = 90^\\circ$, suy ra $\\triangle EAG$ vuông tại $A$. \\\\
Xét $\\triangle EAG$ vuông tại $A$ có $AM$ là đường trung tuyến ứng với cạnh huyền $EG$ ($M$ là trung điểm của $EG$) nên $AM = \\dfrac{1}{2}EG = ME$, suy ra $\\triangle MAE$ cân tại $M$, do đó $\\widehat{MAE} = \\widehat{MEA}$. (1) \\\\
Mặt khác, xét hai tam giác vuông $\\triangle EAG$ và $\\triangle ABC$ có: \\\\
$AE = AD = AB$ (do $ABED$ là hình chữ nhật có $AB = AD$) và $AG = AF = AC$ (do $ACGF$ là hình chữ nhật có $AC = AF$). \\\\
Suy ra $\\triangle EAG = \\triangle ABC$ (hai cạnh góc vuông), do đó $\\widehat{MEA} = \\widehat{ABC}$. (2) \\\\
Gọi $H$ là giao điểm của tia $MA$ và cạnh $BC$. Vì $B, A, F$ thẳng hàng nên $\\widehat{HAB} + \\widehat{MAE} = 90^\\circ$. (3) \\\\
Từ (1), (2), (3) suy ra $\\widehat{HAB} + \\widehat{ABC} = 90^\\circ$. \\\\
Xét $\\triangle ABH$ có $\\widehat{AHB} = 180^\\circ - (\\widehat{HAB} + \\widehat{ABC}) = 180^\\circ - 90^\\circ = 90^\\circ$. \\\\
Vậy $AM \\perp BC$.
\\end{enumEX}''')
    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
