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


def bt_dang2_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tam = random.choice(['O', 'I'])

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (105:1.6);
\\coordinate (B) at (200:1.6);
\\coordinate (C) at (-20:1.6);
\\coordinate (M) at (-85:1.6);
\\coordinate (D) at ($(B)!(M)!(C)$);
\\coordinate (E) at ($(A)!(M)!(C)$);
\\coordinate (F) at ($(A)!(M)!(B)$);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (M)--(D) (M)--(E) (M)--(F);
\\draw[line width=1pt, dashed] (F)--(E) (B)--(F) (C)--(E);
\\fill (O) circle (1pt) node[above right] {$%s$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (F) circle (1pt) node[left] {$F$};
\\end{tikzpicture}
\\end{center}''' % (tam))

        noidungcauhoi = ('''Cho tam giác $ABC$ nội tiếp đường tròn $(%s)$ và điểm $M$ nằm trên cung nhỏ $BC$ ($M \\neq B, M \\neq C$). Kẻ $MD \\perp BC$ tại $D$, $ME \\perp AC$ tại $E$ và $MF \\perp AB$ tại $F$. \\\\
a) Chứng minh rằng các tứ giác $MDCE$ và $MDBF$ nội tiếp đường tròn. \\\\
b) Chứng minh rằng $\\widehat{MDE} = \\widehat{MCE}$ và ba điểm $D, E, F$ thẳng hàng.%s''' % (tam, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $MD \\perp BC$ và $ME \\perp AC$ nên $\\widehat{MDC} = \\widehat{MEC} = 90^\\circ$. Gọi $K$ là trung điểm của đoạn thẳng $MC$, các tam giác vuông $MDC$ và $MEC$ có chung cạnh huyền $MC$ nên $KD = KE = KM = KC = \\dfrac{MC}{2}$. Suy ra tứ giác $MDCE$ nội tiếp đường tròn đường kính $MC$.\\\\
Tương tự, vì $MD \\perp BC$ và $MF \\perp AB$ nên $\\widehat{MDB} = \\widehat{MFB} = 90^\\circ$. Gọi $L$ là trung điểm của $MB$, ta có $LD = LF = LM = LB = \\dfrac{MB}{2}$, suy ra tứ giác $MDBF$ nội tiếp đường tròn đường kính $MB$.
\\item Vì tứ giác $MDCE$ nội tiếp nên $\\widehat{MDE} + \\widehat{MCE} = 180^\\circ$ (nếu $E$ nằm trên tia đối của $CA$) hoặc $\\widehat{MDE} = \\widehat{MCE}$ (hai góc nội tiếp cùng chắn cung $ME$ của đường tròn ngoại tiếp tứ giác $MDCE$).\\\\
Mặt khác, tứ giác $ABMC$ nội tiếp đường tròn $(%s)$ nên $\\widehat{MBF} + \\widehat{MCA} = 180^\\circ$. Lại có $\\widehat{MCA} + \\widehat{MCE} = 180^\\circ$ (hai góc kề bù) nên $\\widehat{MBF} = \\widehat{MCE}$.\\\\
Vì tứ giác $MDBF$ nội tiếp nên $\\widehat{MDF} + \\widehat{MBF} = 180^\\circ$.\\\\
Từ đó suy ra $\\widehat{MDF} + \\widehat{MDE} = \\widehat{MDF} + \\widehat{MBF} = 180^\\circ$. Vậy ba điểm $D, E, F$ thẳng hàng.
\\end{enumEX}''' % (tam))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
