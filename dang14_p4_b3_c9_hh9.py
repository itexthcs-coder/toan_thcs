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


def bt_dang14_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        gocB = randint(64, 76)
        gocC = 120 - gocB
        gocA = 60
        gocBMC = 120

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (110:1.6);
\\coordinate (B) at (210:1.6);
\\coordinate (C) at (-30:1.6);
\\coordinate (M) at (-90:1.6);
\\coordinate (D) at (intersection of A--M and B--C);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(M) (B)--(M)--(C);
\\fill (O) circle (1pt) node[above right] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tam giác $ABC$ nội tiếp đường tròn $(O)$ có $\\widehat{ABC} = %s^\\circ$ và $\\widehat{ACB} = %s^\\circ$. Tia phân giác của góc $BAC$ cắt cạnh $BC$ tại $D$ và cắt đường tròn $(O)$ tại điểm thứ hai là $M$ ($M \\neq A$). \\\\
a) Chứng minh rằng tứ giác $ABMC$ nội tiếp đường tròn $(O)$ và tính số đo góc $\\widehat{BMC}$. \\\\
b) Chứng minh rằng tam giác $MBC$ là tam giác cân.%s''' % (gocB, gocC, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì bốn đỉnh $A, B, M, C$ cùng nằm trên đường tròn $(O)$ nên tứ giác $ABMC$ nội tiếp đường tròn $(O)$.\\\\
Xét tam giác $ABC$ có $\\widehat{BAC} = 180^\\circ - \\widehat{ABC} - \\widehat{ACB} = 180^\\circ - %s^\\circ - %s^\\circ = %s^\\circ$.\\\\
Vì tứ giác $ABMC$ nội tiếp $(O)$ nên $\\widehat{BAC} + \\widehat{BMC} = 180^\\circ \\Rightarrow \\widehat{BMC} = 180^\\circ - %s^\\circ = %s^\\circ$.
\\item Vì $AM$ là tia phân giác của góc $BAC$ nên $\\widehat{BAM} = \\widehat{CAM} = \\dfrac{60^\\circ}{2} = 30^\\circ$.\\\\
Trong đường tròn $(O)$, các góc nội tiếp $\\widehat{MBC}$ và $\\widehat{CAM}$ cùng chắn cung $MC$ nên $\\widehat{MBC} = \\widehat{CAM} = 30^\\circ$.\\\\
Tương tự, các góc nội tiếp $\\widehat{MCB}$ và $\\widehat{BAM}$ cùng chắn cung $MB$ nên $\\widehat{MCB} = \\widehat{BAM} = 30^\\circ$.\\\\
Suy ra $\\triangle MBC$ cân tại $M$ (có $\\widehat{MBC} = \\widehat{MCB} = 30^\\circ$ và $\\widehat{BMC} = 120^\\circ$).
\\end{enumEX}''' % (gocB, gocC, gocA, gocA, gocBMC))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
